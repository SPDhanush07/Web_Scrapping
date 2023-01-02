# Modules to load
from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep

# Using chrome web browser in selenium
driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')

# Requesting web link 
driver.get(f'https://www.foundit.in/')

# Selecting search bar of course and location
input_search = driver.find_element("id", 'SE_home_autocomplete')
input_location = driver.find_element('id', 'SE_home_autocomplete_location')
input_search.send_keys('python')
input_location.send_keys('Bengaluru')

# Selecting search bar for searching jobs
search_button = driver.find_element('xpath', "//input[@class='btn']")
# Clicking the search button
search_button.click()

# Maximizing the browser window
driver.maximize_window()

# scraping job details
items = [] 
for k in range(10): 
    print('scaping page', k+1)
    job_details = driver.find_elements(By.CLASS_NAME, 'cardContainer') 
    for i in job_details: 
        title = i.find_element(By.CLASS_NAME, 'jobTitle').text 
        company = i.find_element(By.CLASS_NAME, 'companyName') 
        company_name = company.find_element(By.TAG_NAME,'p').text 
        details = i.find_elements(By.CLASS_NAME, 'details')[0].text 
        posted_time = i.find_element(By.XPATH, "//p[@class='timeText']").text 
        q = f'{title} - {company_name} - {details} - {posted_time}' 
        items.append(q) 
    next_button = driver.find_element(By.XPATH, "//div[@class='arrow arrow-right']") 
    next_button.click() 
    sleep(5) 

# To transfer the data to text file
for item in items:
    to_write = f"{str(item)}, \n" 
    with open(r'C:\Users\..\jobdetails.txt', 'a') as f: 
        f.write(to_write) 
    f.close() 