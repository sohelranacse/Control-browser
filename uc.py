from seleniumwire.undetected_chromedriver.v2 import Chrome, ChromeOptions
import time

options = {}
chrome_options = ChromeOptions()
chrome_options.add_argument('--user-data-dir=hash')
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--headless")
driver = Chrome(executable_path="E:/Python/Control-browser/chromedriver.exe", chrome_options=chrome_options)

driver.set_window_size(960, 700)
driver.implicitly_wait(100)

# Send a get request to the url
# driver.get('https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin/')
driver.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

driver.find_element_by_name('identifier').send_keys(email)

driver.find_element_by_css_selector('.VfPpkd-vQzf8d').click()

print(driver)
