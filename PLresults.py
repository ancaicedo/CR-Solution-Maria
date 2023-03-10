from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome("C:/Users/andca/Downloads/chromedriver_win32/chromedriver.exe")
driver.get('https://www.skysports.com/premier-league-results/1992-93')

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'plus-more__text')))

if driver.find_element(By.CLASS_NAME,'plus-more__text'):
    print('Found')
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.CLASS_NAME, 'plus-more__text'))
    driver.execute_script("arguments[0].click();", driver.find_element(By.CLASS_NAME, 'plus-more__text'))

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

links = soup.findAll('div', class_='fixres__item')

print(len(links))

driver.quit()