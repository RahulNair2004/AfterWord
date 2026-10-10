from pydantic import ValidationError
import pytest
import json
from app.services.AI.schemas import (
    CaseSummaryResponse,
    EvidenceAnalysisResponse,
    TheoryAnalysisResponse,
    InvestigationAssistantResponse,
    ParadoxAIResponse,
)


from sqlalchemy.exc import SQLAlchemyError

from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from app.services.AI.service import generate_case_summary
from app.services.AI.service import (
    generate_evidence_analysis,
    generate_theory_analysis,
)

def make_groq_response(content):
    """Build a fake Groq completion response."""
    return SimpleNamespace(
        choices=[
            SimpleNamespace(
                message=SimpleNamespace(content=content)
            )
        ]
    )


def make_test_db():
    """Create a mock database session with no cached summary."""
    db = MagicMock()

    # The cache query returns no existing analysis.
    db.query.return_value.filter.return_value.first.return_value = None

    return db


@patch("app.services.AI.service.build_case_ai_context")
@patch("app.services.AI.service.client.chat.completions.create")
def test_service_rejects_invalid_json(mock_groq, mock_context):
    mock_context.return_value = "Test case context"
    mock_groq.return_value = make_groq_response("{invalid json")

    db = make_test_db()

    with pytest.raises(RuntimeError, match="invalid response"):
        generate_case_summary(case_id=1, db=db)

    # Invalid output must never be saved.
    db.add.assert_not_called()
    db.commit.assert_not_called()


@patch("app.services.AI.service.build_case_ai_context")
@patch("app.services.AI.service.client.chat.completions.create")
def test_service_rejects_missing_required_field(mock_groq, mock_context):
    mock_context.return_value = "Test case context"

    mock_groq.return_value = make_groq_response(
        '{"summary": "Test summary", "key_facts": ["A fact"]}'
    )

    db = make_test_db()

    with pytest.raises(RuntimeError, match="invalid response data"):
        generate_case_summary(case_id=1, db=db)

    # Schema-invalid output must never be saved.
    db.add.assert_not_called()
    db.commit.assert_not_called()


@patch("app.services.AI.service.build_case_ai_context")
@patch("app.services.AI.service.client.chat.completions.create")
def test_service_handles_groq_failure(mock_groq, mock_context):
    mock_context.return_value = "Test case context"
    mock_groq.side_effect = Exception("Simulated provider failure")

    db = make_test_db()

    with pytest.raises(
        RuntimeError,
        match="AI service is currently unavailable"
    ):
        generate_case_summary(case_id=1, db=db)

    db.add.assert_not_called()
    db.commit.assert_not_called()


@patch("app.services.AI.service.build_case_ai_context")
@patch("app.services.AI.service.client.chat.completions.create")
def test_cached_summary_is_reused(mock_groq, mock_context):
    mock_context.return_value = "Test case context"

    cached_data = {
        "summary": "Previously saved summary",
        "key_facts": ["Fact A"],
        "unresolved_questions": ["Question A"],
    }

    db = make_test_db()
    db.query.return_value.filter.return_value.first.return_value = (
        SimpleNamespace(response=cached_data)
    )

    result = generate_case_summary(case_id=1, db=db)

    assert result.summary == "Previously saved summary"
    assert result.key_facts == ["Fact A"]
    mock_groq.assert_not_called()
    db.add.assert_not_called()
    db.commit.assert_not_called()


@patch("app.services.AI.service.build_case_ai_context")
@patch("app.services.AI.service.client.chat.completions.create")
def test_valid_summary_is_saved(mock_groq, mock_context):
    mock_context.return_value = "Test case context"

    mock_groq.return_value = make_groq_response(
        '{"summary": "New summary", '
        '"key_facts": ["Fact A"], '
        '"unresolved_questions": ["Question A"]}'
    )

    db = make_test_db()

    result = generate_case_summary(case_id=1, db=db)

    assert result.summary == "New summary"
    db.add.assert_called_once()
    db.commit.assert_called_once()
    db.refresh.assert_called_once()



@patch("app.services.AI.service.build_case_ai_context")
@patch("app.services.AI.service.client.chat.completions.create")
def test_database_save_failure_rolls_back(mock_groq, mock_context):
    mock_context.return_value = "Test case context"

    mock_groq.return_value = make_groq_response(
        '{"summary": "New summary", '
        '"key_facts": ["Fact A"], '
        '"unresolved_questions": ["Question A"]}'
    )

    db = make_test_db()
    db.commit.side_effect = SQLAlchemyError("Simulated database failure")

    with pytest.raises(RuntimeError, match="AI Analysis could not be saved"):
        generate_case_summary(case_id=1, db=db)

    db.rollback.assert_called_once()


@patch("app.services.AI.service.build_evidence_ai_context")
@patch("app.services.AI.service.client.chat.completions.create")
def test_evidence_rejects_invalid_json(mock_groq, mock_context):
    mock_context.return_value = "Test evidence context"
    mock_groq.return_value = make_groq_response("{invalid json")

    db = make_test_db()
    db.query.return_value.filter.return_value.first.side_effect = [
        SimpleNamespace(id=1, case_id=1),  # Evidence lookup
        None,                              # Cache lookup
    ]

    with pytest.raises(RuntimeError, match="invalid response"):
        generate_evidence_analysis(evidence_id=1, db=db)

    db.add.assert_not_called()
    db.commit.assert_not_called()


