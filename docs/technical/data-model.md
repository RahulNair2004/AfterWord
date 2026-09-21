# AfterWords — Data Model & ERD

## 1. Purpose

This document defines the core relational data model for AfterWords.

It converts the database architecture into concrete entities, relationships, keys, constraints, and cardinalities.

The database uses:

* PostgreSQL
* SQLAlchemy
* Alembic
* UUID identifiers
* Foreign keys
* Relational constraints
* JSONB for limited flexible metadata
* Amazon S3 for physical file storage

---

# 2. Core Domain Model

The AfterWords platform is centered around:

```text
User
 │
 ├── Social Activity
 │
 └── Investigation
        │
        └── Case
             │
             ├── Evidence
             │
             ├── Clues
             │
             └── Theories
```

The core investigative relationship is:

```text
Case
 │
 ├── Evidence
 │     │
 │     └── Sources / Files
 │
 ├── Clues
 │     │
 │     └── Evidence
 │
 ├── Theories
 │     ├── Evidence
 │     └── Clues
 │
 └── Investigations
       │
       ├── Members
       ├── Activity
       └── Discussions
```

---

# 3. Entity Groups

The database is divided into six logical groups.

## Identity

```text
users
profiles
```

## Investigation

```text
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
```

## Social

```text
comments
reactions
follows
bookmarks
activities
```

## Platform

```text
notifications
reports
moderation_actions
media_files
```

## AI

```text
ai_interactions
```

## Future / Optional

Additional entities can be introduced later without changing the core model.

---

# 4. users

The `users` table represents platform accounts.

```text
users
------------------------------------------------
id                  UUID PK
email               VARCHAR UNIQUE NOT NULL
username            VARCHAR UNIQUE NOT NULL
password_hash       VARCHAR NOT NULL
role                VARCHAR NOT NULL
status              VARCHAR NOT NULL
last_login_at       TIMESTAMPTZ
created_at          TIMESTAMPTZ NOT NULL
updated_at          TIMESTAMPTZ NOT NULL
```

### Constraints

```text
PRIMARY KEY (id)
UNIQUE (email)
UNIQUE (username)
```

### Relationships

```text
users 1 ─── 1 profiles

users 1 ─── N cases
users 1 ─── N investigations
users 1 ─── N evidence
users 1 ─── N clues
users 1 ─── N theories
users 1 ─── N comments
users 1 ─── N notifications
```

---

# 5. profiles

Stores public-facing user information.

```text
profiles
------------------------------------------------
user_id             UUID PK FK → users.id
display_name        VARCHAR
bio                 TEXT
avatar_media_id     UUID FK → media_files.id
location            VARCHAR
website             VARCHAR
created_at          TIMESTAMPTZ NOT NULL
updated_at          TIMESTAMPTZ NOT NULL
```

Relationship:

```text
users
  │
  │ 1:1
  ▼
profiles
```

---

# 6. cases

Cases are the central content entities.

```text
cases
------------------------------------------------
id                  UUID PK
created_by          UUID FK → users.id
title               VARCHAR NOT NULL
slug                VARCHAR UNIQUE NOT NULL
description         TEXT NOT NULL
status              VARCHAR NOT NULL
difficulty          VARCHAR
visibility          VARCHAR NOT NULL
published_at        TIMESTAMPTZ
created_at          TIMESTAMPTZ NOT NULL
updated_at          TIMESTAMPTZ NOT NULL
deleted_at          TIMESTAMPTZ
```

### Relationships

```text
users 1 ─── N cases

cases 1 ─── N investigations
cases 1 ─── N evidence
cases 1 ─── N clues
cases 1 ─── N theories
```

---

# 7. case_categories

Stores reusable case categories.

```text
case_categories
------------------------------------------------
id                  UUID PK
name                VARCHAR UNIQUE NOT NULL
slug                VARCHAR UNIQUE NOT NULL
description         TEXT
created_at          TIMESTAMPTZ NOT NULL
```

Examples:

```text
Mystery
Crime
Historical
Disappearance
Scientific
Logical
Moral Dilemma
Unsolved
```

---

# 8. case_category_map

Many-to-many relationship between cases and categories.

```text
case_category_map
------------------------------------------------
case_id             UUID FK → cases.id
category_id         UUID FK → case_categories.id
```

Primary key:

```text
PRIMARY KEY (case_id, category_id)
```

Relationship:

```text
cases N ─── M case_categories
```

---

# 9. investigations

An investigation represents a collaborative investigation around a case.

