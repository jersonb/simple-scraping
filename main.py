from playwright.sync_api import sync_playwright
'''
https://github.com/microsoft/playwright-python
'''

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        browser = browser_type.launch(headless=False)
        page = browser.new_page()
        page.goto('http://playwright.dev')
        page.screenshot(path=f'example-{browser_type.name}.png')
        browser.close()