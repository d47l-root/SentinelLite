# SentinelLite

A lightweight log ingestion, detection, and alerting API — a simplified,
educational version of the kind of system a SOC (Security Operations Center)
uses to monitor security logs and automatically flag suspicious activity.

Logs come in through a REST API, get checked against detection rules
(currently: repeated failed login attempts), and any matches generate an
alert that's stored and retrievable through a separate, authenticated endpoint.

## Architecture

```
Log sources → POST /logs (FastAPI) → SQLite (logs table)
                                    ↓
                          Detection engine (rule-based)
                                    ↓
                          SQLite (alerts table) → GET /alerts (authenticated)
```

The application, database, and dependencies run inside a Docker container.

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI + Uvicorn
- **Validation:** Pydantic / pydantic-settings
- **Database:** SQLite + SQLAlchemy (ORM)
- **Testing:** pytest + httpx
- **Auth:** HTTP Basic Auth
- **Containerization:** Docker
- **Version Control:** Git & GitHub (feature branches, PR-based workflow)

## Setup

### Option 1: Docker (recommended)

1. Clone the repo:
   ```bash
   git clone https://github.com/d47l-root/SentinelLite.git
   cd SentinelLite
   ```
2. Copy `.env.example` to `.env` and fill in real values.
3. Build the image:
   ```bash
   docker build -t sentinellite .
   ```
4. Run the container:
   ```bash
   docker run -p 8000:8000 --env-file .env sentinellite
   ```
5. Visit `http://localhost:8000/docs` to explore the API.

### Option 2: Manual (without Docker)

1. Clone the repo and `cd` into it.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and fill in real values.
5. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Usage

All endpoints require HTTP Basic Auth (except `/health`).

### POST /logs
Ingest a new log entry. Automatically checked against detection rules.

**Request:**
```json
{
  "source": "auth-server",
  "message": "User admin failed login from 10.0.0.5"
}
```

**Response (200):**
```json
{
  "id": 5,
  "source": "auth-server",
  "message": "User admin failed login from 10.0.0.5",
  "timestamp": "2026-08-23T14:54:05.462837"
}
```

### GET /alerts
Retrieve all generated alerts.

**Response (200):**
```json
[
  {
    "id": 1,
    "description": "Possible failed login attempt detected",
    "severity": "medium",
    "log_id": 5,
    "timestamp": "2026-08-23T14:54:05.500000"
  }
]
```

## Running Tests

```bash
pytest
```

## Design Decisions

**Authentication:** I used HTTP Basic Auth because it's the simplest way to
learn how endpoint protection works. In production I'd use token-based auth
(OAuth/JWT) instead, since Basic Auth resends the plaintext password on
every request.

**Detection rules:** Rules are plain Python functions registered in a list,
so adding new detection logic doesn't require changing the engine itself —
only appending to the list.

## Roadmap

- [x] Log ingestion API
- [x] Rule-based detection engine
- [x] Alerts API with authentication
- [x] Unit tests
- [x] Dockerized deployment
- [ ] PostgreSQL support
- [ ] Multiple detection rules
- [ ] Stateful detection (e.g. rate-based brute-force detection)
