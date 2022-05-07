# Import the required modules
from selenium import webdriver
import time

# Main Function
if __name__ == '__main__':

    # Provide the email and password
    email = '01712424859'
    # password = 'Mnbvcxz1!'

    options = webdriver.ChromeOptions()
    # options.add_argument('start-maximized')
    # options.add_argument('disable-infobars')

    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    # Provide the path of chromedriver present on your system.
    driver = webdriver.Chrome(executable_path="E:/Python/Control-browser/chromedriver.exe",
                              chrome_options=options)
    driver.set_window_size(960, 700)

    # Send a get request to the url
    driver.get('https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin/')

    driver.find_element_by_name('identifier').send_keys(email)

    driver.find_element_by_css_selector('.VfPpkd-vQzf8d').click()
    # time.sleep(5)

    print(driver)

    # driver.close()
    # driver.quit()
