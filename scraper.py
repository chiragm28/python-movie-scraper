# selenium and bs4 to scrape

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests


browser = webdriver.Chrome('/Users/chiragmali/Downloads/chromedriver')
browser.get('https://www.google.com/')
google_search = browser.find_element_by_name('q')
google_search.send_keys('top imdb movies')
google_search.submit()
# open first imdb link
imdb = browser.find_element_by_xpath('//h3[1]')
imdb.click()
window_before = browser.window_handles[0]
#window_before_title = browser.title

# switch to tab 2 to open fmovies
browser.execute_script("window.open('https://www2.fmovies2.io/', 'new window')")
window_after = browser.window_handles[1]

browser.switch_to_window(window_after)

# using soup to scrape data of the top movies
html = browser.current_url
html_source = requests.get(html).text
soup = BeautifulSoup(html_source, 'lxml')

# stop selenium browser
browser.quit()
