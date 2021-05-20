from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

""" 
자동화 로그인 가능한 사이트 : 네이버, 다음, 인스타그램, 블랙보드, 에브리타임.
해결해야하는 부분 : 구글 자동화 로그인이 막힘 
구글 진짜 너무 어렵다...ㅠ
네이버는 구글링으로 해결 -> 전체적인 이해는 아직 안 됨
#클립보드에 input을 복사한 뒤
#해당 내용을 actionChain을 이용해 로그인 폼에 붙여넣기
"""

def copy_input(xpath, input):
    pyperclip.copy(input)
    driver.find_element_by_xpath(xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(1)

driver = webdriver.Chrome('c:/informs/chromedriver.exe')
driver.implicitly_wait(3)

# 자동화 로그인 하고 싶은 url 입력.
url = 'https://www.youtube.com/'
driver.get(url)

# Google
if url == "https://www.google.co.kr/":
    id = '아이디'
    pw = '비밀번호'

# Naver
if url == "https://www.naver.com/":
    id = '아이디'
    pw = '비밀번호'
    time.sleep(1)
    driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
    copy_input('//*[@id="id"]', id)
    time.sleep(1)
    copy_input('//*[@id="pw"]', pw)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

# CBNU Blackboard
if url == "https://cbnu.blackboard.com/":
    id = '아이디'
    pw = '비밀번호'
    driver.find_element_by_name('uid').send_keys(id)
    time.sleep(1)
    driver.find_element_by_name('pswd').send_keys(pw)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="entry-login"]').click()

# Daum
# ty 선택 카카오계정으로 로그인 OR 다음계정으로 로그인
if url == "https://www.daum.net/":
    ty = '카카오'
    time.sleep(1)
    if ty == "카카오":
        id = '아이디'
        pw = '비밀번호'
        driver.get("https://logins.daum.net/accounts/ksso.do?url=https%3A%2F%2Fwww.daum.net%2F")
        driver.find_element_by_name('email').send_keys(id)
        time.sleep(1)
        driver.find_element_by_name('password').send_keys(pw)
        time.sleep(1)
        driver.find_element_by_class_name('btn_g').click()

    elif ty == "다음":
        id = '아이디'
        pw = '비밀번호'
        driver.get("https://logins.daum.net/accounts/dsso.do?url=https%3A%2F%2Fwww.daum.net%2F")
        driver.find_element_by_name('id').send_keys(id)
        time.sleep(1)
        driver.find_element_by_name('pw').send_keys(pw)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="loginBtn"]').click()

# Instargram
if url == "https://www.instagram.com/":
    id = 'username'
    pw = 'password'
    driver.find_element_by_name('username').send_keys(id)
    time.sleep(1)
    driver.find_element_by_name('password').send_keys(pw)
    time.sleep(1)
    driver.find_element_by_class_name('Igw0E').click()

# Everytime
if url == "https://everytime.kr/":
    id = '아이디'
    pw = '비밀번호'
    time.sleep(1)
    driver.get("https://everytime.kr/login")
    driver.find_element_by_name('userid').send_keys(id)
    time.sleep(1)
    driver.find_element_by_name('password').send_keys(pw)
    time.sleep(1)
    driver.find_element_by_class_name('submit').click()