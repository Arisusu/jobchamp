# frontend.py
import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time


layout = [[sg.Text('Input the job link you would like to autofill')],      
                 [sg.InputText()],      
                 [sg.Submit(), sg.Cancel()]]      

window = sg.Window('JobChamp', layout)    

event, values = window.read()    
window.close()

text_input = values[0]



def parse_content(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')

driver = webdriver.Chrome('/Users/nathanzhu/Documents/chromedriver')
driver.get(text_input)
tester = {"last_name" : "HELP", "first_name": "PLEASE", "phone" : "1111111111", "email" : "imdeadinside@gmail.com"
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

sg.popup('All data has been successfully entered')
