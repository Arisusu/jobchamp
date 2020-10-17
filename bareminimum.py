from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time


def parse_content(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')

driver = webdriver.Chrome('/Users/nathanzhu/Documents/chromedriver')
driver.get("https://www.dropbox.com/jobs/listing/1073977/apply")
tester = {"last_name" : "Zhu", "first_name": "Nathan", "phone" : "7706700310", "email" : "nathanzhu9@gmail.com"
          }


for bruh, data in tester.items():
    try:
        temp = driver.find_element_by_id(bruh)
        temp.send_keys(data)
    except:
        temp = driver.find_element_by_name(bruh)
        temp.send_keys(data)
        time.sleep(1)
    finally:
        time.sleep(1)
        continue
    

html_doc = driver.page_source
parse_content(html_doc)
