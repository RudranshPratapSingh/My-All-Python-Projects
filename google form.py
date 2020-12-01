import time
from selenium import webdriver


name = ["Akshansh", "Pratap", "Singh"]
admno = ["2312"]

input_name = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
input_admno = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'

input_class = '//*[@id="i9"]/div[3]/div'

submit = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span'
         


def sleep():
    time.sleep(11)


browser = webdriver.Chrome()


browser.get("https://docs.google.com/forms/d/e/1FAIpQLSejXLbObszWmSbGwxJ8PzvOuUTdeJ-zCWNLjprAAckTO3YiOw/viewform?usp=sf_link")

i = 0

while i < len(name):
    browser.find_element_by_xpath(input_name).send_keys(name[i])
    browser.find_element_by_xpath(input_admno).send_keys(admno[i])
    browser.find_element_by_xpath(input_class).click()
    sleep()
    browser.find_element_by_xpath(submit).click()



