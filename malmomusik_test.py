import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from helper_tests_malmomusik import simple_assert, boolean_assert


# Constants
MAIN_SITE = "https://www.malmomusikaffar.com/"
ELEC_GUIT = "https://www.malmomusikaffar.com/stranginstrument/gitarr/elgitarrer"
T484 = "https://www.malmomusikaffar.com/eastman-t484-classic-t484"

# Setup/teardown
@pytest.fixture
def load_driver():

    driver = webdriver.Chrome()

    yield driver

    driver.quit()

# Tests
# Test 1: Öppettider
def assert_open_time(load_driver):

    driver = load_driver

    driver.get(MAIN_SITE)

    heading = driver.find_element(By.XPATH, "/html/body/div[3]/footer/section/ul/li[1]/header/span")

    simple_assert(heading.text, "M-F: 10-18 L: 10-14")

# Test 2: Hitta Eastman T484

# Test 3: Lägg till T484 i varukorg

# Test 4: Kontrollera att företagets facebooksida går att nå via hemsidan

