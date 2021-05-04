from conf import DRIVER_DIR
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
# !Make sure you use same VERSION OF CHROME AND DRIVER
def getLink(word):
    PATH =DRIVER_DIR 
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(PATH,options=option)
    #link to get video
    time.sleep(1)  
    driver.get('https://www.talkinghands.co.in/video/'+word)
    time.sleep(2) 
    try:  
        value_xpath=driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div/div/div/div[13]/div[2]/div/div/div/iframe')
        link=value_xpath.get_attribute('src')
        print(link)
        return link
    except NoSuchElementException:
        print("Element not found") 
    
    driver.get("https://www.talkinghands.co.in/video/"+word+"mp4")
    try:
        value_xpath=driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div/div/div/video/source')
        link=value_xpath.get_attribute('src') 
        print(link)
        return link
    except NoSuchElementException:
        print("Element not found") 
    driver.get("https://indiansignlanguage.org/search-dictionary/") 
    time.sleep(1)
    driver.find_element_by_css_selector("a[href*="+word+"]").click() 
    try:
        value_xpath=driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[1]/main/article/div/div/div/iframe")
        link=value_xpath.get_attribute('src')
        print(link)
        return link 
    except NoSuchElementException:
        print("Element not found")
    driver.quit()  