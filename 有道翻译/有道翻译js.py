# encoding:utf-8
# @Time":"2022/7/15 14:07
# @Author":"Alan",
# @boys":"加油！！！奥利给！！！
import requests
import execjs

url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
headers = {
    'Cookie': 'OUTFOX_SEARCH_USER_ID=2009997764@10.110.96.160; OUTFOX_SEARCH_USER_ID_NCOO=230116657.32916912; ___rl__test__cookies=1658126984584',
    'Host': 'fanyi.youdao.com',
    'Origin': 'https://fanyi.youdao.com',
    'Referer': 'https://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
}
word = input('请输入翻译的内容:')

with open('有道.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

# 编译js代码
compile_result = execjs.compile(js_code)
print(compile_result)
# 调用js代码
result = compile_result.call('youdao', word)
print(result)
data = {
    "i": word,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    # "salt": "16581193003738",
    # "sign": "4a9ab64eb3a27b25a2574875ca46f100",
    # "lts": "1658119300373",
    # "bv": "bdc0570a34c12469d01bfac66273680d",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTlME",
}
data.update(result)
print(data)
# requests.post(url)
resp = requests.post(url, headers=headers, data=data)
print(resp.json())

