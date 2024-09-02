from wildberries_project_tests.utils.requests_helper import api_request


def test_kontakt():
    response = api_request('https://www.wildberries.ru', '/webapi/servicesdata/kontakty', 'POST')

    assert response.status_code == 200
    assert response.json()['value']['menuItems'][0]['name'] == 'О нас'
    assert response.json()['value']['menuItems'][1]['name'] == 'Реквизиты'
    assert response.json()['value']['menuItems'][2]['name'] == 'Пресс-служба'
    assert response.json()['value']['menuItems'][3]['name'] == 'Контакты'
    assert response.json()['value']['menuItems'][4]['name'] == 'Bug Bounty'
