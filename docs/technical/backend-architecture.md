# AfterWords — Backend Architecture

## 1. Purpose

This document defines the backend architecture of AfterWords.

The backend will use a **modular monolith architecture** built with:

* FastAPI
* Python
* Pydantic
* SQLAlchemy
* Alembic
* PostgreSQL
* Amazon S3
* Docker

The architecture is designed to keep the system simple during initial development while allowing individual modules to evolve independently as the platform grows.

---

# 2. Backend Architecture Style

AfterWords will use a:

> **Modular Monolith + Layered Architecture**

The backend will run as a single FastAPI application while maintaining strict separation between business domains.

```text
                         Client
                           │
                           ▼
                    ┌──────────────┐
                    │   FastAPI    │
                    │   API Layer  │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │   Routers    │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │   Services   │
                    │ Business Logic│
                    └──────┬───────┘
                           │
                ┌──────────┴──────────┐
                ▼                     ▼
        ┌──────────────┐      ┌──────────────┐
        │ Repositories │      │ External      │
        │              │      │ Services      │
        └──────┬───────┘      └──────────────┘
               │
               ▼
        ┌──────────────┐
        │ PostgreSQL   │
        └──────────────┘
```

The backend will **not** initially use microservices.

---

# 3. Backend Responsibilities

The backend is responsible for:

* User authentication
* User accounts
* Profiles
* Cases
* Investigations
* Evidence
* Clues
* Theories
* Comments
* Discussions
* Votes/reactions
* Social relationships
* Feed generation
* Following
* Notifications
* Search
* Recommendations
* AI functionality
* Moderation
* File management
* Reporting
* Analytics
* Database operations
* API security

---

# 4. Backend Directory Structure

The initial backend structure will be:

```text
backend/
│
├── app/
│   │
│   ├── main.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   ├── dependencies.py
│   │   ├── exceptions.py
│   │   ├── logging.py
│   │   └── constants.py
│   │
│   ├── db/
│   │   ├── database.py
│   │   ├── session.py
│   │   └── base.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── case.py
│   │   ├── investigation.py
│   │   ├── evidence.py
│   │   ├── clue.py
│   │   ├── theory.py
│   │   ├── comment.py
│   │   ├── reaction.py
│   │   ├── follow.py
│   │   ├── notification.py
│   │   └── report.py
│   │
│   ├── schemas/
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── case.py
│   │   ├── investigation.py
│   │   ├── evidence.py
│   │   ├── clue.py
│   │   ├── theory.py
│   │   ├── comment.py
│   │   ├── feed.py
│   │   └── notification.py
│   │
│   ├── modules/
│   │   │
│   │   ├── auth/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   └── repository.py
│   │   │
│   │   ├── users/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   └── repository.py
│   │   │
│   │   ├── cases/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   └── repository.py
│   │   │
│   │   ├── investigations/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   └── repository.py
│   │   │
│   │   ├── evidence/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   └── repository.py
│   │   │
│   │   ├── clues/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   └── repository.py
│   │   │
│   │   ├── theories/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   └── repository.py
│   │   │
│   │   ├── social/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   └── repository.py
│   │   │
│   │   ├── feed/
│   │   │   ├── router.py
│   │   │   └── service.py
│   │   │
│   │   ├── notifications/
│   │   │   ├── router.py
│   │   │   └── service.py
│   │   │
│   │   ├── search/
│   │   │   ├── router.py
│   │   │   └── service.py
│   │   │
│   │   ├── recommendations/
│   │   │   ├── router.py
│   │   │   └── service.py
│   │   │
│   │   ├── ai/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   ├── prompts.py
│   │   │   └── providers.py
│   │   │
│   │   ├── moderation/
│   │   │   ├── router.py
│   │   │   ├── service.py
│   │   │   └── repository.py
│   │   │
│   │   └── media/
│   │       ├── router.py
│   │       ├── service.py
│   │       └── storage.py
│   │
│   └── utils/
│       ├── pagination.py
│       ├── validators.py
│       └── helpers.py
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── api/
│
├── alembic/
│   └── versions/
│
├── alembic.ini
├── requirements.txt
├── Dockerfile
├── .env.example
└── README.md
```

---

# 5. Architectural Layers

Each backend module follows a consistent layered structure.

```text
Router
   ↓
Schema Validation
   ↓
Service
   ↓
Repository
   ↓
SQLAlchemy Model
   ↓
PostgreSQL
```

---

# 6. Router Layer

Routers are responsible for HTTP/API concerns.

Responsibilities:

* Define endpoints
* Parse request parameters
* Validate request schemas
* Authenticate requests
* Call services
* Return response schemas
* Handle HTTP status codes

