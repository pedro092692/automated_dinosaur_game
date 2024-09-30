from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Browser:

    def __init__(self):
        self.url = 'chrome://dino/'
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.options.add_argument('--disable-web-security')
        self.options.add_argument('--allow-running-insecure-content')
        self.driver = webdriver.Chrome(options=self.options)
        try:
            self.driver.get(self.url)
        except WebDriverException:
            pass

    def start_game(self):
        # start game
        time.sleep(2)
        html = self.driver.find_element(By.TAG_NAME, value='html')
        html.send_keys(Keys.SPACE)


