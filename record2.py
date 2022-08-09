from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import datetime as dt
import requests
import os
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv('token_bot')
CHAT_ID = os.getenv('chat_id')
CHAT_ID_LOG = os.getenv('chat_id_log')


def send_telegram(text: str):
    token = TELEGRAM_TOKEN
    url = "https://api.telegram.org/bot"
    channel_id = CHAT_ID
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })


def send_telegram_log(text: str):
    token = TELEGRAM_TOKEN
    url = "https://api.telegram.org/bot"
    channel_id_log = CHAT_ID_LOG
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
        "chat_id": channel_id_log,
        "text": text
    })


def foo():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.get('https://www.visametric.com/Kaliningrad/Germany/ru/p/zapis-na-podachu')
    driver.implicitly_wait(10)
    driver.find_element("xpath", '/html/body/div[7]/div/div/a').click()
    driver.implicitly_wait(10)
    driver.find_element("xpath", '/html/body/div[3]/div[2]/div/div/main/div/div/div/p[14]/a').click()
    driver.implicitly_wait(10)

    time.sleep(10)
    window_before = driver.window_handles[0]

    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    driver.find_element(By.ID, 'input-56').click()
    order1 = driver.find_element(By.ID, 'input-56')
    order1.send_keys("Калининград")
    order1.send_keys(Keys.ENTER)
    driver.implicitly_wait(10)
    time.sleep(2)
    driver.find_elements(By.CLASS_NAME, 'v-input--selection-controls__ripple')[0].click()
    driver.implicitly_wait(10)
    time.sleep(2)
    driver.find_elements(By.CLASS_NAME, 'v-input--selection-controls__ripple')[1].click()
    driver.implicitly_wait(10)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'primary.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default').click()
    driver.implicitly_wait(10)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'primary.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default').click()
    driver.implicitly_wait(10)
    time.sleep(2)
    order2 = driver.find_element(By.ID, 'input-175')
    order2.send_keys("Калининград")
    time.sleep(2)
    driver.find_element(By.ID, 'list-item-198-0').click()
    driver.implicitly_wait(10)
    time.sleep(2)
    driver.find_element("xpath", '//*[@id="app"]/div[1]/main/div/div/div/div/div/div[6]/div/span/div/div[1]/form/div/div[3]/div[2]/button[2]').click()
    driver.implicitly_wait(10)
    time.sleep(2)
    format_date = "%d%m%Y"

    for i in range(20, 160, 15):
        next_date = dt.date.today() + dt.timedelta(days=i)
        date = driver.find_element(By.ID, 'input-187')
        date.send_keys(next_date.strftime(format_date))
        time.sleep(5)
        info = driver.find_element(By.CLASS_NAME, 'v-alert__wrapper')
        if "Нет доступной даты" in info.text:
            print(f"{next_date} - {info.text}")
            send_telegram_log(f"{next_date} - {info.text}")
        else:
            print(f"{next_date} - {info.text}")
            message = f"На дату {next_date} -  {info.text}"
            send_telegram(message)
            driver.implicitly_wait(10)
        new_date = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "input-187")))
        new_date.click()
        driver.implicitly_wait(10)
        date.send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
        time.sleep(60)

    driver.quit()


def main():
    send_telegram(f"-----------Бот запустился {1} раз---------------")
    while True:
        for x in range(99999999):
            print(f"-----------Бот запустился {x+1} раз---------------")
            send_telegram_log(f"-----------Бот запустился {x+1} раз---------------")
            try:
                foo()
                time.sleep(1690)
            except:
                continue


if __name__ == '__main__':
    main()
