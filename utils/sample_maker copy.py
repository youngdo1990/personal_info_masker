#################################################################################################### 
# AUTHOR: ALVARO ENRIQUE PERALTA GUTIERREZ (HWAN-HEE CHAE)                                         #
# PROJECT: SAMPLE MAKER FOR PERSONAL INFO MASKER                                                   #
####################################################################################################
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from tqdm import tqdm


# https://chromedriver.chromium.org/downloads -> Chrome drivers


def get_driver(headless=True):
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    driver = webdriver.Chrome(
        options=options
    )
    return driver


def mine_gpt_samples():
    driver = get_driver(False)
    driver.get('https://auth.openai.com/authorize?client_id=TdJIcbe16WoTHtN95nyywh5E4yOo6ItG&scope=openid%20email%20profile%20offline_access%20model.request%20model.read%20organization.read%20organization.write&response_type=code&redirect_uri=https%3A%2F%2Fchatgpt.com%2Fapi%2Fauth%2Fcallback%2Flogin-web&audience=https%3A%2F%2Fapi.openai.com%2Fv1&device_id=a4cbf48b-a804-42fc-885f-529010d37947&prompt=login&state=6FlY8kFtl1YqpGGHDIj6uJJVyDSvAF-nG2ua98pmmdE&code_challenge=mIMmW3WRiutUBDc7XTDQ-RR6o2hOJtBwCYVmwTSq6rQ&code_challenge_method=S256')
    email_input = driver.find_element(By.XPATH, '//*[@id="email-input"]')
    email_input.send_keys('alvaroperalta2005@hotmail.com')
    email_input.send_keys(Keys.ENTER)
    pass_input = driver.find_element(By.XPATH, '//*[@id="password"]')
    time.sleep(5)
    pass_input.send_keys('Hayoung$2490')
    submit_button = driver.find_element(By.XPATH, '/html/body/div[1]/main/section/div/div/div/form/div[2]/button')
    time.sleep(5)
    submit_button.click()
    # login_button.click()
    # 지연 시간을 지정한다.
    # Define delay time.
    time_sec = 10
    time.sleep(time_sec)
    driver.close()
    return


if __name__ == "__main__":
    mine_gpt_samples()