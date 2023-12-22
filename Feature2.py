from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # Maximize the browser window
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList")


approve_button = driver.find_element(By.CSS_SELECTOR, 'button.oxd-button--medium.oxd-button--label-success')
approve_button.click()


WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'button.oxd-button--medium.oxd-button--label-success')))


leave_status = driver.find_element(By.XPATH, '//td[text()="Approved"]')
assert leave_status is not None, "Leave approval failed"

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")

delete_button = driver.find_element(By.CSS_SELECTOR, 'i.oxd-icon.bi-trash')
delete_button.click()


try:
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
except:
    pass  


no_records_msg = driver.find_element(By.XPATH, '//div[@class="message warning fadable"]')
assert "No Records Found" in no_records_msg.text, "Delete action failed"


driver.quit()
