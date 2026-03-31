import logging

logger = logging.getLogger(__name__)


def add(a: float, b: float) -> float:
    result = a + b
    logger.info("add called", extra={"a": a, "b": b, "result": result})
    return result


def subtract(a: float, b: float) -> float:
    result = a - b
    logger.info("subtract called", extra={"a": a, "b": b, "result": result})
    return result


def multiply(a: float, b: float) -> float:
    result = a * b
    logger.info("multiply called", extra={"a": a, "b": b, "result": result})
    return result


def divide(a: float, b: float) -> float:
    if b == 0:
        logger.error("divide by zero attempted", extra={"a": a, "b": b})
        raise ValueError("Cannot divide by zero")

    result = a / b
    logger.info("divide called", extra={"a": a, "b": b, "result": result})
    return result
