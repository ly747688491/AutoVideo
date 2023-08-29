import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class GetCookie:
    def __init__(self, login_url, home_url, name_xpath, avatar_xpath, cookie_file='cookie.txt', image_file='baidu.png'):
        self.login_url = login_url
        self.home_url = home_url
        self.name_xpath = name_xpath
        self.avatar_xpath = avatar_xpath
        self.cookie_file = cookie_file
        self.image_file = image_file
        self.chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path="resources/chromedriver/chromedriver.exe",
                                       options=self.chrome_options)

    def get_cookies(self, url):
        try:
            self.driver.get(url)
            WebDriverWait(self.driver, 10).until(EC.url_to_be(self.home_url))
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.avatar_xpath)))
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.name_xpath)))
            cookies = self.driver.get_cookies()
            return cookies
        except Exception as e:
            print(f'Error getting cookies: {e}')
            return None

    def save_cookies(self, cookies):
        if cookies is not None:
            with open(self.cookie_file, 'a', encoding='utf-8') as file:
                file.write(json.dumps(cookies))
                print("save cookie")

    def run(self):
        cookies = self.get_cookies(self.login_url)
        self.save_cookies(cookies)
