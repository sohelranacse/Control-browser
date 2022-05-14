# from selenium import webdriver
import time
from selenium_stealth import stealth
# from seleniumwire import webdriver
from seleniumwire.undetected_chromedriver import webdriver
from keyboard import press
import pyautogui

# Main Function
if __name__ == '__main__':

    # Provide the email and password
    email = '01716565093'
    password = '01716565091'

    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')

    options.add_argument("--incognito")
    options.add_argument('ignore-certificate-errors')

    # insecure mode
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

    # test mode flag
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument('--disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(executable_path="E:/Python/Control-browser/chromedriver.exe", chrome_options=options)
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    driver.set_window_size(650, 700)
    driver.implicitly_wait(100)

    driver.delete_all_cookies()

    driver.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

    pyautogui.write(email, interval=0)
    press('enter')

    time.sleep(3)
    try:
        if(driver.find_element_by_name('password')):
            pyautogui.write(password, interval=0)
            press('enter')
            print('Yes')
        else:
            print('no')
            driver.back()
    except:
        print('No')
        driver.back()

    print(driver.current_url)

    # driver.close()
    # driver.quit()
