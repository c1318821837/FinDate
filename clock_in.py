from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

diver=webdriver.Firefox()
diver.get('https://weibo.com')
with open('cookies.txt','r',encoding='utf8') as f:
    listCookies=json.loads(f.read())
for cookie in listCookies:
    cookie_dict={
        'domain':cookie.get('domain'),
        'name':cookie.get('name'),
        'value': cookie.get('value'),
        'expiry':cookie.get('expiry'),
        'path':'/',
        'httpOnly':False,
        'secure':True
    }
    diver.add_cookie(cookie_dict)
diver.refresh()
diver.get('https://weibo.com')
