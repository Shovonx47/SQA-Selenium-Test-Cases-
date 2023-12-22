from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.actionchains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com/")

widgets_button = driver.find_element_by_css_selector(".header-text svg")
widgets_button.click()

dropdown_menu = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#widgets-menu")))

slider_option = driver.find_element_by_css_selector("#item-11")
slider_option.click()

slider_handle = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#range")))

action = ActionChains(driver)
action.drag_and_drop_to_offset(slider_handle, 50, 0).perform()

progress_bar_option = driver.find_element_by_css_selector("#item-12")
progress_bar_option.click()

progress_bar_window = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#progressbar-demo")))

start_button = driver.find_element_by_id("startStopButton")
start_button.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".progress-bar-value[style*='width: 100%']")))

menu_option = driver.find_element_by_css_selector("#item-8")
menu_option.click()

menu_window = driver.find_element_by_css_selector(".main-content")
main_item_1 = menu_window.find_element_by_css_selector(".menu-item-content:nth-child(1)")
main_item_2 = menu_window.find_element_by_css_selector(".menu-item-content:nth-child(2)")
main_item_3 = menu_window.find_element_by_css_selector(".menu-item-content:nth-child(3)")

action.move_to_element(main_item_1).perform()
action.move_to_element(main_item_2).perform()
action.move_to_element(main_item_3).perform()

driver.quit()
