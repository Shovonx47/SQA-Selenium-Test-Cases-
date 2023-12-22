from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://www.softwaretestingo.com/")


search_icon = driver.find_element(By.XPATH, '//svg[@viewBox="0 0 512 512"]')
search_icon.click()


search_field = driver.find_element(By.CLASS_NAME, 'search-field')
search_field.send_keys("Jmeter Testing")
search_field.send_keys(Keys.RETURN)

time.sleep(2)


search_results_link = driver.find_element(By.XPATH, '//svg[@viewBox="0 0 512 512"]/ancestor::a')
search_results_link.click()


time.sleep(2)


print(driver.current_url)


driver.quit()
