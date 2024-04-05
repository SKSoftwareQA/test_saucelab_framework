import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


def test_TC_google(page):
    page.goto('https://www.google.com/')
    assert page.title() == "Google"


def test_login(page):
    page.goto('https://demo.automationtesting.in/SignIn.html')
    page.wait_for_selector('//input[@placeholder="E mail"]').type("user")
    page.wait_for_selector('//input[@placeholder="Password"]').type("user")
    page.wait_for_selector('//img[@id="enterbtn"]').click()
    page.wait_for_timeout(3000)
    