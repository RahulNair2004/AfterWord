# AfterWords — Case System

## 1. Purpose

The Case System is the core information architecture of AfterWords.

A **Case** is not simply an article or story. It is a structured investigation containing:

* A narrative
* Timeline of events
* People, organizations, places, and other entities
* Sources
* Evidence
* Claims
* Hypotheses
* Findings
* Fact synthesis
* An unresolved dilemma

The Case System allows AfterWords to transform scattered information into a structured investigation that users can explore, contribute to, and debate.

The central model is:

```text
CASE
│
├── Story
├── Timeline
├── Entities
├── Sources
├── Evidence
├── Claims
├── Hypotheses
├── Findings
├── Fact Synthesis
└── Dilemma
```

The Case is the single source of context for the investigation and debate surrounding it.

---

# 2. Case Overview

A Case represents a real-world situation, event, mystery, controversy, unresolved question, or complex situation where available information can be investigated and eventually lead to a meaningful dilemma.

Examples:

* An unexplained historical event
* A technological failure
* An unresolved scientific question
* A corporate controversy
* An environmental incident
* A legal mystery
* A disappearance
* A disputed historical event
* A systemic social problem
* An ethical conflict

The objective is not necessarily to "solve" every Case.

Some Cases may end with:

```text
Question → Evidence → Strong Explanation
```

while others may end with:

```text
Question → Evidence → Conflicting Evidence → UNKNOWN
```

Both are valid outcomes.

---

# 3. Case Structure

Every Case consists of several interconnected layers.

```text
                         CASE
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
      STORY            TIMELINE         ENTITIES
        │                 │                 │
        └─────────────────┼─────────────────┘
                          │
                       SOURCES
                          │
                       EVIDENCE
                          │
             ┌────────────┼────────────┐
             │            │            │
           CLAIMS     HYPOTHESES    FINDINGS
             │            │            │
             └────────────┼────────────┘
                          │
                    FACT SYNTHESIS
                          │
                       DILEMMA
                          │
                        DEBATE
```

Each layer should remain traceable to the underlying evidence.

---

# 4. Case Metadata

A Case should conceptually contain the following information.

| Field             | Purpose                    |
| ----------------- | -------------------------- |
| Case ID           | Unique identifier          |
| Title             | Public Case name           |
| Short Description | Brief explanation          |
| Story             | Main Case narrative        |
| Category          | Case classification        |
| Tags              | Search/discovery metadata  |
| Cover Image       | Visual representation      |
| Status            | Current lifecycle stage    |
| Created By        | Case creator               |
| Created At        | Creation timestamp         |
| Updated At        | Last update                |
| Participants      | Users contributing to Case |
| Followers         | Users following Case       |

These are conceptual product fields, not the final database schema.

The final technical schema will be designed during implementation.

---

# 5. Case Categories

Cases can belong to one primary category and multiple secondary tags.

Initial categories:

* Mystery
* History
* Technology
* Science
* Society
* Ethics
* Environment
* Corporate
* Law
* Culture

Examples:

```text
Category:
Technology

Tags:
AI
Privacy
Surveillance
Security
Regulation
```

Categories should remain broad.

Tags provide the finer-grained classification required for discovery.

---

# 6. Case Lifecycle

Every Case follows a controlled lifecycle.

```text
DRAFT
  ↓
INVESTIGATION
  ↓
EVIDENCE_REVIEW
  ↓
FACT_SYNTHESIS
  ↓
DEBATE
  ↓
RESOLVED
  ↓
ARCHIVED
```

Not every Case will have a definitive answer.

Therefore:

```text
RESOLVED
```

means the active investigation phase has ended.

It does **not** necessarily mean:

> "The truth has been completely discovered."

A Case can be resolved with significant uncertainty remaining.

---

# 7. Lifecycle Transition Table

