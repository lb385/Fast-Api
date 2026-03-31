import os

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.e2e
def test_user_can_add_two_numbers(page: Page) -> None:
    base_url = os.getenv("E2E_BASE_URL", "http://127.0.0.1:8000")
    page.goto(base_url)

    page.get_by_placeholder("Enter first number").fill("11")
    page.get_by_placeholder("Enter second number").fill("9")
    page.locator("#operation").select_option("add")
    page.get_by_role("button", name="Calculate").click()

    expect(page.locator("#result")).to_have_text("Result: 20")


@pytest.mark.e2e
def test_divide_by_zero_shows_error(page: Page) -> None:
    base_url = os.getenv("E2E_BASE_URL", "http://127.0.0.1:8000")
    page.goto(base_url)

    page.get_by_placeholder("Enter first number").fill("5")
    page.get_by_placeholder("Enter second number").fill("0")
    page.locator("#operation").select_option("divide")
    page.get_by_role("button", name="Calculate").click()

    expect(page.locator("#error")).to_have_text("Cannot divide by zero")
