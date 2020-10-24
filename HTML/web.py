import requests
from requests_html import HTMLSession
import getpass
import json

'''
Последовательность:
1. Включаем dev tools
2. Вкладка Network / All
3. Логинимся
4. Ищем самый верхний пакет
5. Смотрим передаваемые данные (нас интересует Form data)
6. Получаем имена передаваемых ключей и данных
'''


# Прописываем линк для страницы логина
loginPage = ''


# Прописываем целевую линку (которую парсим)
link = ''


# Прописываем хедеры (User-Agent - Браузер, Content-Type - тип передаваемых данных)
headers = {'User-Agent': '', 'Content-Type': ''}


# Прописываем переменные логина/пароля (либо операторы ввода)
LOGIN = ''
PASSWORD = input('')
PASSWORD = getpass.getpass('')


# Вариант 1: работа без сессии


c = requests.get(loginPage, auth=(LOGIN, PASSWORD), headers=headers)
cookies = c.cookies
response = requests.get(link, headers=headers, cookies=cookies)


# Вариант 2: работа с сессией


loginData = dict(login=LOGIN, password=PASSWORD)

with requests.Session() as session:
    c = session.post(loginPage, headers=headers, loginData)
    response = session.get(link)


# Вариант 3: работа с HTML


session = HTMLSession()
r = session.get(loginPage, headers=headers, auth=(login, password))
par = session.get(link, headers=headers)


# Варианты работы с библиотеками:
# REQUESTS (GET)
r.status_code  # Получение статус-кода
r.headers      # Получение хедеров
r.headers['Content-Type']
r.headers.get('content-type')
r.text         # Получение контента страницы - юнико
r.content      # -бинарные данные
r.json()       # -джейсон
r.url          # Проверка построения url (при params)
r.encoding = 'ISO-8859-1'  # Смена кодировки

# REQUESTS-HTML
r.html.links  # получение ссылок
r.html.absolute_links  # Получение всех ссылок на ресурсы
about = r.html.find('#about', first=True)  # работа с CSS-селектором. about.text / about.attrs / about.html / about.find('a')
r.html.find(sel, first=True).text  # sel - переменная со стрингом селектора
'''
Примеры селекторов:
a
a.someClass
a#someID
a[target=_blank]
'''
r.html.xpath('a')  # работа с xpath



# Передача данных прямиком через линк
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)

# Передача данных через преобразование их в джейсон
payload = {'some': 'data'}
r = requests.post(link, data=json.dumps(payload))

# Запрет на редирект
r = requests.get('http://github.com', allow_redirects=False)

# Выставить таймаут соединения
requests.get('http://github.com', timeout=0.001)

# Исключения
ConnectionError
HTTPError
Timeout
TooManyRedirects
requests.exceptions.RequestException  # Базовый


# поиск по странице
for html in r.html:
    print(html)

r.html.search('Python is a {} language')[0]  # search_all

