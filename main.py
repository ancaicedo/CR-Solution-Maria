from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

SCROLL_PAUSE_TIME = 0.5
uuids = []
filenames = []


def get_filename(_id):
    driver.find_element(By.ID, _id).click()
    return driver.find_element(By.CLASS_NAME, 'detailList__fileButton')


def scroll():
    driver.find_element(By.CSS_SELECTOR, ".ReactVirtualized__Grid").click()
    driver.find_element(By.CSS_SELECTOR, ".ReactVirtualized__Grid").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)


def login():
    driver.find_element(By.ID, "email").click()
    driver.find_element(By.ID, "email").send_keys("mariam@tourismcalgary.com")
    driver.find_element(By.ID, "password").click()
    driver.find_element(By.ID, "password").send_keys("C0l0mb1a1493!")
    driver.find_element(By.CSS_SELECTOR, ".form__submitButton").click()


def find_elements():
    elements = driver.find_elements(By.CLASS_NAME, 'assetThumbnail__spacer')
    num = 0
    # need to find the number of elements there are!
    for i in range(len(elements)):
        # output.writelines(pic.get_attribute('id') + '\n')
        # filenames.append(get_filename(pic.get_attribute('id')))
        uuids.append(elements[i].get_attribute('id'))
        print(get_filename(elements[i].get_attribute('id')).text)
        if num == 25:
            scroll()
            num = 0
        num += 1
        elements += driver.find_elements(By.CLASS_NAME, 'assetThumbnail__spacer')


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://platform.crowdriff.com/')

login()
time.sleep(4)
driver.find_element(By.ID, "menu_icon").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) div:nth-child(2)").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "View Assets").click()
time.sleep(2)

# output = open('output.txt', 'w')

find_elements()

df = pd.DataFrame(uuids, columns=['Picture ID'])
dfn = pd.DataFrame(filenames, columns=['Picture ID'])
print(df)

df.to_excel(r'C:/Users/andca/Downloads/output.xlsx', index=False, header=True)

time.sleep(3)
# driver.quit()
