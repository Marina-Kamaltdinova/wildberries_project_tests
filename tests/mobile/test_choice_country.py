from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be
from wildberries_project_tests.utils.notifications import deny_send_notifications
import pytest


@pytest.mark.parametrize('country, price_icon', [
    ('Россия', '₽'),
    ('Беларусь', 'р'),
    ('Казахстан', '₸'),
    ('Киргизия', '⃀'),
    ('Армения', '֏'),
    ('Узбекистан', 'сўм')
], ids=['Russia', 'Belarus', 'Kazakhstan', 'Kyrgyzstan', 'Armenia', 'Uzbekistan'])
def test_choice_country(country, price_icon):
    deny_send_notifications()
    with (step('Verify choice country screen')):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="title"]')
                        ).should(have.text('Выбор страны')).click()

    with step('Choose country'):
        browser.element((AppiumBy.XPATH, f'//android.widget.TextView[@text="{country}"]')).click()

    with ((step('Verify price country'))):
        browser.element((AppiumBy.XPATH,
                         '//android.widget.FrameLayout[@resource-id="com.wildberries.ru:id/catalogContainer"]')
                        ).with_(timeout=15).should(be.visible)
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[contains(@content-desc, "Цена ")]')
                        ).should(have.text(price_icon))
