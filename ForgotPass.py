from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://bugbug.io/")

login_button = driver.find_element(By.XPATH, '//span[text()="Login"]')
login_button.click()


driver.implicitly_wait(10) 


forgot_password_link = driver.find_element(By.XPATH, '//a[text()="Forgot password?"]')
forgot_password_link.click()

email_input = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
email_input.send_keys("shovon@gmail.com")


reset_password_button = driver.find_element(By.CSS_SELECTOR, 'div.sc-kdBSHD.iMxwCe.sc-hknOHE.ffpPwl')
reset_password_button.click()

driver.quit()
