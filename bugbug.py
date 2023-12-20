from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()


driver.get("https://bugbug.io/")


signup_button = driver.find_element(By.XPATH, '//span[text()="Sign up for free"]')
signup_button.click()


email_input = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
password1_input = driver.find_element(By.CSS_SELECTOR, 'input[name="password1"]')
password2_input = driver.find_element(By.CSS_SELECTOR, 'input[name="password2"]')

email_input.send_keys("mshovon201218@bscse.uiu.ac.bd")
password1_input.send_keys("@6$weYB@ikBDceT")
password2_input.send_keys("@6$weYB@ikBDceT")


create_account_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="Button"]')
create_account_button.click()

driver.quit()
