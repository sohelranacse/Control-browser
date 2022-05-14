from selenium import webdriver
from selenium_stealth import stealth

email = '01775326442'

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options)
stealth(driver,
     languages=["en-US", "en"],
     vendor="Google Inc.",
     platform="Win32",
     webgl_vendor="Intel Inc.",
     renderer="Intel Iris OpenGL Engine",
     fix_hairline=True,
     )
driver.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
driver.find_element_by_name('identifier').send_keys(email)
driver.find_element_by_css_selector('.VfPpkd-vQzf8d').click()