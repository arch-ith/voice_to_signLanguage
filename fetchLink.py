from conf import DRIVER_DIR
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
# !Make sure you use same VERSION OF CHROME AND DRIVER
def getLink(word):
    print("recives word is"+word+"\n")
    PATH =DRIVER_DIR 
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(PATH,options=option)
    #link to get videoptions=option
    time.sleep(1)  
    driver.get('https://www.talkinghands.co.in/video/'+word)
    time.sleep(2) 
    try:  
        value_xpath=driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/a')
        link=value_xpath.get_attribute('src')
        print(link)
        return link
    except NoSuchElementException:
        print("Not found in talking hands") 
    
    driver.get("https://www.talkinghands.co.in/video/"+word+"mp4")
    try:
        value_xpath=driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div/div/div/video/source')
        link=value_xpath.get_attribute('src') 
        print(link)
        return link
    except NoSuchElementException:
        print("Not found in talking hands") 
    driver.get("https://indiansignlanguage.org/"+word+"/") 
    time.sleep(1)  
    try:
        value_xpath=driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[1]/main/article/div/div/div/iframe")
        link=value_xpath.get_attribute('src')
        print(link)
        return link 
    except NoSuchElementException:
        print("Not found in isl") 
    print("Link not found") 
    driver.close() 
    return "lnf" 
