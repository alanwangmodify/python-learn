#!/usr/bin/python
#coding:utf-8


from selenium import webdriver
from selenium.webdriver.common.keys import keys


driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

elem = driver.find_element_by_xpath()
elem.send_keys("test",keys.ENTER)