from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users//DEV/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element_by_name("fName")
fname.click()
fname.send_keys("P")

lname = driver.find_element_by_name("lName")
lname.click()
lname.send_keys("K")

email = driver.find_element_by_name("email")
email.click()
email.send_keys("senf@senf.de")

signup = driver.find_element_by_xpath('/html/body/form/button')
signup.click()

# driver.quit()
