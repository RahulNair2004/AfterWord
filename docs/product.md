# AfterWords — Product Definition

## 1. Product Overview

**AfterWords** is a social investigation platform where users collaboratively investigate compelling real-world cases, examine evidence from multiple sources, identify what is known and unknown, and participate in structured debates around the unresolved questions and dilemmas that emerge from each case.

AfterWords combines:

* Collaborative investigation
* Evidence discovery and analysis
* Structured knowledge synthesis
* Social interaction
* Ethical and systemic dilemmas
* Structured debate
* AI-assisted investigation

The platform is designed around a simple idea:

> **Don't just consume a story. Investigate it, understand it, and decide what you think.**

AfterWords is not intended to simply tell users what happened or what they should believe. Instead, it provides the case, evidence, sources, competing interpretations, and structured discussion tools so that users can investigate and form their own conclusions.

---

# 2. The Problem

Most online platforms separate information consumption from meaningful investigation and discussion.

A user might encounter:

```text
Article
   ↓
Read
   ↓
Comment
   ↓
Leave
```

The user rarely has a structured way to:

* Investigate the underlying case
* Collect evidence from different sources
* Connect pieces of information
* Identify contradictions
* Distinguish verified information from speculation
* Collaborate with other people
* Understand what remains unknown
* Debate the deeper question raised by the case

Traditional mystery experiences have the opposite problem.

They provide:

```text
Clues
 ↓
Solve mystery
 ↓
Answer
```

Once the answer is revealed, the experience largely ends.

AfterWords combines these ideas into a continuous social experience:

```text
Story
 ↓
Investigation
 ↓
Evidence
 ↓
Understanding
 ↓
Uncertainty
 ↓
Dilemma
 ↓
Debate
```

---

# 3. Product Vision

The long-term vision of AfterWords is to create a platform where curiosity, investigation, and structured disagreement become a social experience.

Users should be able to discover a case that interests them and naturally move through:

```text
DISCOVER
   ↓
QUESTION
   ↓
INVESTIGATE
   ↓
DISCOVER EVIDENCE
   ↓
CONNECT INFORMATION
   ↓
UNDERSTAND
   ↓
IDENTIFY UNCERTAINTY
   ↓
DEBATE
   ↓
FORM A CONCLUSION
```

The platform should make users feel like they are participating in an investigation rather than simply consuming content.

---

# 4. Core Product Loop

The central AfterWords experience is:

```text
                    CASE
                     ↓
                INVESTIGATE
                     ↓
              COLLECT EVIDENCE
                     ↓
            CONNECT INFORMATION
                     ↓
              FACT SYNTHESIS
                     ↓
                  DILEMMA
                     ↓
                  DEBATE
                     ↓
            FORM YOUR CONCLUSION
```

This loop is the foundation of the product.

Every major feature should support at least one part of this loop.

---

# 5. What Is a Case?

A **Case** is the primary content object on AfterWords.

A Case represents a structured investigation surrounding an interesting real-world event, mystery, controversy, decision, phenomenon, or unresolved question.

A Case can contain:

```text
Case
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
├── Dilemma
└── Debate
```

Examples of potential Case categories include:

* Historical mysteries
* Unexplained events
* Missing information
* Corporate controversies
* Technological incidents
* Scientific disputes
* Environmental cases
* Institutional failures
* Privacy and surveillance questions
* Social dilemmas
* Ethical conflicts
* Public-interest investigations

A Case does not necessarily need to have one definitive answer.

The interesting outcome may instead be a clearer understanding of:

* What is known
* What is supported
* What is disputed
* What remains unknown
* Why reasonable interpretations differ

---

# 6. The AfterWords Experience

A typical user journey should look like:

```text
Discover a Case
       ↓
Read the Story
       ↓
Explore Timeline
       ↓
Examine Evidence
       ↓
Investigate
       ↓
Submit or discover additional information
       ↓
Understand what is established
       ↓
Identify unresolved questions
       ↓
Read the Dilemma
       ↓
Explore different Positions
       ↓
Participate in Debate
       ↓
Form personal conclusion
```

