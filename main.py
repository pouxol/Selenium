from selenium import webdriver

chrome_driver_path = "C:/Users//DEV/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

events = driver.find_elements_by_xpath('//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[*]/a')
dates = driver.find_elements_by_xpath('//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[*]/time')

upcoming_events = {}
for i in range(len(events)):
    upcoming_events[i] = {
        "time": dates[i].text,
        "name": events[i].text
    }


print(upcoming_events)

# Find
# Find element by name, class name, id, css selector

# Close closes active tab
# driver.close()

# Quit closes everything
driver.quit()
