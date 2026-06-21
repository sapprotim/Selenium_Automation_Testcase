import pytest
import time
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import os

@pytest.fixture(scope="module")
def org_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    file_path = r"D:\userinfo\login info.xlsx"
    df = pd.read_excel(file_path)
    url = df.iloc[0, 1]
    org_userid = df.iloc[1, 1]
    org_pass = df.iloc[1, 2]
    otp = df.iloc[1, 3]
    driver.get(url)
    driver.implicitly_wait(100)
    driver.find_element(By.XPATH, "//div[@class='login-form']//div[1]//label[1]").send_keys(org_userid)
    driver.find_element(By.XPATH, "//div[@class='divisions']//div[2]//label[1]//input[1]").send_keys(org_pass)
    driver.find_element(By.XPATH, "//input[@value='Sign In']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//input[@id='inp']").send_keys(otp)
    driver.find_element(By.XPATH, "//input[@value='Submit']").click()
    time.sleep(5)
    yield driver  # Yielding the driver instance
    time.sleep(5)
    driver.quit()

def test_create_medichine(org_login):
    driver = org_login
    fake = Faker()  # Specify 'en_GB' for UK locale
    global medicine_name
    medicine_name = fake.name()
    brand = fake.name()
    time.sleep(5)
    driver.find_element(By.XPATH, "//span[normalize-space()='Programme Management']").click()
    driver.find_element(By.XPATH, "//a[normalize-space()='Medicines']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[@class='add-patient-btn']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@trim='blur']").send_keys(medicine_name)
    driver.find_element(By.XPATH, "//input[@formcontrolname='brand']").send_keys(brand)
    driver.find_element(By.XPATH, "//label[@class='schedule-drop-value inp']//img").click()
    driver.find_element(By.XPATH,"//*[@id='add-medicine']/div/div/div/div/app-add-medicine/div/div/div[2]/div[2]/form/div[3]/div[1]/div/ul/li[1]").click()
    driver.find_element(By.XPATH, "//label[@class='inp adjacent-box']//input[@id='inp']").send_keys(100)
    driver.find_element(By.XPATH, "//div[@class='schedule-drop-value duration']//img").click()
    driver.find_element(By.XPATH, "//*[@id='add-medicine']/div/div/div/div/app-add-medicine/div/div/div[2]/div[2]/form/div[4]/div/div/ul/li[1]").click()
    driver.find_element(By.XPATH, "//div[@class='next-btn']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@class='btn btn-primary confirm-medi-btn']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@class='btn btn-primary ack-dismiss-btn']").click()
    time.sleep(10)

def test_Edit_medichine(org_login):
    driver = org_login
    driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(medicine_name)
    fake = Faker()
    global new_medicine_name
    new_medicine_name = fake.name()
    driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/div[1]/img[1]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[@class='content-body']//div[1]//label[1]//input[1]").clear()
    driver.find_element(By.XPATH, "//div[@class='content-body']//div[1]//label[1]//input[1]").send_keys(new_medicine_name)
    driver.find_element(By.XPATH, "//div[normalize-space()='Capsule']//img").click()
    driver.find_element(By.XPATH, "//*[@id='add-medicine']/div/div/div/div/app-edit-medicine/div/div[2]/div/form/div[3]/div[2]/div/ul/li[3]").click()
    driver.find_element(By.XPATH, "//label[@class='inp adjacent-box']//input[@id='inp']").clear()
    driver.find_element(By.XPATH, "//label[@class='inp adjacent-box']//input[@id='inp']").send_keys(500)
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[@class='next-btn']").click()

def test_Delete_medichine(org_login):
    driver = org_login
    driver.find_element(By.XPATH, "//img[@title='Refresh']").click()
    driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(new_medicine_name)
    time.sleep(1)
    driver.find_element(By.XPATH, "//img[@src='./assets/images/delete.png']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-view-medicine/div[2]/div/div/div/div/div/app-disable-medicine/div/div[3]/button[2]").click()
    time.sleep(8)
    driver.find_element(By.XPATH, "//img[@title='Refresh']").click()
    time.sleep(2)


