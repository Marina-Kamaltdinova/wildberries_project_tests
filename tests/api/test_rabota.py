from wildberries_project_tests.utils.requests_helper import api_request


def test_travel_page():
    response = api_request('https://vsemrabota.ru', '/', 'GET')

    assert response.status_code == 200

    assert 'Поиск работы по всей России, новые вакансии и большая база резюме' in response.text
    assert ('Удобный поиск работы, большая база резюме, бесплатное размещение вакансий в неограниченном количестве'
            in response.text)
