import os

import requests
import re

index_url = 'https://e1.monidai.com/ppvod/29BC7D1EDE4BA87EB5D23DB76530DAA7.m3u8'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'referer': 'https://z1.m1907.cn/'
}
res = requests.get(index_url, headers=headers).text
p = re.sub(r'#.*\n', '', res)
s = re.findall('https://.*', p)
num = 0
for i in s:
    num += 1
    video_download = requests.get(i, headers=headers)
    with open('ts_video/%s.ts' % num, 'wb') as f:
        f.write(video_download.content)
        print('下载中:', num)
print('下载完毕')

