import requests
import base64
import cv2
import numpy as np

img = cv2.imread('pan2.jpg')
url = 'http://192.168.43.242:8080/extraction/logo'
string = base64.b64encode(cv2.imencode('.jpg', img)[1]).decode()
data = {'image': string}

res = requests.post(url, json=data).json()


for i in res:
    string = i['image']
    jpg_original = base64.b64decode(string)
    jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
    img = cv2.imdecode(jpg_as_np, flags=1)
    cv2.imshow('image', img)
    cv2.waitKey(0)