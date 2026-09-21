# AfterWords — MVP Specification

## 1. Purpose

This document defines the first practical version of AfterWords.

The MVP should prove the core product hypothesis:

> **People will investigate a structured Case, examine evidence, form their own understanding, and participate in evidence-grounded debate around the resulting dilemma.**

The MVP should not attempt to build every long-term feature.

The goal is to build the smallest complete version of the AfterWords experience.

---

# 2. MVP Product Loop

The MVP must support this complete loop:

```text
REGISTER
   ↓
EXPLORE CASE
   ↓
OPEN CASE
   ↓
READ STORY
   ↓
EXPLORE TIMELINE
   ↓
EXPLORE EVIDENCE
   ↓
INVESTIGATE
   ↓
SUBMIT CONTRIBUTION
   ↓
FACT SYNTHESIS
   ↓
READ DILEMMA
   ↓
CHOOSE / CREATE POSITION
   ↓
CREATE ARGUMENT
   ↓
RESPOND TO ARGUMENT
   ↓
FOLLOW CASE
```

If this loop works, the MVP demonstrates the fundamental AfterWords concept.

---

# 3. MVP Goals

The MVP should prove five things.

### Goal 1 — Case Exploration

Users can understand a Case without needing external context.

### Goal 2 — Investigation

Users can contribute useful information.

### Goal 3 — Evidence Structure

Information is connected to sources and evidence.

### Goal 4 — Debate

Users can discuss the Case's central dilemma in a structured format.

### Goal 5 — Social Retention

Users have reasons to return to Cases and conversations.

---

# 4. MVP Users

The MVP requires only a small number of user roles.

```text
Guest
Registered User
Contributor
Moderator
Admin
```

Additional roles such as Trusted Contributor and Investigator can be introduced later using the same permission architecture.

---

# 5. Guest Experience

Guests should be able to:

* View landing page
* Explore public Cases
* Open Cases
* Read Case stories
* View timelines
* View evidence
* Read fact synthesis
* Read dilemmas
* Read debates

Guests cannot:

* Submit evidence
* Create arguments
* Follow Cases
* React
* Comment
* Participate in investigation

The conversion path is:

```text
Guest
 ↓
Explore Case
 ↓
Become Interested
 ↓
Attempt Contribution / Debate
 ↓
Register
```

---

# 6. Authentication

The MVP should support:

* Registration
* Login
* Logout
* Session management
* Basic profile

Optional initial authentication methods:

```text
Email + Password
```

Social login can be added later.

---

# 7. User Profile

The MVP profile should contain:

* Username
* Display name
* Profile image
* Short bio
* Cases followed
* Contributions
* Arguments
* Activity

Example:

```text
PROFILE

Username
Bio

Following
├── Case A
├── Case B
└── Case C

Contributions
├── Evidence
├── Questions
└── Findings

Debate
├── Arguments
└── Responses
```

---

# 8. Home Page

The MVP home page should primarily help users discover Cases.

Possible sections:

```text
HOME

Featured Cases
Trending Cases
Recently Updated
Recently Discussed
New Cases
```

The home page should not become a generic social feed.

The Case remains the primary object.

---

# 9. Explore Page

Users should be able to browse Cases.

Minimum functionality:

* Search
* Category filtering
* Tag filtering
* Sort by recent
* Sort by active discussion
* Sort by popular

Example:

```text
Explore Cases

[ Search Cases ]

Categories:
Mystery
Technology
History
Science
Society
Ethics
Environment
Corporate
Law
Culture
```

---

# 10. Case Page

The Case page is the most important MVP interface.

Recommended structure:

