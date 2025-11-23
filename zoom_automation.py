import json
import time
import schedule

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def join_meeting_on_web(email="melih.berk@std.izmirekonomi.edu.tr", name="MELİH BERK SÖNMEZ 20250602221"):
    url = "https://ieu-edu-tr.zoom.us/wc/join/81846785900?pwd=3JimrVZsUzbTzjabCZ9UegqaZpkmtr.1"

    service = Service("C:/Users/mhbso/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe")

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)

    # wait until email input is visible (up to 10 seconds)
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-for-email"))
    )
    email_input.send_keys(email)

    name_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "input-for-name"))
    )
    name_input.send_keys(name)
    name_input.send_keys(Keys.ENTER)

def get_profile_datas():
    path = "C:/Users/mhbso/OneDrive/Masaüstü/zoom_automation_data.json"

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def join_meeting_for_every_profile():
    data = get_profile_datas()
    print(data)
    for person in data:
        name = person["name"]
        email = person["email"]

        join_meeting_on_web(name=name, email=email)


#schedule task
schedule.every().monday.at("17:35").do(join_meeting_for_every_profile)


#running schedule tasks every 5 seconds so it will check if we reached the goal time
while True:
    schedule.run_pending()
    time.sleep(5)
