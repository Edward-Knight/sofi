import os

import pytest
from selenium import webdriver

from sample_test.sample import register
from sofi.app import Sofi

WD = os.getenv('WD')
ENV_LOCATION = os.getenv('ENV_LOCATION')


def pytest_addoption(parser):
    group = parser.getgroup('selenium', 'selenium')
    group._addoption('--headless',
                     action='store_true',
                     help='enable headless mode for supported browsers.'
                     )


@pytest.yield_fixture(scope="session")
def chrome(request):
    # Check the browser
    browser = request.config.getoption("--driver")
    if browser != 'Chrome':
        pytest.fail('only chrome is supported at the moment')
        return

    # Set Chrome options
    headless = request.config.getoption("--headless")

    chrome_options = webdriver.ChromeOptions()
    if headless:
        chrome_options.add_argument("headless")
        chrome_options.add_argument("no-sandbox")
        chrome_options.add_argument("disable-gpu")

    # Initiate Chrome with the page opened
    browser = webdriver.Chrome(chrome_options=chrome_options)

    browser.get(f"file://{WD}/{ENV_LOCATION}/lib/python3.6/site-packages/sofi/app/main.html")

    yield browser

    browser.quit()


@pytest.fixture(scope="session", autouse=True)
def start_ui():
    # Change the app to be on the background
    app = Sofi(background=True)
    register(app)
    app.start(desktop=False, browser=False)
    # Start the UI
