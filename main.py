from argparse import ArgumentParser
from pathlib import Path
import sys

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def resourcePath(filename):
    if hasattr(sys, "_MEIPASS"):
        return str(Path(sys._MEIPASS).joinpath("data").joinpath(filename).resolve())
    return str(Path(filename).resolve())


scratch_path = r"C:\Program Files (x86)\Scratch Desktop\Scratch Desktop.exe"
driver_path = resourcePath(r"chromedriver.exe")

parser = ArgumentParser()
parser.add_argument('path')
args = parser.parse_args()

options = webdriver.ChromeOptions()
options.binary_location = scratch_path

driver = webdriver.Chrome(driver_path, options=options)
wait = WebDriverWait(driver, 30)
wait.until(EC.element_to_be_clickable((By.XPATH, r'//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]')))
print("Loaded")

# bypass popup asking user-data statistics
try:
    driver.find_element_by_xpath(r'/html/body/div/div/div/div/div[2]/div/button[1]').click()
except Exception as e:
    print(e)

# open file
try:
    driver.find_element_by_xpath(r'//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]').click()     # open menu
    driver.find_element_by_xpath(r'//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]/div/ul/li[2]/input').send_keys(str(Path(args.path).resolve()))    # open file
except Exception as e:
    print(e)
