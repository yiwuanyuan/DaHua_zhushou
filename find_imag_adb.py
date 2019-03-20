# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # File  : find_imag.py
# # Author: Wangyuan
# # Date  : 2019/3/4
#
import aircv as ac
import cv2
import autopy
import time
from screenshot import *
from PIL import Image
import numpy as np
from PIL import ImageGrab

class MatchImg:  # imgsrc=原始图像，imgobj=待查找的图片

    def __init__(self,imgobj,x=0,confindencevalue = 0.9):
        if type(x) == str:
            imm = ac.imread(x)
        else:
            im = pull_screenshot()
            imm = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)

        self.imsrc = imm
        self.imobj = ac.imread(imgobj)
        self.Criterion = confindencevalue

    def is_match(self):
        match_result = ac.find_template(self.imsrc, self.imobj)
        if match_result is not None:
            match_result['shape'] = (self.imsrc.shape[1], self.imsrc.shape[0])  # 0为高，1为宽
            if match_result['confidence'] < self.Criterion:
                return False
            else:
                return match_result
        else:
            return False




if __name__ == '__main__':
    example = MatchImg('element/big_map.png','autojump.png',0.1)
    print(example.is_match())



