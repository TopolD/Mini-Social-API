# Mini social-apie
A Social api  where users can create posts and send likes for those  posts

---
## Features:

- Create post
- send like for post
---
## Techologies

- **Language:** Python
- **Framework:** FastApi
- **Language:** PostgreSQL
- **ORM and migrations:** SQLAlchemy, Alembic
-  **Infrastructure and background tasks:** Docker
---
## Testing

- **Test Framework:** Pytest

---
## Requirements

- **Python:** 3.12
- **Docker**
- **SQLAlchemy**
---
## How start

1. Clone project with GitHub
2. copy requiremens.txt
   ```bash
      pip install -r requirements.txt
   ```
3. Copy a virtual en_example
4. Start with Docker:
   ```bash
      docker compose up --build -d
   ```

---

| Method | URL | description |
|--------|-----|------|
| GET    | `/docs` | Swagger UI документація |
| GET    | `/redoc` | ReDoc документація |
| GET    | `/openapi.json` | OpenAPI JSON документація |
