from selenium import webdriver
import time
import sys

if __name__ == '__main__':

    print('Enter 7 or 9 digit number:')
    start = int(input())
    start_len = len(str(start))
    # here 0 dosen`t not count
    if(start_len < 6 or start_len == 9 or start_len == 11):
        print("Print Enter at least 7 or 9 digit = "+str(start_len+1))
        sys.exit()

    print('Enter 4 or 2 length:')
    n = int(input())
    n_len = len(str(n))
    if(n_len < 2):
        print("Print Enter at least 4 or 2 digit = "+str(n_len))
        sys.exit()

    if(start_len == 6):
        trigger = 10000
    else:
        trigger = 100

    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(
        executable_path="E:/Python/Control-browser/chromedriver.exe", chrome_options=options)
    driver.set_window_size(660, 700)

    driver.delete_all_cookies()
    url = "https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin"

    driver.get(url)

    # file operation
    for x in range(n):
        f = open("number.txt", "a")

        email = "0"+str(int(start)*trigger+x)
        driver.refresh()

        driver.find_element_by_name('identifier').send_keys(email)
        driver.find_element_by_css_selector('.VfPpkd-vQzf8d').click()

        time.sleep(2)
        if(driver.current_url == url):  # unsaved
            print(email)
            driver.refresh()
        else:  # saved data
            f.write(email + "\n")
            print(email+" Yes")
            driver.back()

        f.close()

    driver.close()
    driver.quit()
