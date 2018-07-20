from requests_html import HTMLSession
import requests


session = HTMLSession()
url_login = 'https://adc.luxoft.com/confluence/login.action'
url_target = 'https://adc.luxoft.com/confluence/display/HNAVSTD/'

login = ''
password = ''
auth = (login, password)
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 '
                         'Safari/537.36'}

with requests.Session() as s:
    response = s.get(url_login, auth=auth, headers=headers)
    r = session.get(url_target)
    r.html.find('#childrenspan336669948-0', first=True)


