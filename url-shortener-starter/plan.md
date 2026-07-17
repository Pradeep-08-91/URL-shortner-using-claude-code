# Project Plan: URL Shortener API ("shrtn")

## Goal
A small REST API that shortens URLs, redirects visitors, and reports click stats.
Purpose: exercise a full plan → build → review → test → deploy loop with Claude Code agents on a personal laptop.

## Stack
- Python 3.11+, FastAPI, Uvicorn
- SQLite via SQLAlchemy (no external infra)
- pytest + httpx for tests
- Docker + docker compose for local "deploy"
- GitHub Actions for CI (lint, test, build image)

## Endpoints
| Method | Path | Purpose |
|---|---|---|
| POST | /links | Body: {"url": "..."} → returns {"code": "abc123", "short_url": "..."} |
| GET | /{code} | 302 redirect to the original URL; increments click count |
| GET | /links/{code}/stats | Returns {"url", "code", "clicks", "created_at"} |
| GET | /healthz | Liveness check for deploy step |

## Requirements
1. Validate input URLs: must be http/https, reject javascript:/data: schemes (open-redirect & XSS surface)
2. Codes: 6-char base62, collision-checked on insert
3. Unknown code → 404 JSON error, not a crash
4. Rate limit POST /links (simple in-memory limiter is fine for v1)
5. Config via environment variables (BASE_URL, DATABASE_URL); never hardcode
6. Structured logging of requests (no secrets in logs)

## Milestones
- **M1 – Skeleton**: FastAPI app, /healthz, project layout, Dockerfile
- **M2 – Core**: POST /links + GET /{code} with SQLite persistence
- **M3 – Stats & hardening**: stats endpoint, validation, rate limit, error handling
- **M4 – Tests**: unit tests (code generation, validation) + integration tests (full request cycle); target ≥85% coverage
- **M5 – CI/CD**: GitHub Actions runs lint + tests on every PR; builds Docker image on merge to main; branch protection requires green checks

## Definition of Done (per milestone)
- Code reviewed by the code-reviewer agent, findings addressed
- test-runner agent reports all tests green
- PR merged via squash with a descriptive message

## Out of scope (v1)
Auth, custom aliases, link expiry, web UI, real hosting. Add later as stretch goals.

## Risks / watch-list for the reviewer
- Open redirect via unvalidated schemes
- SQL injection (mitigated by ORM, verify no raw SQL)
- Secrets leaking into logs or the repo
