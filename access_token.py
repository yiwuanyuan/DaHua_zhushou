#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : access_token.py
# Author: Wangyuan
# Date  : 2019/3/4

import urllib, sys
import urllib.request
import urllib.request
import ssl

# client_id 为官网获取的AK， client_secret 为官网获取的SK
# client_id = c7fb3ccb66804c938b48e569bc22c150
# client_secret = edd476453cec436c95a85ce941f65932
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=FOAcdPkEPY1atztdPNKIiegd&client_secret=SMIfVRSoU1csmcZ7LYwIGB28FXRrlegw'
request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
print(response)
content = response.read()
if (content):
    print(content)
