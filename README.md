# scraper of RBC news articles

This project collects news articles' titles and texts from the website of Russian newspaper RBC. You can choose any topic and time period, from which you want to get the articles.

Before running the project, you have to install the necessary software typing this command in your Terminal:

python3.6 -m pip install -r requirements.txt --upgrade

Then you should go to rbc.ru/search, choose the keywords and dates you are interested in, copy the resulting link and replace the link in settings.py file with this url.

![alt text](https://github.com/YaKsenia/scraper_rbc_news/blob/master/output/Screenshot_of_link_you_have_to_copy.png)


then you can just run the file main_rbc.py using this command in your Terminal:

python3.6 main_rbc.py 

Your browser window will be opened automatically. You don't have to do anything, just wait and don't close the window (you can do whatever you want in other programs while this one will be executed). This is what you will see:


![alt text](https://github.com/YaKsenia/scraper_rbc_news/blob/master/output/screenshot_of_browser_in_process.png)

After the browser will be closed, the program will continue executing in the Terminal and you will see headlines of scraped articles:

![alt text](https://github.com/YaKsenia/scraper_rbc_news/blob/master/output/screenshot_of%20the%20terminal_in_process.png)


The resulting csv-file will be saved in the folder of the project (you can see example in the folder "output" now). No matter how many articles will be in your results, the script automatically scrolls the webpage down until it reaches the end and scrapes all the articles.

This is how resulting file looks like:

![alt text](https://github.com/YaKsenia/scraper_rbc_news/blob/master/output/screenshot_of_saved_file.png)

