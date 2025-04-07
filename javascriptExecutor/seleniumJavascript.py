import time

from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

driver.get("prompt('Enter your name'") # in prompt both text field and both ok and confirm button will come

driver.execute_script("alert('ArunMotoori')") #in alert only ok button will come

driver.execute_script("confirm('Are you sure')") # Both Ok and cancel button will come

time.sleep(3)

driver.quit()