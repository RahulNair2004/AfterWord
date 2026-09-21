# AfterWords — Database Architecture

## 1. Purpose

This document defines the database architecture for AfterWords.

The database will be designed around:

* PostgreSQL
* SQLAlchemy
* Alembic
* Relational data modeling
* Strong foreign-key relationships
* Transactions
* Constraints
* Indexing
* Full-text search where appropriate
* JSONB only for genuinely flexible data

PostgreSQL will be the **primary source of truth** for all application data.

---

# 2. Database Architecture

The initial architecture uses a single PostgreSQL database.

```text
                    AfterWords Backend
                           │
                           ▼
                    SQLAlchemy ORM
                           │
                           ▼
                     PostgreSQL
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
     Users             Cases             Investigations
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                           ▼
                 Evidence / Clues / Theories
                           │
                           ▼
                   Social / Activity
```

There will not initially be separate databases for individual modules.

---

# 3. Database Responsibilities

PostgreSQL stores:

* User accounts
* Profiles
* Authentication-related metadata
* Cases
* Case categories
* Investigations
* Investigation membership
* Evidence
* Evidence sources
* Clues
* Theories
* Theory relationships
* Comments
* Reactions
* Follows
* Bookmarks/saves
* Notifications
* Reports
* Moderation records
* Search metadata
* Recommendation-related metadata
* Activity records
* Media metadata
* AI-generated metadata where persistence is required

Actual uploaded files will be stored in Amazon S3.

---

# 4. Logical Database Domains

The database will be organized logically around the following domains:

```text
Users
  │
  ├── Authentication
  ├── Profiles
  └── Social

Cases
  │
  ├── Case Metadata
  ├── Categories
  ├── Evidence
  ├── Clues
  └── Sources

Investigations
  │
  ├── Membership
  ├── Activity
  ├── Theories
  └── Collaboration

Community
  │
  ├── Comments
  ├── Reactions
  ├── Follows
  └── Bookmarks

Platform
  │
  ├── Notifications
  ├── Reports
  ├── Moderation
  └── Media

AI
  │
  ├── AI interactions
  ├── Generated content
  └── Embedding metadata
```

---

# 5. Primary Entities

The initial database will contain these major entities:

```text
users
profiles
cases
case_categories
case_category_map

investigations
investigation_members

evidence
evidence_sources
evidence_files

clues
clue_evidence

theories
theory_evidence
theory_clues

comments
reactions
follows
bookmarks

notifications
reports
moderation_actions

activities
media_files

ai_interactions
```

The exact schema will be finalized in the next **Data Model / ERD** step.

---

# 6. Users

The `users` table represents platform accounts.

Conceptually:

```text
users
-----
id
email
username
password_hash
status
role
created_at
updated_at
last_login_at
```

Important constraints:

* `id` is the primary key.
* Email must be unique.
* Username must be unique.
* Passwords are never stored in plaintext.
* Account status is controlled by the backend.
* Timestamps are stored consistently.

---

# 7. Profiles

Profile-specific information should remain separate from authentication data.

```text
profiles
--------
user_id
display_name
bio
avatar_media_id
location
website
created_at
updated_at
```

Relationship:

```text
users
  │
  │ 1:1
  ▼
profiles
```

This keeps authentication data separate from publicly displayed profile information.

---

# 8. Cases

Cases are one of the most important entities in AfterWords.

Conceptually:

```text
cases
-----
id
created_by
title
slug
description
status
difficulty
visibility
published_at
created_at
updated_at
```

Possible case states:

```text
draft
published
active
resolved
archived
```

The actual state machine will be defined during the Case Engine architecture step.

---

# 9. Case Categories

Cases may belong to multiple categories.

Examples:

```text
Unsolved
Historical
Disappearance
Crime
Mystery
Scientific
Paranormal
Logical
Moral Dilemma
```

Instead of storing multiple categories inside a single text field, use a many-to-many relationship.

```text
cases
  │
  ▼
case_category_map
  │
  ▼
case_categories
```

---

# 10. Investigations

An investigation represents a collaborative investigation around a case.

```text
investigations
--------------
id
case_id
created_by
title
description
status
visibility
created_at
updated_at
```

Relationship:

```text
Case
 │
 ├── Investigation A
 ├── Investigation B
 └── Investigation C
```

Multiple investigations can exist for the same case.

---

# 11. Investigation Members

Investigations require many-to-many membership.

```text
investigations
      │
      ▼
investigation_members
      │
      ▼
users
```

Conceptually:

```text
investigation_members
---------------------
investigation_id
user_id
role
status
joined_at
```

