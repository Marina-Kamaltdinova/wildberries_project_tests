# Проект по тестированию интернет-магазина "https://www.wildberries.ru/"

![main page screenshot](pictures/wildberries_main_page.png)

---
### Список проверок, реализованных в web тестах
1. Открытие чата 'Поддержка Wildberries'.
2. Смена валюты.
3. Поиск товара по артикулу.
4. Поиск товара по фильтру.
5. Добавление товара в избранное.
6. Добавление товара в корзину.
7. Удаление товара из корзины.

---
### Список проверок, реализованных в api тестах
1. Поиск вакансий.
2. Смена валюты.
3. Поиск товара по фильтру.
4. Поиск товара по id.
5. Контакты.
6. Путешествия.
---

### Список проверок, реализованных в mobile тестах
1. Добавление товара в избранное.
2. Поиск товара в каталоге.
3. Выбор страны.
4. Поиск товара по фильтру.
5. Поиск вакансий.
---

### Используемые инструменты
<img title="Python" src="pictures/logo/python.icon.svg" height="40" width="40"/> 
<img title="Pytest" src="pictures/logo/pytest.icon.svg" height="40" width="40"/>
<img title="Allure Report" src="pictures/logo/allure.icon.png" height="40" width="40"/>
<img title="GitHub" src="pictures/logo/github.icon.svg" height="40" width="40"/> 
<img title="Selenoid" src="pictures/logo/selenoid.icon.png" height="40" width="40"/>
<img title="Selene" src="pictures/logo/selene.icon.png" height="40" width="40"/> 
<img title="Pycharm" src="pictures/logo/pycharm.icon.svg" height="40" width="40"/> 
<img title="Telegram" src="pictures/logo/telegram.icon.png" height="40" width="40"/> 
<img title="Jenkins" src="pictures/logo/jenkins.icon.svg" height="40" width="40"/>
<img src="pictures/logo/allure_testops.png" width="40">
<img src="pictures/logo/jira.png" width="40">
<img src="pictures/logo/appium.png" width="40"> 
<img src="pictures/logo/request.png" width="40">

---

### Запуск автотестов осуществляется с использованием Jenkins
> [Ссылка на сборку в Jenkins](https://jenkins.autotests.cloud/job/wildberries_project_tests/)

#### Для запуска автотестов в Jenkins
1. Открыть [задачу в Jenkins](https://jenkins.autotests.cloud/job/wildberries_project_tests/)

![jenkins job main page](pictures/jenkins_job_main_page.png)

2. Нажать "**Build Now**".

---

### Allure отчет

#### Общие результаты
![allure_report main page](pictures/allure_report.png)

---
#### Результаты прохождения тестов
![allure_report suites](pictures/allure_report_suites.png)

---
#### Примеры запуска в Allure TestOps
![This is an image](pictures/testops.png)

![This is an image](pictures/testops_run.png)

---
#### Список тест кейсов в Allure TestOps

![This is an image](pictures/testops_tests.png)
---

#### Интеграция с Jira

![This is an image](pictures/jira.png)
---

### Уведомления в Телеграм

![telegram_notification](pictures/tg_notification.jpg)

---

### Прохождение web теста

![autotest](pictures/video_ui.gif)

---

### Прохождение mobile теста

![autotest](pictures/mobile.gif)