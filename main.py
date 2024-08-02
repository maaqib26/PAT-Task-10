from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class guvi_instagram:

    # Locators Data

    followers_locator = '//li[2]//div//button//span[@class="html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs"]'
    following_locator = '//li[3]//div//button//span[@class="html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs"]'


    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start_automation(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(5)
            return True
        except:
            print("ERROR: Not able to start python automation")
            return False

    def fetch_followers(self):
        followers_count = self.driver.find_element(by=By.XPATH,value=self.followers_locator).text
        print("Total Number of Followers are,",followers_count)
    
    def fetch_following(self):
        following_count = self.driver.find_element(by=By.XPATH,value=self.following_locator).text
        print("Total Number of Following are,",following_count)
 
    def shutdown(self):
        self.driver.close()

if __name__ == "__main__":
    url = "https://www.instagram.com/guviofficial/"
    guvi = guvi_instagram(url)
    guvi.start_automation()
    guvi.fetch_followers()
    guvi.fetch_following()
    guvi.shutdown()
