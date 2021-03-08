from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('--disable-blink-features=AutomationControlled')

browser = webdriver.Chrome(executable_path='chromedriver', options=option)
# browser.get('https://bot.sannysoft.com/')
browser.get('https://www.kroger.com/rx/guest/get-vaccinated')
browser.get('https://www.kroger.com/rx/api/anonymous/scheduler/reasons/pharmacy/01100320')

# This allows me to access Kroger's API, I just need to make sure it can run headless and without problem on my RPI