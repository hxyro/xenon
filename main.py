from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os

#start webdriver
driver = webdriver.Chrome()
#open link
driver.get("https://www.microsoft.com/en-us/microsoft-teams/log-in")
wait = WebDriverWait(driver, 10)

#hardcoded email & passwd
email_str = "myemail"
passwd_str = "mypasswd"


try: #wait for popup to load 
    wait.until(EC.element_to_be_clickable((By.ID, 'dynamicmarketredirect-dialog-inner')))
finally: #accept popup
    driver.find_element(By.ID, "dynamicmarketredirect-dialog-close").send_keys(Keys.ENTER)
#find sign-in element
driver.find_element(By.ID, "mectrl_main_trigger").send_keys(Keys.ENTER)



try: #wait for email field and enter email
    wait.until(EC.element_to_be_clickable((By.ID, "i0116"))).send_keys(email_str + Keys.ENTER)

finally: #wait for password field and enter password
        wait.until(EC.element_to_be_clickable((By.ID, "i0118"))).send_keys(passwd_str + Keys.ENTER)
        try:
            wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9"))).click()
        finally:
            os.system("kitty +kitten icat ww.jpeg")
