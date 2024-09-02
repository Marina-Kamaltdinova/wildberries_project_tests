from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_added_random_item_to_favorite(choose_country):
    with step('Click on add to favorite icon'):
        browser.element((AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Добавить в отложенные"]')).click()

    with step('Verify alert message'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Необходима авторизация"]')
                        ).should(have.text('Необходима авторизация'))
