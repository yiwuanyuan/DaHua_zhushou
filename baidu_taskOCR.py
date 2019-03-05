#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : baidu_taskOCR.py
# Author: Wangyuan
# Date  : 2019/3/4


# client_id 为官网获取的AK， client_secret 为官网获取的SK
# client_id = c7fb3ccb66804c938b48e569bc22c150
# client_secret = edd476453cec436c95a85ce941f65932
import requests
import base64


class Orc_main():
    def orc_look(self, path):
        access_token = "24.76859abcf4836e5c6da0994d1f1fc43c.2592000.1554338131.282335-15677860"  # 自行注册百度云账号，即可获取自己专属的access_token，必须输入！
        with open(path, 'rb') as f:
            image_data = f.read()
            base64_ima = base64.b64encode(image_data)
            data = {
                'image': base64_ima
            }
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=" + str(access_token)
            r = requests.post(url, params=headers, data=data).json()
            for word in r['words_result']:
                yield word['words']
            # 返回一个生成器，可自行修改


if __name__ == '__main__':
    om = Orc_main()
    path = "element/test.png"  # 图片文件路径，必须输入！
    words = om.orc_look(path)
    # 输出文字(返回结果)
    for word in words:

        print(word)
