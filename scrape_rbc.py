from bs4 import BeautifulSoup, SoupStrainer
import urllib.request as urllib2
import re
import requests
import pandas as pd
from headers import HEADERS
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

SCROLL_PAUSE_TIME = 1

driver = webdriver.Firefox()
driver.get('https://www.rbc.ru/search/?query=%D1%80%D0%BE%D1%81%D1%81%D0%B8%D1%8F+%D1%81%D0%B8%D1%80%D0%B8%D1%8F+%D0%B2%D0%BE%D0%B9%D0%BD%D0%B0&project=rbcnews&dateFrom=01.05.2016&dateTo=31.08.2016')
driver.maximize_window()
links = []
last_height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    # Scroll down to bottom

	driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")

    # Wait to load page

	time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height

	new_height = driver.execute_script("return document.documentElement.scrollHeight")
	if new_height == last_height:
		print("break")
		break

	last_height = new_height



#WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Загрузить ещё")))
#while True:
#try:
	
	html = driver.page_source
	html = BeautifulSoup(html, "lxml")
	#print(html)
	#class="search-item__wrap l-col-center"
	#class="search-item__wrap l-col-center"
	#class="search-item js-search-item"
	articles = html.find_all('div', {'class': 'search-item js-search-item'})
	for article in articles:
		ankor_list = article.findChildren('a')
		for ankor in ankor_list:
		    url = ankor.get('href')
		    #url = 'https://russian.rt.com' + url
		    links.append(url)
		    print(url)

print(links)
final = pd.DataFrame({'links' : links})

final = final[~final['links'].str.contains('#ws')]
print(final)

final.to_csv('rbc_links.csv')