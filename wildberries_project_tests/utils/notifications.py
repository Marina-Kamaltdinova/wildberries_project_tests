from selene import browser, be
from allure import step
from appium.webdriver.common.appiumby import AppiumBy


def deny_send_notifications():
    with step('Allow send notifications'):
        if browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_message')
                           ).with_(timeout=5).matching(be.visible):
            browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')).click()
