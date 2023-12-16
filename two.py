import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

# Launch the browser and navigate to the W3Schools signup page
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.w3schools.com/signup/index.php")

# Click the "Sign Up For Free" button
sign_up_button = driver.find_element_by_id("signUpFromSignup")
sign_up_button.click()

# Fill in the email and password fields
email_field = driver.find_element_by_id("modalusername")
password_field = driver.find_element_by_id("new-password")

email_field.send_keys("saifulislamshovon056@gmail.com")
password_field.send_keys("12102000aB#")

# Fill in the first and last name fields
first_name_field = driver.find_element_by_id("modal_first_name")
last_name_field = driver.find_element_by_id("modal_last_name")

first_name_field.send_keys("Shovon")
last_name_field.send_keys("Islam")

# Wait for a few seconds (you may adjust the time as needed)
time.sleep(3)

# Close the browser
driver.quit()