Routers should **not contain business logic**.

Example:

```python
@router.post("/cases")
def create_case(
    data: CaseCreate,
    service: CaseService = Depends(get_case_service)
):
    return service.create_case(data)
```

---

# 7. Schema Layer

Pydantic schemas define API input and output structures.

Example:

```text
CaseCreate
CaseUpdate
CaseResponse
CaseListResponse
```

Schemas are responsible for:

* Validation
* Serialization
* API contracts
* Type safety

Database models should not be directly exposed through API responses.

---

# 8. Service Layer

The service layer contains the primary business logic.

Example:

```text
CaseService
    │
    ├── create_case()
    ├── update_case()
    ├── publish_case()
    ├── close_case()
    └── get_case()
```

Services may coordinate multiple repositories.

For example:

```text
Create Investigation
        │
        ├── InvestigationRepository
        ├── CaseRepository
        ├── UserRepository
        └── NotificationService
```

Services are the main location for domain rules.

---

# 9. Repository Layer

Repositories handle database operations.

Responsibilities:

* Queries
* Inserts
* Updates
* Deletes
* Filtering
* Pagination
* Relationship loading

Example:

```text
CaseRepository

get_by_id()
get_public_cases()
create()
update()
delete()
search()
```

Repositories should not contain high-level business decisions.

---

# 10. Database Layer

SQLAlchemy will provide the database abstraction.

```text
FastAPI
   │
   ▼
Service
   │
   ▼
Repository
   │
   ▼
SQLAlchemy
   │
   ▼
PostgreSQL
```

Alembic will manage database migrations.

Example:

```text
Migration 001
    ↓
users

Migration 002
    ↓
cases

Migration 003
    ↓
investigations

Migration 004
    ↓
evidence
```

---

# 11. Core Module

The `core/` directory contains application-wide functionality.

```text
core/
├── config.py
├── security.py
├── dependencies.py
├── exceptions.py
├── logging.py
└── constants.py
```

### config.py

Responsible for:

* Environment variables
* Database configuration
* AWS configuration
* JWT configuration
* AI provider configuration
* Application settings

### security.py

Responsible for:

* Password hashing
* Token handling
* Authentication utilities
* Security helpers

### dependencies.py

Responsible for:

* Database session dependencies
* Current-user dependency
* Permission dependencies
* Service dependency construction

### exceptions.py

Defines application-specific exceptions.

Example:

```text
ResourceNotFound
Unauthorized
Forbidden
ValidationError
ConflictError
```

---

# 12. Domain Modules

AfterWords will use domain-oriented modules.

## Authentication

Responsible for:

* Registration
* Login
* Logout
* Token handling
* Password management
* Email verification
* Authentication state

Detailed authentication design will be defined separately.

---

## Users

Responsible for:

* User profiles
* User settings
* Profile information
* User statistics
* Account management

---

## Cases

Responsible for:

* Case creation
* Case discovery
* Case metadata
* Case categories
* Case status
* Case publishing
* Case lifecycle

---

## Investigations

Responsible for:

* Creating investigations
* Joining investigations
* Investigation membership
* Investigation progress
* Investigation state
* Investigation activity

---

## Evidence

Responsible for:

* Evidence records
* Evidence metadata
* Evidence relationships
* Evidence sources
* Evidence verification state
* Evidence attachments

---

## Clues

Responsible for:

* Clue creation
* Clue relationships
* Clue discovery
* Clue status
* Clue connections

---

## Theories

Responsible for:

* Theory creation
* Theory editing
* Supporting evidence
* Contradicting evidence
* Theory discussion
* Theory status

---

## Social

Responsible for:

* Following users
* Followers
* Reactions
* Comments
* User interactions
* Social activity

---

## Feed

Responsible for:

* Personalized feed
* Following feed
* Investigation activity
* Case activity
* Social activity

The first implementation can use database queries directly without a dedicated feed infrastructure.

---

## Notifications

Responsible for:

* User notifications
* Investigation notifications
* Social notifications
* System notifications
* Read/unread state

---

## Search

Responsible for:

* Case search
* Evidence search
* Theory search
* User search
* Keyword filtering
* Sorting

The initial implementation will use PostgreSQL search capabilities rather than Elasticsearch/OpenSearch.

---

## Recommendations

Responsible for:

* Case recommendations
* User recommendations
* Investigation recommendations
* Content personalization

Initial recommendation algorithms may use conventional scoring and ML before introducing more complex systems.

---

## AI

Responsible for AI-powered functionality.

Potential functionality:

```text
AI
├── Case assistant
├── Evidence summarization
├── Evidence analysis
├── Theory assistance
├── Similar case discovery
├── Investigation assistance
└── Natural language search
```

The AI module will remain inside the backend initially.

```text
FastAPI
   │
   └── AI Module
          │
          ├── LLM Provider
          ├── Embedding Model
          └── ML Models
```

AI providers should be accessed through interfaces so they can be replaced later.

---

# 13. Media Module

The media module manages uploaded files.

Files should not be stored directly inside PostgreSQL.

```text
User
  │
  ▼
FastAPI
  │
  ▼
Media Service
  │
  ▼
Amazon S3
```

PostgreSQL stores:

```text
file_id
owner_id
storage_key
file_type
file_size
created_at
```

S3 stores the actual file.

---

# 14. Dependency Injection

FastAPI dependency injection will be used for:

* Database sessions
* Current authenticated user
* Authorization checks
* Services
* Configuration
* Shared utilities

Example:

```text
Request
   ↓
Authentication Dependency
   ↓
Current User
   ↓
Authorization Dependency
   ↓
Router
   ↓
Service
```

---

# 15. Error Handling

The application will use centralized error handling.

Example response:

```json
{
  "success": false,
  "error": {
    "code": "CASE_NOT_FOUND",
    "message": "The requested case does not exist."
  }
}
```

Common error categories:

```text
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
409 Conflict
422 Validation Error
429 Rate Limited
500 Internal Server Error
```

Internal errors must not expose sensitive implementation details.

---

# 16. API Versioning

All public APIs will be versioned.

```text
/api/v1/
```

Example:

```text
/api/v1/auth/login
/api/v1/users/me
/api/v1/cases
/api/v1/cases/{case_id}
/api/v1/investigations
/api/v1/evidence
/api/v1/theories
/api/v1/search
/api/v1/notifications
```

Future breaking changes can use:

```text
/api/v2/
```

---

# 17. Request Flow

A typical request will follow:

```text
React Frontend
      │
      ▼
HTTP Request
      │
      ▼
FastAPI Router
      │
      ▼
Authentication
      │
      ▼
Pydantic Validation
      │
      ▼
Service
      │
      ▼
Repository
      │
      ▼
SQLAlchemy
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
Response Schema
      │
      ▼
JSON Response
      │
      ▼
React Frontend
```

---

# 18. Example Investigation Request

Example:

```http
POST /api/v1/investigations
```

Request:

```json
{
  "case_id": "case_123",
  "title": "Investigation Team Alpha"
}
```

Processing:

```text
Router
   ↓
Authentication
   ↓
InvestigationCreate Schema
   ↓
InvestigationService
   ↓
Check Case
   ↓
Check User
   ↓
Create Investigation
   ↓
Create Membership
   ↓
Database Transaction
   ↓
InvestigationResponse
```

---

# 19. Database Transactions

Operations that modify multiple related entities must use database transactions.

Example:

```text
Create Investigation
        │
        ├── Create investigation
        ├── Create owner membership
        └── Create activity
```

All operations should succeed together.

```text
BEGIN
   ↓
Operation 1
   ↓
Operation 2
   ↓
Operation 3
   ↓
COMMIT
```

If an operation fails:

```text
ROLLBACK
```

---

# 20. Background Processing

AfterWords will initially avoid introducing Celery, RabbitMQ, Kafka, or Redis.

Lightweight asynchronous tasks can use FastAPI background tasks.

Suitable examples:

```text
Send notification
Generate small summary
Process lightweight activity
Trigger non-critical cleanup
```

Heavy processing will be introduced later if actual requirements justify a dedicated worker system.

Possible future architecture:

```text
FastAPI
   │
   ▼
Job Queue
   │
   ▼
Worker
```

This is intentionally deferred.

---

# 21. Logging

The backend will use structured application logging.

Important events include:

```text
Application startup
Authentication failures
API errors
Database errors
AI failures
File upload failures
Moderation actions
Important system events
```

Logs must not contain:

* Passwords
* Authentication tokens
* Private user data
* Sensitive credentials

---

# 22. Configuration

Environment-specific configuration will be stored through environment variables.

Example:

```text
DATABASE_URL=
SECRET_KEY=
JWT_SECRET=
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_S3_BUCKET=
LLM_API_KEY=
ENVIRONMENT=
```

A `.env.example` file will document required variables.

Secrets will not be committed to Git.

---

# 23. Testing Architecture

Backend tests will be organized as:

```text
tests/
│
├── unit/
│   ├── services/
│   ├── repositories/
│   └── utilities/
│
├── integration/
│   ├── database/
│   └── modules/
│
└── api/
    ├── auth/
    ├── cases/
    ├── investigations/
    ├── evidence/
    └── theories/
```