The user should be able to enter the experience at different points.

For example:

* A casual user may only read the Case.
* A curious user may explore the evidence.
* An Investigator may spend significant time connecting information.
* A Debater may focus primarily on the dilemma.
* A Contributor may discover and submit an important source.

---

# 7. Target Users

AfterWords initially targets people who enjoy:

* Mysteries
* Investigative stories
* History
* Technology
* Philosophy
* Ethics
* Current affairs
* Unresolved questions
* Critical thinking
* Structured discussion

The product should not require users to be professional investigators or researchers.

The interface should support both:

```text
Casual participation
        +
Deep investigation
```

---

# 8. User Roles

AfterWords uses progressive capabilities rather than complicated reputation systems.

### Guest

Can:

* Browse Cases
* Search Cases
* Read Case stories
* View public evidence
* Read debates
* View public profiles

Cannot:

* Submit contributions
* Participate in investigations
* Create arguments
* Comment

---

### Registered User

Can:

* Follow Cases
* Save Cases
* React to content
* Comment
* Participate in investigations
* Participate in debates
* Submit basic contributions

---

### Contributor

A Contributor is a user who actively provides information to Cases.

They can:

* Submit sources
* Submit evidence
* Suggest timeline events
* Suggest relevant entities
* Submit corrections
* Provide contextual information

A contribution is not automatically accepted.

---

### Investigator

An Investigator actively analyzes Cases.

They can:

* Analyze evidence
* Connect evidence
* Identify contradictions
* Create hypotheses
* Submit findings
* Ask investigation questions
* Help establish relationships between information

---

### Debater

A Debater participates in structured Case discussions.

They can:

* Express a Position
* Create Arguments
* Reference Evidence
* Challenge Arguments
* Create Counterarguments
* Respond to other users

---

### Trusted Contributor

A Trusted Contributor is a user whose previous contributions have demonstrated consistent value and reliability.

For the initial product, trusted status should remain simple and primarily administrative.

```text
is_trusted = true / false
```

Complex automated reputation scoring is not part of the initial MVP.

Trusted Contributors may later receive additional capabilities such as:

* Higher contribution visibility
* Additional review privileges
* Ability to help review evidence
* Community moderation assistance

---

### Moderator

Moderators are responsible for reviewing:

* Reports
* Flagged content
* Unverified accusations
* Harassment
* Spam
* Harmful content
* Potential misinformation

---

### Admin

Admins manage the platform itself.

They can:

* Create and manage Cases
* Manage users
* Manage moderators
* Review evidence
* Control Case lifecycle
* Remove content
* Resolve reports
* Configure platform settings

---

# 9. Core Concepts

AfterWords uses the following core concepts.

### Case

The main investigation object.

### Source

The origin of information used by a Case.

Examples:

* Article
* Document
* Interview
* Public record
* Archive
* Dataset

### Evidence

Information extracted or submitted from a Source that is relevant to a Case.

### Claim

A statement made about the Case that has not necessarily been verified.

### Fact

Information that has been sufficiently established and accepted into the Case's factual synthesis.

### Hypothesis

A proposed explanation that requires further investigation.

### Finding

A conclusion or observation produced through investigation.

### Dilemma

The central unresolved question or trade-off emerging from the Case.

### Position

A perspective taken in response to the Dilemma.

### Argument

A structured reason supporting or challenging a Position.

### Contribution

Any meaningful information submitted by a user to help develop a Case.

---

# 10. Information Classification

AfterWords must distinguish between different levels of certainty.

Information may be classified as:

```text
FACT
CLAIM
ALLEGATION
HYPOTHESIS
OPINION
```

The platform should avoid presenting speculation as established fact.

Within the Case's factual synthesis, information should also be grouped as:

```text
CONFIRMED
SUPPORTED
DISPUTED
UNKNOWN
```

Example:

