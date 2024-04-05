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
    if page.title() == "Google":
        page.screenshot(path="abc.png")
        assert True
    else:
        page.screenshot(path="fail.png")
        assert False

    


def test_login(page):
    page.goto('https://demo.automationtesting.in/SignIn.html')
    page.wait_for_selector('//input[@placeholder="E mail"]').type("user")
    page.wait_for_selector('//input[@placeholder="Password"]').type("user")
    page.wait_for_selector('//img[@id="enterbtn"]').click()
    page.wait_for_timeout(3000)


def test_login(page):
    page.goto("https://www.saucedemo.com/")
    print(page.title)
    #login Process
    firstname = page.wait_for_selector('//input[@id = "user-name"]')
    firstname.type('visual_user')
    lastname = page.wait_for_selector('//input[@id = "password"]')
    lastname.type('secret_sauce')
    page.wait_for_selector('//input[@id = "login-button"]').click()
    page.screenshot(path="userpage.png")
    #login completed
    whitetshirt = page.wait_for_selector('//button[@id = "add-to-cart-sauce-labs-onesie"]').click()
    blacktshirt = page.wait_for_selector('//button[@id = "add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    addtocart = page.wait_for_selector('//div[@id  ="shopping_cart_container"]/a').click()
    checkout = page.wait_for_selector('//button[@id  ="checkout"]').click()
    fstname = page.wait_for_selector('//input[@id  ="first-name"]')
    fstname.type('Raja')
    lstname = page.wait_for_selector('//input[@id  ="last-name"]')
    lstname.type('Ram')
    pincode = page.wait_for_selector('//input[@id  ="postal-code"]')
    pincode.type('452002')
    continuebutton = page.wait_for_selector('//input[@id = "continue"]').click()
    finish = page.wait_for_selector('//button[@id = "finish"]').click()
    success = page.wait_for_selector('//h2[contains(text(), "Thank you for your order!")]')
    page.wait_for_selector('//button[@id = "back-to-products"]').click()
    print('passed')
    page.wait_for_timeout(2000)
     
    # To view the trace run the command in the terminal- playwright show-trace trace.zip
    