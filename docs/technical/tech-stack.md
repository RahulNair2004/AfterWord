
# 1. Stack Overview

AfterWords will use a deliberately focused technology stack.

```text
                        AFTERWORDS
                            │
                            ▼
                  ┌──────────────────┐
                  │ React Frontend   │
                  │ Tailwind CSS     │
                  └────────┬─────────┘
                           │
                         HTTP
                           │
                           ▼
                  ┌──────────────────┐
                  │ FastAPI Backend  │
                  │ Python           │
                  └────────┬─────────┘
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
        PostgreSQL       AI/ML        File Storage
             │             │             │
             └─────────────┼─────────────┘
                           │
                           ▼
                         AWS
                           │
                           ▼
                         Docker
```

---

# 2. Frontend

## React

**Technology:** React

React will be used to build the AfterWords web application.

Responsibilities:

* UI rendering
* Routing
* Component architecture
* Forms
* Client-side state
* API communication
* User interactions
* Loading and error states

The frontend will use standard React patterns.

We will **not introduce Zustand, Redux, TanStack Query, or another state-management library initially**.

Where practical:

```text
React State
    +
React Context
    +
Native Fetch
```

will be sufficient.

---

# 3. Styling

## Tailwind CSS

Tailwind CSS will be used for the complete frontend styling system.

Responsibilities:

* Layout
* Responsive design
* Typography
* Spacing
* Components
* Themes
* Responsive breakpoints
* UI states

No additional UI framework is required initially.

---

# 4. Frontend Routing

## React Router

React Router will handle application navigation.

Example:

```text
/
├── /login
├── /register
├── /feed
├── /explore
├── /cases
├── /cases/:id
├── /investigations/:id
├── /theories/:id
├── /profile/:username
├── /search
├── /notifications
└── /settings
```

---

# 5. Frontend API Communication

The frontend will communicate with FastAPI through REST APIs.

```text
React
   │
   │ HTTP/HTTPS
   ▼
FastAPI
```

The frontend will initially use the browser's native:

```javascript
fetch()
```

for API communication.

A small reusable API utility layer can be created without introducing a large data-fetching framework.

---

# 6. Backend

## FastAPI

**Technology:** FastAPI

FastAPI will be the primary backend framework.

Responsibilities:

* REST APIs
* Request validation
* Authentication
* Authorization
* Business logic
* Database interaction
* AI/ML integration
* File handling
* Background processing where appropriate

Backend language:

```text
Python 3.x
```

---

# 7. Backend Supporting Technologies

## Pydantic

Used for:

* Request validation
* Response schemas
* Configuration
* Data serialization

---

## SQLAlchemy

Used as the ORM/database abstraction layer.

Responsibilities:

* Database models
* Queries
* Relationships
* Transactions
* Database interaction

---

## Alembic

Used for database migrations.

Example:

```text
Model change
     ↓
Alembic migration
     ↓
PostgreSQL schema update
```

---

# 8. Database

## PostgreSQL

PostgreSQL will be the primary database for AfterWords.

It will store:

```text
Users
Profiles
Cases
Investigations
Evidence
Clues
Theories
Posts
Comments
Reactions
Followers
Bookmarks
Notifications
Reports
Moderation data
AI-related metadata
```

PostgreSQL will remain the primary source of truth.

---

# 9. AI / ML

The AI/ML layer will use Python because the backend and ML ecosystem are both strongest in Python.

Core technologies:

```text
Python
FastAPI
PyTorch
scikit-learn
Transformers
LLM APIs / Models
```

The exact AI model/provider will be selected when implementing the AI architecture.

---

# 10. AI Responsibilities

AI will potentially support:

```text
Case summarization
Evidence analysis
Theory assistance
Question generation
Semantic understanding
Content analysis
Recommendations
Moderation assistance
```

AI will remain a separate logical layer inside the backend.