```text
┌──────────────────────────────────────────┐
│ CASE HEADER                              │
│                                          │
│ Title                                    │
│ Category / Tags                          │
│ Description                              │
│ Follow Case                              │
└──────────────────────────────────────────┘

┌──────────────────────────────────────────┐
│ STORY                                    │
└──────────────────────────────────────────┘

┌──────────────────────────────────────────┐
│ TIMELINE                                 │
└──────────────────────────────────────────┘

┌──────────────────────────────────────────┐
│ EVIDENCE                                 │
└──────────────────────────────────────────┘

┌──────────────────────────────────────────┐
│ FACT SYNTHESIS                           │
└──────────────────────────────────────────┘

┌──────────────────────────────────────────┐
│ DILEMMA                                  │
└──────────────────────────────────────────┘

┌──────────────────────────────────────────┐
│ DEBATE                                   │
└──────────────────────────────────────────┘
```

The user should be able to understand the Case without navigating through dozens of pages.

---

# 11. Case Story

The Case Story is the narrative introduction.

It should answer:

* What happened?
* Why is this Case interesting?
* Why is it unresolved?
* What should the user investigate?

The story should not reveal unsupported conclusions.

The story is an entry point into the investigation.

---

# 12. Timeline MVP

The MVP timeline should support:

* Date
* Event title
* Description
* Related entities
* Evidence references

Example:

```text
2019
│
├── Event A
│
2020
│
├── Event B
│
2021
│
└── Event C
```

Advanced timeline visualization can come later.

---

# 13. Evidence MVP

The MVP must allow users to:

* View evidence
* Filter evidence
* Open source
* See evidence status
* See contributor
* See related facts
* Submit new evidence

Evidence card:

```text
Evidence #42

Title:
...

Type:
Article

Status:
Verified

Source:
...

Submitted by:
...

Why it matters:
...

Related:
Fact #7
Timeline Event #4
```

---

# 14. Evidence Submission MVP

User flow:

```text
Submit Evidence
       ↓
Title
       ↓
Description
       ↓
Evidence Type
       ↓
Source
       ↓
URL / Reference
       ↓
Why is this relevant?
       ↓
Submit
```

After submission:

```text
PENDING
```

A moderator/admin can then:

```text
VERIFY
DISPUTE
REJECT
```

---

# 15. Fact Synthesis MVP

The MVP should display four categories:

```text
CONFIRMED
SUPPORTED
DISPUTED
UNKNOWN
```

Example:

```text
WHAT WE KNOW

CONFIRMED
✓ Event occurred on X date.

SUPPORTED
~ Organization received warnings.

DISPUTED
! Exact sequence of events remains contested.

UNKNOWN
? Who made the final decision.
```

This section is one of the most important differentiators of the product.

---

# 16. Dilemma MVP

Each Case should have one primary dilemma in the MVP.

The dilemma should contain:

```text
Central Question
Relevant Facts
Important Uncertainties
```

Example:

```text
THE DILEMMA

Should the organization have continued
with the deployment despite the known risks?

Relevant facts:
...

Uncertainties:
...
```

---

# 17. Debate MVP

The MVP debate should support:

* View positions
* Create position
* Create argument
* Attach evidence
* Respond
* Counterargument
* React
* Report

The initial interface can remain relatively simple.

```text
DILEMMA
   ↓
POSITIONS
   ↓
ARGUMENTS
   ↓
RESPONSES
```

Advanced debate graphs can come later.

---

# 18. Argument MVP

An argument should contain:

```text
Position
Argument text
Optional Case evidence
Optional source
Author
Timestamp
```

The basic creation flow:

```text
Choose Position
      ↓
Write Argument
      ↓
Attach Evidence
      ↓
Publish
```

---

# 19. Response MVP

Users should be able to respond to arguments.

Initial response types can remain simple:

```text
Reply
Counterargument
Question
```

Example:

```text
Argument
   ↓
Counterargument
   ↓
Response
```

Do not build deeply nested Reddit-style comments in the first version.

Keep discussion focused around arguments.

---

# 20. Following Cases

Users should be able to follow a Case.

Following allows notifications when:

* New evidence is accepted
* Important Case information changes
* Debate activity increases
* New arguments appear
* Case enters a new lifecycle stage

