from selenium import webdriver
import time

bro = webdriver.Chrome(executable_path=r"E:\python 13期\上课课件\爬虫+数据\day03\驱动程序\chromedriver.exe")
bro.get("https://qzone.qq.com/")
bro.switch_to.frame('login_frame')
bro.find_element_by_id('switcher_plogin').click()
username = bro.find_element_by_id('u')
username.send_keys("输入qq账号")
time.sleep(1)
password = bro.find_element_by_id('p')
password.send_keys('输入QQ密码')
time.sleep(1)
btn = bro.find_element_by_id("login_button")
btn.click()
time.sleep(20)
print(bro.page_source)
bro.quit()