from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
# !Make sure you use same VERSION OF CHROME AND DRIVER
def getLink(word):
    word="accept"
    PATH ="D:\chromedriver.exe"
    driver =webdriver.Chrome(PATH)
    #link to get video
    time.sleep(2)
    driver.get("https://indiansignlanguage.org/search-dictionary/")
    time.sleep(2)
    value_xpath=driver.find_element_by_css_selector("a[href*="+word+"]")
    # to go to that link ->>driver.find_element_by_css_selector("a[href*="+word+"]").click()
    link=value_xpath.get_attribute('href')
    print(link)
    value=value_xpath.get_attribute('innerHTML')
    print(value.strip())
    return link