#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 15:50
# @Author  : WangYuan
# @Site    : 
# @File    : auto_five.py
# @Software: PyCharm

import pytesseract
from PIL import ImageGrab, Image
import time
from screenshot import *
from find_imag_adb import *
import win32api
import win32con
import win32gui

adb = auto_adb()


def move_base(x,y=0.1,delay = 0.5):
    #如果x输入的是一个元组
    if type(x) == tuple:
        a = x[0]
        b = x[1]
    else:
        # a = (1920 - window_origin[0]) * x + window_origin[0]
        # b = (window_max[1] - window_origin[1]) * y + window_origin[1]
        a = x
        b = y
    time.sleep(delay)
    cmd = 'shell input tap {x1} {y1} '.format(
        x1=a,
        y1=b,
    )
    # 打开大地图
    adb.run(cmd)


def find_task(): #判断是否找到侍卫
    not_find = True
    while not_find:
        find_result = MatchImg('element/TaskButton1.png', (0, 0, window_max[0], window_max[1]),0.5).is_match()
        if find_result:
            not_find = False
            return find_result


def find_and_click(src,x=0,y=0.9):
    time.sleep(0.5)
    find_img = MatchImg(src,x,y).is_match()
    print(find_img)
    move_base(find_img['result'],0,0.2)

def is_find(src):
    is_img = MatchImg(src).is_match()
    if is_img:
        return True
    else:
        return False

def Recieve_mission():
    find_and_click('element/big_map.png',0,0.1) #打开大地图
    move_base(0.287, 0.503)# 打开宝象国地图
    move_base(0.276, 0.888)# 打开人物筛选
    move_base(0.263, 0.711)# 选择任务
    move_base(0.276, 0.888)# 关闭人物筛选
    move_base(0.364, 0.596) # 降魔侍卫
    print("this ok")
    find_and_click('element/map_close.png',0,0.8)  # 关闭对话框
    Rm_result = find_task()
    move_base(Rm_result['result'])# 领取任务
    find_and_click('element/Close.png')  #关闭对话框
    find_and_click('element/props.png') #打开道具
    move_base(0.576, 0.242) #打开任务道具栏

    if is_find('element/Transferbook.png'): #看看有没有传送卷轴
        if is_find('element/magnifier.png'): #这段后期改为锁妖网
            find_and_click('element/Close.png')  # 关闭对话框
        else: #不是锁妖任务，随便杀
            find_and_click('element/Close.png')  # 关闭对话框
            find_and_click('element/Task.png',0,0.8)  #打开任务栏

    else:
        find_and_click('element/Close.png')
        #以下内容仅为测试能否跑通
        find_and_click('element/Task.png', 0, 0.8)  # 打开任务栏

        pass #还没想好


#使用传送工具，重新领任务
def Recieve_again():


    move_base(0.871,0.936)# 打开任务栏
    move_base(0.617,0.263)# 打开任务道具
    move_base(0.837,0.468)# 选择任务道具
    move_base(0.738, 0.48)# 使用任务道具
    move_base(0.497, 0.162) # 冗余
    move_base(0.865, 0.167) #关闭道具栏
    move_base(0.11, 0.136) # 选择宝象国地图

    move_base(0.29, 0.801)  # 打开人物筛选
    move_base(0.307, 0.677)  # 选择任务
    move_base(0.29, 0.801)  # 关闭人物筛选
    move_base(0.41, 0.571)  # 降魔侍卫
    move_base(0.852, 0.368, 3)  # 领取任务

def return_position():
    time.sleep(1)
    print(autopy.mouse.location()[0])
    print(autopy.mouse.location()[1])


#位置捕捉 文字识别
def position_grab():
    #计算相对位置
    start_x = 0.09 * float(window_max[0])
    start_y = 0.09 * float(window_max[1])
    end_x =  0.150 * float(window_max[0])
    end_y =  0.164 * float(window_max[1])

    img = ImageGrab.grab([start_x,start_y, end_x,end_y])
    img.show()
    text1 = pytesseract.image_to_string(img,lang='num')  # 训练的数字库
    print(text1)

def let_start():
    global window_max,window_origin

    window_max ,window_origin = [],[]

    Descartes0 = MatchImg('element/Benchmark1.png')
    benchmark0 = Descartes0.is_match()['result']
    Descartes1 = MatchImg('element/Benchmark.png')
    benchmark1 = Descartes1.is_match()['result']

    window_origin.append(benchmark0[0])
    window_origin.append(benchmark0[1])
    window_max.append(benchmark1[0])
    window_max.append(benchmark1[1])
    print(window_max,window_origin)

if __name__ == '__main__':
    # let_start()
    # find_and_click('element/sign.png')
    Recieve_mission()


# 959
# 539