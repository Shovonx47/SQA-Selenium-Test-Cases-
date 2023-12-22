import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.avijatrik.org/")


adventure_button = driver.find_element(By.XPATH, "//span[@class='opacity-0 group-hover:opacity-100 absolute inset-0 bg-black bg-opacity-10 transition-opacity']")
driver.execute_script("arguments[0].scrollIntoView();", adventure_button)
adventure_button.click()

sreemangal_button = driver.find_element(By.XPATH, "//span[@class='line-clamp-2 text-base' and contains(text(),'A Tour in the Wildlife: Lawachora Reserve Forest')]")
sreemangal_button.click()

time.sleep(3)

driver.switch_to.window(driver.window_handles[1])

check_availability_button = driver.find_element(By.XPATH, "//button[contains(@class, 'nc-Button') and contains(@class, 'focus:ring-primary-6000')]/a[text()='Check Availability']")
check_availability_button.click()

time.sleep(3)

driver.quit()
