# encoding:utf-8
import tkinter as tk
from tkinter import messagebox
from bs4 import BeautifulSoup
import pandas as pd

import requests


def load_data(urls):
    # cookie自己设置
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "Cookie": "user_trace_token=20230515145642-d0a851a4-57cf-42c2-adfb-e826db5da854; _ga=GA1.2.1918883672.1684133804; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1684133804; LGSID=20230515145644-0e47c0b6-2ec0-4d52-b105-a8d622b3f9a7; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fother.php%3Fsc.K00000aItsIJV1%5FTCvrZIHK9y6X9yFWm%5Fd-N2imaFoN-8YV2FDa8YiZR1s13t-FXP-o3c6Py6027jDOvf7Vb6VWZVkg4Vknzlpc2f7z2uVaFhY-N%5FNgrSImGTiPVZObgjJ7p6IKeCrjzKyI9-3n2Vao88vNn6886oU65lFlVKOvJdwdy1gg51BgrAS0c1nuGDrkbIq0uPPFb7u-z5t5OU2QGxlAi.7Y%5FNR2Ar5Od663rj6tJQrGvKD77h24SU5WudF6ksswGuh9J4qt7jHzk8sHfGmYt%5FrE-9kYryqM764TTPqKi%5FnYQZHuukL0.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqs2v4VnL30ZN1ugFxIZ-suHYs0A7bgLw4TARqnsKLULFb5TaV8UHPS0KzmLmqn0KdThkxpyfqnHRYPW0LrH63n6KVINqGujYkPHc4PH6YP6KVgv-b5HDznH64njD40AdYTAkxpyfqnHc3nWm0TZuxpyfqn0KGuAnqiDF70ZKGujYzPsKWpyfqnWfd0APzm1Y1PjTsPf%26dt%3D1684133798%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26tpl%3Dtpl%5F12826%5F31784%5F0%26l%3D1546079882%26us%3DlinkVersion%253D1%2526compPath%253D10036.0-10032.0%2526label%253D%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkType%253D%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520-%252520%2525E4%2525BA%252592%2525E8%252581%252594%2525E7%2525BD%252591%2525E9%2525AB%252598%2525E8%252596%2525AA%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm%5Fsource%3Dm%5Fcf%5Fcpt%5Fbaidu%5Fpcbt; LGUID=20230515145644-1ad22347-dbe6-404c-bcb0-baa840767733; sajssdk_2015_cross_new_user=1; _gid=GA1.2.654596242.1684133860; gate_login_token=v1####70207620ef39cee4c0fcb7a144eca1b09810edf93563c8295d695de1f64d6851; _putrc=832D22A16F7ACC7E123F89F2B170EADC; privacyPolicyPopup=false; login=true; unick=%E8%89%BE%E9%BE%99; sensorsdata2015session=%7B%7D; X_HTTP_TOKEN=376f9fe420bbc1ad37833148618580900735225035; __SAFETY_CLOSE_TIME__24796296=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1684133873; LGRID=20230515145753-d492903e-28fa-4bd7-b38e-70a57c568156; __lg_stoken__=363b70fdbcd05f927d67521bb14aa83571c52f6533a6d1e43506fd1a49ed73a6828dda7b2c857ee723bd6550385d86b73f17ca032bf83ccf2e4cccc7259eb396d6cdb43e47ce; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2224796296%22%2C%22%24device_id%22%3A%221881e334e6a229-051edd8d4ff339-26031b51-1327104-1881e334e6b776%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%22112.0.0.0%22%7D%2C%22first_id%22%3A%221881e334e6a229-051edd8d4ff339-26031b51-1327104-1881e334e6b776%22%7D"
    }
    job_names, job_areas, job_gz_mins, job_gz_maxs, job_exps, job_xls = [], [], [], [], [], []
    for url in urls:
        # 获取网页源代码
        html = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html, "lxml")
        items = soup.select(".item__10RTO")
        for item in items:
            arr1 = item.find(attrs={"class": "p-top__1F7CL"}).a.text.split("[")
            "岗位名称"
            job_name = arr1[0]
            "工作区域"
            job_area = arr1[1].replace("]", "")

            arr2 = item.find(attrs={"class": "p-bom__JlNur"}).text.split("k")
            "最低月薪"
            job_gz_min = arr2[0]
            "最高月薪"
            job_gz_max = arr2[1].replace("-", "")

            arr3 = arr2[2].split("/")
            "工作要求"
            job_exp = arr3[0].strip()
            "学历要求"
            job_xl = arr3[1].strip()

            job_names.append(job_name)
            job_areas.append(job_area)
            job_gz_mins.append(job_gz_min)
            job_gz_maxs.append(job_gz_max)
            job_exps.append(job_exp)
            job_xls.append(job_xl)

    df = pd.DataFrame({
        "岗位名称": job_names,
        "工作区域": job_areas,
        "最低月薪": job_gz_mins,
        "最高月薪": job_gz_maxs,
        "工作要求": job_exps,
        "学历要求": job_xls
    })
    df.to_excel("招聘.xlsx")
    messagebox.showinfo("提示", "爬取完毕！！！")


def exe_spider():
    # 获取到输入的关键字
    keyword = keyword_entry.get()
    # 获取到选中的城市
    city = city_var.get()
    # 获取到输入的页数
    page_num = page_entry.get()
    # 判断是否为空
    if not keyword or not city or not page_num:
        messagebox.showerror("提示", "不能为空")
        return
    # 获取所有页的url地址
    urls = [f"https://www.lagou.com/wn/jobs?pn={i + 1}&kd={keyword}&city={city}" for i in range(int(page_num))]
    load_data(urls)


if __name__ == '__main__':
    # 创建主窗口
    root = tk.Tk()
    root.title("爬虫界面")
    root.geometry("600x80")
    # 创建关键字输入框
    keyword_label = tk.Label(root, text="关键字：")
    # pack显示 靠左
    keyword_label.pack(side=tk.LEFT)
    # 创建文本框
    keyword_entry = tk.Entry(root)
    # css的浮动
    keyword_entry.pack(side=tk.LEFT)

    city_label = tk.Label(root, text="城市：")
    city_label.pack(side=tk.LEFT)
    city_var = tk.StringVar()
    # 设置一个初始值
    city_var.set("全国")  # city_var 选中的值
    city_choices = ["全国", "北京", "上海", "广州", "深圳", "苏州", "杭州", "长沙", "西安", "成都"]
    # OptionMenu 下拉菜单
    city_dropdown = tk.OptionMenu(root, city_var, *city_choices)
    city_dropdown.pack(side=tk.LEFT)
    # 创建页数输入框
    page_label = tk.Label(root, text="页数：")
    page_label.pack(side=tk.LEFT)
    page_entry = tk.Entry(root)
    page_entry.pack(side=tk.LEFT)

    # 创建执行按钮
    execute_button = tk.Button(root, text="执行", command=exe_spider)
    execute_button.pack(side=tk.LEFT)

    # 显示窗体
    root.mainloop()
