from selenium import webdriver
import time
bro = webdriver.Chrome()
bro.get("https://www.baidu.com")
time.sleep(3)
input_text = bro.find_element_by_id("kw")
input_text.send_keys("小姐姐")
time.sleep(3)
btn = bro.find_element_by_id('su')
btn.click()
time.sleep(3)
print(bro.page_source)
bro.quit()