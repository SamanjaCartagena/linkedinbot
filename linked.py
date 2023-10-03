from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/")
time.sleep(3)
driver.maximize_window()


email=driver.find_element(By.ID,"session_key")
password = driver.find_element(By.ID,"session_password")
submit = driver.find_element(By.XPATH,"/html[1]/body[1]/main[1]/section[1]/div[1]/div[1]/form[1]/div[2]/button[1]")
email.send_keys("cart.samanja09@gmail.com")
password.send_keys("Sam#Carta32")
submit.click()
time.sleep(20)
search=driver.find_element(By.XPATH,"//input[@placeholder='Search']")
search.send_keys("software engineer",Keys.ENTER)
time.sleep(3)

people=driver.find_element(By.XPATH,"//button[text()='People']")
time.sleep(3)
people.click()
time.sleep(5)


all_buttons= driver.find_elements(By.TAG_NAME,"button")
connect_buttons=[btn for btn in all_buttons if btn.text == "Connect"]

if connect_buttons:
   for btn in connect_buttons:
    btn.click()
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(3)
    send=driver.find_element(By.XPATH,"//button[@aria-label='Send now']")
    time.sleep(3)
    send.click()
    time.sleep(3)
    driver.execute_script("document.activeElement")
   driver.execute_script("window.scrollBy(0,1000)","")
   time.sleep(10)
   next = driver.find_element(By.XPATH,"//button[@aria-label='Next']").click()
   time.sleep(5)
else:
  driver.execute_script("window.scrollBy(0,1000)","")
  time.sleep(5)
  next = driver.find_element(By.XPATH,"//button[@aria-label='Next']").click()
  time.sleep(5)
  all_buttons= driver.find_elements(By.TAG_NAME,"button")
  connect_buttons=[btn for btn in all_buttons if btn.text == "Connect"]
  if connect_buttons:
   for btn in connect_buttons:
    btn.click()
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(3)
    send=driver.find_element(By.XPATH,"//button[@aria-label='Send now']")
    time.sleep(3)
    send.click()
    time.sleep(3)
    driver.execute_script("document.activeElement")
   driver.execute_script("window.scrollBy(0,1000)","")
   time.sleep(10)
   next = driver.find_element(By.XPATH,"//button[@aria-label='Next']").click()
   time.sleep(5)
  else:
    driver.execute_script("window.scrollBy(0,1000)","")
    time.sleep(5)
    next = driver.find_element(By.XPATH,"//button[@aria-label='Next']").click()
    time.sleep(5)

hashtag=driver.find_element(By.XPATH,"//input[@placeholder='Search']")
search.clear()
search.send_keys("real estate",Keys.ENTER)
time.sleep(10)



all_buttons= driver.find_elements(By.TAG_NAME,"button")
messages=[btn for btn in all_buttons if btn.text == "Message"]
for btn in messages:
    btn.click()
    driver.execute_script("arguments[0].click();", btn)
    
    time.sleep(3)
    time.sleep(3)

posts=driver.find_elements(By.XPATH,'/html[1]/body[1]/div[5]/div[3]/div[2]/section[1]/div[1]/nav[1]/div[1]/ul[1]/li[1]/div[1]/button[1]').click()



driver.quit()

print("Automation Complete")
