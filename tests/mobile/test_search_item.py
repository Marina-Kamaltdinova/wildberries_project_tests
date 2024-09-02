from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_search_item_in_site(choose_country):
    with step('Click on search input'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Поиск"]')).click()

        browser.element((AppiumBy.XPATH, '//android.widget.EditText')).type('Платье')

    with step('Choose dress category'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="платье женское"]')).click()

    with step('Verify search result'):
        browser.element((AppiumBy.ID, 'com.wildberries.ru:id/toolbarClickTitle')
                        ).with_(timeout=10).should(have.text('платье женское'))

    with step('Verify card item visible'):
        browser.element((AppiumBy.ID, 'com.wildberries.ru:id/catalogContainer')).with_(timeout=10).should(be.visible)
