#imports
#class
#constructor with three params because we have self and two fixtures

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import config
import time

class LoginPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.username_locator = (By.ID, 'username')
        self.password_locator = (By.ID, 'password')
        self.submit_locator = (By.XPATH, '//button[@type="submit"]')

    def enter_username(self):
        username_field = self.wait.until(EC.presence_of_element_located(self.username_locator))
        username_field.send_keys(config.USER_NAME)

    def enter_password(self):
        password_field = self.wait.until(EC.presence_of_element_located(self.password_locator))
        password_field.send_keys(config.PASSWORD)

    def submit(self):
        submit_field = self.wait.until(EC.presence_of_element_located(self.submit_locator))
        submit_field.click()