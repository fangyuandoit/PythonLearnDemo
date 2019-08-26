import requests

headers = {
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
url = "http://upos-hz-mirrorks3u.acgvideo.com/dspxcode/m190826wsc4nkz4dyr3k519f8uae10j5-1-56.mp4?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfq99M=&uipk=5&nbs=1&deadline=1566835480&gen=playurl&os=ks3u&oi=2874709328&trid=1214a838debd482e8e40c4b00d7fbf7as&platform=html5&upsig=a42b647b9871d1d1d94fe64f2503314c&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=0&wsTime=1566835480"

chunk_size = 1024  # 每次下载的数据大小
response = requests.get(url, headers=headers, stream=True)
with open("video.mp4", 'wb') as file:
    for data in response.iter_content(chunk_size=chunk_size):
        file.write(data)