```text
investigations
------------------------------------------------
id                  UUID PK
case_id             UUID FK → cases.id
created_by          UUID FK → users.id
title               VARCHAR NOT NULL
description         TEXT
status              VARCHAR NOT NULL
visibility          VARCHAR NOT NULL
created_at          TIMESTAMPTZ NOT NULL
updated_at          TIMESTAMPTZ NOT NULL
deleted_at          TIMESTAMPTZ
```

Relationships:

```text
cases 1 ─── N investigations

users 1 ─── N investigations
```

---

# 10. investigation_members

Connects users to investigations.

```text
investigation_members
------------------------------------------------
investigation_id    UUID FK → investigations.id
user_id             UUID FK → users.id
role                VARCHAR NOT NULL
status              VARCHAR NOT NULL
joined_at           TIMESTAMPTZ NOT NULL
```

Primary key:

```text
PRIMARY KEY (investigation_id, user_id)
```

Relationship:

```text
users N ─── M investigations
```

Possible roles:

```text
owner
member
moderator
```

---

# 11. evidence

Stores evidence associated with cases and investigations.

```text
evidence
------------------------------------------------
id                  UUID PK
case_id             UUID FK → cases.id
investigation_id    UUID FK → investigations.id
created_by          UUID FK → users.id
title               VARCHAR NOT NULL
description         TEXT
evidence_type       VARCHAR NOT NULL
verification_status VARCHAR NOT NULL
created_at          TIMESTAMPTZ NOT NULL
updated_at          TIMESTAMPTZ NOT NULL
deleted_at          TIMESTAMPTZ
```

Relationships:

```text
cases 1 ─── N evidence

investigations 1 ─── N evidence

users 1 ─── N evidence
```

`investigation_id` may be nullable when evidence belongs to the public case rather than a specific investigation.

---

# 12. evidence_sources

Stores provenance information.

```text
evidence_sources
------------------------------------------------
id                  UUID PK
evidence_id         UUID FK → evidence.id
source_type         VARCHAR NOT NULL
source_title        VARCHAR
source_url          TEXT
publisher           VARCHAR
author              VARCHAR
published_at        TIMESTAMPTZ
accessed_at         TIMESTAMPTZ
source_metadata     JSONB
created_at          TIMESTAMPTZ NOT NULL
```

Relationship:

```text
evidence 1 ─── N evidence_sources
```

---

# 13. media_files

Stores metadata for files stored in S3.

```text
media_files
------------------------------------------------
id                  UUID PK
owner_id            UUID FK → users.id
storage_provider    VARCHAR NOT NULL
storage_key         TEXT NOT NULL
file_name           VARCHAR
mime_type            VARCHAR
file_size           BIGINT
checksum            VARCHAR
created_at          TIMESTAMPTZ NOT NULL
```

Relationship:

```text
users 1 ─── N media_files
```

Physical file:

```text
media_files.storage_key
        │
        ▼
Amazon S3
```

---

# 14. evidence_files

Associates evidence with uploaded files.

```text
evidence_files
------------------------------------------------
id                  UUID PK
evidence_id         UUID FK → evidence.id
media_file_id       UUID FK → media_files.id
created_at          TIMESTAMPTZ NOT NULL
```

Relationships:

```text
evidence 1 ─── N evidence_files

media_files 1 ─── N evidence_files
```

---

# 15. clues

Stores clues discovered during investigations.

```text
clues
------------------------------------------------
id                  UUID PK
case_id             UUID FK → cases.id
investigation_id    UUID FK → investigations.id
created_by          UUID FK → users.id
title               VARCHAR NOT NULL
description         TEXT
status              VARCHAR NOT NULL
importance          VARCHAR
created_at          TIMESTAMPTZ NOT NULL
updated_at          TIMESTAMPTZ NOT NULL
deleted_at          TIMESTAMPTZ
```

Relationships:

```text
cases 1 ─── N clues

investigations 1 ─── N clues

users 1 ─── N clues
```

---

# 16. clue_evidence

Connects clues to evidence.

```text
clue_evidence
------------------------------------------------
clue_id             UUID FK → clues.id
evidence_id         UUID FK → evidence.id
relationship        VARCHAR
created_at          TIMESTAMPTZ NOT NULL
```

Primary key:

```text
PRIMARY KEY (clue_id, evidence_id)
```

Relationship:

```text
clues N ─── M evidence
```

---

# 17. theories

Stores user-created investigative theories.

