from wildberries_project_tests.utils.requests_helper import api_request


def test_travel_page():
    response = api_request('https://vmeste.wildberries.ru', '/', 'GET')

    assert response.status_code == 200

    assert 'Популярные направления' in response.text
    assert 'Идеи путешествий' in response.text