@patch("app.services.AI.service.build_evidence_ai_context")
@patch("app.services.AI.service.client.chat.completions.create")
def test_evidence_rejects_missing_required_field(mock_groq, mock_context):
    mock_context.return_value = "Test evidence context"
    mock_groq.return_value = make_groq_response(
        '{"summary": "Evidence summary", '
        '"significance": "Potentially relevant", '
        '"questions": ["When did this happen?"]}'
    )

    db = make_test_db()
    db.query.return_value.filter.return_value.first.side_effect = [
        SimpleNamespace(id=1, case_id=1),
        None,
    ]

    with pytest.raises(RuntimeError, match="invalid response format"):
        generate_evidence_analysis(evidence_id=1, db=db)

    db.add.assert_not_called()
    db.commit.assert_not_called()


@patch("app.services.AI.service.build_theory_ai_context")
@patch("app.services.AI.service.client.chat.completions.create")
def test_theory_rejects_invalid_json(mock_groq, mock_context):
    mock_context.return_value = "Test theory context"
    mock_groq.return_value = make_groq_response("{invalid json")

    db = make_test_db()
    db.query.return_value.filter.return_value.first.side_effect = [
        SimpleNamespace(id=1, case_id=1),  # Theory lookup
        None,                              # Cache lookup
    ]

    with pytest.raises(RuntimeError, match="invalid response"):
        generate_theory_analysis(theory_id=1, db=db)

    db.add.assert_not_called()
    db.commit.assert_not_called()


@patch("app.services.AI.service.build_theory_ai_context")
@patch("app.services.AI.service.client.chat.completions.create")
def test_theory_rejects_missing_required_field(mock_groq, mock_context):
    mock_context.return_value = "Test theory context"
    mock_groq.return_value = make_groq_response(
        '{"summary": "Theory summary", '
        '"supporting_evidence": ["Evidence A"], '
        '"contradictions": []}'
    )

    db = make_test_db()
    db.query.return_value.filter.return_value.first.side_effect = [
        SimpleNamespace(id=1, case_id=1),
        None,
    ]

    with pytest.raises(RuntimeError, match="invalid response"):
        generate_theory_analysis(theory_id=1, db=db)

    db.add.assert_not_called()
    db.commit.assert_not_called()


@patch("app.services.AI.service.client.chat.completions.create")
@patch("app.services.AI.service.build_investigation_assistant_context")
def test_assistant_rejects_invalid_json(mock_context, mock_groq):
    from app.services.AI.service import generate_investigation_assistant

    mock_context.return_value = "Test case context"
    mock_groq.return_value = make_groq_response("invalid json")

    with pytest.raises(RuntimeError):
        generate_investigation_assistant(
            case_id=1,
            question="What should I investigate?",
            db=make_test_db(),
        )


@patch("app.services.AI.service.client.chat.completions.create")
@patch("app.services.AI.service.build_investigation_assistant_context")
def test_assistant_rejects_missing_fields(mock_context, mock_groq):
    from app.services.AI.service import generate_investigation_assistant

    mock_context.return_value = "Test case context"
    mock_groq.return_value = make_groq_response(
        json.dumps({
            "answer": "Investigate the timeline."
        })
    )

    with pytest.raises(RuntimeError):
        generate_investigation_assistant(
            case_id=1,
            question="What should I investigate?",
            db=make_test_db(),
        )


# PARADOX AI TESTS

@patch("app.services.AI.service.client.chat.completions.create")
@patch("app.services.AI.service.build_paradox_ai_context")
def test_paradox_rejects_invalid_json(mock_context, mock_groq):
    from app.services.AI.service import generate_paradox_ai
    from app.services.AI.schemas import ParadoxMessage

    mock_context.return_value = "Test case context"
    mock_groq.return_value = make_groq_response("invalid json")

    with pytest.raises(RuntimeError):
        generate_paradox_ai(
            case_id=1,
            messages=[
                ParadoxMessage(
                    role="user",
                    content="Could this evidence mean something else?",
                )
            ],
            db=make_test_db(),
        )


@patch("app.services.AI.service.client.chat.completions.create")
@patch("app.services.AI.service.build_paradox_ai_context")
def test_paradox_rejects_missing_fields(mock_context, mock_groq):
    from app.services.AI.service import generate_paradox_ai
    from app.services.AI.schemas import ParadoxMessage

    mock_context.return_value = "Test case context"
    mock_groq.return_value = make_groq_response(
        json.dumps({
            "challenge": "Consider another explanation."
        })
    )

    with pytest.raises(RuntimeError):
        generate_paradox_ai(
            case_id=1,
            messages=[
                ParadoxMessage(
                    role="user",
                    content="Could this evidence mean something else?",
                )
            ],
            db=make_test_db(),
        )

def test_invalid_json():
    invalid_json = "{invalid json"
    with pytest.raises(ValueError):
        json.loads(invalid_json)

def test_case_summary_missing_required_field():
    with pytest.raises(ValidationError):
        CaseSummaryResponse.model_validate({
            "summary": "A case summary",
            "key_facts": ["A fact"],
        })

def test_evidence_analysis_missing_requierd_field():
    with pytest.raises(ValidationError):
        EvidenceAnalysisResponse.model_validate(
            {
                "summary": "Evidence summary",
                "significance": "Potentially relevant",
                "questions": ["When did this happen?"],
            }
        )

def test_theory_analysis_missing_requried_field():
    with pytest.raises(ValidationError):
        TheoryAnalysisResponse.model_validate(
            {
                "summary": "Theory summary",
                "supporting_evidence": ["Evidence A"],
                "contradictions": [],
                
            }
        )

def test_assistant_missing_required_field():
    with pytest.raises(ValidationError):
        InvestigationAssistantResponse.model_validate({
            "answer": "Consider the available evidence.",
            "key_points": ["Review the timeline"],
        })


def test_paradox_missing_required_field():
    with pytest.raises(ValidationError):
        ParadoxAIResponse.model_validate({
            "challenge": "Is there another explanation?",
            "alternative_explanation": "An alternative scenario", 
            "supporting_points": [],
        })