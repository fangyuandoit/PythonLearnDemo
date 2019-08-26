
import requests

html = requests.get("http://i0.hdslb.com/bfs/face/cfc95dc3c11b4d2289a352ea14c895bf348a5829.jpg",stream=True)
# html = requests.get("https://pic.cnblogs.com/face/1492800/20181209120930.png",stream=True)

file = open("demo1.png", "wb")
file.write(html.content)
file.close()