| Stage           | Purpose                  | Who Can Act                  | Main Actions                                       | Publication Condition              |
| --------------- | ------------------------ | ---------------------------- | -------------------------------------------------- | ---------------------------------- |
| DRAFT           | Prepare Case             | Creator/Admin                | Edit Case, add initial sources, timeline, evidence | Not publicly investigable          |
| INVESTIGATION   | Community investigation  | Community                    | Submit evidence, sources, hypotheses, questions    | Contributions become reviewable    |
| EVIDENCE_REVIEW | Validate contributions   | Reviewers/Moderators         | Verify, dispute, reject evidence                   | Reviewed evidence becomes usable   |
| FACT_SYNTHESIS  | Organize knowledge       | Editors/Trusted contributors | Classify facts, resolve contradictions             | Human-reviewed synthesis published |
| DEBATE          | Explore dilemma          | Community                    | Positions, arguments, counterarguments             | Debate becomes active              |
| RESOLVED        | End active investigation | Editors/Admin                | Corrections and limited additions                  | Case remains publicly readable     |
| ARCHIVED        | Preserve historical Case | Admin                        | Read-only access                                   | No normal contributions            |

---

# 8. DRAFT

A Case begins in `DRAFT`.

During this stage, the Case creator or authorized editor can prepare the initial structure.

They can:

* Write the Case story
* Add initial sources
* Create timeline events
* Add entities
* Add initial evidence
* Define the investigation question
* Prepare the initial dilemma
* Configure Case metadata

The public cannot yet participate in investigation.

The Case should not appear as an active investigation.

```text
DRAFT
│
├── Story
├── Initial Sources
├── Initial Timeline
├── Initial Entities
└── Investigation Question
```

Once the Case has enough initial material, it can transition to:

```text
INVESTIGATION
```

---

# 9. INVESTIGATION

Investigation is the primary community research stage.

Users can investigate the Case by:

* Finding sources
* Submitting evidence
* Adding timeline information
* Identifying entities
* Connecting entities
* Asking questions
* Proposing hypotheses
* Submitting findings
* Challenging existing information
* Identifying contradictions

The investigation should encourage users to contribute information rather than simply comment on the Case.

The fundamental contribution loop is:

```text
Find Information
       ↓
Submit Contribution
       ↓
Provide Source
       ↓
Explain Relevance
       ↓
Community / Moderator Review
       ↓
Contribution Becomes Part of Case
```

---

# 10. Investigation Objects

Investigation revolves around several structured objects.

```text
Investigation
│
├── Evidence
├── Source
├── Timeline Event
├── Entity
├── Connection
├── Question
├── Hypothesis
└── Finding
```

These objects should be connected rather than existing as isolated posts.

For example:

```text
Evidence
   ↓
supports
   ↓
Hypothesis
   ↓
explains
   ↓
Timeline Event
   ↓
involves
   ↓
Entity
```

This creates the foundation for the future investigation graph.

---

# 11. Investigation Actions

A registered contributor can perform actions such as:

### Submit Evidence

Provide information relevant to the Case.

### Add Source

Submit a source supporting information already present or introducing new information.

### Add Timeline Event

Identify an important event and its approximate or confirmed date.

### Add Entity

Identify a person, organization, location, document, event, or other relevant entity.

### Create Connection

Explain a relationship between two entities or pieces of evidence.

### Ask Question

Identify information that is missing or unclear.

### Propose Hypothesis

Suggest a possible explanation.

### Submit Finding

Provide a structured observation based on collected evidence.

### Challenge Information

Identify an unsupported, disputed, or potentially incorrect statement.

---

# 12. Sources

A Source is the origin from which information or evidence is obtained.

Examples:

* News article
* Government document
* Court record
* Academic paper
* Public database
* Archive
* Interview
* Dataset
* Video
* Photograph
* Official statement
* Historical document

A source should preserve attribution.

Conceptually:

```text
SOURCE
│
├── Title
├── Publisher / Author
├── URL / Reference
├── Publication Date
├── Source Type
└── Access Information
```

A source can support multiple pieces of evidence.

```text
Source
   ├── Evidence A
   ├── Evidence B
   └── Evidence C
```

---

# 13. Evidence

Evidence is information extracted from or directly supported by a source that is relevant to the Case.

Evidence is more structured than a normal comment.

Conceptually:

```text
EVIDENCE
│
├── ID
├── Case
├── Submitted By
├── Title
├── Description
├── Type
├── Source
├── Source URL / Reference
├── Publication Date
├── Submitted At
└── Status
```

The exact technical representation will be defined during backend development.

---

# 14. Evidence Types

Initial evidence types:

| Type          | Example                    |
| ------------- | -------------------------- |
| Article       | Investigative news article |
| Document      | Official report            |
| Photo         | Historical photograph      |
| Video         | Recorded event             |
| Interview     | Recorded testimony         |
| Court Record  | Legal filing               |
| Public Record | Government record          |
| Dataset       | Public dataset             |
| Archive       | Archived material          |
| Other         | Other relevant material    |

