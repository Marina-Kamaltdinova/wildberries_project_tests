import allure
import os
import logging
import json
from requests import Response
from allure_commons.types import AttachmentType
import requests


def screenshot(browser):
    allure.attach(
        body=browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
        extension='.png'
    )


def html(browser):
    source_html = browser.driver.page_source
    allure.attach(
        body=source_html,
        name='page_source',
        attachment_type=allure.attachment_type.HTML,
        extension='.html'
    )


def video(browser):
    selenoid = os.getenv('SELENOID_URL')
    video_url = f"https://{selenoid}/video/" + browser.driver.session_id + ".mp4"
    html_markup = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
                  + video_url \
                  + "' type='video/mp4'></video></body></html>"
    allure.attach(
        body=html_markup,
        name='video_' + browser.driver.session_id,
        attachment_type=allure.attachment_type.HTML,
        extension='.html')


def add_xml(browser):
    xml_dump = browser.driver.page_source
    allure.attach(body=xml_dump,
                  name='XML screen',
                  attachment_type=allure.attachment_type.XML)


def add_video(session_id):
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(os.getenv('USER_NAME'), os.getenv('ACCESS_KEY')),
    ).json()

    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )


def response_logging(response: Response):
    logging.info("Request: " + response.request.url)
    if response.request.body:
        logging.info("INFO Request body: " + response.request.body)
    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Response code " + str(response.status_code))
    logging.info("Response: " + response.text)


def response_attaching(response: Response):

    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )
    allure.attach(
        body=response.request.method,
        name="Method",
        attachment_type=AttachmentType.TEXT,
    )
    allure.attach(
        body=str(response.request.headers),
        name="Request headers",
        attachment_type=AttachmentType.TEXT,
    )
    allure.attach(
        body=str(response.status_code),
        name="Response code",
        attachment_type=AttachmentType.TEXT,
    )

    if response.request.body:
        allure.attach(
            body=json.dumps(response.request.body, indent=4, ensure_ascii=True),
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
        allure.attach(
            body=json.dumps(response.json(), indent=4, ensure_ascii=True),
            name="Response",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
