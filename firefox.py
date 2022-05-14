
# Import the required modules
from selenium import webdriver
import time
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Main Function
if __name__ == '__main__':

    # Provide the email and password
    email = '01775326442'

    GeckoDriverManager().install()

    profile = webdriver.FirefoxProfile()
    profile.accept_untrusted_certs = True

    desired = DesiredCapabilities.FIREFOX

    driver = webdriver.Firefox(firefox_profile=profile, desired_capabilities=desired)

    driver.set_window_size(960, 700)
    driver.get('http://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

    time.sleep(3)
    driver.find_element_by_name('identifier').send_keys(email)
    time.sleep(2)

    driver.find_element_by_css_selector('.VfPpkd-vQzf8d').click()

    print(driver)