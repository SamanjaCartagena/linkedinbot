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
time.sleep(5)
search=driver.find_element(By.XPATH,"//input[@placeholder='Search']")
search.send_keys("real estate",Keys.ENTER)
time.sleep(3)

driver.find_element(By.XPATH,"//button[text()='People']")
people=driver.find_element(By.XPATH,"//button[text()='People']")
time.sleep(3)
people.click()
time.sleep(5)
def checkconnections():
 if driver.find_element(By.XPATH,"//span[text()='Connect']"):
    return True
 else:
    return False
 
if checkconnections == True:
   connect=driver.find_element(By.XPATH,"//span[text()='Connect']")
   for x in range(5):
     connect.click() 
     time.sleep(3)
     driver.execute_script("document.activeElement")
     time.sleep(3)
     send=driver.find_element(By.XPATH,"//button[@aria-label='Send now']")
     time.sleep(3)
     send.click()
     time.sleep(3)
     driver.execute_script("document.activeElement")

else:
 n=2
 number=driver.find_element(By.XPATH,"//button[@aria-label='Page 3']")
 time.sleep(5)
 number.click()
 time.sleep(5)
 if checkconnections() == True:
      connect=driver.find_element(By.XPATH,"//span[text()='Connect']")
      for x in range(5):
        connect.click() 
        time.sleep(3)
        driver.execute_script("document.activeElement")
        time.sleep(3)
        send=driver.find_element(By.XPATH,"//button[@aria-label='Send now']")
        time.sleep(3)
        send.click()
        time.sleep(3)
        if driver.find_element(By.XPATH,"//button[@aria-label='Withdraw']"):
         withdraw=driver.find_element(By.XPATH,"//button[@aria-label='Withdraw']")
        else:
         driver.execute_script("document.activeElement")


      driver.execute_script("document.activeElement")
 else:
     number=driver.find_element(By.XPATH,"//button[@aria-label='Page 3']")
     time.sleep(5)
     number.click()
     time.sleep(5)   
driver.quit()
print("Automation Complete") 