#  Create Specialised Nutrition
def test_Create_Specialised_Nutrition(org_login):
    driver = org_login
    fake = Faker()
    global Specialised_Nutrition
    Specialised_Nutrition = fake.name()
    brand = fake.name()
    flavor = fake.name()
    consistency = fake.name()
    stock_left = fake.random_number(2)
    strength = fake.random_number(2)
    driver.find_element(By.XPATH, "//span[normalize-space()='Programme Management']").click()
    driver.find_element(By.XPATH, "//a[normalize-space()='Specialised Nutrition']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[@class='add-patient-btn']").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-view-nutrition/div[2]/div/div/div/div/div/app-add-nutrition/div/div/div[2]/div[2]/form/div[1]/label/input").send_keys(Specialised_Nutrition)
    driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-view-nutrition/div[2]/div/div/div/div/div/app-add-nutrition/div/div/div[2]/div[2]/form/div[2]/label/input").send_keys(brand)
    driver.find_element(By.XPATH,"//input[@formcontrolname='flavor']").send_keys(flavor)
    driver.find_element(By.XPATH,"//label[@class='schedule-drop-value inp']//img").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='add-nutrition']/div/div/div/div/app-add-nutrition/div/div/div[2]/div[2]/form/div[3]/div[2]/div/ul/li[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@formcontrolname='consistency']").send_keys(consistency)
    driver.find_element(By.XPATH, "//input[@formcontrolname='stockLeft']").send_keys(stock_left)
    driver.find_element(By.XPATH, "//input[@formcontrolname='tempStrength']").send_keys(strength)
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[@class='schedule-drop-value duration']//img").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='add-nutrition']/div/div/div/div/app-add-nutrition/div/div/div[2]/div[2]/form/div[4]/div[2]/div/ul/li[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-nutrition/div[2]/div/div/div/div/div/app-add-nutrition/div/div/div[2]/div[2]/form/div[10]/div").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-nutrition/div[2]/div/div/div/div/div/app-add-nutrition/div/div[3]/button[2]").click()
    time.sleep(8)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-nutrition/div[1]/div[1]/img").click()
    time.sleep(2)

# Edit Specialised Nutrition
def test_Edit_Specialised_Nutrition(org_login):
    driver = org_login
    driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(Specialised_Nutrition)
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[@src='./assets/images/edit.png']").click()
    time.sleep(5)
    fake = Faker() # Specify 'en_GB' for UK locale
    global new_Specialised_Nutrition
    new_Specialised_Nutrition = fake.name()
    brand = fake.name()
    flavor = fake.name()
    consistency = fake.name()
    stock_left = fake.random_number(1)
    strength = fake.random_number(2)
    driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-view-nutrition/div[2]/div/div/div/div/div/app-edit-nutrition/div/div[2]/div/form/div[1]/label/input").clear()
    driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-view-nutrition/div[2]/div/div/div/div/div/app-edit-nutrition/div/div[2]/div/form/div[1]/label/input").send_keys(new_Specialised_Nutrition)
    driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-view-nutrition/div[2]/div/div/div/div/div/app-edit-nutrition/div/div[2]/div/form/div[2]/label/input").clear()
    driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-view-nutrition/div[2]/div/div/div/div/div/app-edit-nutrition/div/div[2]/div/form/div[2]/label/input").send_keys(brand)
    driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-view-nutrition/div[2]/div/div/div/div/div/app-edit-nutrition/div/div[2]/div/form/div[3]/label[1]/input").clear()
    driver.find_element(By.XPATH,"/html/body/app-root/div[3]/app-view-nutrition/div[2]/div/div/div/div/div/app-edit-nutrition/div/div[2]/div/form/div[3]/label[1]/input").send_keys(flavor)
    driver.find_element(By.XPATH,"//*[@id='add-nutrition']/div/div/div/div/app-edit-nutrition/div/div[2]/div/form/div[3]/div/div[2]/div/img").click()
    driver.find_element(By.XPATH,"//*[@id='add-nutrition']/div/div/div/div/app-edit-nutrition/div/div[2]/div/form/div[3]/div/div[2]/ul/li[3]").click()
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-nutrition/div[2]/div/div/div/div/div/app-edit-nutrition/div/div[2]/div/form/div[3]/label[2]/input").clear()
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-nutrition/div[2]/div/div/div/div/div/app-edit-nutrition/div/div[2]/div/form/div[3]/label[2]/input").send_keys(consistency)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-nutrition/div[2]/div/div/div/div/div/app-edit-nutrition/div/div[2]/div/form/div[4]/label[1]/input").clear()
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-nutrition/div[2]/div/div/div/div/div/app-edit-nutrition/div/div[2]/div/form/div[4]/label[1]/input").send_keys(stock_left)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-nutrition/div[2]/div/div/div/div/div/app-edit-nutrition/div/div[2]/div/form/div[4]/label[2]/input").clear()
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-nutrition/div[2]/div/div/div/div/div/app-edit-nutrition/div/div[2]/div/form/div[4]/label[2]/input").send_keys(strength)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-nutrition/div[2]/div/div/div/div/div/app-edit-nutrition/div/div[2]/div/form/div[4]/div/div/div/img").click()
    driver.find_element(By.XPATH, "//*[@id='add-nutrition']/div/div/div/div/app-edit-nutrition/div/div[2]/div/form/div[4]/div/div/ul/li[3]").click()
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-nutrition/div[2]/div/div/div/div/div/app-edit-nutrition/div/div[2]/div/form/div[10]/div").click()
    time.sleep(7)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-nutrition/div[1]/div[1]/img").click()
    time.sleep(2)

