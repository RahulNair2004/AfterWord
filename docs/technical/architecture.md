

# 1. Architecture Overview

AfterWords is a social investigation platform combining:

* Social networking
* Collaborative investigations
* Case management
* Evidence and clue management
* Theory building and discussion
* AI-assisted investigation
* Search and discovery
* Recommendations
* Notifications
* Moderation
* User-generated content

The system will initially use a **modular monolith architecture**.

```text
                         ┌─────────────────────┐
                         │        USERS        │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   React Frontend    │
                         └──────────┬──────────┘
                                    │
                              HTTPS / WS
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    FastAPI API      │
                         │       Layer         │
                         └──────────┬──────────┘
                                    │
          ┌─────────────────────────┼─────────────────────────┐
          │                         │                         │
          ▼                         ▼                         ▼
   ┌─────────────┐          ┌──────────────┐          ┌─────────────┐
   │   Identity  │          │ Core Platform│          │ AI Services │
   │    Module   │          │    Modules   │          │             │
   └─────────────┘          └──────┬───────┘          └──────┬──────┘
                                   │                         │
                  ┌────────────────┼────────────────┐        │
                  │                │                │        │
                  ▼                ▼                ▼        │
                Cases           Social          Discovery   │
                  │                │                │        │
                  ▼                ▼                ▼        │
            Investigation        Feed            Search     │
                  │                                         │
        ┌─────────┼─────────┐                               │
        ▼         ▼         ▼                               │
     Evidence   Clues     Theories                           │
        │         │         │                               │
        └─────────┼─────────┘                               │
                  │                                         │
                  └──────────────────┬──────────────────────┘
                                     │
                              Event / Job Layer
                                     │
                      ┌──────────────┼──────────────┐
                      ▼              ▼              ▼
                Notifications    Workers       Analytics
                                     │
                                     ▼
                         ┌────────────────────────┐
                         │       Data Layer       │
                         ├────────────────────────┤
                         │ PostgreSQL             │
                         │ Redis                  │
                         │ Object Storage         │
                         │ Search Index           │
                         │ Vector Storage*        │
                         └────────────────────────┘

                         * Added when required
```

---

# 2. Architectural Style

## Primary Architecture

AfterWords will use a:

> **Modular Monolith**

The backend will initially run as a single application while maintaining strict internal module boundaries.

```text
                    AFTERWORDS BACKEND
                           │
                     FastAPI Application
                           │
       ┌───────────────────┼───────────────────┐
       │                   │                   │
     Identity            Cases              Social
       │                   │                   │
       │             Investigation            │
       │             Evidence                 │
       │             Theory                   │
       │                   │                   │
       └───────────────────┼───────────────────┘
                           │
                      Shared Core
                           │
                       PostgreSQL
```

Microservices will only be introduced if a specific component later requires independent scaling or deployment.

---

# 3. Major System Components

AfterWords consists of the following major components:

```text
1. Frontend
2. API Gateway / API Layer
3. Authentication & Identity
4. User/Profile System
5. Case Management
6. Investigation Engine
7. Evidence System
8. Clue System
9. Theory System
10. Social System
11. Feed System
12. Discovery System
13. Search System
14. AI System
15. Recommendation System
16. Notification System
17. Moderation System
18. Media/Storage System
19. Background Job System
20. Event System
21. Analytics System
22. Data Layer
```

---

# 4. Frontend Layer

The frontend provides the user-facing application.

```text
Frontend
│
├── Authentication
├── Home / Feed
├── Explore
├── Cases
├── Case Details
├── Investigation Workspace
├── Evidence
├── Clues
├── Theories
├── Discussions
├── Posts
├── User Profiles
├── Notifications
├── Search
└── Settings
```

The frontend is responsible for:

* UI rendering
* User interaction
* Client-side state
* API communication
* Form handling
* Client-side validation
* Loading/error states
* Real-time UI updates

Business-critical logic remains on the backend.

---

# 5. API Layer

The API layer is the primary communication boundary between frontend and backend.

```text
Frontend
    │
    ▼
API Layer
    │
    ├── Authentication
    ├── Users
    ├── Cases
    ├── Investigations
    ├── Evidence
    ├── Clues
    ├── Theories
    ├── Posts
    ├── Comments
    ├── Feed
    ├── Search
    ├── Notifications
    ├── Recommendations
    ├── AI
    └── Moderation
```

