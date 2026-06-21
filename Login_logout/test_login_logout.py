import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import os
from datetime import datetime


@pytest.fixture()
def login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    file_path = r"D:\userinfo\login info.xlsx"
    df = pd.read_excel(file_path)
    global url
    global facility_userid
    global facility_pass
    global otp
    facility_userid = df.iloc[2, 1]
    facility_pass = df.iloc[2, 2]
    url = df.iloc[0, 1]
    otp = df.iloc[2, 3]
    driver.get(url)
    driver.implicitly_wait(10)
    yield driver  # Yielding the driver instance
    time.sleep(5)
    driver.quit()


@pytest.fixture()
def loginfinal():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//div[@class='login-form']//div[1]//label[1]").send_keys(facility_userid)
    driver.find_element(By.XPATH, "//div[@class='divisions']//div[2]//label[1]//input[1]").send_keys(facility_pass)
    driver.find_element(By.XPATH, "//input[@value='Sign In']").click()
    time.sleep(5)
    yield driver  # Yielding the driver instance
    time.sleep(5)
    driver.quit()

@pytest.fixture
def take_screenshot(login, request):
    """Fixture to capture a screenshot at specific points in the test."""
    driver = login
    test_name = request.node.name
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    screenshots_dir = r"D:\Testcase\screenshots/login_logout"

    os.makedirs(screenshots_dir, exist_ok=True)

    def _screenshot():
        file_name = f"{test_name}_{timestamp}.png"
        file_path = os.path.join(screenshots_dir, file_name)
        driver.save_screenshot(file_path)
        print(f"Screenshot saved at {file_path}")

    return _screenshot


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture a screenshot if a test fails."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get('facility_login')
        if driver:
            test_name = item.name
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            screenshots_dir = r"D:\Testcase\screenshots/login_logout"
            os.makedirs(screenshots_dir, exist_ok=True)
            file_name = f"{test_name}_failed_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, file_name)
            driver.save_screenshot(file_path)
            print(f"Screenshot for failed test saved at {file_path}")

def test_login_with_invalid_user(login, take_screenshot):
    driver = login
    driver.find_element(By.XPATH, "//div[@class='login-form']//div[1]//label[1]").send_keys("invalid_user@example.com")
    driver.find_element(By.XPATH, "//div[@class='divisions']//div[2]//label[1]//input[1]").send_keys(facility_pass)
    driver.find_element(By.XPATH, "//input[@value='Sign In']").click()
    message = driver.find_element(By.XPATH, "//*[@id='loginForm']/div[3]").text
    assert message == "Incorrect username or password. Please try again."
    time.sleep(2)
    take_screenshot()
    time.sleep(1)


def test_login_with_invalid_password(login, take_screenshot):
    driver = login
    driver.find_element(By.XPATH, "//div[@class='login-form']//div[1]//label[1]").send_keys(facility_userid)
    driver.find_element(By.XPATH, "//div[@class='divisions']//div[2]//label[1]//input[1]").send_keys("WrongPassword@000")
    driver.find_element(By.XPATH, "//input[@value='Sign In']").click()
    message = driver.find_element(By.XPATH, "//*[@id='loginForm']/div[3]").text
    assert message == "Incorrect username or password. Please try again."
    time.sleep(2)
    take_screenshot()
    time.sleep(1)


def test_login_with_valid_userid_password(login, take_screenshot):
    driver = login
    driver.find_element(By.XPATH, "//div[@class='login-form']//div[1]//label[1]").send_keys(facility_userid)
    driver.find_element(By.XPATH, "//div[@class='divisions']//div[2]//label[1]//input[1]").send_keys(facility_pass)
    driver.find_element(By.XPATH, "//input[@value='Sign In']").click()
    message = driver.find_element(By.XPATH, "//h3[normalize-space()='Enter PIN']").text
    assert message == "Enter PIN"
    time.sleep(2)
    take_screenshot()
    time.sleep(1)


def test_invalid_otp(loginfinal, take_screenshot):
    driver = loginfinal
    driver.find_element(By.XPATH, "//input[@id='inp']").send_keys("000000")
    driver.find_element(By.XPATH, "//input[@value='Submit']").click()
    message = driver.find_element(By.XPATH, "//*[@id='pinForm']/div[2]").text
    assert message == "Back to Log in"
    time.sleep(2)
    take_screenshot()
    time.sleep(1)


def test_valid_otp(loginfinal, take_screenshot):
    driver = loginfinal
    driver.find_element(By.XPATH, "//input[@id='inp']").clear()
    driver.find_element(By.XPATH, "//input[@id='inp']").send_keys(otp)
    driver.find_element(By.XPATH, "//input[@value='Submit']").click()
    time.sleep(2)
    take_screenshot()
    time.sleep(1)


def test_log_out(loginfinal, take_screenshot):
    driver = loginfinal
    driver.find_element(By.XPATH, "//input[@id='inp']").send_keys(otp)
    driver.find_element(By.XPATH, "//input[@value='Submit']").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "//div[@class='name-card-value']").click()
    driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
    time.sleep(2)
    take_screenshot()
    time.sleep(1)
