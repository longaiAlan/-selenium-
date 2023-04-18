# encoding:utf-8
import requests
import re
import json

url_id = 'https://www.acfun.cn/u/32320972'
data = {
    'quickViewId': 'ac-space-video-list',
    'reqID': '4',
    'ajaxpipe': '1',
    'type': 'video',
    'order': 'newest',
    'page': '1',
    'pageSize': '20',
    't': '1681752822806'
}
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
response = requests.get(url=url_id, params=data, headers=headers)
# print(response.text)
# 第一页所以视频地址id
id_list = re.findall('{.*?atomid.*?:(.*?),', response.text)
for ids in id_list:
    id_url = ids.replace('\\"', '')

    url = f'https://www.acfun.cn/v/ac{id_url}'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    response = requests.get(url=url, headers=headers)
    # print(response.text)
    # 解析数据
    # 标题
    title = re.findall('<meta name="keywords" content="(.*?),', response.text)[0]
    html_data = re.findall('window.pageInfo = window.videoInfo = (.*);', response.text)[0]  # 匹配 ; 容易隔断
    character = '\/:*?"<>|'
    for s in character:
        if s in title:
            # print(s)  # 打印特殊字符
            title = title.replace(s, '')
    print(title)
    # print(html_data)
    # 字符串转字典 loads
    dict_data = json.loads(html_data)
    # 提取链接
    link = \
    json.loads(dict_data['currentVideoInfo']['ksPlayJson'])['adaptationSet'][0]['representation'][0]['backupUrl'][0]
    # print(link)
    # 发请求link 获取数据
    link_data = requests.get(url=link, headers=headers).text
    # print(link_data)
    # 提取ts视频片段
    link_urls = re.sub('#E.*', '', link_data).split()
    for link_url in link_urls:
        ts_url = 'https://ali-safety-video.acfun.cn/mediacloud/acfun/acfun_video/' + link_url
        # print(ts_url)
        # 保存数据 二进制
        content_data = requests.get(url=ts_url, headers=headers).content
        with open(title + '.mp4', 'ab') as f:
            f.write(content_data)