Possible roles:

```text
owner
member
moderator
```

---

# 12. Evidence

Evidence represents information relevant to a case or investigation.

```text
evidence
--------
id
case_id
investigation_id
created_by
title
description
evidence_type
verification_status
created_at
updated_at
```

Evidence may include:

* Documents
* Images
* Audio
* Video
* Statements
* Articles
* Records
* Physical evidence descriptions
* External sources

---

# 13. Evidence Sources

Evidence should maintain provenance.

```text
evidence_sources
----------------
id
evidence_id
source_type
source_title
source_url
publisher
author
published_at
accessed_at
source_metadata
```

This is important because AfterWords is an investigation platform and users should be able to distinguish:

```text
Evidence
   ↓
Source
   ↓
Origin
```

---

# 14. Evidence Files

Actual files should not be stored directly in PostgreSQL.

```text
evidence_files
--------------
id
evidence_id
media_file_id
file_type
created_at
```

Actual files:

```text
Amazon S3
```

Metadata:

```text
PostgreSQL
```

---

# 15. Clues

Clues represent potentially meaningful pieces of information discovered during investigations.

```text
clues
-----
id
case_id
investigation_id
created_by
title
description
status
importance
created_at
updated_at
```

Possible status values:

```text
unverified
active
confirmed
disproved
archived
```

---

# 16. Clue-Evidence Relationships

A clue can be connected to multiple evidence items.

```text
clues
  │
  ▼
clue_evidence
  │
  ▼
evidence
```

This allows investigation graphs such as:

```text
Clue A
 ├── Evidence 1
 ├── Evidence 3
 └── Evidence 7
```

---

# 17. Theories

Theories represent explanations or hypotheses proposed by users.

```text
theories
--------
id
case_id
investigation_id
created_by
title
description
status
created_at
updated_at
```

Possible states:

```text
proposed
under_review
supported
disputed
rejected
resolved
```

The exact state model will be finalized in the Investigation Engine step.

---

# 18. Theory-Evidence Relationships

Theories can be supported or contradicted by evidence.

```text
theory_evidence
---------------
theory_id
evidence_id
relationship
created_by
created_at
```

Possible relationships:

```text
supports
contradicts
contextual
```

This enables:

```text
Theory A
   │
   ├── Evidence 1 → supports
   ├── Evidence 4 → supports
   └── Evidence 8 → contradicts
```

---

# 19. Theory-Clue Relationships

Theories can also connect directly to clues.

```text
theory_clues
------------
theory_id
clue_id
relationship
created_by
created_at
```

This allows:

```text
Theory
  ├── Clue A
  ├── Clue D
  └── Clue F
```

---

# 20. Comments

Comments support discussions around:

* Cases
* Evidence
* Clues
* Theories
* Investigations

A flexible comment model can use:

```text
comments
--------
id
user_id
parent_comment_id
target_type
target_id
content
status
created_at
updated_at
```

However, polymorphic relationships require careful validation.

The implementation should ensure that `target_type` and `target_id` always refer to a valid resource.

For high-integrity relationships, dedicated relationship tables may be used later if the domain requires them.

---

# 21. Reactions

Users can react to community content.

```text
reactions
---------
id
user_id
target_type
target_id
reaction_type
created_at
```

Possible reactions:

```text
like
interesting
helpful
insightful
```

The available reactions will be finalized during the Social Architecture step.

A uniqueness constraint should prevent duplicate identical reactions from the same user.

---

# 22. Follows

Users can follow other users.

```text
follows
-------
follower_id
following_id
created_at
```

Constraint:

```text
UNIQUE(follower_id, following_id)
```

A user should not be able to follow themselves.

---

# 23. Bookmarks

Users can save content for later.

```text
bookmarks
---------
id
user_id
target_type
target_id
created_at
```

Potential targets:

```text
case
investigation
evidence
clue
theory
post
```

---

# 24. Notifications

Notifications are persisted in PostgreSQL.

```text
notifications
-------------
id
user_id
type
title
message
reference_type
reference_id
is_read
created_at
```

Examples:

```text
Someone joined your investigation.

Someone commented on your theory.

New evidence was added to an investigation.

Your theory received a reaction.
```

---

# 25. Activities

Activities record important platform actions.

```text
activities
----------
id
user_id
activity_type
target_type
target_id
metadata
created_at
```

Examples:

```text
created_case
joined_investigation
created_theory
added_evidence
solved_case
followed_user
```

Activities can later power:

* Feeds
* Notifications
* User activity history
* Analytics
* Recommendations

