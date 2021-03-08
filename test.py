#!/bin/python3

# TODO: Figure Out Why V-Screen and Headless Causes Captcha Tripping!!!

# Bot Testing Site
# https://bot.sannysoft.com/
from easyprocess import EasyProcessError
from selenium import webdriver
from pyvirtualdisplay import Display

# Start Headless Display
headless: bool = False
try:
    display = Display(visible=0, size=(800, 600))
    # display.start()
except EasyProcessError as e:
    headless: bool = True

# Setup Chrome/Chromium
option = webdriver.ChromeOptions()
option.add_argument('--disable-blink-features=AutomationControlled')
option.add_argument('--user-agent=Chrome/90')
# option.add_argument('--remote-debugging-port=9222')

if headless:
    print("No V-Screen Available!!! Starting Headless!!!")
    option.add_argument('--headless')

browser = webdriver.Chrome(executable_path='chromedriver', options=option)
browser.set_window_size(width=1024, height=900)
# browser.maximize_window()

browser.get('https://www.kroger.com/rx/guest/get-vaccinated')
browser.get('https://www.kroger.com/rx/api/anonymous/scheduler/reasons/pharmacy/01100320')
browser.get_screenshot_as_file(filename="test.png")
browser.quit()