```text
theories
------------------------------------------------
id                  UUID PK
case_id             UUID FK → cases.id
investigation_id    UUID FK → investigations.id
created_by          UUID FK → users.id
title               VARCHAR NOT NULL
description         TEXT NOT NULL
status              VARCHAR NOT NULL
created_at          TIMESTAMPTZ NOT NULL
updated_at          TIMESTAMPTZ NOT NULL
deleted_at          TIMESTAMPTZ
```

Relationships:

```text
cases 1 ─── N theories

investigations 1 ─── N theories

users 1 ─── N theories
```

---

# 18. theory_evidence

Connects theories with supporting or contradictory evidence.

```text
theory_evidence
------------------------------------------------
theory_id           UUID FK → theories.id
evidence_id         UUID FK → evidence.id
relationship        VARCHAR NOT NULL
created_by          UUID FK → users.id
created_at          TIMESTAMPTZ NOT NULL
```

Primary key:

```text
PRIMARY KEY (theory_id, evidence_id)
```

Possible relationships:

```text
supports
contradicts
contextual
```

---

# 19. theory_clues

Connects theories with clues.

```text
theory_clues
------------------------------------------------
theory_id           UUID FK → theories.id
clue_id             UUID FK → clues.id
relationship        VARCHAR NOT NULL
created_by          UUID FK → users.id
created_at          TIMESTAMPTZ NOT NULL
```

Primary key:

```text
PRIMARY KEY (theory_id, clue_id)
```

---

# 20. comments

Comments support discussion throughout the platform.

```text
comments
------------------------------------------------
id                  UUID PK
user_id             UUID FK → users.id
parent_comment_id   UUID FK → comments.id
target_type         VARCHAR NOT NULL
target_id           UUID NOT NULL
content             TEXT NOT NULL
status              VARCHAR NOT NULL
created_at          TIMESTAMPTZ NOT NULL
updated_at          TIMESTAMPTZ NOT NULL
deleted_at          TIMESTAMPTZ
```

Self-reference:

```text
comments
   │
   └── parent_comment_id
             │
             ▼
          comments
```

This supports threaded discussions.

---

# 21. reactions

Stores user reactions.

```text
reactions
------------------------------------------------
id                  UUID PK
user_id             UUID FK → users.id
target_type         VARCHAR NOT NULL
target_id           UUID NOT NULL
reaction_type       VARCHAR NOT NULL
created_at          TIMESTAMPTZ NOT NULL
```

A uniqueness constraint should prevent duplicate identical reactions.

```text
UNIQUE(
    user_id,
    target_type,
    target_id,
    reaction_type
)
```

---

# 22. follows

Represents user-to-user relationships.

```text
follows
------------------------------------------------
follower_id         UUID FK → users.id
following_id        UUID FK → users.id
created_at          TIMESTAMPTZ NOT NULL
```

Primary key:

```text
PRIMARY KEY (follower_id, following_id)
```

Constraint:

```text
follower_id != following_id
```

---

# 23. bookmarks

Stores saved resources.

```text
bookmarks
------------------------------------------------
id                  UUID PK
user_id             UUID FK → users.id
target_type         VARCHAR NOT NULL
target_id           UUID NOT NULL
created_at          TIMESTAMPTZ NOT NULL
```

Possible targets:

```text
case
investigation
evidence
clue
theory
```

---

# 24. notifications

Stores user notifications.

```text
notifications
------------------------------------------------
id                  UUID PK
user_id             UUID FK → users.id
type                VARCHAR NOT NULL
title               VARCHAR NOT NULL
message             TEXT NOT NULL
reference_type      VARCHAR
reference_id        UUID
is_read             BOOLEAN NOT NULL DEFAULT FALSE
created_at          TIMESTAMPTZ NOT NULL
```

Relationship:

```text
users 1 ─── N notifications
```

---

# 25. activities

Stores significant user/platform actions.

```text
activities
------------------------------------------------
id                  UUID PK
user_id             UUID FK → users.id
activity_type       VARCHAR NOT NULL
target_type         VARCHAR
target_id           UUID
metadata            JSONB
created_at          TIMESTAMPTZ NOT NULL
```

Examples:

```text
created_case
joined_investigation
created_theory
added_evidence
created_clue
followed_user
commented
```

Activities can power:

```text
Feed
Notifications
Recommendations
Analytics
Profile activity
```

---

# 26. reports

Stores user-submitted reports.

