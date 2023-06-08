import time
from selenium import webdriver

import requests


# Open the website using Selenium
driver = webdriver.Chrome()  # Make sure to have Chrome driver installed and in PATH
driver.get("https://dhruv2424.blogspot.com/2022/06/blog-post.html?showComment=1685887785424&m=1")

# Wait for 10 seconds
time.sleep(10)

# Get the website content
website_content = driver.page_source

# Close the Selenium driver
driver.quit()