def test_delete_Specialised_Nutrition(org_login):
    driver = org_login
    driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(new_Specialised_Nutrition)
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[@src='./assets/images/delete.png']").click()
    driver.find_element(By.XPATH, "//button[normalize-space()='Delete Specialised Nutrition']").click()
    time.sleep(7)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-nutrition/div[1]/div[1]/img").click()
    time.sleep(2)

# Physiotherapy
def test_create_Physiotherapy_Exercises(org_login):
    driver = org_login
    fake = Faker()  # Specify 'en_GB' for UK locale
    global exercise_name
    exercise_name = fake.name()
    steps = fake.sentence()
    video_path = os.path.abspath('Programme Management/Exercise.mp4')
    driver.find_element(By.XPATH, "/html/body/app-root/div[2]/div[2]/div[3]/span").click()
    driver.find_element(By.XPATH, "//a[normalize-space()='Physiotherapy']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-exercise/div/div[1]/div[2]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-exercise/div/div[3]/div[1]/div/div/div/div/app-add-exercise/div/div[2]/div[1]/form/div[1]/label/input").send_keys(exercise_name)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-exercise/div/div[3]/div[1]/div/div/div/div/app-add-exercise/div/div[2]/div[1]/form/div[2]/textarea").send_keys(steps)
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='drop-file']/ngx-file-drop/div/div/input").send_keys(video_path)
    time.sleep(5)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-exercise/div/div[3]/div[1]/div/div/div/div/app-add-exercise/div/div[2]/div[1]/form/div[6]/div").click()
    time.sleep(8)
    driver.find_element(By.XPATH, "//img[@title='Refresh']").click()
    time.sleep(2)


def test_Edit_Physiotherapy_Exercises(org_login):
    driver = org_login
    driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(exercise_name)
    driver.find_element(By.XPATH, "//img[@src='./assets/images/edit.png']").click()
    time.sleep(2)
    fake = Faker()
    global new_exercise_name
    new_exercise_name = fake.name()
    steps = fake.sentence()
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-exercise/div/div[3]/div[1]/div/div/div/div/app-edit-exercise/div/div[2]/div/form/div[1]/label/input").clear()
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-exercise/div/div[3]/div[1]/div/div/div/div/app-edit-exercise/div/div[2]/div/form/div[1]/label/input").send_keys(new_exercise_name)
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-exercise/div/div[3]/div[1]/div/div/div/div/app-edit-exercise/div/div[2]/div/form/div[2]/textarea").clear()
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-exercise/div/div[3]/div[1]/div/div/div/div/app-edit-exercise/div/div[2]/div/form/div[2]/textarea").send_keys(steps)
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-exercise/div/div[3]/div[1]/div/div/div/div/app-edit-exercise/div/div[2]/div/form/div[6]/div").click()
    time.sleep(8)
    driver.find_element(By.XPATH, "//img[@title='Refresh']").click()
    time.sleep(2)

