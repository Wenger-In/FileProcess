import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Selecting folder path
folder_path = 'E:/Research/Work/tianwen_IPS/s1a26x'

# Creating Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Iterating for all html files
for file_name in os.listdir(folder_path):
    if file_name.endswith('.html'):
        # Opening html files
        file_path = os.path.join(folder_path, file_name)
        driver.get(f'file://{file_path}')
        # Waiting for loading finished
        time.sleep(2)
        # Screen-shooting
        screenshot = driver.get_screenshot_as_png()
        # Saving as png files
        new_file_name = file_name.replace('.html', '.png')
        screenshot_path = os.path.join(folder_path, new_file_name)
        with open(screenshot_path, 'wb') as f:
            f.write(screenshot)

# Close Chrome
driver.quit()
