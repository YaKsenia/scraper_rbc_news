#from scrape_rbc import scrape_links
from scrape_article import Scraper
import pandas as pd
import traceback

try:
	url = 'https://www.rbc.ru/search/?query=%D1%80%D0%BE%D1%81%D1%81%D0%B8%D1%8F+%D1%81%D0%B8%D1%80%D0%B8%D1%8F+%D0%B2%D0%BE%D0%B9%D0%BD%D0%B0&project=rbcnews&dateFrom=01.05.2016&dateTo=31.08.2016'

	#links = scrape_links(url)
	#links = pd.read_csv('/home/ksenia_new/projects/scraping_thesis/rbc_scripts/rbc_links_check.csv')

	scraper = Scraper()

	links = scraper.scrape_links(url)

	df_articles = scraper.scrape_all(links)

	df_articles.to_csv('scraped_articles_rbc2.csv')

except Exception as e:
	print(e)
	print(traceback.format_exc())