The Case remains the central social object.

---

# 21. Notifications MVP

Initial notification types:

```text
CASE_UPDATE
EVIDENCE_ACCEPTED
EVIDENCE_DISPUTED
ARGUMENT_REPLY
COUNTERARGUMENT
CASE_STAGE_CHANGED
```

Notifications should link directly to the relevant Case or discussion.

---

# 22. Search MVP

Search should support:

* Case title
* Case description
* Tags
* Categories
* Evidence titles
* Entity names

Later versions can introduce semantic search.

MVP search can initially use PostgreSQL full-text search or another simple search mechanism.

---

# 23. Moderation MVP

The MVP requires basic moderation.

Moderators should be able to:

* Review reported content
* Review evidence
* Verify evidence
* Dispute evidence
* Reject evidence
* Hide content
* Remove content
* Suspend users
* Review Case contributions

Admin users should have broader Case management permissions.

---

# 24. Reporting

Users should be able to report:

```text
Spam
Harassment
Hate
Misinformation
Unverified accusation
Personal information
Manipulated media
Copyright
Other
```

A report should contain:

```text
Reporter
Target content
Reason
Description
Timestamp
Status
```

---

# 25. Admin Case Creation

The MVP should initially use controlled Case creation.

An admin/editor creates:

```text
Case
 ↓
Story
 ↓
Initial Sources
 ↓
Timeline
 ↓
Entities
 ↓
Initial Evidence
 ↓
Fact Synthesis
 ↓
Dilemma
 ↓
Publish Investigation
```

This avoids launching with an empty platform.

---

# 26. Seed Cases

The MVP should launch with multiple high-quality Cases.

Recommended starting point:

```text
5–10 Cases
```

Each Case should have:

* Complete story
* Timeline
* Multiple sources
* Evidence
* Fact synthesis
* Dilemma
* Initial debate positions
* At least some example arguments

A completely empty social platform makes it difficult to test the product loop.

---

# 27. Case Quality Standard

Before a Case enters public investigation, it should have:

```text
✓ Clear story
✓ Defined investigation question
✓ Initial timeline
✓ Initial entities
✓ Multiple sources
✓ Initial evidence
✓ Clear uncertainties
✓ Dilemma
```

The Case should not simply be:

> "Here is an interesting story. Discuss."

It needs an investigation structure.

---

# 28. AI MVP

AI should **not** be the foundation of the MVP.

The MVP can initially implement limited AI functionality.

Recommended first AI capabilities:

### Source Summarization

Help users understand long sources.

### Evidence Summarization

Summarize collections of evidence.

### Timeline Extraction

Suggest timeline events from sources.

### Related Evidence

Suggest evidence relevant to an argument.

### Case Question Suggestions

Identify potentially unanswered questions.

### Debate Summary

Summarize long discussions.

AI outputs should be marked as AI-generated or AI-assisted.

Human-reviewed Case information remains authoritative.

---

# 29. Features Explicitly Outside MVP

The following should not block the initial launch.

### Advanced AI Investigator

Future feature.

### Autonomous Case Creation

Future feature.

### Real-time collaborative investigation

Future feature.

### Advanced investigation graph

Future feature.

### Reputation system

Future feature.

### Gamification

Future feature.

### Achievements

Future feature.

### Advanced recommendation engine

Future feature.

### Semantic search

Future feature.

### Mobile application

Future feature.

### Dedicated graph database

Future feature.

### Advanced moderation AI

Future feature.

### Real-time debate rooms

Future feature.

### Complex voting mechanisms

Future feature.

The MVP should remain focused.

---

# 30. MVP Navigation

Recommended navigation:

```text
┌──────────────────────────────────────────────┐
│ AfterWords                                   │
│                                              │
│ Home   Explore   Following   Notifications   │
│                                              │
│ Search                                       │
│                                              │
│ Profile                                      │
└──────────────────────────────────────────────┘
```

