from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.actionchains import ActionChains

# Open Chrome browser and maximize window
driver = webdriver.Chrome()
driver.maximize_window()

# Go to DemoQA website
driver.get("https://demoqa.com/")

# Click on "Interactions" button
interactions_button = driver.find_element_by_css_selector(".card-body h5")[0]
interactions_button.click()

# Click on "Droppable" button from the left menu
droppable_option = driver.find_element_by_css_selector("#item-5")
droppable_option.click()

# Wait for droppable window to appear
droppable_window = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#droppableContainer")))

# Find drag element and drop element
drag_element = driver.find_element_by_id("draggable")
drop_element = driver.find_element_by_id("droppable")

# Create an ActionChains object
action = ActionChains(driver)

# Perform drag-and-drop action
action.drag_and_drop(drag_element, drop_element).perform()

# (Optional) Add code to interact with the dropped element or check for successful drop

# Quit the browser
driver.quit()
