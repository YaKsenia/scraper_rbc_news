import requests
import re
from bs4 import BeautifulSoup
from headers import HEADERS
from selenium import webdriver
import pandas as pd

#url = 'https://www.rbc.ru/rbcfreenews/5799c3159a794750747d6337#ws'


def scrape_article(url):

	req = requests.get(url, HEADERS)

	plain_text = req.text

	html = BeautifulSoup(plain_text, "lxml")

	title = html.find('span', {'class': 'js-slide-title'})

	title_final = title.text

	articles = html.find('div', {'class': 'article__text article__text_free'})

	article_text = articles.text

	print(title_final, article_text)

	return {'title' : title_final, 'text' : article_text}


if __name__ == '__main__':
 
	df = pd.read_csv('/home/ksenia/Desktop/rbc_scripts/rbc_links_final.csv', sep=',', low_memory=False, na_values = ['no info', '.'])
	df = df.drop_duplicates(subset=['links'], keep='first', inplace=False)
	links = list(df['links'])
	titles = []
	texts = []
	for link in links:
		info = scrape_article(link)
		titles.append(info['title'])
		texts.append(info['text'])


	final = pd.DataFrame({'link' : links, 'title' : titles, 'text' : texts})

	final.to_csv('rbc_articles_all.csv')

#print(plain_text)
#article__text article__text_free