Multiple evidence types can be associated with the same Case.

---

# 15. Evidence Status

Evidence passes through a review process.

```text
PENDING
   ↓
UNDER_REVIEW
   ↓
VERIFIED
```

Alternative outcomes:

```text
UNDER_REVIEW
   ├── VERIFIED
   ├── DISPUTED
   └── REJECTED
```

### PENDING

The contribution has been submitted but not reviewed.

### UNDER_REVIEW

The contribution is actively being evaluated.

### VERIFIED

The source and contribution meet the Case's evidence standards.

### DISPUTED

The evidence is potentially relevant but has credible conflicting information or unresolved issues.

### REJECTED

The contribution does not meet the Case's evidence requirements.

Rejected evidence should generally remain available internally for moderation/audit purposes even if it is not publicly displayed.

---

# 16. Evidence Submission

The evidence submission flow is:

```text
Case
 ↓
Submit Evidence
 ↓
Select Evidence Type
 ↓
Title
 ↓
Description
 ↓
Source
 ↓
URL / Reference
 ↓
Explain Relevance
 ↓
Submit
 ↓
PENDING
 ↓
UNDER_REVIEW
 ↓
VERIFIED / DISPUTED / REJECTED
```

Users should be encouraged to explain:

> "Why does this evidence matter?"

rather than simply attaching a link.

This makes contributions more useful for investigators.

---

# 17. Evidence Review

Reviewers should evaluate:

### Relevance

Does the evidence actually relate to the Case?

### Source Quality

Is the source identifiable and reasonably credible?

### Authenticity

Is there evidence that the material is genuine?

### Context

Could the evidence be misleading without additional context?

### Corroboration

Is the information supported elsewhere?

### Contradiction

Does credible evidence conflict with it?

### Attribution

Can the origin of the information be clearly identified?

The review system should avoid reducing evidence quality to a single numerical score.

Instead, the system should preserve the reasoning and status behind the evidence.

---

# 18. Claims

A Claim is a statement made by a person, organization, source, or contributor.

Example:

> "Organization X knew about the issue before the public announcement."

This should initially remain a claim unless sufficient evidence establishes it.

Claims should retain attribution.

```text
CLAIM
│
├── Statement
├── Source / Author
├── Evidence
├── Attribution
└── Status
```

The system should never automatically transform an allegation into a fact.

---

# 19. Information Classification

AfterWords uses explicit information classifications.

```text
FACT
CLAIM
ALLEGATION
HYPOTHESIS
OPINION
```

### FACT

Information supported by sufficient reliable evidence within the Case.

### CLAIM

A statement attributed to a person, organization, or source.

### ALLEGATION

A claim that alleges wrongdoing or misconduct but has not been established as fact.

### HYPOTHESIS

A proposed explanation that requires investigation.

### OPINION

A person's interpretation, judgment, or belief.

These classifications help prevent different types of information from being presented as equivalent.

---

# 20. Timeline

The Timeline organizes the Case chronologically.

Example:

```text
2018
 │
 ├── Event A
 │
2019
 │
 ├── Event B
 │
2020
 │
 ├── Event C
 │
2021
 │
 └── Event D
```

Each timeline event can connect to:

* People
* Organizations
* Locations
* Evidence
* Sources
* Other events
* Claims

Conceptually:

```text
TIMELINE EVENT
│
├── Date / Date Range
├── Title
├── Description
├── Location
├── Related Entities
├── Supporting Evidence
└── Sources
```

Dates should support uncertainty.

For example:

```text
Exact Date
Approximate Date
Date Range
Unknown Date
```

The system should not force investigators to invent precision that does not exist.

---

# 21. Entities

Entities represent important objects involved in the Case.

Initial entity types:

* Person
* Organization
* Location
* Event
* Document
* Other

Example:

```text
CASE
│
├── Person A
├── Person B
├── Organization X
├── Organization Y
├── Location Z
└── Event Q
```

Entities can be connected.

```text
Person A
   │
   ├── worked_for
   ↓
Organization X
   │
   ├── involved_in
   ↓
Event Q
```

This structure provides the foundation for a future graph-based investigation interface.

---

# 22. Connections

