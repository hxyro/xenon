from libxenon import *

#start webdriver
driver = webdriver.Chrome()

ehh = get_config()
if ehh == None:
    exit
else:
    a,b = login(driver, ehh['url'], ehh['email'] ,ehh['password'])
    print_status(a,b)
