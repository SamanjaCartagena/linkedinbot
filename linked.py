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

driver.get('https://www.linkedin.com/search/results/people/?keywords=real%20estate&origin=SWITCH_SEARCH_VERTICAL&sid=JU(')
time.sleep(5)



all_buttons= driver.find_elements(By.TAG_NAME,"button")
messages=[btn for btn in all_buttons if btn.text =='Message']
for i in range(0,2):
   messages[i].click()
   time.sleep(5)
   try:
     subject=driver.find_element(By.XPATH,"//input[@name='subject']")

     if subject.is_displayed():
       subject.send_keys('Hi')
       time.sleep(10)
       main_div  = driver.find_element(By.CLASS_NAME,"msg-form__contenteditable")
       main_div.click()
       main_div.send_keys('Hello there, I have built a bot and I am testing it. Sorry if I bothered you. This is automated and not Samanja')
       time.sleep(10)
       send_button=driver.find_element(By.CLASS_NAME,"msg-form__send-button") 
       send_button.click() 
       time.sleep(5)  
       close=driver.find_element(By.XPATH,"//button//li-icon[@type='close']//*[name()='svg']//*[name()='path' and contains(@d,'M14 3.41L9')]").click()
   except :  
    close=driver.find_element(By.XPATH,"//button//li-icon[@type='close']//*[name()='svg']//*[name()='path' and contains(@d,'M14 3.41L9')]").click()
    print('None')
   time.sleep(10)

driver.get('https://www.linkedin.com/search/results/content/?keywords=real%20estate&origin=SWITCH_SEARCH_VERTICAL&sid=~yz')

time.sleep(5)
driver.execute_script("window.scrollBy(0,300)","")

repost=driver.find_element(By.XPATH,'/html[1]/body[1]/div[4]/div[3]/div[2]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[6]/div[2]/div[1]/span[1]/button[1]/span[1]')
repost.click()
rep=driver.find_element(By.XPATH,'/html[1]/body[1]/div[4]/div[3]/div[2]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[1]/div[6]/div[2]/div[1]/span[1]/div[1]/div[1]/ul[1]/li[2]/div[1]/span[2]')
rep.click()
time.sleep(5)
driver.quit()

print("Automation Complete")

#connect with real estate salesperson,realestate broker New York and Connecticut
#repost share hastag real estate, regular real estate, hashtag home for sale, westchester county, rockland county, chappaqua, armonk, ardsley, mamaroneck, stony point, goshen,  
#addnote to salesperson 
#messages per day 
#like other real estate salesperson's posts


