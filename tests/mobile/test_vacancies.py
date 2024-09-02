from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_vacancies_in_wildberries(choose_country):
    with step('Click on profile'):
        browser.element((AppiumBy.XPATH, '//android.view.View[@content-desc="Профиль"]')).click()

    with step('Click on vacancies link'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Вакансии Wildberries"]')).click()

    with step('Verify vacancies page'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Wildberries"]')
                        ).should(have.text('Wildberries'))

        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Новая работа за\u00A0несколько минут"]')
                        ).with_(timeout=10).should(have.text('Новая работа за\u00A0несколько минут'))

        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Нам нужны близкие по\u00A0духу люди, '
                                         'разделяющие ценности Wildberries"]')).with_(timeout=10).should(
            have.text('Нам нужны близкие по\u00A0духу люди, разделяющие ценности Wildberries'))
