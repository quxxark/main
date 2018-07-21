import requests
from bs4 import BeautifulSoup as BS


loginPage = 'https://rutracker.org/forum/index.php'
url = 'https://rutracker.org/forum/viewforum.php?f=1960'

LOGIN = ''
PASSWORD = ''

formData = {'login_username': LOGIN, 'login_password': PASSWORD, 'login': '(unable to decode value)'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/67.0.3396.99 Safari/537.36'}


with requests.Session() as s:
    s.post(loginPage, data=formData, headers=headers)
    response = s.get(url)

    soup = BS(response.content, 'html.parser')
    soup.prettify()   # Красивый вывод HTML
    ul_list = soup.find_all('ul')   # Ищет все КЛАССЫ с тегом UL -- <ul class="inlined middot-separated floatL">
    # Ищет все классы с UL и с конкретным ЗНАЧЕНИЕМ КЛАССА
    lst = soup.find_all('ul', {'class': 'inlined middot-separated floatL'})

    for opt in lst:
        print(opt.text)

    '''
    Есть ещё вариант создатьп устой словарь. Если в списке вариантов есть ещё какие-либо списка, искать среди 
    всего с тегом "а", потом добавлять ТЕКСТ по тегу в словарь как ключ, и добавлять как значение ссылку "href" на
    этот самый тег
    Ниже приведён пример для такого класса:
    <ul class="height6" id="list">
    <li><a href="//LINK_FOR_1-ST">TEXT-1</a></li>
    <li><a href="//LINK_FOR_2-ND">TEXT-2</a></li>
    <li><a href="//LINK_FOR_3-RD">TEXT-3</a></li>
    </ul>
    
    city_dict = {}
    for city in city_list.find_all('a'):
        city_dict[city.text] = city['href']
    '''