Testing layers:

```text
Unit Tests
    ↓
Integration Tests
    ↓
API Tests
```

---

# 24. Module Dependency Rules

Modules should follow controlled dependencies.

Allowed:

```text
Router
  ↓
Service
  ↓
Repository
  ↓
Database
```

A module may call another module's **service layer** when necessary.

Example:

```text
InvestigationService
        ↓
CaseService
```

Avoid:

```text
Router → Repository directly
Repository → Router
Repository → Service
Database Model → Router
```

This prevents tightly coupled code.

---

# 25. Shared Code Rules

Shared functionality belongs in:

```text
core/
utils/
```

Only genuinely shared functionality should be placed there.

Do not create a giant `utils.py` containing unrelated business logic.

---

# 26. API Response Convention

Successful responses should return predictable structures.

Example:

```json
{
  "success": true,
  "data": {
    "id": "case_123",
    "title": "Example Case"
  }
}
```

Collections:

```json
{
  "success": true,
  "data": [],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 120
  }
}
```

The exact response convention will be finalized during API architecture.

---

# 27. Pagination

Large collections must not return unlimited records.

Endpoints such as:

```text
/cases
/investigations
/evidence
/comments
/notifications
```

will support pagination.

Initial approach:

```text
page
limit
```

The implementation can later move to cursor-based pagination for high-volume feeds if required.

---

# 28. Security Boundaries

The backend must enforce authorization server-side.

The frontend must never be trusted to enforce permissions.

Example:

```text
User
  ↓
Authentication
  ↓
Authorization
  ↓
Resource Ownership
  ↓
Business Rules
  ↓
Database Operation
```

Examples:

* Users can modify only resources they own.
* Investigation members receive only permitted access.
* Moderators receive moderation permissions.
* Administrative operations require elevated authorization.
* Private resources must never be returned to unauthorized users.

Detailed authentication and authorization rules will be defined in the dedicated security/authentication architecture steps.

---

# 29. Backend Scalability Strategy

The initial system will remain a single backend application.

```text
                 Load
                  │
                  ▼
            FastAPI Backend
                  │
          ┌───────┴───────┐
          ▼               ▼
      PostgreSQL          S3
```

If traffic increases, the backend can later scale horizontally:

```text
                Load Balancer
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
    FastAPI       FastAPI      FastAPI
        │            │            │
        └────────────┼────────────┘
                     ▼
                 PostgreSQL
```

The modular structure allows future extraction of individual domains if there is a genuine need.

---

# 30. Backend Architecture Principles

The backend will follow these principles:

### 1. Modular

Each domain has a clear responsibility.

### 2. Maintainable

Business logic belongs primarily in services.

### 3. Testable

Services and repositories should be independently testable.

### 4. Secure

Authorization is enforced server-side.

### 5. API-first

Frontend and backend communicate through clearly defined APIs.

### 6. Database-safe

Database operations use transactions where required.

### 7. Simple

Avoid infrastructure that is not currently necessary.

### 8. Extensible

AI, recommendations, search, and other advanced systems can evolve without restructuring the entire backend.

### 9. Observable

Important operations and failures are logged.

### 10. Production-oriented

The architecture should support containerized deployment and AWS hosting.

---

# 31. Final Backend Architecture

```text
                         AFTERWORDS
                             │
                             ▼
                    ┌─────────────────┐
                    │   React Client  │
                    └────────┬────────┘
                             │
                         REST API
                             │
                             ▼
                 ┌───────────────────────┐
                 │       FastAPI         │
                 │                       │
                 │ ┌───────────────────┐ │
                 │ │ Authentication    │ │
                 │ │ Users             │ │
                 │ │ Cases             │ │
                 │ │ Investigations    │ │
                 │ │ Evidence          │ │
                 │ │ Clues             │ │
                 │ │ Theories          │ │
                 │ │ Social            │ │
                 │ │ Feed              │ │
                 │ │ Notifications     │ │
                 │ │ Search            │ │
                 │ │ Recommendations   │ │
                 │ │ AI                │ │
                 │ │ Moderation        │ │
                 │ │ Media             │ │
                 │ └───────────────────┘ │
                 └───────────┬───────────┘
                             │
                  ┌──────────┴──────────┐
                  ▼                     ▼
           ┌──────────────┐      ┌──────────────┐
           │ PostgreSQL   │      │ Amazon S3    │
           │              │      │              │
           │ Application  │      │ Media /      │
           │ Data         │      │ Documents    │
           └──────────────┘      └──────────────┘
```


