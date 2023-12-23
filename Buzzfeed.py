from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to the system users page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")

    # Click on the "Buzz" option
    buzz_option = driver.find_element(By.XPATH, '//span[text()="Buzz"]')
    buzz_option.click()

    # Wait for the Buzz page to load
    WebDriverWait(driver, 10).until(EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz"))

    # Find the textarea and write the specified text
    buzz_textarea = driver.find_element(By.CSS_SELECTOR, 'textarea.oxd-buzz-post-input')
    buzz_textarea.send_keys("As we navigate the dynamic landscape of business, our commitment to sustainable development remains unwavering. We strive to create value not only for our stakeholders but also for the communities we serve. Our vision extends beyond profit margins; it encompasses a future where responsible business practices contribute to the betterment of society.")

    # Click on the "Post" button
    post_button = driver.find_element(By.CSS_SELECTOR, 'button.oxd-button--main')
    post_button.click()

    # Wait for the post to be submitted
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.buzz-post-body')))

finally:
    # Close the browser window
    driver.quit()
