# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
from UpdateJson import JsonOpen,JsonUpdate,JsonStore
import datetime


def JsonOpen(path):
    with open(path, 'r', encoding='UTF-8') as fr:
        data = json.loads(fr.read())
    return data

def JsonUpdate(data,newdata):
    data.append(newdata)
    return data

def JsonStore(data):
    data= json.dumps(data, ensure_ascii=False)
    with open('repurchases.json', 'w', encoding='UTF-8') as f:
        f.write(data)
        
        
        
diver=webdriver.Firefox()
diver.get('https://data.eastmoney.com/notices/hsa/6.html')
print("opendiver")
today=datetime.datetime.now().strftime('%Y-%m-%d')
todayjson=[]
#元素定位到回购事件
element=diver.find_element(By.XPATH,'/html/body/div[1]/div[8]/div[2]/div[3]/div[2]/ul/li[14]')
element.click()
time.sleep(2)


diver.close()