```text
FastAPI
   │
   └── AI Module
          │
          ├── LLM
          ├── NLP
          ├── Embeddings
          └── ML Models
```

---

# 11. Machine Learning

For traditional ML functionality:

**scikit-learn** will be used initially.

Potential applications:

* Recommendation models
* Classification
* Ranking
* Content analysis
* User/content similarity

For deep learning:

**PyTorch** will be used where necessary.

We will not introduce ML infrastructure that isn't required by the actual product.

---

# 12. NLP / LLM

The NLP/LLM layer may use:

* Hugging Face Transformers
* Sentence Transformers
* LLM APIs
* Embedding models

The specific models will be finalized during the AI architecture/implementation stage.

The application should keep model/provider integration behind an internal interface so models can be replaced later.

---

# 13. File & Media Storage

Large files should not be stored directly inside PostgreSQL.

AWS object storage will be used.

## Amazon S3

S3 will store:

```text
Case images
Evidence documents
User uploads
Profile images
Audio
Video
Other media
```

PostgreSQL stores metadata and references to those objects.

---

# 14. Cloud Platform

## AWS

AWS will be the primary cloud platform.

The initial architecture will use only the AWS services that are actually necessary.

Potential services:

```text
Amazon EC2 / ECS
Amazon RDS
Amazon S3
CloudFront
Route 53
IAM
CloudWatch
```

The exact service selection will be finalized during the deployment phase.

We will avoid unnecessary AWS services during the MVP.

---

# 15. AWS Responsibilities

### Compute

Runs:

```text
FastAPI backend
Background processing
AI services where appropriate
```

### Database

Amazon RDS can host:

```text
PostgreSQL
```

### Storage

Amazon S3:

```text
Media
Evidence
Documents
Uploads
```

### CDN

CloudFront can serve:

```text
Frontend assets
Static content
Public media where appropriate
```

### DNS

Route 53 can manage:

```text
afterwords domain
API domain
DNS records
```

### Monitoring

CloudWatch can provide:

```text
Application logs
Infrastructure logs
Basic monitoring
```

### IAM

IAM controls:

```text
AWS users
Roles
Permissions
Service access
```

---

# 16. Docker

Docker will be used to create reproducible development and deployment environments.

Main containers:

```text
Frontend
Backend
PostgreSQL
```

Development architecture:

```text
Docker Compose
│
├── frontend
├── backend
└── postgres
```

AI dependencies can remain within the backend container initially unless their resource requirements justify separation later.

---

# 17. Docker Responsibilities

Docker provides:

* Environment consistency
* Reproducible development
* Dependency isolation
* Easy local setup
* Deployment packaging

Example:

```text
Developer
    ↓
docker compose up
    ↓
Frontend + Backend + PostgreSQL
```

---

# 18. Version Control

## Git

Git will be used for source control.

## GitHub

GitHub will host:

```text
Source code
Documentation
Issues
Pull requests
CI/CD configuration
```

Repository structure:

```text
afterwords/
```

---

# 19. Testing

Testing stack:

### Backend

```text
pytest
```

### API

```text
FastAPI TestClient
```

### Frontend

```text
Vitest
React Testing Library
```

Testing will cover:

* Unit tests
* API tests
* Service tests
* Database tests
* Component tests
* Integration tests

End-to-end testing can be introduced later if required.

---

# 20. Code Quality

Backend:

```text
Ruff
Black
Pytest
```

Frontend:

```text
ESLint
Prettier
```

The exact formatter/linter configuration will be finalized during the development infrastructure stage.

---

# 21. CI/CD

GitHub Actions will eventually automate:

```text
Push
  ↓
Install dependencies
  ↓
Lint
  ↓
Run tests
  ↓
Build Docker images
  ↓
Deploy
```

Deployment targets will be defined during the deployment phase.

---

# 22. Authentication

Authentication will be implemented in FastAPI.

The system will support:

