from conf import DRIVER_DIR
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
# !Make sure you use same VERSION OF CHROME AND DRIVER
def getLink(word):
    PATH =DRIVER_DIR
    driver =webdriver.Chrome(PATH)
    #link to get video
    time.sleep(1)
    driver.get("https://indiansignlanguage.org/search-dictionary/")
    time.sleep(1)
    driver.find_element_by_css_selector("a[href*="+word+"]").click() 
    time.sleep(1)
    value_xpath=driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[1]/main/article/div/div/div/iframe")
    link=value_xpath.get_attribute('src')
    print(link) 
    return link 