```text
reports
------------------------------------------------
id                  UUID PK
reporter_id         UUID FK → users.id
target_type         VARCHAR NOT NULL
target_id           UUID NOT NULL
reason              VARCHAR NOT NULL
description         TEXT
status              VARCHAR NOT NULL
created_at          TIMESTAMPTZ NOT NULL
resolved_at         TIMESTAMPTZ
```

---

# 27. moderation_actions

Stores moderator actions.

```text
moderation_actions
------------------------------------------------
id                  UUID PK
moderator_id        UUID FK → users.id
target_type         VARCHAR NOT NULL
target_id           UUID NOT NULL
action              VARCHAR NOT NULL
reason              TEXT
created_at          TIMESTAMPTZ NOT NULL
```

Relationship:

```text
reports
   │
   ▼
moderation_actions
```

The report and moderation action should remain separate because one report can lead to different moderation decisions.

---

# 28. ai_interactions

Stores persisted AI interactions where necessary.

```text
ai_interactions
------------------------------------------------
id                  UUID PK
user_id             UUID FK → users.id
case_id             UUID FK → cases.id
investigation_id    UUID FK → investigations.id
interaction_type    VARCHAR NOT NULL
input_reference     TEXT
output              TEXT
model               VARCHAR
metadata            JSONB
created_at          TIMESTAMPTZ NOT NULL
```

Possible interaction types:

```text
case_summary
evidence_summary
theory_analysis
similar_case
investigation_assistance
```

AI interaction storage should be subject to retention rules.

---

# 29. Complete ERD

The conceptual ERD is:

```text
                                    ┌───────────────┐
                                    │     USERS     │
                                    └───────┬───────┘
                                            │
                   ┌────────────────────────┼────────────────────────┐
                   │                        │                        │
                   ▼                        ▼                        ▼
              PROFILES                  FOLLOWS                 ACTIVITIES
                                           
                   │
                   │ created_by
                   ▼
              ┌───────────────┐
              │     CASES     │
              └───────┬───────┘
                      │
        ┌─────────────┼────────────────┐
        │             │                │
        ▼             ▼                ▼
   CATEGORIES     EVIDENCE           CLUES
        │             │                │
        │             ├──────┐         │
        │             │      │         │
        │             ▼      ▼         ▼
        │          SOURCES  FILES  CLUE_EVIDENCE
        │                     │         │
        │                     ▼         │
        │                MEDIA_FILES    │
        │                               │
        └───────────────────────────────┘

                      │
                      ▼
                INVESTIGATIONS
                      │
                      ▼
              INVESTIGATION_MEMBERS
                      │
                      ▼
                    USERS

                      │
             ┌────────┴────────┐
             ▼                 ▼
          THEORIES          EVIDENCE
             │
        ┌────┴─────┐
        ▼          ▼
 THEORY_EVIDENCE  THEORY_CLUES

USERS ───────────► COMMENTS
                      │
                      └──► COMMENTS

USERS ───────────► REACTIONS
USERS ───────────► BOOKMARKS
USERS ───────────► NOTIFICATIONS
USERS ───────────► REPORTS
REPORTS ─────────► MODERATION_ACTIONS

USERS ───────────► AI_INTERACTIONS
CASES ───────────► AI_INTERACTIONS
INVESTIGATIONS ──► AI_INTERACTIONS
```

---

# 30. Core Relationship Matrix

| Entity A      | Relationship | Entity B          |
| ------------- | ------------ | ----------------- |
| User          | 1:1          | Profile           |
| User          | 1:N          | Case              |
| User          | 1:N          | Investigation     |
| User          | 1:N          | Evidence          |
| User          | 1:N          | Clue              |
| User          | 1:N          | Theory            |
| User          | 1:N          | Comment           |
| User          | N:M          | Investigation     |
| User          | N:M          | User              |
| User          | 1:N          | Notification      |
| User          | 1:N          | Activity          |
| User          | 1:N          | Report            |
| Case          | N:M          | Category          |
| Case          | 1:N          | Investigation     |
| Case          | 1:N          | Evidence          |
| Case          | 1:N          | Clue              |
| Case          | 1:N          | Theory            |
| Investigation | N:M          | User              |
| Investigation | 1:N          | Evidence          |
| Investigation | 1:N          | Clue              |
| Investigation | 1:N          | Theory            |
| Evidence      | 1:N          | Source            |
| Evidence      | 1:N          | Media File        |
| Clue          | N:M          | Evidence          |
| Theory        | N:M          | Evidence          |
| Theory        | N:M          | Clue              |
| Comment       | 1:N          | Comment           |
| Report        | 1:N          | Moderation Action |
| User          | 1:N          | AI Interaction    |

