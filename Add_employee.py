from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")


add_button = driver.find_element(By.CSS_SELECTOR, 'button.oxd-button--medium.oxd-button--secondary')
add_button.click()


save_system_user_url = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser"
WebDriverWait(driver, 10).until(EC.url_to_be(save_system_user_url))


ess_dropdown = driver.find_element(By.CSS_SELECTOR, 'i.oxd-icon.bi-caret-down-fill.oxd-select-text--arrow')
ess_dropdown.click()
ess_option = driver.find_element(By.XPATH, '//li[contains(text(), "ESS")]')
ess_option.click()


name_input = driver.find_element(By.CSS_SELECTOR, 'input[data-v-75e744cd]')
name_input.send_keys("Goutam Ganesh")

status_dropdown = driver.find_element(By.CSS_SELECTOR, 'i.oxd-icon.bi-caret-down-fill.oxd-select-text--arrow')
status_dropdown.click()
status_option = driver.find_element(By.XPATH, '//li[contains(text(), "Enabled")]')
status_option.click()

username_input = driver.find_element(By.CSS_SELECTOR, 'input[data-v-1f99f73c]:nth-child(2)')
username_input.send_keys("Shovon")

password_input = driver.find_element(By.CSS_SELECTOR, 'input[data-v-1f99f73c]:nth-child(3)')
password_input.send_keys("Lagoslanded1")

confirm_password_input = driver.find_element(By.CSS_SELECTOR, 'input[data-v-1f99f73c]:nth-child(4)')
confirm_password_input.send_keys("Lagoslanded1")


save_button = driver.find_element(By.CSS_SELECTOR, 'button.orangehrm-left-space[data-v-10d463b7]')
save_button.click()


view_system_users_url = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"
WebDriverWait(driver, 10).until(EC.url_to_be(view_system_users_url))


driver.quit()
