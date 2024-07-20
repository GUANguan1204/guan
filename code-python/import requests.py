import requests
url="https://v2.kwaicdn.com/ksc2/Y8I_Vn7OPUmqXdTk-vMPi1vY_Y3ooSZleCpgvstBzyQg98TWG6ifA4ruKHttgVuUhFC6fdx2e7Z2jM0TBtTg9a_-bmMxYonxg4d8D_kY-wpYQsPUC1Mqunv8WWOKSWeQ0LBh2gu6RyJdxx8B-VXFu-ftr5b2q5gTJUhndxGpl-Y7G24L3c5o54B9s6C2iqr8.mp4?pkey=AAVMIHmD-qZ5BPSf4B4mg3q8v4AvlMbg15rttyIIJv9YOkIz0lz7VBTq7mmB00avZdTnYA0X_t14txB5gezVEaEfQ-LkWuuF1RmjRMttc6w0hKBFHqrG_5rU0-mJjoSqBmI&tag=1-1721394279-unknown-0-y6z9yfc4xo-a3e81e640c204ca3&clientCacheKey=3xp6sva3rip6qd2_b.mp4&di=JAiCGj0RIAAAAAAAAAAAAg==&bp=10004&tt=b&ss=vp"
res = requests.get(url)
#print(res.status_code)#网址响应
#print(res.content)#得到的视频数据
open("视频.mp4","wb").write(res.content)