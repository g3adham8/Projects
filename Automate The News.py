from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable)
now = datetime.now().strftime("%Y-%m-%d")
website = 'https://www.thesun.co.uk/sport/football/'

options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)
driver.get(website)

containers = driver.find_elements(by='xpath', value="//div[@class = 'story__copy-container']")

titles = []
sub_titles = []
links = []

for container in containers:
    title = container.find_element(by='xpath', value=".//p").text
    sub_title = container.find_element(by='xpath', value=".//h3").text
    link = container.find_element(by='xpath', value=".//a").get_attribute("href")

    titles.append(title)
    sub_titles.append(sub_title)
    links.append(link)

my_dict = {"Title": titles, "Sub Title": sub_titles, "Link": links}
df_headlines = pd.DataFrame(my_dict)

file_path = os.path.join(application_path, f"football_new_{now}.csv")
df_headlines.to_csv(file_path, index=True, encoding='utf-8-sig')

driver.quit()