Connections describe relationships between Case objects.

Examples:

```text
Person → worked for → Organization

Organization → involved in → Event

Evidence → supports → Claim

Evidence → contradicts → Hypothesis

Source → documents → Event
```

Connections should have an explanation and, where appropriate, supporting evidence.

The goal is to prevent users from simply creating unsupported relationship graphs.

---

# 23. Questions

Questions represent unresolved information gaps.

Examples:

* Who was responsible for the decision?
* When did the organization first become aware?
* Which source is more reliable?
* Why did the event occur?
* What evidence is still missing?

Questions are important because investigation should not only collect information.

It should also identify what remains unknown.

```text
QUESTION
   ↓
Investigation
   ↓
Evidence
   ↓
Finding
   ↓
Resolved / Partially Resolved / Unknown
```

---

# 24. Hypotheses

A Hypothesis is a proposed explanation for an unresolved part of the Case.

Example:

> "The failure may have resulted from a previously undocumented software dependency."

A hypothesis should contain:

* Statement
* Author
* Supporting evidence
* Contradicting evidence
* Status

Initial statuses:

```text
PROPOSED
SUPPORTED
CHALLENGED
REJECTED
```

A hypothesis is not automatically converted into a fact.

Its status should depend on the evidence associated with it.

---

# 25. Findings

A Finding is a structured observation resulting from investigation.

A Finding should answer:

> "What can we reasonably conclude from the available evidence?"

Example:

```text
Finding:

Multiple independent records indicate that the system
experienced failures during the same period.

Supporting Evidence:
- Evidence A
- Evidence B
- Evidence C

Classification:
SUPPORTED
```

Findings can later contribute to the Case's Fact Synthesis.

---

# 26. Fact Synthesis

Fact Synthesis is the stage where investigated information is organized into a coherent factual foundation.

The goal is not to create a single "truth score."

Instead, information is categorized according to the available evidence.

```text
FACT SYNTHESIS
│
├── CONFIRMED
├── SUPPORTED
├── DISPUTED
└── UNKNOWN
```

---

## 26.1 CONFIRMED

Information supported by strong and sufficiently reliable evidence.

Example:

```text
Event occurred on March 4.
```

when reliable records establish the event and date.

---

## 26.2 SUPPORTED

Information with credible supporting evidence, but where absolute certainty may not be justified.

This distinction is important.

```text
SUPPORTED ≠ CERTAIN
```

---

## 26.3 DISPUTED

Information where credible evidence conflicts.

Example:

```text
Source A → says Event occurred at 8:00 PM
Source B → says Event occurred at 9:00 PM
```

The Case should preserve the disagreement instead of arbitrarily selecting one.

---

## 26.4 UNKNOWN

The available evidence is insufficient to establish the answer.

This is a legitimate outcome.

```text
UNKNOWN
```

does not mean:

> "Nobody knows."

It means:

> "The Case currently lacks sufficient reliable evidence to establish an answer."

---

# 27. Fact Synthesis Rules

The synthesis layer must follow several principles.

### Rule 1 — Evidence First

Important factual statements should be traceable to evidence.

### Rule 2 — Preserve Uncertainty

If the evidence does not establish something, the system should not manufacture certainty.

### Rule 3 — Preserve Disagreement

Conflicting credible sources should remain visible.

### Rule 4 — Preserve Attribution

Claims should remain attributed to their source.

### Rule 5 — Human Approval

AI-generated synthesis should require human review.

### Rule 6 — Traceability

Users should be able to navigate:

```text
Fact
 ↓
Evidence
 ↓
Source
```

---

# 28. AI Assistance

AI can assist investigators, but it should not independently determine truth.

The intended model is:

```text
AI
 ↓
SUGGESTION
 ↓
HUMAN REVIEW
 ↓
PUBLISHED INFORMATION
```

Potential AI capabilities include:

### Source Summarization

Summarize long documents for investigators.

### Timeline Extraction

Identify dates and events from sources.

### Entity Extraction

Identify people, organizations, locations, and events.

### Evidence Clustering

Group related pieces of evidence.

### Contradiction Detection

Identify potentially conflicting statements.

### Question Generation

Suggest unanswered questions.

### Hypothesis Assistance

Suggest possible explanations based on existing evidence.

### Fact Synthesis Drafting

Generate a preliminary synthesis from reviewed evidence.

