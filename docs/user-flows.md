# AfterWords — User Flows

## 1. Purpose

This document defines the primary user journeys and interactions within AfterWords.

The goal is to establish how users move through the product before implementation begins.

The core experience is:

```text
DISCOVER
   ↓
UNDERSTAND
   ↓
INVESTIGATE
   ↓
CONTRIBUTE
   ↓
REVIEW
   ↓
SYNTHESIZE
   ↓
DEBATE
   ↓
RETURN
```

---

# 2. User Types

AfterWords supports the following user types:

```text
Guest
Registered User
Contributor
Investigator
Debater
Trusted Contributor
Moderator
Admin
```

These are primarily capability levels rather than completely separate account types.

A user can participate in multiple activities simultaneously.

For example:

```text
Registered User
      ↓
Contributor
      ↓
Investigator
      ↓
Debater
```

---

# 3. Global Navigation

The primary application navigation should contain:

```text
Home
Explore
Investigate
Debate
Saved
Notifications
Profile
```

Authenticated users can access all relevant features based on their permissions.

Guests primarily have access to:

```text
Home
Explore
Case Pages
Public Profiles
```

---

# 4. Guest Flow

A guest should be able to understand the product without creating an account.

```text
Landing Page
      ↓
Explore Cases
      ↓
Open Case
      ↓
Read Overview
      ↓
Explore Timeline
      ↓
View Evidence
      ↓
Read Fact Synthesis
      ↓
Read Dilemma
      ↓
Read Debate
      ↓
Register / Login
```

### Guest capabilities

Guests can:

* Browse Cases
* Search Cases
* Filter Cases
* Read Case stories
* View public evidence
* View timelines
* Read fact synthesis
* Read debates
* View public profiles

When a guest attempts an authenticated action:

```text
Guest
  ↓
Authenticated Action
  ↓
Login/Register Prompt
```

Examples:

```text
Follow Case
Submit Evidence
Comment
Create Argument
React
Save Case
```

---

# 5. Registration Flow

```text
Landing Page
      ↓
Register
      ↓
Email / Username / Password
      ↓
Account Created
      ↓
Basic Profile Setup
      ↓
Home
```

The initial registration process should remain simple.

Do not require users to configure complicated interests, reputation settings, or roles during registration.

---

# 6. Login Flow

```text
Login
  ↓
Credentials
  ↓
Authentication
  ↓
Home
```

If authentication fails:

```text
Invalid Credentials
       ↓
Error Message
       ↓
Retry / Password Recovery
```

---

# 7. Home Flow

The Home page is the user's primary starting point after authentication.

```text
Home
 │
 ├── Featured Cases
 ├── Recently Active Cases
 ├── Cases You Follow
 ├── Recommended Cases
 └── Recent Activity
```

The initial MVP can keep recommendations simple.

The home page should encourage users to enter a Case rather than endlessly scroll through generic social content.

---

# 8. Explore Cases Flow

```text
Explore
   ↓
Browse Cases
   ↓
Search / Filter
   ↓
Case Cards
   ↓
Open Case
```

Users should be able to filter by:

```text
Category
Case Status
Activity
Date
```

Potential categories include:

```text
Mystery
History
Technology
Science
Society
Ethics
Environment
Corporate
Law
Culture
```

---

# 9. Case Entry Flow

When a user opens a Case:

```text
Case Card
   ↓
Case Overview
```

The Case page should provide a clear progression:

```text
Overview
   ↓
Timeline
   ↓
Evidence
   ↓
Investigation
   ↓
Fact Synthesis
   ↓
Dilemma
   ↓
Debate
```

Users should not be forced to follow this order.

The interface should allow navigation between sections.

However, the product should visually communicate the intended journey.

---

# 10. Case Overview Flow

The Overview introduces the Case.

```text
Case
 │
 ├── Title
 ├── Short Description
 ├── Category
 ├── Status
 ├── Case Image
 ├── Key Question
 └── Start Investigation
```

The user should quickly understand:

* What happened?
* Why is this Case interesting?
* What is currently unknown?
* Why should I investigate it?

---

# 11. Timeline Flow

Users can inspect important events chronologically.

```text
Case
 ↓
Timeline
 ↓
Event
 ↓
Event Details
 ↓
Related Evidence
```

A timeline event may connect to:

```text
People
Organizations
Locations
Evidence
Sources
Other Events
```

Example:

```text
2008
 ↓
Event A
 ↓
Document X

2010
 ↓
Event B
 ↓
Interview Y

2012
 ↓
Event C
 ↓
Evidence Z
```

---

# 12. Evidence Exploration Flow

```text
Case
 ↓
Evidence
 ↓
Evidence List
 ↓
Open Evidence
 ↓
View Details
 ↓
View Source
 ↓
View Related Claims
```

Each Evidence item should communicate:

```text
What is this?
Where did it come from?
Who submitted it?
What does it support?
Is it verified?
Is it disputed?
```

---

# 13. Investigation Flow

