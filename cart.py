from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://www.amazon.com/Casio-MTP4500D-1AV-Slide-Aviator-Stainless/dp/B00134OJYA/ref=sr_1_23?crid=E5WMR294G4GX&keywords=watch&qid=1703257437&sprefix=watch%2Caps%2C502&sr=8-23")


add_to_cart_button = driver.find_element(By.ID, 'add-to-cart-button')
add_to_cart_button.click()


cart_page_url = "https://www.amazon.com/cart/smart-wagon?newItems=3ca19cb9-0834-4f40-9e61-84991952b77d,1&ref_=sw_refresh"
if cart_page_url in driver.current_url:
    
    go_to_cart_button = driver.find_element(By.CSS_SELECTOR, 'a[href="/cart?ref_=sw_gtc"]')
    go_to_cart_button.click()


driver.quit()
