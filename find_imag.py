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
from PIL import Image
import numpy as np
from PIL import ImageGrab

class MatchImg:  # imgsrc=原始图像，imgobj=待查找的图片

    def __init__(self,imgobj,x=0,confindencevalue = 0.9):
        if type(x) == str:
            imm = ac.imread(x)
        else:
            if x ==0 :
                im = ImageGrab.grab()
            else:
                im = ImageGrab.grab(x)
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
    # example = MatchImg('element/TaskButton1.png',0,0.1)
    # print(example.is_match())

    not_find = True
    while not_find:
        autopy.mouse.move(158,285)
        autopy.mouse.toggle(button=autopy.mouse.Button.LEFT,down=True)
        autopy.mouse.smooth_move(158, 184)
        autopy.mouse.toggle(button=autopy.mouse.Button.LEFT, down=False)
        time.sleep(3)
        example = MatchImg('element/test01.png', 0, 0.1).is_match()
        if  not example:
            pass
        else:
            not_find = True
            print(example)

    # for i in range(3000):
    #
    #     try:
    #
    #         autopy.mouse.move(0, i)
    #
    #         k = i
    #
    #     except ValueError:
    #
    #         break
    #
    # print(k)