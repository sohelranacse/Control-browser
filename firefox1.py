from selenium import webdriver

profile = webdriver.FirefoxProfile("E:/Python/Control-browser/geckodriver.exe")
profile.accept_untrusted_certs = True

driver = webdriver.Firefox(firefox_profile=profile)
driver.get('https://cacert.org/')

driver.close()