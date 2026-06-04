import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import pandas as pd
import os
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.maximize_window()
file_path = r"D:\userinfo\login info.xlsx"
df = pd.read_excel(file_path)
url = df.iloc[0, 1]
stm1_userid = df.iloc[4, 1]
stm1_pass = df.iloc[4, 2]
otp = df.iloc[4, 3]
user = df.iloc[10, 1]
driver.get(url)
driver.implicitly_wait(100)
driver.find_element(By.XPATH, "//div[@class='login-form']//div[1]//label[1]").send_keys(stm1_userid)
driver.find_element(By.XPATH, "//div[@class='divisions']//div[2]//label[1]//input[1]").send_keys(stm1_pass)
driver.find_element(By.XPATH, "//input[@value='Sign In']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='inp']").send_keys(otp)
driver.find_element(By.XPATH, "//input[@value='Submit']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(user)
driver.find_element(By.XPATH, "//div[@class='p-element blurry-text']").click()
time.sleep(3)




fake = Faker()
global group_name
group_name = fake.name()
notes = fake.sentence()
driver.find_element(By.XPATH, "//div[@class='navigation-bars']//div[4]").click()
driver.find_element(By.XPATH, "//div[normalize-space()='Activity']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//div[@class='add-exercise']").click()
driver.find_element(By.XPATH, "//input[@placeholder='Enter group name']").send_keys(group_name)
time.sleep(1)
driver.find_element(By.XPATH, "//span[@class='ng-arrow-wrapper']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//span[normalize-space()='Walking (For Stride Analysis)']").click()
time.sleep(5)



button = driver.find_element(By.XPATH, "//button[@class='btn-outline-single']")
actions = ActionChains(driver)
actions.move_to_element(button).click().perform()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@placeholder='Eg. Take 2-3 minutes rest in between each set.']").send_keys("Create using automation")
time.sleep(2)
driver.find_element(By.XPATH, "//div[contains(text(),'End Date')]//img").click()
time.sleep(2)
button = driver.find_element(By.XPATH, "//li[normalize-space()='Number of Days']")
actions = ActionChains(driver)
actions.move_to_element(button).click().perform()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@type='number']").clear()
driver.find_element(By.XPATH, "//input[@type='number']").send_keys(5)
time.sleep(4)




button = driver.find_element(By.XPATH, "//button[normalize-space()='Add to Schedule']")
actions = ActionChains(driver)
actions.move_to_element(button).click().perform()
time.sleep(3)
time.sleep(4)


driver.find_element(By.XPATH, "//img[@src='./assets/images/edit.png']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@placeholder='Enter group name']").clear()
driver.find_element(By.XPATH, "//input[@placeholder='Enter group name']").send_keys(group_name)
time.sleep(2)
button = driver.find_element(By.XPATH, "//button[normalize-space()='Update Schedule']")
actions = ActionChains(driver)
actions.move_to_element(button).click().perform()
time.sleep(3)




driver.find_element(By.XPATH, "//img[@src='./assets/images/edit.png']").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-profile/div[1]/div[2]/div/app-edit-landing-screen/div/div[1]/app-nw-edit-exercise/div[2]/button").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-profile/div[1]/div[2]/div/app-edit-landing-screen/div/div[1]/app-nw-edit-exercise/div[5]/div/div/div/div/div[3]/button[2]").click()
time.sleep(3)

