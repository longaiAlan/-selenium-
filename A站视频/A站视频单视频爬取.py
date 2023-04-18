# encoding:utf-8

import requests
import re
import json
import pprint  # 格式化输出

# 1.发送请求
url = 'https://www.acfun.cn/v/ac41150811'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
response = requests.get(url=url, headers=headers)
# print(response.text)
# 2.解析数据
# 标题
title = re.findall('<h1 class="title"><a.*?<span>(.*?)</span></h1>', response.text)[0]
html_data = re.findall('window.pageInfo = window.videoInfo = (.*);', response.text)[0]  # 匹配 ; 容易隔断
print(title)
# print(html_data)
# 字符串转字典 loads
dict_data = json.loads(html_data)
# 提取链接
link = json.loads(dict_data['currentVideoInfo']['ksPlayJson'])['adaptationSet'][0]['representation'][0]['backupUrl'][0]
print(link)
# 3.发请求link 获取数据
link_data = requests.get(url=link, headers=headers).text
# print(link_data)
# 提取ts视频片段
link_urls = re.sub('#E.*', '', link_data).split()
for link_url in link_urls:
    ts_url = 'https://ali-safety-video.acfun.cn/mediacloud/acfun/acfun_video/'+link_url
    print(ts_url)
    # 4.保存数据 二进制
    content_data = requests.get(url=ts_url, headers=headers).content
    with open(title+'.mp4', 'ab')as f:
        f.write(content_data)


