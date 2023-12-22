from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://bugbug.io/")

login_button = driver.find_element(By.XPATH, '//span[text()="Login"]')
login_button.click()

email_input = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
password_input = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')

email_input.send_keys("shovon@gmail.com")
password_input.send_keys("@abc")

sign_in_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="Button"]')

ActionChains(driver).move_to_element(sign_in_button).click().perform()


driver.quit()
