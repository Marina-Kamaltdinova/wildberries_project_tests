import json
from jsonschema import validate
import pytest
from wildberries_project_tests.utils.resource import path
from wildberries_project_tests.utils.requests_helper import api_request


@pytest.mark.parametrize('currency', [
    pytest.param('RUB', id='RUB'),
    pytest.param('BYN', id='BYN'),
    pytest.param('KZT', id='KZT'),
    pytest.param('AMD', id='AMD'),
    pytest.param('KGS', id='KGS'),
    pytest.param('UZS', id='UZS')
])
def test_change_currency(currency):
    response = api_request('https://user-geo-data.wildberries.ru', '/get-geo-info', 'GET',
                           params={"currency": currency, "locale": "ru"})
    body = response.json()
    assert response.status_code == 200
    assert body['currency'] == currency
    assert body['locale'] == 'ru'

    with open(path('change_currency.json')) as file:
        f = file.read()
        validate(body, schema=json.loads(f))