def test_Edit_Physiotherapy_delete(org_login):
    driver = org_login
    driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(new_exercise_name)
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[@src='./assets/images/delete.png']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[normalize-space()='Delete Exersice']").click()
    time.sleep(8)
    driver.find_element(By.XPATH, "//img[@title='Refresh']").click()
    time.sleep(2)


#  Equipments
def test_create_Equipments(org_login):
    driver = org_login
    fake = Faker()  # Specify 'en_GB' for UK locale
    global equipment_name
    equipment_name = fake.name()
    size = fake.random_number(1)
    weight_resistance = fake.random_number(2)
    driver.find_element(By.XPATH, "//button[normalize-space()='Exercises']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='dropdown']/ul/li[2]/a").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[@class='add-patient-btn']").click()
    driver.find_element(By.XPATH, "//div[@class='form-wrap']//input[@id='inp']").send_keys(equipment_name)
    time.sleep(1)
    driver.find_element(By.XPATH, "//img[@src='./assets/images/Add-image-dash.png']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[@class='input-wrapper size']//input[@id='inp']").send_keys(size)
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div/mat-dialog-container/div/div/app-edit-equipment/div/div/div/form/div[3]/div/div[1]/div[2]/div/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div/mat-dialog-container/div/div/app-edit-equipment/div/div/div/form/div[3]/div/div[1]/div[2]/div/ul/li[1]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[@class='input-wrapper weight']//input[@id='inp']").send_keys(weight_resistance)
    driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div/mat-dialog-container/div/div/app-edit-equipment/div/div/div/form/div[3]/div/div[1]/div[4]/div/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div/mat-dialog-container/div/div/app-edit-equipment/div/div/div/form/div[3]/div/div[1]/div[4]/div/ul/li[2]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div/mat-dialog-container/div/div/app-edit-equipment/div/div/div/form/div[5]/div").click()
    time.sleep(8)
    driver.find_element(By.XPATH, "//img[@title='Refresh']").click()
    time.sleep(2)

def test_edit_Equipments(org_login):
    driver = org_login
    driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(equipment_name)
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[@src='./assets/images/edit.png']").click()
    time.sleep(2)
    fake = Faker()  # Specify 'en_GB' for UK locale
    global new_equipment_name
    new_equipment_name = fake.name()
    size = fake.random_number(1)
    weight_resistance = fake.random_number(2)
    driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div/mat-dialog-container/div/div/app-edit-equipment/div/div/div/form/div[1]/label/input").clear()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div/mat-dialog-container/div/div/app-edit-equipment/div/div/div/form/div[1]/label/input").send_keys(new_equipment_name)
    driver.find_element(By.XPATH, "//div[@class='input-wrapper size']//input[@id='inp']").clear()
    driver.find_element(By.XPATH, "//div[@class='input-wrapper size']//input[@id='inp']").send_keys(size)
    driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div/mat-dialog-container/div/div/app-edit-equipment/div/div/div/form/div[3]/div/div[1]/div[2]/div/button").click()
    driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div/mat-dialog-container/div/div/app-edit-equipment/div/div/div/form/div[3]/div/div[1]/div[2]/div/ul/li[2]").click()
    driver.find_element(By.XPATH, "//div[@class='input-wrapper weight']//input[@id='inp']").clear()
    driver.find_element(By.XPATH, "//div[@class='input-wrapper weight']//input[@id='inp']").send_keys(weight_resistance)
    driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div/mat-dialog-container/div/div/app-edit-equipment/div/div/div/form/div[3]/div/div[1]/div[4]/div/button").click()
    driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div/mat-dialog-container/div/div/app-edit-equipment/div/div/div/form/div[3]/div/div[1]/div[4]/div/ul/li[1]").click()
    driver.find_element(By.XPATH, "/html/body/div[7]/div[2]/div/mat-dialog-container/div/div/app-edit-equipment/div/div/div/form/div[5]/div").click()
    time.sleep(8)
    driver.find_element(By.XPATH, "//img[@title='Refresh']").click()
    time.sleep(2)

