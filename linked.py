from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/")
time.sleep(3)

email=driver.find_element(By.ID,"session_key")
password = driver.find_element(By.ID,"session_password")
submit = driver.find_element(By.XPATH,"/html[1]/body[1]/main[1]/section[1]/div[1]/div[1]/form[1]/div[2]/button[1]")
email.send_keys("")
password.send_keys("")
submit.click()
time.sleep(10)
search=driver.find_element(By.XPATH,"//input[@placeholder='Search']")
search.send_keys("real estate",Keys.ENTER)
time.sleep(3)
people=driver.find_element(By.XPATH,"//button[text()='People']")
time.sleep(3)
people.click()
time.sleep(5)
for x in range(5):
 connect=driver.find_element(By.XPATH,"//span[text()='Connect']")
#connect=driver.find_element(By.XPATH,"/html[1]/body[1]/div[4]/div[3]/div[2]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[x]/div[1]/div[1]/div[3]/div[1]/button[1]/span[1]")
 time.sleep(3)
 connect.click() 
 time.sleep(3)
 driver.execute_script("document.activeElement")
 time.sleep(3)
 send=driver.find_element(By.XPATH,"//button[@aria-label='Send now']")
 time.sleep(3)
 send.click()
 time.sleep(3)
 
driver.execute_script("document.activeElement")

driver.quit()
print("Automation Complete") 






