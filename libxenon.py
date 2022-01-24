#import's
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import datetime
import requests
import os
import json
import sys
import time
####################################################################

global opt,driver


#set default options

#Login
def login(driver,email, passwd):
    url = "https://go.microsoft.com/fwlink/p/?LinkID=873020&clcid=0x409&culture=en-us&country=US&lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn"
    wait = WebDriverWait(driver, 10)
    wait_2 = WebDriverWait(driver, 2)
    next_button_id = (By.ID, "idSIButton9")
    
    driver.get(url)

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
def join_meet(driver, url):
    wait = WebDriverWait(driver, 10)
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

def is_time(timestamp):
    day = timestamp.split('T')[0].split('-')
    day = datetime.date(int(day[0]),int(day[1]),int(day[2]))
    if datetime.date.today() == day:
        block_time = timestamp.split('T')[1].split('.')[0]
        current_time_m = datetime.datetime.now().hour * 60 + datetime.datetime.now().minute
        block_time_m = int(block_time.split(':')[0])*60 + int(block_time.split(':')[1]) + 330
        time_diff = current_time_m - block_time_m
        if time_diff < 45 and time_diff > 0:
            
            if current_time_m >= 540 and current_time_m <= 600:
                return True, 610 - current_time_m
            if current_time_m >= 615 and current_time_m <= 675:
                return True, 685 - current_time_m
            if current_time_m >= 690 and current_time_m <= 750:
                return True, 760 - current_time_m
            if current_time_m >= 810 and current_time_m <= 870:
                return True, 880 - current_time_m
            if current_time_m >= 885:
                return True, 1020 - current_time_m

            return True, 60 - (current_time_m - block_time_m)
        return False, 0
    return False, 0

def filter(driver, url):
    driver.get(url)
    url = driver.current_url
    driver.quit()
    time.sleep(1)
    return url

#retrieve  messages from discord
def get_messages(channel_id, mention_role_id, token):
    filter_list = []
    r = requests.get(
            f'https://discord.com/api/v9/channels/{channel_id}/messages?limit=12',
            headers={'authorization': token}
            )
    message_list = json.loads(r.text)
    for v in message_list:
        if v['author']['username'] == "IIITB DASH" and mention_role_id in v['mention_roles']:
            filter_list.append(v['embeds'][0])
    return filter_list[0]
