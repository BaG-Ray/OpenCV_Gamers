#----------------------------------引用部分（此部分所有脚本都一样，不需要修改）--------------------------------------------
# -*- encoding=utf8 -*-
#Version = 2.1

__author__ = "Ray"

import os
import shutil

import cv2
import pytesseract
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from PIL import Image

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["ios:///http+usbmux://00008020-001318C00A91002E",])

from poco.drivers.ios import iosPoco

poco = iosPoco()

#----------------------------------变量部分（需要改）--------------------------------------------

#-----以下为基础部分--------

Log_Dir = './ShinyColors/log'
Game_Name = "jp.co.bandainamcoent.BNEI0354"
Game_Process = 0

#----以下为图片--------------

#----以下为坐标--------------

#----以下为变量--------------


#----------------------------------基础程序部分（此部分所有游戏一致，不需要更改）--------------------------------------------

#未裁剪的图片，也就是还没有打开过的图片就用这个来读取ocr,此时读取的应该是全地址。更改为判断游戏状态相关
def Pic_Ocr_Unshape():
    snapshot(filename = 'Game_Pic.jpg')
    Pic_Dir = Log_Dir + '/Game_Pic.jpg'
    Ocr_Pic = Image.open(Pic_Dir)
    Ocr_Text = pytesseract.image_to_string(Ocr_Pic, lang='jpn')
    return(Ocr_Text)

def Remove_Temp_File():
    for root, dirs, files in os.walk(Log_Dir, topdown=False):
        for name in files:
            try:
                os.remove(os.path.join(root, name))
            except:
                continue

def Exit_Game():
    print("游戏结束，退出游戏")
    stop_app(Game_Name)
    Remove_Temp_File()
    exit()

def Get_Pixel_Rgb(Coordinate):
    snapshot(filename = 'Game_Pic.jpg')
    Pic_Dir = Log_Dir + '/Game_Pic.jpg'
    Img_Pic = Image.open(Pic_Dir)
    r, g, b = Img_Pic.getpixel(Coordinate)
    return (r,g,b)

def Pic_Ocr_Shape(x1,y1,x2,y2):
    if x1 < x2:
        xx1 = x1
        xx2 = x2
    else:
        xx1 = x2
        xx2 = x1
    if y1 < y2:
        yy1 = y1
        yy2 = y2
    else:
        yy1 = y2
        yy2 = y1

    snapshot(filename = 'Game_Pic.jpg')
    Pic_Dir = Log_Dir + '/Game_Pic.jpg'
    Ocr_Pic = cv2.imread(Pic_Dir)
    Ocr_Auto_Pic = Ocr_Pic[yy1:yy2,xx1:xx2]  
    Ocr_Text = pytesseract.image_to_string(Ocr_Auto_Pic, lang='eng')
    return(Ocr_Text)

#-----------------------------以下为各游戏的不同部分--------------------------------------------


def Check_Game_Mode(Ocr_Text):
    if "" in Ocr_Text:
        return 

#----------------------------------主程序部分(不需要更改)--------------------------------------------
        
    
if __name__ == '__main__':
    start_app(Game_Name)
    while True:
        
        Game_Ocr_Text = Pic_Ocr_Unshape()
        try:
            print(Game_Ocr_Text)
        except:
            pass
        Game_Mode = Check_Game_Mode(Game_Ocr_Text)

#--------------------------------以下部分为主程序中的专属部分-----------------------------


