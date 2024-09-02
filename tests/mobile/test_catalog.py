from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search_item_in_catalog(choose_country):
    with step('Click on catalog'):
        browser.element((AppiumBy.XPATH, '//android.view.View[@content-desc="Каталог"]')).click()

    with step('Click on woman category'):
        browser.element((AppiumBy.XPATH, '//android.view.View[@content-desc="Женщинам"]')).click()

    with step('Click on blouse and shirt category'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Блузки и рубашки"]')).click()

    with step('Verify title page'):
        browser.element((AppiumBy.ID, 'com.wildberries.ru:id/toolbarTitle')).should(have.text('Блузки и рубашки'))
