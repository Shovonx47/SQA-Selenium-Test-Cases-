from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://support.orangehrm.com/portal/en/signin")


username_input = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
password_input = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')

username_input.send_keys("mshovon201218@bscse.uiu.ac.bd")
password_input.send_keys("lagoslanded")


sign_in_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
sign_in_button.click()


driver.quit()
