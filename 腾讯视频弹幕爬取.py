# encoding:utf-8
import json
import requests


def load_words(urls):
    barrage_list = []
    for url in urls:
        headers = {
            "user-agent": "Mozilla/5.0  (Windows  NT  10.0;  Win64;  x64)  AppleWebKit/537.36  (KHTML,  like  Gecko)  Chrome/112.0.0.0  Safari/537.36"
        }
        try:
            response = requests.get(url=url, headers=headers).text
            response_dict = json.loads(response)
            barrage_list.extend([item["content"] for item in response_dict["barrage_list"]])
        except Exception as e:
            print(f"请求出现异常：{e}")
            continue
    barrage = "".join(barrage_list)
    print(barrage)


if __name__ == '__main__':
    page = int(input("输入获取弹幕页数："))
    urls = [f"https://dm.video.qq.com/barrage/segment/k0046zri4a1/t/v1/{i * 30000}/{(i + 1) * 30000}" for i in
            range(page)]

    load_words(urls)
