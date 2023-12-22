from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()


driver.get("https://bugbug.io/")


login_button = driver.find_element(By.XPATH, '//span[text()="Login"]')
login_button.click()


email_input = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
password_input = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')

email_input.send_keys("mshovon201218@bscse.uiu.ac.bd")
password_input.send_keys("@6$weYB@ikBDceT")

sign_in_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="Button"]')
sign_in_button.click()


driver.quit()
