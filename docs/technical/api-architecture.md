# AfterWords — API Architecture

## 1. API Architecture

```text
React Frontend
      │
      │ HTTP / JSON
      ▼
   FastAPI
      │
      ▼
   /api/v1
      │
 ┌────┼───────────────────────────────────────┐
 │    │       │       │       │       │       │
 ▼    ▼       ▼       ▼       ▼       ▼       ▼
Auth Users   Cases  Invest. Evidence Theory Social
 │
 ├── Search
 ├── Feed
 ├── Notifications
 ├── AI
 ├── Recommendations
 └── Moderation
      │
      ▼
   Services
      │
      ▼
 PostgreSQL / S3 / AI APIs
```

---

## 2. API Base URL

```text
/api/v1
```

---

## 3. Authentication

```text
POST   /auth/register
POST   /auth/login
POST   /auth/logout
GET    /auth/me
POST   /auth/refresh
```

---

## 4. Users

```text
GET    /users/{id}
GET    /users/me
PATCH  /users/me
GET    /users/{id}/activity
GET    /users/{id}/followers
GET    /users/{id}/following
POST   /users/{id}/follow
DELETE /users/{id}/follow
```

---

## 5. Cases

```text
GET    /cases
POST   /cases
GET    /cases/{id}
PATCH  /cases/{id}
DELETE /cases/{id}

POST   /cases/{id}/publish
POST   /cases/{id}/bookmark
DELETE /cases/{id}/bookmark
```

Query parameters:

```text
?page=1
&limit=20
&category=
&status=
&difficulty=
&sort=
```

---

## 6. Investigations

```text
GET    /investigations
POST   /investigations
GET    /investigations/{id}
PATCH  /investigations/{id}
DELETE /investigations/{id}

POST   /investigations/{id}/join
DELETE /investigations/{id}/leave

GET    /investigations/{id}/members
GET    /investigations/{id}/activity
```

---

## 7. Evidence

```text
GET    /cases/{id}/evidence
POST   /cases/{id}/evidence

GET    /evidence/{id}
PATCH  /evidence/{id}
DELETE /evidence/{id}

POST   /evidence/{id}/sources
POST   /evidence/{id}/files
```

---

## 8. Clues

```text
GET    /cases/{id}/clues
POST   /cases/{id}/clues

GET    /clues/{id}
PATCH  /clues/{id}
DELETE /clues/{id}

POST   /clues/{id}/evidence/{evidence_id}
DELETE /clues/{id}/evidence/{evidence_id}
```

---

## 9. Theories

```text
GET    /cases/{id}/theories
POST   /cases/{id}/theories

GET    /theories/{id}
PATCH  /theories/{id}
DELETE /theories/{id}

POST   /theories/{id}/evidence
POST   /theories/{id}/clues
```

---

## 10. Comments

```text
GET    /{resource}/{id}/comments
POST   /{resource}/{id}/comments

PATCH  /comments/{id}
DELETE /comments/{id}

POST   /comments/{id}/reactions
DELETE /comments/{id}/reactions
```

---

## 11. Feed

```text
GET /feed
```

Initial feed:

```text
Following
   +
Investigations
   +
Cases
   +
Community activity
```

---

## 12. Search

```text
GET /search
```

Example:

```text
/search?q=disappearance&type=case
/search?q=moon&type=all
```

Supported types:

```text
all
cases
users
investigations
evidence
theories
```

---

## 13. Notifications

```text
GET   /notifications
PATCH /notifications/{id}/read
POST  /notifications/read-all
```

---

## 14. AI

```text
POST /ai/cases/{id}/summarize
POST /ai/evidence/{id}/analyze
POST /ai/theories/{id}/analyze
POST /ai/investigations/{id}/assist
POST /ai/search
```

AI endpoints should call the internal AI service rather than exposing model providers directly.

---

## 15. Recommendations

```text
GET /recommendations/cases
GET /recommendations/users
GET /recommendations/investigations
```

---

## 16. Media

```text
POST   /media/upload
GET    /media/{id}
DELETE /media/{id}
```

Actual files:

```text
Client
  ↓
FastAPI
  ↓
S3
```

---

## 17. Moderation

```text
POST /reports
GET  /moderation/reports
PATCH /moderation/reports/{id}
```

---

## 18. Standard Response

```json
{
  "success": true,
  "data": {}
}
```

Error:

```json
{
  "success": false,
  "error": {
    "code": "NOT_FOUND",
    "message": "Resource not found"
  }
}
```

---

## 19. API Request Flow

```text
Frontend
   ↓
Router
   ↓
Auth
   ↓
Validation
   ↓
Service
   ↓
Repository
   ↓
Database
   ↓
Response Schema
   ↓
Frontend
```

---

## 20. API Rules

```text
REST
JSON
/api/v1
JWT/session authentication
Pydantic validation
Pagination
HTTP status codes
Centralized errors
Server-side authorization
```

