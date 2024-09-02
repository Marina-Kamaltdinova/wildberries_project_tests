from wildberries_project_tests.utils.attach import response_logging, response_attaching
import requests


def api_request(url, endpoint, method, data=None, params=None):
    url = f"{url}{endpoint}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/124.0.0.0 Safari/537.36',
        'Content-Type': 'application/json'
    }
    response = requests.request(method, url, data=data, params=params, headers=headers)
    response_logging(response)
    response_attaching(response)
    return response
