from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


username_input = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
password_input = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')

username_input.send_keys("Admin")
password_input.send_keys("admin123")


login_button = driver.find_element(By.CSS_SELECTOR, 'button.orangehrm-login-button')
login_button.click()


dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
WebDriverWait(driver, 10).until(EC.url_to_be(dashboard_url))


user_dropdown_icon = driver.find_element(By.CSS_SELECTOR, 'i.oxd-icon.bi-caret-down-fill')
user_dropdown_icon.click()


logout_link = driver.find_element(By.CSS_SELECTOR, 'a.oxd-userdropdown-link[href="/web/index.php/auth/logout"]')
logout_link.click()


login_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
WebDriverWait(driver, 10).until(EC.url_to_be(login_url))


driver.quit()
