import pytest
from appium import webdriver
from dotenv import load_dotenv
from selene import browser, have, be
from appium.webdriver.common.appiumby import AppiumBy
from allure import step

import config
from wildberries_project_tests.utils import attach
from wildberries_project_tests.utils.notifications import deny_send_notifications


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="bstack",
        help="Specify the test context"
    )


def pytest_configure(config):
    context = config.getoption("--context")
    env_file_path = f".env.{context}"

    load_dotenv(dotenv_path=env_file_path)


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function', autouse=True)
def mobile_management(context):
    options = config.to_driver_options(context=context)

    browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)
    browser.config.timeout = 10.0

    yield

    attach.screenshot(browser)
    attach.add_xml(browser)

    browser.quit()

    if context == 'bstack':
        session_id = browser.driver.session_id
        attach.add_video(session_id)


@pytest.fixture()
def choose_country():
    deny_send_notifications()
    with (step('Verify choice country screen')):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="title"]')
                        ).should(have.text('Выбор страны')).click()

    with step('Choose country'):
        browser.element((AppiumBy.XPATH, f'//android.widget.TextView[@text="Россия"]')).click()

    with (step('Verify item visible')):
        browser.element((AppiumBy.XPATH,
                         '(//android.widget.FrameLayout[@resource-id="com.wildberries.ru:id/catalogContainer"])')
                        ).with_(timeout=15).should(be.visible)