Inside a Case:

```text
Case
├── Story
├── Timeline
├── Evidence
├── Investigation
├── Facts
├── Dilemma
└── Debate
```

---

# 31. MVP Screens

The first implementation should aim for approximately these major screens:

```text
1. Landing Page
2. Login
3. Register
4. Home
5. Explore Cases
6. Case Page
7. Investigation / Evidence
8. Submit Evidence
9. Fact Synthesis
10. Debate
11. Create Argument
12. Profile
13. Notifications
14. Moderator Dashboard
15. Admin Case Editor
```

Some can be implemented as sections of the same page rather than separate routes.

---

# 32. MVP Backend Capabilities

The backend must support:

```text
Authentication
User Profiles
Cases
Categories
Tags
Sources
Evidence
Timeline Events
Entities
Claims
Hypotheses
Findings
Fact Synthesis
Dilemmas
Positions
Arguments
Responses
Reactions
Reports
Notifications
Moderation
```

The exact API design belongs to Phase 2.

---

# 33. MVP Data Relationship

The conceptual backend relationship is:

```text
USER
 │
 ├── follows → CASE
 ├── submits → EVIDENCE
 ├── creates → HYPOTHESIS
 ├── creates → FINDING
 ├── chooses → POSITION
 ├── creates → ARGUMENT
 ├── responds → ARGUMENT
 └── reports → CONTENT

CASE
 │
 ├── has → SOURCES
 ├── has → EVIDENCE
 ├── has → TIMELINE
 ├── has → ENTITIES
 ├── has → CLAIMS
 ├── has → HYPOTHESES
 ├── has → FINDINGS
 ├── has → FACT SYNTHESIS
 └── has → DILEMMA

DILEMMA
 │
 └── has → POSITIONS

POSITION
 │
 └── has → ARGUMENTS

ARGUMENT
 │
 ├── references → EVIDENCE
 ├── references → SOURCES
 └── receives → RESPONSES
```

---

# 34. MVP Technical Boundaries

The MVP should be designed so that the product can later scale without requiring a complete rewrite.

The initial architecture should therefore keep clear boundaries between:

```text
Frontend
   ↓
API
   ↓
Business Logic
   ↓
Database
   ↓
AI Services
```

Recommended conceptual architecture:

```text
React
  ↓
FastAPI
  ↓
PostgreSQL
  ↓
AI / Background Services
```

The exact architecture will be defined in Phase 2.

---

# 35. MVP Non-Functional Requirements

The MVP should prioritize:

### Reliability

Core Case and contribution data should not be easily lost.

### Traceability

Important changes should preserve authorship/history.

### Security

Authentication, authorization, and user-generated content must be protected.

### Moderation

Users must have reporting and moderation mechanisms.

### Performance

Case pages should load quickly even with substantial evidence.

### Extensibility

The architecture should allow future AI and graph features.

---

# 36. MVP Success Criteria

The MVP is successful if a new user can complete this journey without assistance:

```text
LANDING
   ↓
DISCOVER CASE
   ↓
READ CASE
   ↓
UNDERSTAND TIMELINE
   ↓
EXPLORE EVIDENCE
   ↓
UNDERSTAND FACT SYNTHESIS
   ↓
UNDERSTAND DILEMMA
   ↓
READ ARGUMENTS
   ↓
CREATE ARGUMENT
   ↓
ATTACH EVIDENCE
   ↓
RECEIVE RESPONSE
   ↓
RETURN TO CASE
```

A second success criterion is contribution:

```text
User finds information
       ↓
Submits evidence
       ↓
Evidence reviewed
       ↓
Case improves
```

A third is reconsideration:

```text
User reads evidence
       ↓
Forms position
       ↓
Reads counterargument
       ↓
Reviews evidence
       ↓
Refines position
```

---

# 37. MVP Product Metrics

The first version should measure behavior rather than vanity metrics.

