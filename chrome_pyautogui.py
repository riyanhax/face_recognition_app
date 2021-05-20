# 지금까지 알아본 구글 뚫을 수 있는 방법
# 1. 계정보안 낮추기(실패)
# 2. 스택오버플로우 우회하기(실패)
# 3. 크롬 디버깅 모드로 전환

# 크롬의 디버깅 모드로 셀레니움 사용 -> pyautogui 라이브러리 사용 -> 사람이 키보드로 ID와 PW를 직접 입력하는 것처럼
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess
import shutil
import pyautogui 

try:
    shutil.rmtree("C:\chrometemp")  # remove Cookie, Cache files
except FileNotFoundError:
    pass

try:
    subprocess.Popen('C:\Program Files(x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')
except FileNotFoundError:
    pass 

option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
    
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
driver.implicitly_wait(10)

driver.get(
    url='https://accounts.google.com/ServiceLogin')

# Google login page

pyautogui.write('아이디')    # Fill in your ID or E-mail
pyautogui.press('tab', presses=3)   # Press the Tab key 3 times
pyautogui.press('enter')
time.sleep(3)   # wait a process
pyautogui.write('비번')   # Fill in your PW
pyautogui.press('enter')
