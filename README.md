# FastAPI Calculator with Testing + CI

This project contains a FastAPI calculator application with:
- Unit tests for `operations.py`
- Integration tests for all API endpoints in `main.py`
- End-to-end tests using Playwright
- Logging for operations and errors
- GitHub Actions CI workflow

## Project Structure

- `app/main.py` - FastAPI app and API routes
- `app/operations.py` - calculator operations
- `app/templates/index.html` - web UI
- `tests/unit` - unit tests
- `tests/integration` - integration tests
- `tests/e2e` - Playwright E2E tests
- `.github/workflows/ci.yml` - CI pipeline

## Run Locally

1. Create and activate a Python virtual environment.
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Install browser dependencies for Playwright:
   - `python -m playwright install --with-deps chromium`
4. Run the app:
   - `uvicorn app.main:app --reload`
5. Open browser:
   - `http://127.0.0.1:8000`

## Run Tests

- Unit tests:
  - `pytest tests/unit`
- Integration tests:
  - `pytest tests/integration`
- E2E tests (app must be running):
  - `E2E_BASE_URL=http://127.0.0.1:8000 pytest tests/e2e`

## Logging

Application logs are written to:
- `logs/app.log`

## Git Workflow (Suggested)

Use descriptive commit messages, for example:
- `feat: add calculator operations and API routes`
- `test: add unit and integration tests`
- `test: add playwright end-to-end tests`
- `ci: add github actions workflow`