Responsibilities:

* Routing
* Request validation
* Authentication
* Authorization
* Rate limiting
* Response serialization
* Error handling
* API versioning

---

# 6. Backend Architecture

The backend follows domain-based modular architecture.

```text
backend/
│
├── app/
│   │
│   ├── api/
│   │
│   ├── core/
│   │
│   ├── modules/
│   │   ├── auth/
│   │   ├── users/
│   │   ├── cases/
│   │   ├── investigations/
│   │   ├── evidence/
│   │   ├── clues/
│   │   ├── theories/
│   │   ├── social/
│   │   ├── feed/
│   │   ├── discovery/
│   │   ├── search/
│   │   ├── recommendations/
│   │   ├── notifications/
│   │   ├── moderation/
│   │   └── ai/
│   │
│   ├── workers/
│   ├── events/
│   └── main.py
│
├── migrations/
├── tests/
└── pyproject.toml
```

Each module should maintain separation between:

```text
API
 ↓
Service
 ↓
Repository
 ↓
Database
```

---

# 7. Core Backend Layers

Each domain follows the same general structure.

```text
                API / Router
                     │
                     ▼
              Service Layer
                     │
              ┌──────┴──────┐
              ▼             ▼
        Repository       External Service
              │
              ▼
           Database
```

### API Layer

Handles HTTP requests and responses.

### Service Layer

Contains business logic.

### Repository Layer

Handles database access.

### Model Layer

Represents persistent data.

### Schema Layer

Handles request/response validation.

---

# 8. Identity & Authentication

Responsible for:

* Registration
* Login
* Logout
* Password management
* Email verification
* Sessions/tokens
* User roles
* Permissions

Architecture:

```text
User
 │
 ▼
Authentication
 │
 ├── Identity
 ├── Credentials
 ├── Session
 └── Permissions
```

Authorization is enforced server-side.

---

# 9. User/Profile System

The user system manages:

```text
User
 │
 ├── Profile
 ├── Preferences
 ├── Interests
 ├── Activity
 ├── Followers
 ├── Following
 ├── Bookmarks
 └── Contributions
```

User activity may feed into:

* Recommendations
* Discovery
* Social feed
* Investigation history

---

# 10. Case Management System

A Case is the central investigative object.

```text
CASE
│
├── Metadata
├── Description
├── Categories
├── Topics
├── Timeline
├── Questions
├── Evidence
├── Clues
├── Sources
├── Theories
├── Investigations
└── Resolution
```

The Case Management module controls:

* Case creation
* Case editing
* Case lifecycle
* Case visibility
* Case categorization
* Case status
* Case discovery

---

# 11. Investigation Engine

The investigation engine manages how users investigate a case.

```text
CASE
 │
 └── INVESTIGATION
       │
       ├── Investigator(s)
       ├── Notes
       ├── Evidence references
       ├── Clue references
       ├── Theories
       └── Progress
```

The system supports:

### Individual Investigations

One user investigates independently.

### Collaborative Investigations

Multiple users contribute to a shared investigation.

The investigation engine connects:

```text
Users
 ↓
Cases
 ↓
Evidence
 ↓
Clues
 ↓
Theories
```

---

# 12. Evidence System

Evidence is a first-class system entity.

```text
Evidence
│
├── Source
├── Type
├── Description
├── Media
├── Metadata
├── Verification Status
├── Related Case
├── Related Clues
└── Related Theories
```

Evidence states:

```text
UNVERIFIED
VERIFIED
DISPUTED
REJECTED
```

Evidence provenance must be preserved.

---

# 13. Clue System

Clues represent investigative information extracted from case material.

```text
Clue
│
├── Description
├── Source
├── Related Evidence
├── Related Timeline Event
├── Related Theory
└── Status
```

Clues may be:

* explicitly provided
* discovered through evidence
* community-contributed
* AI-assisted

AI-generated clues must be distinguishable from verified source material.

---

# 14. Theory System

Theories are structured investigative hypotheses.

```text
THEORY
│
├── Author
├── Claim
├── Explanation
├── Supporting Evidence
├── Contradicting Evidence
├── Related Clues
├── Discussion
└── Status
```

