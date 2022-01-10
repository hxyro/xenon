from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("./drivers/chromedriver")

driver.get("https://www.youtube.com/")

search = driver.find_element_by_name("search_query")
search.send_keys("linux")
search.send_keys(Keys.RETURN)
