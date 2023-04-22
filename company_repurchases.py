# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
from UpdateJson import JsonOpen,JsonUpdate,JsonStore
import datetime

diver=webdriver.Firefox()
diver.get('https://data.eastmoney.com/notices/hsa/6.html')
print("opendiver")
#today=datetime.datetime.now().strftime('%Y-%m-%d')
today='2023-04-20'
todayjson=[]
#元素定位到回购事件
element=diver.find_element(By.XPATH,'/html/body/div[1]/div[8]/div[2]/div[3]/div[2]/ul/li[14]')
element.click()
time.sleep(2)
address='/html/body/div[1]/div[8]/div[2]/div[3]/div[3]/div[2]/div[2]/table/tbody/tr['
for i in range(1,50):
    elements=diver.find_element(By.XPATH,address+str(i)+']')
    if today==elements.find_element(By.XPATH, address + str(i) + ']' + '/td[6]').text:
        data_dict = {
            'StockCode': elements.find_element(By.XPATH,address+str(i)+']'+'/td[1]').text,
            'StockName':elements.find_element(By.XPATH,address+str(i)+']'+'/td[2]').text,
            'Title':elements.find_element(By.XPATH, address + str(i) + ']' + '/td[4]').text,
            'Time':today,
            'ContextUrl':elements.find_element(By.XPATH, address + str(i) + ']' + '/td[4]').find_element(By.CSS_SELECTOR,'a').get_attribute('href')
        }
        print(today)
        todayjson.append(data_dict)
JsonStore(JsonUpdate(JsonOpen('repurchases.json'),todayjson))
diver.close()








