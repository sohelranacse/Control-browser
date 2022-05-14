import pyautogui
import time
import webbrowser
from keyboard import press


if __name__ == '__main__':

    phone = "01775326442"
    password = "123456"

    openBrowser = webbrowser.open(
        'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

    if(openBrowser == True):
        print(openBrowser)
        time.sleep(3)
        pyautogui.typewrite(phone, interval=0.1)
        press('enter')

    print('ok')
