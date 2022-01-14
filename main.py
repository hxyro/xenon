#hard-coded email-password
email = "myemail"
passwd = "mypasswd"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os

#login_url
url = "https://go.microsoft.com/fwlink/p/?LinkID=873020&clcid=0x409&culture=en-us&country=US&lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn"
#start webdriver
driver = webdriver.Chrome()

#Login
def login(driver, url, email, passwd):
    wait = WebDriverWait(driver, 10)
    driver.get(url)

    next_button_id = (By.ID, "idSIButton9")
    #enter email and check its validity
    try:
        wait.until(EC.element_to_be_clickable((By.ID, "i0116"))).send_keys(email)
        wait.until(EC.element_to_be_clickable(next_button_id)).click()
    except Exception:
        return False, "Login Error"
    try:
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, "usernameError")))
    except:pass
    else:
        return False, "Invalid Email"
    #enter passwd and check its validity
    try:
        wait.until(EC.element_to_be_clickable((By.ID, "i0118"))).send_keys(passwd)
        wait.until(EC.element_to_be_clickable(next_button_id)).click()
    except Exception:
        return False, "Login Error"
    try:
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, "passwordError")))
    except:pass
    else:
        return False, "Invalid Password"
    #stay sign-in shit(click next)
    try:
        wait.until(EC.element_to_be_clickable(next_button_id)).click()
    except Exception:
        return False, "Login Error"

    return True, "huehue"


any_error,message = login(driver, url, email ,passwd)

if any_error :
    os.system("echo -en '\\e[32mlogin successfully\\n\\e[0m'")
else:
    os.system("echo -en '\\e[31m'")
    print(message)
    os.system("echo -en '\\e[0m'")
    driver.quit()