Important metrics:

### Case Engagement

* Cases opened
* Average Case reading time
* Timeline interactions
* Evidence interactions

### Investigation

* Evidence submissions
* Accepted evidence
* Disputed evidence
* Questions submitted
* Hypotheses submitted

### Debate

* Arguments created
* Evidence-backed arguments
* Counterarguments
* Questions
* Responses
* Position changes

### Retention

* Users returning to Cases
* Users following Cases
* Users contributing to multiple Cases

### Conversion

```text
Guest
 ↓
Registered User
 ↓
Contributor
 ↓
Returning Contributor
```

---

# 38. MVP Anti-Goals

The MVP should explicitly avoid becoming:

### A News Website

The Case is more structured than an article.

### Reddit Clone

Discussion is attached to structured Cases and arguments.

### Twitter/X Clone

The product is not primarily a short-form feed.

### Wikipedia Clone

Users investigate collaboratively, but the product culminates in a dilemma and debate.

### Online Court

AfterWords does not determine guilt or deliver authoritative verdicts.

### AI Answer Engine

AI assists investigation but does not replace human judgment.

### Mystery Game

The Cases may be mysterious, but the product is built around real investigation and reasoning rather than fictional gameplay.

---

# 39. MVP Scope Summary

```text
┌─────────────────────────────────────────────┐
│                  MVP                        │
├─────────────────────────────────────────────┤
│                                             │
│ Authentication                               │
│        ↓                                    │
│ Case Discovery                               │
│        ↓                                    │
│ Case Exploration                             │
│        ↓                                    │
│ Timeline + Evidence                          │
│        ↓                                    │
│ Community Investigation                      │
│        ↓                                    │
│ Evidence Review                              │
│        ↓                                    │
│ Fact Synthesis                               │
│        ↓                                    │
│ Dilemma                                      │
│        ↓                                    │
│ Structured Debate                            │
│        ↓                                    │
│ Arguments + Responses                        │
│        ↓                                    │
│ Follow Cases + Notifications                 │
│        ↓                                    │
│ Moderation                                   │
│                                             │
└─────────────────────────────────────────────┘
```

---

# 40. Phase 1 Completion Definition

Phase 1 is complete when the following are clearly defined:

```text
✓ Product concept
✓ Target users
✓ User roles
✓ Core product loop
✓ User flows
✓ Case structure
✓ Case lifecycle
✓ Investigation model
✓ Evidence model
✓ Source model
✓ Timeline
✓ Entities
✓ Claims
✓ Hypotheses
✓ Findings
✓ Fact synthesis
✓ Dilemma
✓ Debate model
✓ Positions
✓ Arguments
✓ Counterarguments
✓ Moderation
✓ MVP scope
✓ MVP screens
✓ MVP capabilities
✓ MVP success criteria
```

At this point, the product should be sufficiently defined to begin technical architecture.

---

# 41. Final Product Definition

The complete AfterWords system can now be represented as:

```text
                         AFTERWORDS
                              │
              ┌───────────────┴───────────────┐
              │                               │
           CASE SYSTEM                   SOCIAL SYSTEM
              │                               │
       ┌──────┴──────┐                 ┌──────┴──────┐
       │             │                 │             │
   INVESTIGATION  FACTS             POSITIONS    DEBATE
       │             │                 │             │
   Evidence      Synthesis          Arguments    Responses
   Sources          │                 │             │
   Timeline         │                 └──────┬──────┘
   Entities         │                        │
   Claims           │                   Reconsideration
   Hypotheses       │
   Findings         │
       └─────────────┴──────────┐
                                ↓
                             DILEMMA
                                │
                                ↓
                         HUMAN JUDGMENT
```

The fundamental product loop is:

```text
DISCOVER
   ↓
INVESTIGATE
   ↓
VERIFY
   ↓
UNDERSTAND
   ↓
DEBATE
   ↓
RECONSIDER
```
