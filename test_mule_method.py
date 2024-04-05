from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


    page.goto("https://bootswatch.com/default/")
    print(page.title)
    heading = page.get_by_role('heading', name='Heading 4')
    heading.highlight
    print(heading.text_content())
    #page.wait_for_timeout(5000)