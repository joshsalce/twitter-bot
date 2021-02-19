from selenium import webdriver
import requests
from selenium.webdriver.common.keys import Keys
import datetime as dt
import time

USERNAME = "USERNAME"
PASSWORD = "PASSWORD"
chrome_driver_path = "/Applications/chromedriver"
TWEET_DRAFT = input("What would you like to tweet out today?: ")

class TwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.up = 0
        self.down = 0

    def tweet(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(3)

        username = self.driver.find_element_by_name("session[username_or_email]")
        password = self.driver.find_element_by_name("session[password]")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        sign_in = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
        sign_in.click()

        time.sleep(3)

        tweet_compose = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = TWEET_DRAFT
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()

bot = TwitterBot(chrome_driver_path)
bot.tweet()