---

# 26. Reports

Users can report problematic content.

```text
reports
-------
id
reporter_id
target_type
target_id
reason
description
status
created_at
resolved_at
```

Possible statuses:

```text
pending
reviewing
resolved
dismissed
```

---

# 27. Moderation Actions

Moderator actions should be stored separately from reports.

```text
moderation_actions
------------------
id
moderator_id
target_type
target_id
action
reason
created_at
```

This provides an auditable moderation history.

---

# 28. Media Files

All uploaded files can have centralized metadata.

```text
media_files
-----------
id
owner_id
storage_provider
storage_key
file_name
mime_type
file_size
checksum
created_at
```

Example:

```text
PostgreSQL
    │
    └── media_files
             │
             └── S3 storage_key
                     │
                     ▼
                   S3
```

---

# 29. AI Interactions

AI-generated functionality may need persistence.

```text
ai_interactions
---------------
id
user_id
case_id
investigation_id
interaction_type
input_reference
output
model
created_at
```

Examples:

```text
case_summary
evidence_summary
theory_analysis
similar_cases
investigation_assistant
```

Sensitive or unnecessary AI conversation data should not be persisted indefinitely.

Retention policies will be defined later.

---

# 30. IDs

The system should use non-sequential public identifiers.

A UUID-based identifier strategy is recommended.

Example:

```text
id = UUID
```

Benefits:

* Difficult to enumerate
* Suitable for distributed systems later
* Safer public URLs
* Easier future scaling

Internal database relationships will still use indexed UUID values.

---

# 31. Primary Keys

Every major entity should have a primary key.

Example:

```text
users.id
cases.id
investigations.id
evidence.id
clues.id
theories.id
comments.id
notifications.id
```

Join tables may use composite primary keys where appropriate.

Example:

```text
follows
PRIMARY KEY (follower_id, following_id)
```

---

# 32. Foreign Keys

Relationships should use explicit foreign keys.

Example:

```text
investigations.case_id
        ↓
cases.id
```

Foreign keys prevent orphaned records.

Important relationships include:

```text
investigations.case_id → cases.id

investigation_members.investigation_id
    → investigations.id

investigation_members.user_id
    → users.id

evidence.case_id → cases.id

evidence.created_by → users.id

clues.case_id → cases.id

theories.case_id → cases.id

theories.created_by → users.id
```

---

# 33. Referential Integrity

Foreign-key behavior should be chosen according to the domain.

Examples:

### User deletion

Usually:

```text
RESTRICT
```

or an account-deactivation strategy rather than physically deleting all related content.

### Investigation deletion

Dependent memberships may use:

```text
CASCADE
```

### Evidence deletion

Dependent relationship records may use:

```text
CASCADE
```

The exact behavior will be specified during the ERD implementation.

---

# 34. Timestamps

Major tables should contain:

```text
created_at
updated_at
```

Where appropriate:

```text
published_at
deleted_at
resolved_at
joined_at
```

Use timezone-aware timestamps.

Recommended PostgreSQL type:

```text
TIMESTAMPTZ
```

---

# 35. Soft Deletion

Important user-generated content should generally support soft deletion.

Example:

```text
deleted_at
```

Instead of immediately deleting the record.

This is useful for:

* Moderation
* Auditing
* Recovery
* Maintaining relationships
* Preventing broken references

Not every table needs soft deletion.

---

# 36. Indexing Strategy

Indexes will be created for:

### User lookup

```text
users.email
users.username
```

### Case discovery

```text
cases.status
cases.visibility
cases.created_at
cases.category
```

### Investigation

```text
investigations.case_id
investigations.created_by
investigation_members.user_id
investigation_members.investigation_id
```

### Evidence

```text
evidence.case_id
evidence.investigation_id
evidence.created_at
```

### Theories

```text
theories.case_id
theories.investigation_id
theories.created_by
```

### Social

```text
follows.follower_id
follows.following_id
comments.target_id
notifications.user_id
notifications.is_read
```

Indexes will be added based on actual query patterns rather than indexing every column.

---

# 37. Composite Indexes

Frequently combined filters should use composite indexes.

Example:

```text
cases(status, created_at)
```

or:

```text
evidence(case_id, created_at)
```

or:

```text
notifications(user_id, is_read, created_at)
```

The exact indexes will be validated using query plans once the application is implemented.

---

# 38. Unique Constraints

Important uniqueness rules include:

```text
users.email
users.username
```

and:

```text
UNIQUE(follower_id, following_id)
```

and:

```text
UNIQUE(user_id, target_type, target_id, reaction_type)
```