This is the central interactive flow.

```text
Open Case
    ↓
Read Existing Information
    ↓
Explore Evidence
    ↓
Explore Sources
    ↓
Identify Question
    ↓
Search / Research
    ↓
Find Relevant Information
    ↓
Submit Contribution
```

A user may submit:

```text
Evidence
Source
Timeline Event
Entity
Question
Hypothesis
Finding
Correction
```

---

# 14. Evidence Submission Flow

```text
Case
 ↓
Submit Evidence
 ↓
Select Evidence Type
 ↓
Enter Title
 ↓
Enter Description
 ↓
Add Source
 ↓
Add URL / Reference
 ↓
Explain Relevance
 ↓
Submit
 ↓
PENDING
```

The user should see:

```text
Your contribution has been submitted for review.
```

The evidence then enters:

```text
PENDING
   ↓
UNDER REVIEW
   ↓
VERIFIED
   OR
DISPUTED
   OR
REJECTED
```

---

# 15. Contribution Tracking Flow

Users should be able to see the status of their contributions.

```text
Profile
 ↓
My Contributions
 ↓
Contribution
 ↓
Status
```

Possible statuses:

```text
Pending
Under Review
Accepted
Disputed
Rejected
```

This prevents users from submitting information and having no idea what happened afterward.

---

# 16. Investigation Hypothesis Flow

Investigators can propose explanations.

```text
Case
 ↓
Investigation
 ↓
Create Hypothesis
 ↓
Explain Hypothesis
 ↓
Attach Supporting Evidence
 ↓
Attach Contradicting Evidence
 ↓
Submit
```

A Hypothesis should not automatically become a Case fact.

It remains:

```text
HYPOTHESIS
```

until sufficient evidence changes its status or it is incorporated into the Case's findings.

---

# 17. Fact Synthesis Flow

Once sufficient evidence has been reviewed:

```text
Evidence
   ↓
Review
   ↓
Fact Synthesis
```

Users can view:

```text
CONFIRMED
SUPPORTED
DISPUTED
UNKNOWN
```

For example:

```text
CONFIRMED
3 facts

SUPPORTED
5 claims

DISPUTED
2 claims

UNKNOWN
4 unresolved questions
```

The purpose is to give users a shared factual foundation before the debate begins.

---

# 18. Dilemma Flow

After understanding the Case:

```text
Fact Synthesis
      ↓
Dilemma
```

The Dilemma presents:

```text
Context
    ↓
Known Facts
    ↓
Relevant Uncertainty
    ↓
Central Question
```

Example:

```text
Should an organization disclose information
that could protect the public if disclosure
could also put vulnerable individuals at risk?
```

The user can then:

```text
Read Arguments
      ↓
Explore Positions
      ↓
Join Debate
```

---

# 19. Debate Flow

The core debate journey is:

```text
Dilemma
   ↓
View Positions
   ↓
Choose / Express Position
   ↓
Create Argument
   ↓
Attach Evidence
   ↓
Publish
   ↓
Receive Responses
   ↓
Respond / Counter
```

Arguments should remain attached to the Case.

---

# 20. Creating an Argument

```text
Create Argument
       ↓
Select Position
       ↓
Write Argument
       ↓
Attach Evidence
       ↓
Preview
       ↓
Publish
```

An Argument can contain:

```text
Position
Title
Body
Evidence References
Author
Timestamp
```

---

# 21. Counterargument Flow

```text
Argument
   ↓
Challenge
   ↓
Create Counterargument
   ↓
Write Response
   ↓
Attach Evidence
   ↓
Publish
```

Users should be encouraged to challenge ideas rather than people.

---

# 22. Social Interaction Flow

Users can interact with Cases and users through:

```text
Follow
Save
React
Comment
Share
```

### Follow Case

```text
Case
 ↓
Follow
 ↓
Case appears in Saved/Following
 ↓
Receive relevant notifications
```

### Save Case

```text
Case
 ↓
Save
 ↓
Saved Cases
```

### Follow User

```text
Profile
 ↓
Follow
 ↓
User activity becomes visible
```

---

# 23. Notification Flow

Users may receive notifications when:

```text
Someone responds to your Argument
Someone responds to your Comment
Your Evidence is reviewed
Your contribution is disputed
A followed Case changes stage
A followed Case receives important activity
Someone interacts with your contribution
```

MVP notifications can be simple in-app notifications.

Email and push notifications can be added later.

---

# 24. Profile Flow

```text
Profile
 │
 ├── About
 ├── Cases Following
 ├── Contributions
 ├── Investigations
 ├── Arguments
 └── Activity
```

A public profile should communicate what the user has contributed without turning the platform into a follower-count competition.

---

# 25. Trusted Contributor Flow

Trusted status is initially controlled by administrators.

```text
User
 ↓
Consistent Contributions
 ↓
Admin Review
 ↓
Trusted Status
```

A Trusted Contributor may later receive:

```text
Additional contribution visibility
Evidence review capabilities
Community assistance privileges
```

