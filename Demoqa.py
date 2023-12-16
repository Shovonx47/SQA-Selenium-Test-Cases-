import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demoqa.com/")
driver.maximize_window()




try:
    # Click on the "Elements" button
    elements_button = driver.find_element(By.XPATH, "//div[@class='header-text']/span[contains(@class, 'pr-1')]")
    elements_button.click()

    # Click on "Check Box" from the dropdown menu
    checkbox_option = driver.find_element(By.XPATH, "//span[text()='Check Box']")
    checkbox_option.click()

    # Click on the square checkbox to select it
    checkbox = driver.find_element(By.XPATH, "//span[@class='rct-checkbox']//svg[contains(@class, 'rct-icon-uncheck')]")
    checkbox.click()

    # Click on "Text Box" from the left side
    text_box_option = driver.find_element(By.XPATH, "//span[text()='Text Box']")
    text_box_option.click()

    # Fill in the text fields
    full_name_input = driver.find_element(By.ID, "userName")
    email_input = driver.find_element(By.ID, "userEmail")
    current_address_textarea = driver.find_element(By.ID, "currentAddress")
    permanent_address_textarea = driver.find_element(By.ID, "permanentAddress")

    full_name_input.send_keys("Shovon Islam")
    email_input.send_keys("shovon06@gmail.com")
    current_address_textarea.send_keys("Badda")
    permanent_address_textarea.send_keys("Jashore")

    # Click on "Submit" button
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # Click on "Buttons" from the left side
    buttons_option = driver.find_element(By.XPATH, "//span[text()='Buttons']")
    buttons_option.click()

    # Click on "Click Me" button
    click_me_button = driver.find_element(By.ID, "doubleClickBtn")
    click_me_button.click()

    # Click on "Links" from the left side
    links_option = driver.find_element(By.XPATH, "//span[text()='Links']")
    links_option.click()

    # Click on "Not Found" link
    not_found_link = driver.find_element(By.ID, "invalid-url")
    not_found_link.click()

finally:
    # Close the browser window
    time.sleep(2)
    driver.quit()
