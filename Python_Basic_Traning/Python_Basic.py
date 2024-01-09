print("Hello, World!")

a = 10
b = 20
print(a+b)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.drivers.chrome import ChromeDriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
#driver.find_element(By.ID,"checkBoxOption1").click()    #Click on Check-Box
time.sleep(2)
#driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()  #click on link
time.sleep(2)

#it is for select the radio button.

driver.find_element(By.CSS_SELECTOR,"input[value='radio1']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"input[value=radio2]").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"input.radioButton[value=radio3]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@value='radio2' and @name='radioButton']").click()

#it is use for enter the text or value.
Name= driver.find_element(By.XPATH,"//*[@id='name']")
Name.send_keys("Shekhar")

#it is use for clear the text or value from text box.
Name.clear()
Name.send_keys(" Shekhar Tyagi")

Alert= driver.find_element(By.XPATH,"//legend[normalize-space()='Switch To Alert Example']")
Alert1= Alert.text
print(Alert1)