### Missing Information Detection

Identify areas where the Case appears to lack evidence.

AI output should always be clearly distinguishable from human-reviewed Case information.

---

# 29. Dilemma Creation

The investigation eventually leads to a central dilemma.

The dilemma should emerge from the Case rather than being artificially attached to it.

The structure is:

```text
Evidence
   ↓
Investigation
   ↓
Fact Synthesis
   ↓
Unresolved Question
   ↓
Dilemma
   ↓
Debate
```

A dilemma can involve:

* Ethical conflict
* Social conflict
* Legal conflict
* Technological trade-off
* Institutional responsibility
* Scientific uncertainty
* Individual vs Society
* Privacy vs Security
* Freedom vs Safety

The dilemma should contain:

```text
DILEMMA
│
├── Central Question
├── Context
├── Relevant Facts
├── Known Uncertainties
├── Competing Considerations
└── Evidence
```

The Case should not force a single correct opinion.

---

# 30. Investigation → Dilemma Example

A simplified Case might look like:

```text
CASE

A technology company deploys an automated system.
        ↓
Multiple failures occur.
        ↓
Users report unexpected behavior.
        ↓
Internal documents reveal earlier warnings.
        ↓
Investigators find conflicting explanations.
        ↓
Fact Synthesis establishes:
    - Failures occurred
    - Warnings existed
    - Responsibility remains disputed
        ↓
DILEMMA

Should organizations deploy potentially beneficial
technology when significant risks remain uncertain?
```

The investigation establishes the factual foundation.

The debate explores the unresolved question.

---

# 31. Moderation

Because AfterWords is user-generated, the Case System requires structured moderation.

Users should be able to report:

* Spam
* Harassment
* Hate
* Misinformation
* Unverified accusation
* Personal information
* Manipulated media
* Copyright concerns
* Other violations

Content can have the following states:

```text
VISIBLE
FLAGGED
UNDER_REVIEW
HIDDEN
REMOVED
```

Moderation actions should preserve an audit trail.

---

# 32. Sensitive Claims

Claims involving real people or organizations require additional care.

The system should avoid presenting:

```text
Unverified allegation
```

as:

```text
Established fact
```

Instead:

```text
ALLEGATION
   ↓
Source
   ↓
Evidence
   ↓
Review
   ↓
Confirmed / Supported / Disputed / Unknown
```

Attribution should remain visible.

For example:

```text
"Source X reported that..."
```

is materially different from:

```text
"X happened."
```

The Case System should preserve that distinction.

---

# 33. Case Permissions

Case permissions depend on both user role and Case lifecycle.

| Role                | Read | Investigate | Submit Evidence | Hypotheses | Findings | Moderate | Lifecycle |
| ------------------- | ---: | ----------: | --------------: | ---------: | -------: | -------: | --------: |
| Guest               |    ✓ |     Limited |               — |          — |        — |        — |         — |
| Registered User     |    ✓ |           ✓ |               ✓ |    Limited |  Limited |        — |         — |
| Investigator        |    ✓ |           ✓ |               ✓ |          ✓ |        ✓ |        — |         — |
| Trusted Contributor |    ✓ |           ✓ |               ✓ |          ✓ |        ✓ |  Limited |         — |
| Moderator           |    ✓ |           ✓ |               ✓ |          ✓ |        ✓ |        ✓ |         — |
| Case Editor/Admin   |    ✓ |           ✓ |               ✓ |          ✓ |        ✓ |        ✓ |         ✓ |

Exact permissions can be refined during backend implementation.

---

# 34. Lifecycle-Based Restrictions

The lifecycle also controls what users can do.

### DRAFT

```text
Public investigation: OFF
Community contributions: OFF
Editing: ON for authorized users
```

### INVESTIGATION

```text
Community investigation: ON
Evidence submission: ON
Hypotheses: ON
Questions: ON
Findings: ON
```

### EVIDENCE_REVIEW

```text
New contributions: Limited
Evidence review: ON
Verification: ON
Dispute handling: ON
```

### FACT_SYNTHESIS

```text
Investigation: Limited
Fact organization: ON
Synthesis editing: Restricted
Human approval: Required
```

### DEBATE

```text
Evidence exploration: ON
Debate: ON
New investigation: Limited
```

### RESOLVED