def test_delete_Equipments(org_login):
    driver = org_login
    driver.find_element(By.XPATH,"//input[@placeholder='Search']").clear()
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(new_equipment_name)
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[@src='./assets/images/delete.png']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-exercise/div/div[3]/div[1]/div/div/div/div/app-disable-exercise/div/div[3]/button[2]").click()
    time.sleep(8)
    driver.find_element(By.XPATH, "//img[@title='Refresh']").click()
    time.sleep(2)


def test_create_Predefined_Messages(org_login):
    driver = org_login
    fake = Faker()
    global message
    message = fake.sentence()
    driver.find_element(By.XPATH, "//span[normalize-space()='Programme Management']").click()
    driver.find_element(By.XPATH, "//a[normalize-space()='Predefined Messages']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[@class='add-patient-btn']").click()
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/predefined-messages/div[2]/div/div/div/div[2]/textarea").send_keys(message)
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/predefined-messages/div[2]/div/div/div/div[4]/button[1]").click()
    time.sleep(8)
    driver.find_element(By.XPATH, "//img[@title='Refresh']").click()
    time.sleep(2)

def test_edit_Predefined_Messages(org_login):
    driver = org_login
    driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(message)
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[@src='./assets/images/edit.png']").click()
    fake = Faker()  # Specify 'en_GB' for UK locale
    global new_message
    new_message = fake.sentence()
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/predefined-messages/div[2]/div/div/div/div[2]/textarea").clear()
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/predefined-messages/div[2]/div/div/div/div[2]/textarea").send_keys(new_message)
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/predefined-messages/div[2]/div/div/div/div[4]/button[1]").click()
    time.sleep(8)
    driver.find_element(By.XPATH, "//img[@title='Refresh']").click()
    time.sleep(2)

def test_delete_Predefined_Messages(org_login):
    driver = org_login
    driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(new_message)
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[@src='./assets/images/delete.png']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/predefined-messages/div[4]/div/div/div/div/div[3]/button[2]").click()
    time.sleep(8)
    driver.find_element(By.XPATH, "//img[@title='Refresh']").click()
    time.sleep(2)

def test_create_Clinician_Predefined_Messages(org_login):
    driver = org_login
    fake = Faker()  # Specify 'en_GB' for UK locale
    global message
    message = fake.sentence()
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/predefined-messages/div[1]/div[1]/div[2]/div/button").click()
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/predefined-messages/div[1]/div[1]/div[2]/div/ul/li[2]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[@class='add-patient-btn']").click()
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/predefined-messages/div[2]/div/div/div/div[2]/textarea").send_keys(message)
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/predefined-messages/div[2]/div/div/div/div[4]/button[1]").click()
    time.sleep(8)
    driver.find_element(By.XPATH, "//img[@title='Refresh']").click()
    time.sleep(2)

def test_edit_Clinician_Predefined_Messages(org_login):
    driver = org_login
    driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(message)
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[@src='./assets/images/edit.png']").click()
    fake = Faker()  # Specify 'en_GB' for UK locale
    global new_message
    new_message = fake.sentence()
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/predefined-messages/div[2]/div/div/div/div[2]/textarea").clear()
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/predefined-messages/div[2]/div/div/div/div[2]/textarea").send_keys(new_message)
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/predefined-messages/div[2]/div/div/div/div[4]/button[1]").click()
    time.sleep(8)
    driver.find_element(By.XPATH, "//img[@title='Refresh']").click()
    time.sleep(2)

def test_delete_Clinician_Predefined_Messages(org_login):
    driver = org_login
    driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(new_message)
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[@src='./assets/images/delete.png']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/predefined-messages/div[4]/div/div/div/div/div[3]/button[2]").click()
    time.sleep(8)
    driver.find_element(By.XPATH, "//img[@title='Refresh']").click()
    time.sleep(2)

