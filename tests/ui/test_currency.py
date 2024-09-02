from wildberries_project_tests.models.pages.currency_page import currency
from wildberries_project_tests.models.pages.home_page import home


def test_currency_replacement():
    home.open_page()
    currency.currency_replacement_check('RUB')
    currency.choice_currency()
    currency.currency_replacement('Казахстанский тенге')
    currency.check_replacement('KZT')
    currency.choice_currency()
    currency.check_replacement('KZT')
    currency.currency_back('Российский рубль')
    currency.check_replacement('RUB')
