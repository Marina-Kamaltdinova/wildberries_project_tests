import json
from jsonschema import validate
from wildberries_project_tests.utils.resource import path
from wildberries_project_tests.utils.requests_helper import api_request

nm = '144132398'
dest = '-1257786'
query = 'платье'


def test_search_item_by_id():
    response = api_request('https://card.wb.ru', '/cards/v2/detail', 'GET',
                           params={"dest": dest, "nm": nm})
    body = response.json()
    schema = path('search_item_by_id.json')

    assert response.status_code == 200
    assert body['data']['products'][0]['id'] == 144132398

    with open(schema) as file:
        f = file.read()
        validate(body, schema=json.loads(f))


def test_search_item_by_name():
    response = api_request('https://search.wb.ru', '/exactmatch/ru/common/v7/search', 'GET',
                           params={"dest": dest, "query": query, "resultset": "catalog"})
    assert response.status_code == 200
    assert response.json()['metadata']['name'] == query
