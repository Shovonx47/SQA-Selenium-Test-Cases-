import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demoqa.com/")
driver.maximize_window()




try:
    
    elements_button = driver.find_element(By.XPATH, "//div[@class='header-text']/span[contains(@class, 'pr-1')]")
    elements_button.click()


    checkbox_option = driver.find_element(By.XPATH, "//span[text()='Check Box']")
    checkbox_option.click()


    checkbox = driver.find_element(By.XPATH, "//span[@class='rct-checkbox']//svg[contains(@class, 'rct-icon-uncheck')]")
    checkbox.click()


    text_box_option = driver.find_element(By.XPATH, "//span[text()='Text Box']")
    text_box_option.click()


    full_name_input = driver.find_element(By.ID, "userName")
    email_input = driver.find_element(By.ID, "userEmail")
    current_address_textarea = driver.find_element(By.ID, "currentAddress")
    permanent_address_textarea = driver.find_element(By.ID, "permanentAddress")

    full_name_input.send_keys("Shovon Islam")
    email_input.send_keys("shovon06@gmail.com")
    current_address_textarea.send_keys("Badda")
    permanent_address_textarea.send_keys("Jashore")


    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()


    buttons_option = driver.find_element(By.XPATH, "//span[text()='Buttons']")
    buttons_option.click()

    click_me_button = driver.find_element(By.ID, "doubleClickBtn")
    click_me_button.click()

    links_option = driver.find_element(By.XPATH, "//span[text()='Links']")
    links_option.click()

    not_found_link = driver.find_element(By.ID, "invalid-url")
    not_found_link.click()

finally:
    time.sleep(2)
    driver.quit()