Complex automated reputation calculations are outside the MVP.

---

# 26. Moderation Flow

Users can report problematic content.

```text
Content
 ↓
Report
 ↓
Select Reason
 ↓
Submit
 ↓
MODERATION QUEUE
 ↓
Moderator Review
 ↓
Action
```

Possible actions:

```text
No Action
Warning
Hide
Remove
Restrict User
Escalate
```

---

# 27. Evidence Moderation Flow

```text
Evidence Submitted
       ↓
PENDING
       ↓
Review
       ↓
┌──────┼─────────┐
↓      ↓         ↓
VERIFY DISPUTE  REJECT
```

A disputed contribution should not simply disappear.

It should remain clearly marked as disputed when appropriate so users understand that disagreement exists.

---

# 28. Case Creation Flow

Initial Case creation should be controlled.

```text
Admin / Authorized Creator
          ↓
     Create Case
          ↓
     Add Background
          ↓
     Add Initial Sources
          ↓
     Add Initial Timeline
          ↓
     Add Initial Evidence
          ↓
        DRAFT
          ↓
      Publish Case
          ↓
    INVESTIGATION
```

Community-created Cases can be introduced later.

---

# 29. Case Lifecycle Flow

The overall lifecycle is:

```text
                         ┌───────────────┐
                         │     DRAFT     │
                         └───────┬───────┘
                                 ↓
                         ┌───────────────┐
                         │ INVESTIGATION │
                         └───────┬───────┘
                                 ↓
                      ┌─────────────────────┐
                      │   EVIDENCE_REVIEW   │
                      └──────────┬──────────┘
                                 ↓
                      ┌─────────────────────┐
                      │   FACT_SYNTHESIS    │
                      └──────────┬──────────┘
                                 ↓
                         ┌───────────────┐
                         │    DEBATE     │
                         └───────┬───────┘
                                 ↓
                         ┌───────────────┐
                         │    RESOLVED   │
                         └───────┬───────┘
                                 ↓
                         ┌───────────────┐
                         │    ARCHIVED   │
                         └───────────────┘
```

Each stage controls what actions are available.

---

# 30. End-to-End User Journey

The complete AfterWords journey is:

```text
                    LANDING
                       ↓
                    EXPLORE
                       ↓
                     CASE
                       ↓
              ┌────────┴────────┐
              ↓                 ↓
           STORY             TIMELINE
              │                 │
              └────────┬────────┘
                       ↓
                    EVIDENCE
                       ↓
                  INVESTIGATION
                       ↓
              ┌────────┼────────┐
              ↓        ↓        ↓
           SOURCES  HYPOTHESES QUESTIONS
              │        │        │
              └────────┼────────┘
                       ↓
                FACT SYNTHESIS
                       ↓
              ┌────────┼────────┐
              ↓        ↓        ↓
           CONFIRMED SUPPORTED DISPUTED
                       │
                       ↓
                    UNKNOWN
                       ↓
                    DILEMMA
                       ↓
                    DEBATE
                       ↓
              ┌────────┼────────┐
              ↓        ↓        ↓
          ARGUMENT  COUNTER   RESPONSE
              │        │        │
              └────────┼────────┘
                       ↓
                 CONCLUSION
                       ↓
                 FOLLOW CASE
                       ↓
                RETURN LATER
```

---

# 31. Core UX Principles

### Minimize Friction

A user should be able to go from:

```text
"I found something"
```

to:

```text
"I contributed it"
```

with minimal steps.

### Make Context Visible

Users should always understand:

```text
Where am I?
What stage is this Case in?
What is known?
What is uncertain?
What can I contribute?
```

### Encourage Investigation

The interface should make the next investigative action obvious.

### Separate Facts From Opinions

Users should clearly distinguish between:

```text
Evidence
Facts
Claims
Hypotheses
Arguments
Opinions
```

### Keep Debate Connected to Evidence

Arguments should be easy to connect back to Case evidence.

---

# 32. MVP User Journey

The minimum complete user experience is:

```text
REGISTER
   ↓
EXPLORE
   ↓
OPEN CASE
   ↓
READ STORY
   ↓
VIEW EVIDENCE
   ↓
SUBMIT CONTRIBUTION
   ↓
VIEW FACT SYNTHESIS
   ↓
READ DILEMMA
   ↓
CREATE ARGUMENT
   ↓
RESPOND TO ARGUMENT
   ↓
FOLLOW CASE
```

If this journey works smoothly, the fundamental AfterWords experience works.

---

# 33. Product Flow Summary

The entire product can be reduced to:

```text
              AFTERWORDS
                  │
                  ↓
              DISCOVER
                  │
                  ↓
                CASE
                  │
                  ↓
             INVESTIGATE
                  │
                  ↓
               EVIDENCE
                  │
                  ↓
           FACT SYNTHESIS
                  │
                  ↓
               DILEMMA
                  │
                  ↓
                DEBATE
                  │
                  ↓
             CONCLUSION
```