---

# 31. Investigation Graph Model

One of the most important aspects of AfterWords is the ability to represent relationships between investigative entities.

Conceptually:

```text
                    CASE
                     │
       ┌─────────────┼──────────────┐
       │             │              │
       ▼             ▼              ▼
    EVIDENCE       CLUE          THEORY
       │             │              │
       │             │              │
       └──────┬──────┴──────┬───────┘
              │             │
              ▼             ▼
           SUPPORTS      CONTRADICTS
```

This creates a graph-like structure while still using PostgreSQL relational tables.

A graph database is therefore **not required initially**.

---

# 32. Public vs Private Data

The model distinguishes between:

### Public

```text
Published cases
Public profiles
Public theories
Public discussions
Public investigations
```

### Private

```text
Account credentials
Private investigations
Private messages if introduced later
Private AI interactions
Moderation information
Internal platform metadata
```

Authorization determines whether a record can be exposed through the API.

---

# 33. Data Integrity Rules

The database must enforce:

```text
1. Every investigation belongs to a case.

2. Every investigation member references an existing user.

3. Every theory belongs to a case.

4. Evidence cannot reference a nonexistent case.

5. Evidence relationships cannot reference nonexistent evidence.

6. A user cannot follow themselves.

7. Duplicate follow relationships are prohibited.

8. Duplicate reactions are prohibited.

9. Category mappings are unique.

10. Investigation memberships are unique.

11. Required fields cannot be NULL.

12. Deleted content should not appear in normal queries.
```

---

# 34. Index Plan

Initial indexes:

```text
users
├── email
└── username

cases
├── slug
├── status
├── visibility
├── created_at
└── created_by

investigations
├── case_id
├── created_by
└── status

investigation_members
├── investigation_id
└── user_id

evidence
├── case_id
├── investigation_id
├── created_by
└── created_at

clues
├── case_id
├── investigation_id
└── created_by

theories
├── case_id
├── investigation_id
└── created_by

comments
├── target_type + target_id
└── parent_comment_id

notifications
├── user_id
├── is_read
└── created_at

activities
├── user_id
├── target_type + target_id
└── created_at

follows
├── follower_id
└── following_id
```

Indexes will be adjusted after real query patterns are measured.

---

# 35. Normalization Strategy

The core schema will generally follow relational normalization principles.

Avoid:

```text
cases
-----
evidence_1
evidence_2
evidence_3
```

Use:

```text
cases
  │
  └── evidence
```

Avoid storing relationship lists as comma-separated strings.

Instead:

```text
case
  │
  ▼
case_category_map
  │
  ▼
category
```

JSONB is reserved for genuinely flexible metadata.

---

# 36. Data Lifecycle

A typical case lifecycle:

```text
Draft
  ↓
Published
  ↓
Active
  ↓
Resolved
  ↓
Archived
```

Investigation:

```text
Created
  ↓
Active
  ↓
Completed
  ↓
Archived
```

Theory:

```text
Proposed
  ↓
Under Review
  ↓
Supported / Disputed
  ↓
Resolved / Rejected
```

The exact state transitions will be defined in the Investigation Engine architecture.

---

# 37. Deletion Strategy

Hard deletion should be limited.

For important user-generated entities:

```text
deleted_at
```

can mark content as deleted.

Normal queries should filter deleted records.

Permanent deletion may be performed through controlled administrative or scheduled processes.

---

# 38. Future Extensions

The model can later support:

```text
private messages
groups
events
gamification
badges
leaderboards
case solving scores
advanced recommendation models
vector embeddings
semantic search
real-time collaboration
subscriptions
premium investigations
```

These are not required for the initial database.

---

# 39. Final Database Architecture

```text
                       POSTGRESQL
                           │
       ┌───────────────────┼───────────────────┐
       │                   │                   │
       ▼                   ▼                   ▼
    IDENTITY          INVESTIGATION          SOCIAL
       │                   │                   │
       ▼                   ▼                   ▼
    Users               Cases              Comments
    Profiles            Evidence           Reactions
                        Clues               Follows
                        Theories            Bookmarks
                        Investigations      Activities
                            │
                            ▼
                       RELATIONSHIPS
                            │
                            ▼
                      PLATFORM DATA
                            │
                 ┌──────────┼──────────┐
                 ▼          ▼          ▼
           Notifications  Reports    Media
                                      │
                                      ▼
                                      S3
```

