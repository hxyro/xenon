#from os import times
from libxenon import*
#import time

global user, email, password, role_id, channel_id, discord_token, time_delay

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

def main():
    config = parse_config()
    
    if config == None:
        return 1    
    else:
        user = config['user']
        email = config['email']
        password = config['password']
        mention_role_id = config['mention_role_id']
        channel_id = config['channel_id']
        discord_token = config['discord_token']
        time_delay = config['time_delay']
    
    
    print(f"user: {user}")
    while True:
        block = get_messages(channel_id, mention_role_id, discord_token)
        timestamp = block['timestamp']
        is_ok , time_diff = is_time(timestamp)
        if is_ok:
            time.sleep(0.2)
            print_status(True, f"recent message:\n{block['footer']['text']}\t   tag: @IT branch")
            print_status(True, f"\nurl: {block['url']}")
            time.sleep(0.2)
            print(f"\ntime difference: {time_diff}min")

            driver = webdriver.Chrome(options=opt,service_log_path='NUL')
            url = filter(driver, block['url'])
            driver = webdriver.Chrome(options=opt,service_log_path='NUL')
            
            is_login, text = login(driver,email,password)
            print_status(is_login, text)
            
            if is_login:
                
                time.sleep(0.2)
                is_join, text = join_meet(driver, url)
                print_status(is_join, text)
                
                if is_join:
                    time.sleep(0.3)
                    os.system("notify-send 'Joined Successfully'")
                    print(f"sleeping for {time_diff} min")
                    sleeping_time = time_diff * 60
                    time.sleep(sleeping_time)
                    try: driver.quit()
                    except: pass
                    os.system("notify-send 'ehhhhhhh'")
                else:
                    break
            else:
                break
        print("waiting for link")
        time.sleep(time_delay)


if __name__ == "__main__":
    main()
