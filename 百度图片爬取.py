# encoding:utf-8
import json
import requests
import uuid
from threading import Thread
from concurrent.futures import ThreadPoolExecutor


class MyThread(Thread):
    def __init__(self, url):
        Thread.__init__(self)
        self.url = url

    def run(self):
        load_img(self.url)


def load_img(url):
    headers = {
        'User-Agent': 'Mozilla/5.0  (Windows  NT  10.0;  Win64;  x64)  AppleWebKit/537.36  (KHTML,  like  Gecko)  Chrome/112.0.0.0  Safari/537.36'
    }
    #  创建Session对象，利用它保持长连接
    session = requests.Session()
    session.headers.update(headers)
    response = session.get(url).text
    response_dict = json.loads(response)
    for item in response_dict["data"]:
        img_url = item.get("thumbURL", "")
        if img_url == "":
            continue
        #  利用Session对象发送请求，保持长连接
        img_data = session.get(img_url).content
        with open(f"image/{uuid.uuid4()}.jpg", "wb") as f:
            f.write(img_data)


if __name__ == '__main__':
    word = input("输入搜索内容： ")
    page = int(input("输入获取页数： "))
    all_url = [
        f"https://image.baidu.com/search/acjson?tn=resultjson_com&logid=7287771915393277458&ipn=rj&ct=201326592&is=&fp=result&fr=&word={word}&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&expermode=&nojc=&isAsync=&pn={(i + 1) * 30}&rn=30&gsm=3c&1683561226935="
        for i in range(page)]
    with ThreadPoolExecutor(max_workers=4) as execute:
        #  创建线程实例并启动线程
        for url in all_url:
            execute.submit(MyThread(url).start)

