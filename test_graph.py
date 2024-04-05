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



def test_open_url(page):
    page.goto("https://www.saucedemo.com/")
    login= page.wait_for_selector("//input[@id='user-name']")
    login.type('standard_user')
    password = page.wait_for_selector("//input[@id='password']")
    password.type('secret_sauce')
    page.wait_for_selector("//input[@id='login-button']").click()
    print(page.title)
    print("success")

    