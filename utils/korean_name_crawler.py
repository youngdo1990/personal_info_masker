#################################################################################################### 
# AUTHOR: ALVARO ENRIQUE PERALTA GUTIERREZ (HWAN-HEE CHAE)                                         #
# PROJECT: KOREAN NAMES CRAWLER                                                                    #
####################################################################################################
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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


def mine_korean_names():
    # https://www.name-ranking.com/ranking#from=2008&to=2024&p=577
    
    driver = get_driver()
    driver.get('https://www.name-ranking.com/ranking#from=2008&to=2024&p=577')
    # 지연 시간을 지정한다.
    # Define delay time.
    time_sec = 10
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d} 후 크롤링을 시작하겠습니다.'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
    names = driver.find_elements(By.CLASS_NAME, "name")
    print("중복된 이름을 제거하고 있습니다.")
    file_name = "korean_names.txt"
    names = [n.get_attribute("innerHTML") for n in names if not n.get_attribute("innerHTML").startswith("<span")]
    print("파일을 저장하고 있습니다.")
    with open(file_name, "w", encoding="utf-8", errors="ignore") as file:            
        for name in tqdm(names):
            file.write(name + "\n")
    print("이름 " + str(len(names)) + "개를 저장했습니다.")
    driver.close()
    return


def mine_korean_lastnames():
    driver = get_driver()
    driver.get('https://ko.wikipedia.org/wiki/%ED%95%9C%EA%B5%AD%EC%9D%98_%EC%84%B1%EC%94%A8')
    last_names_table = driver.find_elements(By.TAG_NAME, "tbody")[1]
    rows = last_names_table.find_elements(By.TAG_NAME, "tr")
    rows = rows[:-2]
    last_name_list = []
    print("성씨를 찾고 중복된 성씨를 제거하고 있습니다.")
    for row in tqdm(rows):
        last_name = row.find_elements(By.TAG_NAME, "td")[0].get_attribute("innerText")
        last_name = last_name.split("(")[0]
        if last_name not in last_name_list:
            last_name_list.append(last_name)
    print("파일 저장하고 있습니다.")
    with open("korean_last_names.txt", "w", encoding="utf-8", errors="ignore") as file:
        for last_name in tqdm(last_name_list):
            file.write(last_name + "\n")
    print("성씨 " + str(len(last_name_list)) + "개 저장했습니다.")
    driver.close()
    return


if __name__ == "__main__":
    mine_korean_names()
    mine_korean_lastnames()