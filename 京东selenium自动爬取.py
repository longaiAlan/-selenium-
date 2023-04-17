# encoding:utf-8
# @Time: 2022/5/29 17:20
# @Author: Alan
# @boys: 加油！！！奥利给！！！
"""
需求：
获取页面价格，书名，评价指数，店铺
"""
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv


class JdSprider:
    lst = []  # 类属性

    # 1初始化方法（加载驱动，）
    def __init__(self):
        self.driver = webdriver.Chrome()
        # 访问网址
        self.driver.get('https://www.jd.com/')
        # 定位输入内容
        self.driver.find_element(By.ID, 'key').send_keys('')
        time.sleep(1)
        self.driver.find_element(By.ID, 'key').send_keys(Keys.ENTER)
        time.sleep(2)

    # 2解析数据
    def parse_html(self):
        # 滑动滚动条到底部
        self.driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight)'
        )
        time.sleep(2)
        lists = self.driver.find_elements(By.XPATH, '//div[@id="J_goodsList"]/ul/li')

        for li in lists:
            try:
                item = {}
                # 价格
                item['price'] = li.find_element(By.XPATH, './/div[@class="p-price"]/strong/i').text
                # 书名
                item['name'] = li.find_element(By.XPATH, './/div[@class="p-name"]/a/em').text
                # 评价条数
                item['commit'] = li.find_element(By.XPATH, './/div[@class="p-commit"]/strong').text
                # 店铺
                item['shop'] = li.find_element(By.XPATH, './/div[@class="p-shopnum"]/a').text
                # 图片
                item['img'] = li.find_element(By.XPATH,'.//div[@class="p-img"]/a/img').get_attribute('src')
                # print(item)
                self.lst.append(item)
            except Exception as e:
                print(e)

    # 3存储数据
    def save_data(self):
        with open('京东书籍.csv', 'w', encoding='utf-8', newline='') as f:
            write = csv.DictWriter(f, fieldnames=['price', 'name', 'commit', 'shop', 'img'])
            write.writeheader()
            write.writerows(self.lst)

    # 主函数
    def main(self):
        while True:
            self.parse_html()
            # 下一页不可用， -1不是最后一页
            if self.driver.page_source.find('pn-next disabled') == -1:
                self.driver.find_element(By.CLASS_NAME, 'pn-next').click()
                time.sleep(1)
            else:
                self.driver.quit()
                break
        self.save_data()


spider = JdSprider()
spider.main()
