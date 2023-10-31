from selenium import webdriver
from selenium.webdriver.common.by import By
import os

os.system("cls")

drive = webdriver.Chrome()
drive.get("https://amomeuvascos2.blogspot.com/")

copy = drive.find_element(By.XPATH, "//div[@class='post-body entry-content']")
print(copy.text)

drive.quit()