This allows users to compare theories based on their underlying evidence rather than treating theories as ordinary comments.

---

# 15. Social System

The social layer provides:

```text
Users
│
├── Follow
├── Posts
├── Comments
├── Reactions
├── Shares
├── Bookmarks
├── Mentions
└── Discussions
```

Social activity can reference investigation objects.

For example:

```text
Post
 └── references Case

Comment
 └── references Theory

Discussion
 └── references Evidence
```

---

# 16. Feed System

The feed aggregates content relevant to the user.

Potential sources:

```text
Following
Cases
Investigations
Posts
Communities
Topics
Recommendations
```

Architecture:

```text
User Activity
      │
      ▼
Candidate Generation
      │
      ▼
Ranking
      │
      ▼
Feed
```

The initial implementation can use deterministic ranking before introducing ML-based ranking.

---

# 17. Discovery System

Discovery exposes:

* Trending cases
* New cases
* Popular investigations
* Interesting theories
* Active discussions
* Recommended users
* Topics

Discovery can consume data from:

```text
Social Activity
Case Activity
Search
Recommendations
Engagement
```

---

# 18. Search System

Search supports:

```text
Cases
Users
Posts
Evidence
Theories
Topics
```

Architecture:

```text
Search Query
     │
     ▼
Query Processing
     │
     ▼
Search Index
     │
     ▼
Ranking
     │
     ▼
Results
```

The initial implementation may use PostgreSQL search capabilities.

A dedicated search engine can be introduced later.

---

# 19. AI System

AI is implemented as a separate logical subsystem.

```text
                      AI SYSTEM
                         │
          ┌──────────────┼──────────────┐
          │              │              │
    Investigation      Content      Recommendations
          │              │
          │              ├── Summaries
          │              └── Questions
          │
          ├── Evidence Analysis
          ├── Theory Analysis
          ├── Case Summarization
          └── Investigation Assistance
```

The AI system must not replace authoritative case/source data.

AI-generated information should be clearly separated from verified source information.

---

# 20. AI Request Flow

```text
User
 │
 ▼
Frontend
 │
 ▼
API
 │
 ▼
Relevant Domain Service
 │
 ▼
AI Service
 │
 ├── Prompt Construction
 ├── Context Retrieval
 ├── Model Request
 ├── Output Validation
 └── Response
 │
 ▼
Domain Service
 │
 ▼
Frontend
```

AI services remain replaceable so the application isn't permanently tied to one model provider.

---

# 21. Recommendation System

Recommendation uses user and platform activity.

```text
User Activity
      │
      ▼
Feature Generation
      │
      ▼
Candidate Generation
      │
      ▼
Ranking
      │
      ▼
Recommendations
```

Potential signals:

* cases viewed
* cases investigated
* topics followed
* posts interacted with
* users followed
* theories interacted with
* investigation history

The system will initially use a simple recommendation strategy and evolve toward ML-based recommendation.

---

# 22. Notification System

Notifications are generated from application events.

```text
Application Event
       │
       ▼
Notification Service
       │
       ├── In-App
       ├── Email
       └── Push
```

Examples:

```text
New follower
New comment
Theory interaction
Evidence update
Case update
Mention
Investigation activity
Moderation action
```

---

# 23. Event System

Internal events decouple backend modules.

Example:

```text
Theory Created
      │
      ▼
THEORY_CREATED
      │
 ┌────┼─────────────┐
 ▼    ▼             ▼
Feed  Notification  AI
```

Other events:

```text
USER_REGISTERED
CASE_CREATED
CASE_UPDATED
EVIDENCE_SUBMITTED
EVIDENCE_VERIFIED
THEORY_CREATED
COMMENT_CREATED
USER_FOLLOWED
POST_CREATED
REPORT_CREATED
```

Events may trigger background jobs.

---

# 24. Background Processing

Heavy operations are moved outside normal HTTP requests.

```text
API Request
    │
    ▼
Create Job
    │
    ▼
Job Queue
    │
    ▼
Worker
    │
    ├── AI Processing
    ├── Embeddings
    ├── Search Indexing
    ├── Notifications
    ├── Media Processing
    └── Recommendation Updates
```

---

# 25. Moderation System

The moderation architecture handles:

```text
Reports
Spam
Harassment
Abuse
Malicious Content
Fake Evidence
Manipulated Content
AI Abuse
```