```text
CONFIRMED
The event occurred on a specific date.

SUPPORTED
Multiple independent sources indicate that X occurred.

DISPUTED
Different sources provide conflicting accounts.

UNKNOWN
There is currently insufficient reliable evidence.
```

This distinction is a fundamental part of the AfterWords product.

---

# 11. Case Lifecycle

Cases progress through a controlled lifecycle:

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

### DRAFT

The Case is being prepared.

### INVESTIGATION

Users can actively investigate and contribute information.

### EVIDENCE_REVIEW

Submitted evidence is reviewed and classified.

### FACT_SYNTHESIS

The available evidence is organized into a structured understanding of the Case.

### DEBATE

The central Dilemma is presented and users can participate in structured discussion.

### RESOLVED

The active investigation has ended and the Case has reached its defined conclusion or stopping point.

Resolved does not necessarily mean that every question has an answer.

### ARCHIVED

The Case is preserved as historical content and is no longer actively investigated.

---

# 12. Evidence Philosophy

Evidence is central to AfterWords.

The platform should encourage users to support meaningful claims with sources.

The basic relationship is:

```text
SOURCE
   ↓
EVIDENCE
   ↓
CLAIM
   ↓
FACT / DISPUTED / UNKNOWN
```

Evidence may include:

* Articles
* Documents
* Photographs
* Videos
* Interviews
* Court records
* Public records
* Datasets
* Historical archives
* Other credible sources

Users should be able to see where important information came from.

---

# 13. Investigation Philosophy

Investigation should feel collaborative.

Users should be able to:

```text
Find information
      ↓
Submit evidence
      ↓
Connect information
      ↓
Identify contradictions
      ↓
Create hypotheses
      ↓
Test hypotheses
      ↓
Submit findings
```

The platform should encourage users to build upon previous contributions rather than repeatedly discovering the same information.

---

# 14. The Dilemma

The Dilemma is what separates AfterWords from a traditional mystery platform.

After investigating a Case, users should encounter a deeper question.

Examples:

```text
Should an institution disclose information
if disclosure could protect the public but
also expose vulnerable individuals?

Should privacy be sacrificed for security
in certain circumstances?

Should an organization prioritize individual
welfare over institutional survival?

When does technological convenience justify
loss of privacy?
```

The Dilemma does not need to have a universally correct answer.

The goal is to present the relevant evidence and competing considerations clearly enough for users to reason about the question themselves.

---

# 15. Debate Philosophy

AfterWords debates should be structured around the Case.

The basic structure is:

```text
DILEMMA
   ↓
POSITION
   ↓
ARGUMENT
   ↓
EVIDENCE
   ↓
COUNTERARGUMENT
   ↓
RESPONSE
```

This is intentionally different from a traditional comment section.

The goal is to encourage:

* Evidence-backed reasoning
* Clear positions
* Constructive disagreement
* Counterarguments
* Questions
* Nuanced discussion

Users should be able to disagree without the Case becoming an unstructured argument thread.

---

# 16. Social Layer

AfterWords is a social platform, but the Case remains the center of the social experience.

Users can:

* Follow Cases
* Save Cases
* Follow other users
* React to contributions
* Comment
* Participate in investigations
* Participate in debates
* Receive notifications
* View activity

The intended social graph is:

```text
USER
 │
 ├── follows → USER
 │
 ├── follows → CASE
 │
 ├── contributes → CASE
 │
 ├── investigates → CASE
 │
 └── debates → CASE
```

Social features should strengthen investigation rather than distract from it.

---

# 17. AI's Role

AI is an assistant to investigation, not the authority on truth.

AI may assist with:

### Investigation

* Summarizing sources
* Extracting entities
* Extracting timeline events
* Identifying potentially related evidence
* Detecting potential contradictions
* Generating investigation questions
* Identifying information gaps

### Debate

* Summarizing arguments
* Finding related arguments
* Linking arguments to evidence
* Identifying repeated arguments
* Suggesting potential counterpoints

### Moderation

* Detecting spam
* Flagging potentially harmful content
* Detecting potential personal information
* Identifying content requiring human review

