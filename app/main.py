import logging
from logging.config import dictConfig
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from app.operations import add, divide, multiply, subtract


class CalculatorRequest(BaseModel):
    a: float
    b: float


LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)


def configure_logging() -> None:
    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                },
                "file": {
                    "class": "logging.FileHandler",
                    "formatter": "default",
                    "filename": str(LOG_DIR / "app.log"),
                },
            },
            "root": {"level": "INFO", "handlers": ["console", "file"]},
        }
    )


configure_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="FastAPI Calculator")


@app.get("/", response_class=HTMLResponse)
def home() -> str:
    logger.info("Home page requested")
    index_path = Path("app/templates/index.html")
    return index_path.read_text(encoding="utf-8")


@app.get("/health")
def health() -> dict[str, str]:
    logger.info("Health check requested")
    return {"status": "ok"}


@app.post("/add")
def add_numbers(payload: CalculatorRequest) -> dict[str, float]:
    logger.info("/add endpoint called", extra={"a": payload.a, "b": payload.b})
    return {"result": add(payload.a, payload.b)}


@app.post("/subtract")
def subtract_numbers(payload: CalculatorRequest) -> dict[str, float]:
    logger.info("/subtract endpoint called", extra={"a": payload.a, "b": payload.b})
    return {"result": subtract(payload.a, payload.b)}


@app.post("/multiply")
def multiply_numbers(payload: CalculatorRequest) -> dict[str, float]:
    logger.info("/multiply endpoint called", extra={"a": payload.a, "b": payload.b})
    return {"result": multiply(payload.a, payload.b)}


@app.post("/divide")
def divide_numbers(payload: CalculatorRequest) -> dict[str, float]:
    logger.info("/divide endpoint called", extra={"a": payload.a, "b": payload.b})
    try:
        return {"result": divide(payload.a, payload.b)}
    except ValueError as exc:
        logger.exception("Error during divide operation")
        raise HTTPException(status_code=400, detail=str(exc)) from exc