Flow:

```text
Content
  │
  ▼
Report / Automated Detection
  │
  ▼
Moderation Queue
  │
  ▼
Moderator
  │
  ▼
Action
```

Possible actions:

```text
Warning
Content Removal
Restriction
Suspension
Account Action
```

---

# 26. Media & File Storage

Large files will not be stored directly in PostgreSQL.

Architecture:

```text
Frontend
   │
   ▼
API
   │
   ▼
Object Storage
   │
   ├── Images
   ├── Documents
   ├── Audio
   ├── Video
   └── Other Evidence
```

Database stores metadata and references to stored files.

---

# 27. Data Architecture

Primary data infrastructure:

```text
                    DATA LAYER
                       │
        ┌──────────────┼──────────────┐
        │              │              │
   PostgreSQL        Redis       Object Storage
        │              │              │
 Structured Data    Cache/Jobs       Files
```

Additional infrastructure may be introduced later:

```text
Search Index
Vector Storage
Analytics Warehouse
```

Only when justified by scale or functionality.

---

# 28. PostgreSQL

PostgreSQL will be the primary source of truth for structured application data.

It will store:

* Users
* Profiles
* Cases
* Investigations
* Evidence metadata
* Clues
* Theories
* Posts
* Comments
* Relationships
* Notifications
* Reports
* Permissions
* Application configuration

---

# 29. Redis

Redis will be used for temporary/high-speed data such as:

* Caching
* Rate limiting
* Session-related data where appropriate
* Background job queues
* Temporary state

Redis will not replace PostgreSQL as the primary database.

---

# 30. Object Storage

Object storage will contain:

```text
Profile Images
Case Images
Evidence Files
Documents
Audio
Video
Other Media
```

The database stores references and metadata rather than large binary objects.

---

# 31. Vector Storage

Vector storage will be introduced if AI retrieval requires it.

Potential use cases:

```text
Case embeddings
Evidence embeddings
Document embeddings
Semantic search
AI retrieval
Related evidence discovery
```

Vector storage should not become the primary source of truth.

---

# 32. System Communication

Primary communication:

```text
Frontend → REST API → Backend
```

Real-time communication where required:

```text
Frontend ↔ WebSocket / Real-Time Layer
```

Asynchronous operations:

```text
Backend → Job Queue → Worker
```

Internal domain communication:

```text
Module → Event → Other Module
```

---

# 33. Request Flow

Standard request:

```text
User
 │
 ▼
Frontend
 │
 ▼
API Endpoint
 │
 ▼
Authentication
 │
 ▼
Authorization
 │
 ▼
Validation
 │
 ▼
Service
 │
 ▼
Repository
 │
 ▼
PostgreSQL
 │
 ▼
Repository
 │
 ▼
Service
 │
 ▼
API Response
 │
 ▼
Frontend
```

---

# 34. Example Investigation Flow

```text
User opens Case
       │
       ▼
Frontend requests Case
       │
       ▼
API
       │
       ▼
Case Service
       │
       ├── Case data
       ├── Evidence
       ├── Clues
       ├── Theories
       └── Investigation state
       │
       ▼
PostgreSQL
       │
       ▼
Response
       │
       ▼
Frontend
```

When the user submits a theory:

```text
User
 │
 ▼
API
 │
 ▼
Authorization
 │
 ▼
Theory Service
 │
 ├── Validate
 ├── Save
 └── Publish event
          │
          ├── Notification
          ├── Feed
          ├── AI processing
          └── Analytics
```

---

# 35. Security Boundary

Security is enforced at multiple levels.

```text
Internet
   │
   ▼
HTTPS
   │
   ▼
API
   │
   ├── Authentication
   ├── Authorization
   ├── Validation
   ├── Rate Limiting
   └── Abuse Protection
   │
   ▼
Services
   │
   ▼
Database
```

No frontend-only authorization is trusted.

---

# 36. Scalability Strategy

The system will scale incrementally.

### Stage 1

```text
React
   +
FastAPI
   +
PostgreSQL
   +
Redis
   +
Object Storage
```

### Stage 2

Introduce:

```text
Background Workers
Search Infrastructure
Advanced Caching
AI Infrastructure
```

### Stage 3

If required:

