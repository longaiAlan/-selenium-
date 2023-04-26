# encoding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


word = input("输入翻译内容：")
driver = webdriver.Chrome()
driver.get('https://fanyi.baidu.com/')
try:
    #  等待网页指引元素加载
    close_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "app-guide-close")))
    close_btn.click()
    #  等待翻译输入框加载
    text_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "baidu_translate_input")))
    text_btn.send_keys(word)
    #  等待翻译按钮加载
    tran_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "translate-button")))
    tran_btn.click()
    #  等待翻译结果加载
    text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'target-output'))).text
    print(text)
except Exception as e:
    print('翻译出现错误:', e)
finally:
    # 退出
    driver.quit()
