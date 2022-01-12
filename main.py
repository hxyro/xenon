from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.microsoft.com/en-us/microsoft-teams/log-in")
wait = WebDriverWait(driver, 10)

email_str = "myemail"
passwd_str = "mypasswd"

try:wait.until(EC.element_to_be_clickable((By.ID, 'dynamicmarketredirect-dialog-inner')))
finally:driver.find_element(By.ID, "dynamicmarketredirect-dialog-close").send_keys(Keys.ENTER)
driver.find_element(By.ID, "mectrl_main_trigger").send_keys(Keys.ENTER)

try:
    wait.until(EC.element_to_be_clickable((By.ID, "i0116")))
finally:
    driver.find_element(By.ID, "i0116").send_keys(email_str + Keys.ENTER)
    try: wait.until(EC.element_to_be_clickable((By.ID, "i0118")))                                                          
    finally: driver.find_element(By.ID, "i0118").send_keys(passwd_str + Keys.ENTER)
time.sleep(0)
