#import's
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import json
import sys
####################################################################

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

    return True, "login successfully"

#print status
def print_status(is_ok,message):
    #print if 'ok'
    if is_ok :
        os.system("echo -en '\\e[32m'")
        print(message)
        os.system("echo -en '\\e[0m'")
    #print if 'error'
    else:
        os.system("echo -en '\\e[31m'")
        print(message)
        os.system("echo -en '\\e[0m'")

#get json config
def get_config():
    try:
        config = sys.argv[1]
        user_config = json.load(open(config, "r"))
        return user_config
    except IndexError as err:
        print_status(False, f"Error: No Config Foung! Exception: {err}")
        exit
    except FileNotFoundError as err:
        print_status(False, f"Error: No Config Foung! Exception: {err}")
        exit
