#import's
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import json
import sys
####################################################################

global opt,driver,wait

#set default options
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument("--start-maximized")
opt.add_experimental_option("prefs", 
   {"profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2, 
    "profile.default_content_setting_values.notifications": 2 
    })

#start webdriver
driver = webdriver.Chrome(options=opt,service_log_path='NUL')

#explicit waits
wait = WebDriverWait(driver, 10)
wait_2 = WebDriverWait(driver, 2)

#Login
def login(url, email, passwd):
    driver.get(url)

    next_button_id = (By.ID, "idSIButton9")
    #enter email and check its validity
    try:
        wait.until(EC.element_to_be_clickable((By.ID, "i0116"))).send_keys(email)
        wait.until(EC.element_to_be_clickable(next_button_id)).click()
    except Exception as exc:
        return False, f"Login Error!! Exception: {exc}"
    try:
        wait_2.until(EC.visibility_of_element_located((By.ID, "usernameError")))
    except:pass
    else:
        return False, "Invalid Email"
    #enter passwd and check its validity
    try:
        wait.until(EC.element_to_be_clickable((By.ID, "i0118"))).send_keys(passwd)
        wait.until(EC.element_to_be_clickable(next_button_id)).click()
    except Exception as exc:
        return False, f"Login Error!! Exception: {exc}"
    try:
        wait_2.until(EC.visibility_of_element_located((By.ID, "passwordError")))
    except:pass
    else:
        return False, "Invalid Password"
    #stay sign-in shit(click next)
    try:
        wait.until(EC.element_to_be_clickable(next_button_id)).click()
    except Exception as exc:
        return False, f"Login Error!! Exception: {exc}"

    return True, "login successfully"

#join meet with url
def join_meet(url):
    driver.get(url)
    #wait for "open in browser" shit to be clickable
    try:wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "text"))).click()
    except Exception as exc:
        return False, f"Error!! Exception: {exc}"
    #mute microphone
    try:wait.until(EC.element_to_be_clickable((By.ID, "preJoinAudioButton"))).click()
    except Exception as exc:
        return False, f"Error!! Exception: {exc}"
    #join meet
    try:wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button-col"))).click()
    except Exception as exc:
        return False, f"Error!! Exception: {exc}"
    return True, "huehuehue"
    

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
def parse_config():
    try:
        config = sys.argv[1]
        user_config = json.load(open(config, "r"))
        return user_config
    except IndexError as err:
        print_status(False, f"Error: No Config Foung! Exception: {err}")
        return None
    except FileNotFoundError as err:
        print_status(False, f"Error: No Config Foung! Exception: {err}")
        return None