where applicable.

Database constraints should enforce critical business invariants whenever possible.

---

# 39. JSONB Usage

PostgreSQL JSONB may be used for genuinely flexible metadata.

Examples:

```text
source_metadata
activity.metadata
AI metadata
external API metadata
```

JSONB should **not** replace normal relational columns when the data:

* Is frequently queried
* Has strong relationships
* Requires constraints
* Is core to the domain

---

# 40. Search

Initial search will use PostgreSQL.

Possible capabilities:

```text
Keyword search
Full-text search
Filtering
Sorting
Category filtering
Status filtering
```

Potential PostgreSQL features:

```text
tsvector
GIN indexes
ILIKE
full-text search
```

A dedicated search engine is intentionally deferred.

---

# 41. Database Transactions

Operations involving multiple tables should use transactions.

Example:

```text
Create Theory
    │
    ├── Insert theory
    ├── Insert evidence relationships
    ├── Insert clue relationships
    └── Insert activity
```

These should be committed atomically.

---

# 42. Concurrency

The database must account for concurrent actions.

Examples:

```text
Two users join an investigation
Two users react simultaneously
Two users edit the same resource
Multiple users add evidence
```

Protection mechanisms may include:

* Unique constraints
* Transactions
* Row-level locking where required
* Optimistic concurrency where useful

---

# 43. Database Migration Strategy

Alembic will manage schema changes.

Development:

```text
Model change
    ↓
Alembic migration
    ↓
Test migration
    ↓
Apply migration
```

Production:

```text
GitHub
   ↓
Deployment
   ↓
Migration
   ↓
Application
```

Database migrations must be version-controlled.

---

# 44. Backup Strategy

Production PostgreSQL should have:

* Automated backups
* Point-in-time recovery where supported
* Backup retention policy
* Restore testing

AWS-managed PostgreSQL/RDS can provide the underlying backup infrastructure.

Exact AWS configuration belongs to the Deployment Architecture step.

---

# 45. Database Security

The application database should:

* Use authenticated connections
* Use encrypted connections in production
* Keep credentials outside source code
* Restrict database network access
* Use least-privilege database credentials
* Never expose PostgreSQL directly to the public internet
* Separate development and production databases

---

# 46. Database Environment Separation

There should be separate environments:

```text
Development
    ↓
Testing
    ↓
Production
```

Each environment should have its own database configuration.

Production data must never be casually used for development.

---

# 47. Initial Database Relationship Overview

```text
                         USERS
                           │
            ┌──────────────┼──────────────┐
            ▼              ▼              ▼
        PROFILES        FOLLOWS       ACTIVITIES
            │
            │
            ▼
          CASES
            │
     ┌──────┼────────┬──────────┐
     ▼      ▼        ▼          ▼
  CLUES   EVIDENCE  THEORIES  INVESTIGATIONS
     │       │        │          │
     │       │        │          ▼
     │       │        │     INVESTIGATION
     │       │        │       MEMBERS
     │       │        │
     └───────┴────────┘
             │
             ▼
          COMMENTS
             │
             ▼
         REACTIONS

USERS ───────────────► NOTIFICATIONS
USERS ───────────────► BOOKMARKS
USERS ───────────────► REPORTS
REPORTS ─────────────► MODERATION ACTIONS

EVIDENCE ────────────► MEDIA FILES ─────────► S3
```

---

# 48. Database Design Principles

AfterWords database design follows these principles:

### 1. PostgreSQL is the source of truth

Core application state belongs in PostgreSQL.

### 2. Relational-first

Important relationships should be represented relationally.

### 3. Strong integrity

Use foreign keys, constraints, transactions, and unique indexes.

### 4. Avoid premature denormalization

Optimize only after identifying real performance bottlenecks.

### 5. Query-driven indexing

Indexes should reflect actual access patterns.

### 6. File separation

Large files belong in S3, not PostgreSQL.

### 7. Auditable

Important actions should be traceable.

### 8. Extensible

The schema should support future AI, recommendation, and investigation functionality.

### 9. Privacy-aware

Only necessary user information should be persisted.

### 10. Migration-controlled

Every schema change must be managed through Alembic.

---

# 49. What Is Intentionally Deferred

The following will be designed in later steps:

* Complete ERD
* Exact column types
* Exact foreign-key behavior
* Exact indexes
* Case state machine
* Investigation state machine
* Authentication schema
* Detailed authorization model
* Recommendation data model
* AI/vector data model
* Search implementation
* Notification architecture
* Moderation architecture
* Deployment database configuration