```text
Reading: ON
Debate: Limited/Read-only
Corrections: Restricted
New investigation: OFF
```

### ARCHIVED

```text
Reading: ON
Editing: OFF
Investigation: OFF
Debate: OFF
```

---

# 35. End-to-End Case Example

A complete Case can conceptually look like:

```text
CASE
│
├── Title
│
├── Story
│
├── Timeline
│   ├── Event 1
│   ├── Event 2
│   ├── Event 3
│   └── Event 4
│
├── Entities
│   ├── Person A
│   ├── Organization A
│   └── Location A
│
├── Sources
│   ├── Source A
│   ├── Source B
│   └── Source C
│
├── Evidence
│   ├── Evidence A
│   ├── Evidence B
│   └── Evidence C
│
├── Claims
│   ├── Claim A
│   └── Claim B
│
├── Hypotheses
│   ├── Hypothesis A
│   └── Hypothesis B
│
├── Findings
│   ├── Finding A
│   └── Finding B
│
├── Fact Synthesis
│   ├── Confirmed
│   ├── Supported
│   ├── Disputed
│   └── Unknown
│
└── Dilemma
    ├── Central Question
    ├── Context
    ├── Relevant Facts
    └── Uncertainties
```

---

# 36. Case Information Graph

The long-term Case architecture can be represented as a graph.

```text
                    ┌─────────────┐
                    │    CASE     │
                    └──────┬──────┘
                           │
             ┌─────────────┼─────────────┐
             ↓             ↓             ↓
         Timeline       Entities       Sources
             │             │             │
             └──────┬──────┘             │
                    ↓                    ↓
                 Evidence ←───────────────┘
                    │
          ┌─────────┼─────────┐
          ↓         ↓         ↓
        Claims  Hypotheses  Findings
          │         │         │
          └─────────┼─────────┘
                    ↓
             Fact Synthesis
                    │
                    ↓
                 Dilemma
                    │
                    ↓
                  Debate
```

This graph structure is particularly important for the future technical architecture.

The first implementation does not need to be a dedicated graph database.

A relational database can represent these relationships initially.

---

# 37. Case Integrity Rules

The following rules are fundamental product invariants.

### 1. Unverified claims are not facts

A claim must not automatically become a fact.

### 2. Evidence must retain attribution

Every meaningful evidence item should identify its source.

### 3. AI output is not authoritative by default

AI suggestions require human review before becoming authoritative Case information.

### 4. Disputed information remains identifiable

Conflicting evidence should not silently disappear.

### 5. Case stage controls actions

Users cannot bypass lifecycle restrictions.

### 6. Debate depends on investigation

The central debate should be grounded in the Case's evidence and fact synthesis.

### 7. Resolution does not imply certainty

A Case can be resolved while important questions remain unknown.

### 8. Archived Cases preserve history

Archiving should not erase the investigative record.

### 9. Contributions remain traceable

Changes to important Case information should preserve authorship and history.

### 10. Important factual changes require review

A contributor should not be able to silently rewrite established Case information.

---

# 38. Case Design Philosophy

AfterWords should treat every Case as a living investigation rather than a static article.

Traditional article:

```text
AUTHOR
  ↓
ARTICLE
  ↓
READER
```

AfterWords:

```text
CASE
 ↓
INITIAL EVIDENCE
 ↓
COMMUNITY INVESTIGATION
 ↓
NEW EVIDENCE
 ↓
REVIEW
 ↓
FACT SYNTHESIS
 ↓
DILEMMA
 ↓
COMMUNITY DEBATE
```

This distinction is central to the product.

Users are not simply consuming information.

They are participating in the process of understanding it.

---

# 39. Core Case Loop

The complete Case loop is:

```text
DISCOVER CASE
      ↓
READ STORY
      ↓
EXPLORE TIMELINE
      ↓
EXPLORE EVIDENCE
      ↓
INVESTIGATE
      ↓
FIND INFORMATION
      ↓
SUBMIT CONTRIBUTION
      ↓
REVIEW
      ↓
FACT SYNTHESIS
      ↓
IDENTIFY UNKNOWN
      ↓
DILEMMA
      ↓
DEBATE
      ↓
CASE RESOLUTION
```

The most important transition is:

```text
INFORMATION
     ↓
EVIDENCE
     ↓
UNDERSTANDING
     ↓
DILEMMA
     ↓
DISCUSSION
```
