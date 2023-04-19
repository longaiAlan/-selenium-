# encoding:utf-8

import requests
import re
import json
import pprint
import subprocess

url = 'https://www.bilibili.com/video/BV1yK41127zY'
headers = {
    'referer': 'https://search.bilibili.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
# print(response.text)
# 标题
title = re.findall('<h1 title="(.*?)" class="video-title tit">.*?</h1>', response.text)[0]
# url所在的位置
data_text = re.findall('<script>window.__playinfo__=(.*?)</script>', response.text)[0]
print(title)
json_data = json.loads(data_text)
# pprint.pprint(json_data)
# 音频url
audio = json_data['data']['dash']['audio'][0]['baseUrl']
# 视频url
video = json_data['data']['dash']['video'][0]['baseUrl']
print(audio)
print(video)

audio_data = requests.get(url=audio, headers=headers).content
video_data = requests.get(url=video, headers=headers).content
with open('video\\'+title + '.mp3', mode='wb') as f:
    f.write(audio_data)
with open('video\\'+title + '.mp4', mode='wb') as f:
    f.write(video_data)
# 合成音频+视频
COMMAND = f'E:\DELL\Downloads\\ffmpeg-N-110315-g0b0fa5c2a8-win64-gpl-shared\\bin\\ffmpeg -i video\\{title}.mp4 -i video\\{title}.mp3 -c:v copy -c:a aac -strict experimental video\\{title}output.mp4'
subprocess.run(COMMAND, shell=True)