def test_create_Link(org_login):
    driver = org_login
    fake = Faker()
    global link_name
    link_name = fake.name()
    link_address = fake.url()
    driver.find_element(By.XPATH, "//span[normalize-space()='Programme Management']").click()
    driver.find_element(By.XPATH, "//a[normalize-space()='Links']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[@class='add-patient-btn']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-links/div[2]/div/div/div/div/div/app-add-links/div/div[2]/div/form/div[1]/label/input").send_keys(link_name)
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-links/div[2]/div/div/div/div/div/app-add-links/div/div[2]/div/form/div[2]/div[1]/textarea").send_keys(link_address)
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='add-medicine']/div/div/div/div/app-add-links/div/div[2]/div/form/div[3]/div/label[1]/span").click()
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-links/div[2]/div/div/div/div/div/app-add-links/div/div[2]/div/form/div[4]/button").click()
    time.sleep(8)
    driver.find_element(By.XPATH, "//img[@title='Refresh']").click()
    time.sleep(2)

def test_edit_Link(org_login):
    driver = org_login
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-links/div[1]/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[5]/div/img[1]").click()
    time.sleep(2)
    fake = Faker()
    global new_link_name
    new_link_name = fake.name()
    link_address = fake.url()
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-links/div[2]/div/div/div/div/div/app-edit-links/div/div[2]/div/form/div[1]/label/input").clear()
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-links/div[2]/div/div/div/div/div/app-edit-links/div/div[2]/div/form/div[1]/label/input").send_keys(new_link_name)
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-links/div[2]/div/div/div/div/div/app-edit-links/div/div[2]/div/form/div[2]/label/textarea").clear()
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-links/div[2]/div/div/div/div/div/app-edit-links/div/div[2]/div/form/div[2]/label/textarea").send_keys(link_address)
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='add-medicine']/div/div/div/div/app-edit-links/div/div[2]/div/form/div[3]/div/label[1]/span").click()
    driver.find_element(By.XPATH, "//*[@id='add-medicine']/div/div/div/div/app-edit-links/div/div[2]/div/form/div[3]/div/label[2]/span").click()
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-links/div[2]/div/div/div/div/div/app-edit-links/div/div[2]/div/form/div[4]/button").click()
    time.sleep(8)
    driver.find_element(By.XPATH, "//img[@title='Refresh']").click()
    time.sleep(2)

def test_delete_Link(org_login):
    driver = org_login
    driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/div[1]/img[2]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-links/div[2]/div/div/div/div/div/app-disable-links/div/div[3]/button[2]").click()
    time.sleep(8)
    driver.find_element(By.XPATH, "//img[@title='Refresh']").click()
    time.sleep(2)

def test_edit_Themes(org_login):
    driver = org_login
    fake = Faker()  # Specify 'en_GB' for UK locale
    theme_name = fake.name()
    driver.find_element(By.XPATH, "//span[normalize-space()='Programme Management']").click()
    driver.find_element(By.XPATH, "//a[normalize-space()='Themes']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[@src='./assets/images/edit.png']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-theme/div[2]/div/div/div/div/div/app-edit-theme/div/div[2]/div/form/div[1]/label/input").clear()
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-theme/div[2]/div/div/div/div/div/app-edit-theme/div/div[2]/div/form/div[1]/label/input").send_keys(theme_name)
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-theme/div[2]/div/div/div/div/div/app-edit-theme/div/div[2]/div/form/div[8]/button").click()
    time.sleep(8)
    driver.find_element(By.XPATH, "//img[@title='Refresh']").click()
    time.sleep(2)