```text
Registration
Login
Logout
Password hashing
Email verification
Access authentication
Authorization
```

The exact authentication/token implementation will be defined in the Authentication Architecture step.

---

# 23. API Architecture

Primary API style:

```text
REST
```

Example:

```text
/api/v1/auth
/api/v1/users
/api/v1/cases
/api/v1/investigations
/api/v1/evidence
/api/v1/clues
/api/v1/theories
/api/v1/posts
/api/v1/comments
/api/v1/search
/api/v1/notifications
/api/v1/ai
```

API versioning will begin with:

```text
/api/v1/
```

---

# 24. What We Are NOT Using Initially

To keep the architecture manageable, the MVP will **not** introduce:

```text
Redis
Kafka
RabbitMQ
Kubernetes
Microservices
GraphQL
Redux
Zustand
TanStack Query
Elasticsearch
OpenSearch
Separate AI microservices
Separate databases per service
Complex event infrastructure
```

These can be introduced later only if actual requirements justify them.

---

# 25. Core Technology Stack

| Layer               | Technology                                       |
| ------------------- | ------------------------------------------------ |
| Frontend            | React                                            |
| Styling             | Tailwind CSS                                     |
| Routing             | React Router                                     |
| Frontend API        | Native Fetch                                     |
| Backend             | FastAPI                                          |
| Language            | Python                                           |
| Validation          | Pydantic                                         |
| ORM                 | SQLAlchemy                                       |
| Migrations          | Alembic                                          |
| Database            | PostgreSQL                                       |
| AI/ML Language      | Python                                           |
| ML                  | scikit-learn                                     |
| Deep Learning       | PyTorch                                          |
| NLP                 | Hugging Face Transformers                        |
| Embeddings          | Sentence Transformers / suitable embedding model |
| LLM                 | Selected LLM/API during AI implementation        |
| File Storage        | Amazon S3                                        |
| Cloud               | AWS                                              |
| Containers          | Docker                                           |
| Local Orchestration | Docker Compose                                   |
| Version Control     | Git                                              |
| Repository          | GitHub                                           |
| Backend Testing     | Pytest                                           |
| Frontend Testing    | Vitest + React Testing Library                   |
| Backend Linting     | Ruff                                             |
| Frontend Linting    | ESLint                                           |
| Formatting          | Black + Prettier                                 |
| CI/CD               | GitHub Actions                                   |

---

# 26. Final Technology Architecture

```text
                         AFTERWORDS
                             │
                             ▼
                  ┌────────────────────┐
                  │   React Frontend   │
                  │   Tailwind CSS     │
                  │   React Router     │
                  └─────────┬──────────┘
                            │
                         HTTPS
                            │
                            ▼
                  ┌────────────────────┐
                  │   FastAPI Backend  │
                  │      Python        │
                  └─────────┬──────────┘
                            │
              ┌─────────────┼─────────────┐
              │             │             │
              ▼             ▼             ▼
        ┌──────────┐   ┌──────────┐   ┌──────────┐
        │PostgreSQL│   │  AI / ML │   │   S3     │
        │          │   │ PyTorch  │   │  Media   │
        │          │   │ sklearn  │   │  Files   │
        └──────────┘   │Transformers│  └──────────┘
                       └──────────┘
                            │
                            ▼
                           AWS
                            │
                       ┌────┴────┐
                       │         │
                    Docker    GitHub
```

---

# 27. Technology Principles

1. **Keep the MVP simple.**
2. **Use React + Tailwind for the frontend.**
3. **Use FastAPI + Python for the backend.**
4. **Use PostgreSQL as the primary database.**
5. **Use Python for AI/ML.**
6. **Use S3 for large files.**
7. **Use Docker for reproducible environments.**
8. **Use AWS for cloud infrastructure.**
9. **Avoid unnecessary infrastructure.**
10. **Introduce additional technologies only when a concrete requirement appears.**

---
