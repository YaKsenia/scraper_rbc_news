# scraper_rbc_news

This project collects news articles' titles and texts from the website of Russian newspaper RBC. You can choose any topic and time period, from which you want to get the articles.

Before running the project, you have to install the necessary software typing this command in your Terminal:

python3.6 -m pip install -r requirements.txt --upgrade

Then you should go to rbc.ru/search, choose the keywords and dates you are interested in, copy the resulting link and replace the link in settings.py file with this url.

then you can just run the file main_rbc.py using this command in your Terminal:

python3.6 main_rbc.py 


The resulting csv-file will be saved in the folder of the project. No matter how many articles will be in your results, the script automatically scrolls the webpage down until it reaches the end and scrapes all the articles.