def test_Create_Nudge_and_Alert(org_login):
    driver = org_login
    fake = Faker()  # Specify 'en_GB' for UK locale
    global template_name
    template_name = fake.name()
    description = fake.paragraph()
    title = fake.name()
    message = fake.sentence()
    step_data = int(fake.random_number(4))
    driver.find_element(By.XPATH, "//span[normalize-space()='Programme Management']").click()
    driver.find_element(By.XPATH, "//a[normalize-space()='Alerts/Nudges']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[@class='add-patient-btn']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-alert-templates/div[2]/div/div/div/div/div/app-add-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-rules/form/div[1]/label/input").send_keys(template_name)
    driver.find_element(By.XPATH, "//*[@id='add-alert-template']/div/div/div/div/app-add-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-rules/form/div[2]/div[2]/label[2]/span").click()
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-alert-templates/div[2]/div/div/div/div/div/app-add-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-rules/form/div[4]/label/textarea").send_keys(description)
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[@src='./assets/images/downarrow.png']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='add-alert-template']/div/div/div/div/app-add-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-rules/form/div[5]/app-dropdown/div/div/ul/li[1]/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//body[1]/app-root[1]/div[3]/app-view-alert-templates[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/app-add-alert-template[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/app-alert-rules[1]/form[1]/div[6]/app-jdm-editor[1]/div[1]/decision-table[1]/div[1]/div[2]/table[2]/thead[1]/tr[1]/th[2]/div[1]/div[2]/button[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[normalize-space()='Edit column']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='field-update-dialog']/div[1]/div/div[2]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div/ul/li[2]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div/ul[2]/li[1]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div/ul[3]/li[1]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-alert-templates/div[2]/div/div/div/div/div/app-add-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-rules/form/div[6]/app-jdm-editor/div/decision-table/div/div[3]/div[2]/div/div[2]/div[3]/button[2]/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//body[1]/app-root[1]/div[3]/app-view-alert-templates[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/app-add-alert-template[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/app-alert-rules[1]/form[1]/div[6]/app-jdm-editor[1]/div[1]/decision-table[1]/div[1]/div[2]/table[2]/tbody[1]/tr[1]/td[2]/div[1]/input[1]").send_keys(step_data)
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[@class='next-btn']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[@src='./assets/images/Plus Btn.png']").click()
    driver.find_element(By.XPATH, "//img[@src='./assets/images/downarrow.png']").click()
    driver.find_element(By.XPATH, "//*[@id='add-alert-template']/div/div/div/div/app-add-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-messages/div[2]/app-alert-message/div/form/div[1]/div/div[1]/ul/li[1]/label/span").click()
    driver.find_element(By.XPATH, "//*[@id='add-alert-template']/div/div/div/div/app-add-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-messages/div[2]/app-alert-message/div/form/div[1]/div/div[1]/ul/li[2]/label/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-alert-templates/div[2]/div/div/div/div/div/app-add-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-messages/div[2]/app-alert-message/div/form/div[2]/label/input").send_keys(title)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-alert-templates/div[2]/div/div/div/div/div/app-add-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-messages/div[2]/app-alert-message/div/form/div[3]/label/textarea").send_keys(message)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-alert-templates/div[2]/div/div/div/div/div/app-add-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-messages/div[2]/app-alert-message/div/form/div[4]/div/button[2]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-alert-templates/div[2]/div/div/div/div/div/app-add-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-messages/div[3]/div[2]").click()
    time.sleep(8)
    driver.find_element(By.XPATH, "//img[@title='Refresh']").click()
    time.sleep(2)

