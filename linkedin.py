# Importing necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import pandas as pd

# initializing the web browser
driver = webdriver.Chrome()

course = input('Type course to search: ')
loc = input('Typr your preferred locatoin: ')

# requesting the targeted website
driver.get(f"https://www.linkedin.com/jobs/search?keywords={course}&location={loc}")
driver.implicitly_wait(3)

# Scrolling to end of the document with targeted action
i = 2
while i <= 15:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    i += 1
    try:
        search_more = driver.find_element(By.XPATH, "//button[@class='infinite-scroller__show-more-button infinite-scroller__show-more-button--visible']")
        search_more.click()
        sleep(3)
    except:
        pass
        sleep(3)

# loading the targeted elements in the website through inspection
ul = driver.find_element(By.XPATH, "//ul[@class='jobs-search__results-list']")
lists = ul.find_elements(By.TAG_NAME, "li")
items = []

for job in lists:
    try:
        title = job.find_element(By.XPATH, ".//h3[@class='base-search-card__title']").text
        company = job.find_element(By.XPATH, ".//a[@class='hidden-nested-link']").text
        location = job.find_element(By.XPATH, ".//span[@class='job-search-card__location']").text
        posted_time = job.find_element(By.XPATH, ".//time[@class='job-search-card__listdate']").text
        #  print(f'{title} - {company} - {location}- {posted_time}') # to inspect data through printing
        item = {
        'Title':title,
        'Company':company,
        'Location':location,
        'Posted_time':posted_time
        }
        items.append(item) # add scrapped elements to item list
    except:
        print('done')


# loading scrapped data to pandas and retriveing output as CSV file 
df = pd.DataFrame(items)
df.to_csv(r"C:\Users\..\linkedin.csv")

## loading scrapped data into a text document
for item in items:
    to_write = f"{str(item)}, \n"
    with open(r"C:\Users\..\linkeddin.txt", 'a') as f: 
        f.write(to_write) 
        f.close()