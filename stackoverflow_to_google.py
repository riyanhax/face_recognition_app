# 지금까지 알아본 구글 뚫을 수 있는 방법
# 1. 계정보안 낮추기(실패)
# 2. 스택오버플로우 우회하기(실패)
# 3. 크롬 디버깅 모드로 전환

# 스택오버플로우 통해서 들어가기(막힘)
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome() 
driver.get('https://stackoverflow.com/') 
time.sleep(0.5) 
driver.find_element_by_xpath('/html/body/header/div/ol[2]/li[2]/a[1]').click() 
time.sleep(0.5) 
driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click() 
time.sleep(0.5) 
driver.find_element_by_id('identifierId').send_keys('구글아이디') 
driver.find_element_by_xpath( '//*[@id="identifierNext"]/div/button/div[2]').click() 
time.sleep(2) 
driver.find_element_by_xpath( '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('비번') driver.find_element_by_xpath( '//*[@id="passwordNext"]/div/button/div[2]').click() 
time.sleep(2) 
driver.get('https://accounts.google.com/signin/v2/identifier?hl=en&continue=https://news.google.com/') 
time.sleep(2)
