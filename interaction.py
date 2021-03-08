from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users//DEV/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

arts = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')

search = driver.find_element_by_name("search")
search.click()
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# driver.quit()
