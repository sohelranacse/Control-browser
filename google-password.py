# Import the required modules
from selenium import webdriver
import time
from selenium_stealth import stealth

# Main Function
if __name__ == '__main__':

    # Provide the email and password
    email = '01775326442'
    # password = 'Mnbvcxz1!'

    options = webdriver.ChromeOptions()
    # options.add_argument('start-maximized')
    # options.add_argument('disable-infobars')

    options.add_argument("--start-maximized")
    # options.add_argument('--log-level=3')

    options.add_argument("--incognito")

    # insecure mode
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

    # test mode flag
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument('--disable-blink-features=AutomationControlled')

    # driver = webdriver.Chrome(executable_path="E:/Python/Control-browser/chromedriver.exe", chrome_options=options)
    driver = webdriver.Chrome(options=options, executable_path=r"E:/Python/Control-browser/chromedriver.exe")

    # driver = webdriver.Chrome(options=options)
    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=False,
        )
    driver.set_window_size(960, 700)

    # Send a get request to the url
    # driver.get('https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin/')
    driver.refresh()
    driver.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

    driver.find_element_by_name('identifier').send_keys(email)

    driver.find_element_by_css_selector('.VfPpkd-vQzf8d').click()
    # time.sleep(5)

    print(driver)

    # driver.close()
    # driver.quit()