The fundamental AI workflow is:

```text
AI
 ↓
SUGGESTION
 ↓
HUMAN REVIEW
 ↓
PUBLISHED INFORMATION
```

AI should not independently determine that an unverified claim is a fact.

---

# 18. Product Principles

AfterWords should follow these principles.

### 1. Evidence Before Confidence

Users should be encouraged to support important claims with evidence.

### 2. Uncertainty Is Valid

Not every Case needs a definitive answer.

Unknown information should remain explicitly unknown.

### 3. Investigation Before Debate

Users should have access to the relevant factual context before engaging with the central Dilemma.

### 4. Structured Disagreement

Debate should focus on arguments and evidence rather than personal attacks.

### 5. Human Judgment

AI assists users but does not replace human judgment.

### 6. Transparency

Users should be able to understand where important information came from.

### 7. Progressive Complexity

The basic experience should be simple enough for casual users while allowing deeper investigation for highly engaged users.

### 8. Case-Centered Social Interaction

Social features should support the Case rather than turn AfterWords into a generic social network.

---

# 19. What Makes AfterWords Different?

AfterWords combines three experiences:

```text
        AFTERWORDS
            │
    ┌───────┼───────┐
    ↓       ↓       ↓
 MYSTERY  EVIDENCE DEBATE
    │       │       │
    └───────┼───────┘
            ↓
     SOCIAL INVESTIGATION
```

Traditional mystery experiences generally focus on:

```text
Clue → Solution
```

Social networks generally focus on:

```text
Content → Reaction → Discussion
```

AfterWords focuses on:

```text
Case
 ↓
Investigation
 ↓
Evidence
 ↓
Understanding
 ↓
Uncertainty
 ↓
Dilemma
 ↓
Structured Debate
```

The experience therefore continues even when the "mystery" itself does not have a definitive solution.

---

# 20. What AfterWords Is NOT

AfterWords is **not**:

* A traditional social-media platform
* A generic discussion forum
* A news website
* A simple mystery game
* A crowdsourced accusation platform
* An AI that decides what is true
* A voting system for determining facts
* A platform where popularity determines truth
* A replacement for professional journalism, legal proceedings, or academic research

AfterWords provides a structured environment for investigation and discussion.

---

# 21. Initial Product Scope

The initial version of AfterWords will focus on:

```text
CASE DISCOVERY
        ↓
CASE INVESTIGATION
        ↓
EVIDENCE
        ↓
FACT SYNTHESIS
        ↓
DILEMMA
        ↓
STRUCTURED DEBATE
```

The MVP should prioritize the quality of this loop over the number of social features.

---

# 22. Long-Term Vision

The long-term AfterWords platform could evolve into a large ecosystem of:

```text
Cases
Investigations
Evidence
Researchers
Contributors
Debaters
Communities
AI investigation tools
```

Potential future capabilities include:

* Advanced case graphs
* Collaborative investigation workspaces
* Sophisticated reputation systems
* Personalized Case discovery
* Advanced AI research assistants
* Real-time investigation
* Community-created Cases
* Expert participation
* Cross-case knowledge discovery
* Investigation archives

These are future possibilities and are not part of the initial MVP.

---

# 23. One-Sentence Definition

> **AfterWords is a social investigation platform where people collaboratively examine evidence from real-world cases, establish what is known and uncertain, and then debate the deeper questions those cases leave behind.**

---

# 24. Core Product Equation

The simplest way to think about AfterWords is:

```text
MYSTERY
    +
INVESTIGATION
    +
EVIDENCE
    +
SOCIAL COLLABORATION
    +
STRUCTURED DEBATE
    =
AFTERWORDS
```

And the fundamental user experience is:

```text
            "I found something interesting."
                         ↓
            "I want to understand it."
                         ↓
            "I'll investigate it."
                         ↓
            "What does the evidence say?"
                         ↓
            "What is still uncertain?"
                         ↓
            "What should we think about this?"
                         ↓
            "Let's debate."
```