```text
Dedicated AI Services
Dedicated Search
Independent Workers
Independent High-traffic Services
```

Microservices are not required until actual scaling requirements justify them.

---

# 37. Deployment Boundary

Production architecture:

```text
                         INTERNET
                             │
                             ▼
                       CDN / HTTPS
                             │
                 ┌───────────┴───────────┐
                 │                       │
                 ▼                       ▼
             Frontend                 API
                                      │
                          ┌───────────┼───────────┐
                          │           │           │
                          ▼           ▼           ▼
                      PostgreSQL    Redis     Object Storage
                          │
                          ▼
                       Workers
```

Cloud-specific services will be finalized in **Step 2 — Technology Stack** and the later deployment architecture step.

---

# 38. Architectural Principles

AfterWords follows these principles:

1. **Modularity** — Every major domain has a defined responsibility.
2. **Separation of concerns** — Presentation, business logic, and persistence remain separate.
3. **API-first communication** — Frontend and backend communicate through defined APIs.
4. **Database as source of truth** — Structured application state lives in PostgreSQL.
5. **Asynchronous processing** — Heavy operations run through background jobs.
6. **Event-driven extensions** — Important domain events can trigger independent processes.
7. **AI as an isolated capability** — Core application functionality must not depend entirely on AI availability.
8. **Security by design** — Authentication, authorization and validation are built into the architecture.
9. **Incremental scalability** — Infrastructure complexity is introduced only when required.
10. **Production-ready modularity** — The initial architecture should allow future extraction of high-scale services.

---

# 39. Final Architecture

```text
                               AFTERWORDS
                                   │
                                   ▼
                            ┌─────────────┐
                            │   USERS     │
                            └──────┬──────┘
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │   React Frontend    │
                        └──────────┬──────────┘
                                   │
                              HTTPS / WS
                                   │
                                   ▼
                        ┌─────────────────────┐
                        │    FastAPI API      │
                        └──────────┬──────────┘
                                   │
          ┌────────────────────────┼────────────────────────┐
          │                        │                        │
          ▼                        ▼                        ▼
     ┌─────────┐            ┌──────────────┐          ┌─────────┐
     │  Auth   │            │ Core Modules │          │   AI    │
     └─────────┘            └───────┬──────┘          └────┬────┘
                                    │                       │
              ┌─────────────────────┼────────────────┐      │
              │          │          │        │        │      │
              ▼          ▼          ▼        ▼        ▼      │
            Cases   Investigation Evidence Theory Social Discovery
              │          │          │        │        │      │
              └──────────┴──────────┴────────┴────────┘      │
                                    │                        │
                                    └────────────┬───────────┘
                                                 │
                                      ┌──────────▼──────────┐
                                      │   Events / Queue    │
                                      └──────────┬──────────┘
                                                 │
                                  ┌──────────────┼──────────────┐
                                  ▼              ▼              ▼
                            Notifications    Workers       Analytics
                                  │              │
                                  └──────────────┼──────────────┘
                                                 │
                                      ┌──────────▼──────────┐
                                      │      DATA LAYER     │
                                      ├─────────────────────┤
                                      │ PostgreSQL          │
                                      │ Redis               │
                                      │ Object Storage      │
                                      │ Search Index*       │
                                      │ Vector Storage*     │
                                      └─────────────────────┘

                                      * Added when required
```

---

# 40. Architecture Decision Summary

| Decision               | Choice                                                      |
| ---------------------- | ----------------------------------------------------------- |
| Architecture           | Modular Monolith                                            |
| Backend                | Domain-based modules                                        |
| API                    | REST-first                                                  |
| Real-time              | WebSocket where required                                    |
| Primary Database       | PostgreSQL                                                  |
| Cache / Queue          | Redis                                                       |
| File Storage           | Object Storage                                              |
| Background Processing  | Worker-based                                                |
| Internal Communication | Domain Events                                               |
| AI                     | Isolated AI Service Layer                                   |
| Search                 | PostgreSQL initially, dedicated search later if needed      |
| Vector Storage         | Added when AI retrieval requires it                         |
| Scaling Strategy       | Incremental                                                 |
| Microservices          | Not initially                                               |
| Deployment             | Cloud-based                                                 |
| Security               | Authentication + Authorization + Validation + Rate Limiting |

---

