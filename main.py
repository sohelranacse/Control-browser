# Import the required modules
from selenium import webdriver
import time

# Main Function
if __name__ == '__main__':

    # Provide the email and password
    email = 'mdsohelranacse@gmail.com'
    password = 'Mnbvcxz1!'

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')

    # Provide the path of chromedriver present on your system.
    driver = webdriver.Chrome(executable_path="E:/Python/Control-browser/chromedriver.exe",
                              chrome_options=options)
    driver.set_window_size(1920, 1080)

    # Send a get request to the url
    driver.get('https://auth.geeksforgeeks.org/')
    # time.sleep(5)

    # Finds the input box by name in DOM tree to send both
    # the provided email and password in it.
    driver.find_element_by_name('user').send_keys(email)
    driver.find_element_by_name('pass').send_keys(password)

    # Find the signin button and click on it.
    driver.find_element_by_css_selector(
        'button.btn.btn-green.signin-button').click()
    time.sleep(5)

    # Returns the list of elements
    # having the following css selector.
    container = driver.find_elements_by_css_selector(
        'div.mdl-cell.mdl-cell--9-col.mdl-cell--12-col-phone.textBold')

    # Extracts the text from name,
    # institution, email_id css selector.
    name = container[0].text
    try:
        institution = container[1].find_element_by_css_selector('a').text
    except:
        institution = container[1].text
    email_id = container[2].text

    # Output Example 1
    print("Basic Info")
    print({"Name": name,
           "Institution": institution,
           "Email ID": email})

    # Clicks on Practice Tab
    driver.find_elements_by_css_selector(
        'a.mdl-navigation__link')[1].click()
    # time.sleep(5)

    # # Selected the Container containing information
    # container = driver.find_element_by_css_selector(
    #     'div.mdl-cell.mdl-cell--7-col.mdl-cell--12-col-phone.\
    #   whiteBgColor.mdl-shadow--2dp.userMainDiv')

    # # Selected the tags from the container
    # grids = container.find_elements_by_css_selector(
    #     'div.mdl-grid')

    # # Iterate each tag and append the text extracted from it.
    # res = set()
    # for grid in grids:
    #     res.add(grid.text.replace('\n', ':'))

    # # Output Example 2
    # print("Practice Info")
    # print(res)

    # Quits the driver
    driver.close()
    driver.quit()