def test_Edit_Nudge_and_Alert(org_login):
    driver = org_login
    driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(template_name)
    driver.find_element(By.XPATH, "//tbody//tr//img[1]").click()
    time.sleep(2)
    fake = Faker()  # Specify 'en_GB' for UK locale
    global new_template_name
    new_template_name = fake.name()
    description = fake.paragraph()
    title = fake.name()
    message = fake.sentence()
    data = fake.random_number(2)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-alert-templates/div[2]/div/div/div/div/div/app-edit-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-rules/form/div[1]/label/input").clear()
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-alert-templates/div[2]/div/div/div/div/div/app-edit-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-rules/form/div[1]/label/input").send_keys(new_template_name)
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-alert-templates/div[2]/div/div/div/div/div/app-edit-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-rules/form/div[2]/label/textarea").clear()
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-alert-templates/div[2]/div/div/div/div/div/app-edit-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-rules/form/div[2]/label/textarea").send_keys(description)
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[@src='./assets/images/downarrow.png']").click()
    driver.find_element(By.XPATH, "//*[@id='add-alert-template']/div/div/div/div/app-edit-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-rules/form/div[3]/app-dropdown/div/div/ul/li[2]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[normalize-space()='Daily']//img").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='add-alert-template']/div/div/div/div/app-edit-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-rules/form/div[4]/div[1]/app-dropdown/div/div/ul/li[2]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//app-dropdown[@multiple='true']//img").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='add-alert-template']/div/div/div/div/app-edit-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-rules/form/div[4]/div[2]/div[1]/app-dropdown/div/div/ul/li[1]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='add-alert-template']/div/div/div/div/app-edit-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-rules/form/div[4]/div[2]/div[2]/app-dropdown/div/div/div").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='add-alert-template']/div/div/div/div/app-edit-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-rules/form/div[4]/div[2]/div[2]/app-dropdown/div/div/ul/li[15]").click()
    driver.find_element(By.XPATH, "//*[@id='add-alert-template']/div/div/div/div/app-edit-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-rules/form/div[5]/app-jdm-editor/div/decision-table/div/div[2]/table[2]/thead/tr/th[2]/div[1]/div[2]/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[8]/div/ul/li[1]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='field-update-dialog']/div[1]/div/div[2]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div/ul/li[2]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div/ul[2]/li[2]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div/ul[3]/li[1]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-alert-templates/div[2]/div/div/div/div/div/app-edit-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-rules/form/div[5]/app-jdm-editor/div/decision-table/div/div[3]/div[2]/div/div[2]/div[3]/button[2]/span").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='add-alert-template']/div/div/div/div/app-edit-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-rules/form/div[5]/app-jdm-editor/div/decision-table/div/div[2]/table[2]/tbody/tr/td[2]/div/input").clear()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='add-alert-template']/div/div/div/div/app-edit-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-rules/form/div[5]/app-jdm-editor/div/decision-table/div/div[2]/table[2]/tbody/tr/td[2]/div/input").clear()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='add-alert-template']/div/div/div/div/app-edit-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-rules/form/div[5]/app-jdm-editor/div/decision-table/div/div[2]/table[2]/tbody/tr/td[2]/div/input").send_keys(data)
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[@class='next-btn']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[@class='alert-message-wrapper']//img[1]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//img[@src='./assets/images/downarrow.png']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='add-alert-template']/div/div/div/div/app-edit-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-messages/div[1]/div/div[2]/app-alert-message/div/form/div[1]/div/div/ul/li[2]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-alert-templates/div[2]/div/div/div/div/div/app-edit-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-messages/div[1]/div/div[2]/app-alert-message/div/form/div[2]/label/input").clear()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-alert-templates/div[2]/div/div/div/div/div/app-edit-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-messages/div[1]/div/div[2]/app-alert-message/div/form/div[2]/label/input").send_keys(title)
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-alert-templates/div[2]/div/div/div/div/div/app-edit-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-messages/div[1]/div/div[2]/app-alert-message/div/form/div[3]/label/textarea").clear()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-alert-templates/div[2]/div/div/div/div/div/app-edit-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-messages/div[1]/div/div[2]/app-alert-message/div/form/div[3]/label/textarea").send_keys(message)
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-alert-templates/div[2]/div/div/div/div/div/app-edit-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-messages/div[1]/div/div[2]/app-alert-message/div/form/div[4]/div/button[2]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-alert-templates/div[2]/div/div/div/div/div/app-edit-alert-template/div/div/div[2]/div[2]/div/div[2]/app-alert-messages/div[3]/div[2]").click()
    time.sleep(8)
    driver.find_element(By.XPATH, "//img[@title='Refresh']").click()
    time.sleep(2)

def test_delete_Nudge_and_Alert(org_login):
    driver = org_login
    driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(new_template_name)
    time.sleep(2)
    driver.find_element(By.XPATH, "//img[@src='./assets/images/delete.png']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/app-root/div[3]/app-view-alert-templates/div[2]/div/div/div/div/div/app-delete-alert-templates/div/div[3]/button[2]").click()
    time.sleep(8)
    driver.find_element(By.XPATH, "//img[@title='Refresh']").click()
    time.sleep(2)
