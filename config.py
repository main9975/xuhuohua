import os
import json

def get_config():
    with open('cookies.json','r') as f:
        cookies = f.read()
        # print(cookies)
    nickname = os.getenv("NICKNAME")
    msg = os.getenv("MSG","火花")
    proxy = os.getenv("PROXY")

    if proxy == '':
        proxy = None

    if cookies == '' or nickname == '':
        raise ValueError("SECRETS 未正确配置！")

    return {
        'cookies' : cookies,
        'nickname' : nickname,
        'msg' : msg,
        'proxy' : proxy
    }