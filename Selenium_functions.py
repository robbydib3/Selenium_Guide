# These are all the packages we will need to operate Selenium via python

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

# Wait is needed so the page has time to load
import time

# Disclaimer: All the functions below will use ID and XPATH for elements on webpages. These can be found inside the structure of
# any website. In chrome for example you can inspect an element with right click and then copy the ID or XPATH from there.


#Function 1: This function is used to select an object by ID. 
def interact_id(item_id):
    i = 1 # set a value to 1
    while i != 0: # while that value does NOT equal 0, run this try
    
        try:
            a = driver.find_element(By.ID,item_id) 
            # set the driver to find element by ID, if this works it will then set i = 0 and break the while loop
            i = 0
        except:
            time.sleep(2) 
            # if it doesn't work wait 2 seconds (page maybe loading) 
            i = i+2 # add 2 to value this will keep track of time ran. Print i to see time

    return(a)

#Function 2: This is the exact same function as before but with XPATH. These two functions could be merged into one if
# desired.
def interact_XPATH(item_XPATH):
    i = 1
    while i != 0:
    
        try:
            a = driver.find_element(By.XPATH,item_XPATH) 
            i = 0
        except:
            time.sleep(2)
            i = i+2

    return(a)

# The 2 functions only select the item which won't do anything. Once selected you then have to tell selenium to commit an action. The most common two actions are
# '.click()' and '.send_keys()'. This will allow you to either click an element or type something.


def interact_dropdown(item_ID):
    i = 1
    while i != 0:
    
        try:
            dropdown = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID, item_ID))) #dropdown for format type
            dropdown.click()
            select = Select(dropdown)
            select.select_by_visible_text('CSV (comma delimited)')
            dropdown.click()

            i = 0
        except:
            time.sleep(2)
            i = i+2

    return(dropdown)


driver = webdriver.Chrome() # Start server
driver.get('https://www.youtube.com/') # enter website

