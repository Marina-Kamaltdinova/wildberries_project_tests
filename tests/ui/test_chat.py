from wildberries_project_tests.models.pages.home_page import home


def test_open_chat():
    home.open_page()
    home.open_chat()
    home.verify_chat_title('Поддержка Wildberries')

