# ----------------------------------引用部分（此部分所有脚本都一样，不需要修改）--------------------------------------------
# -*- encoding=utf8 -*-
# Version = 1.0
# UpdateTime = 2023-07-13

#################################1.0更新###################################
# UpdateTime = 2023-07-13
# 大规模重新整合OpenCV_Gamers的程序框架，优化后续

__author__ = "BaG-Ray+"

import cv2
import pytesseract
from PIL import Image
from airtest.core.api import *


# ----------------------------------基础程序部分（此部分所有游戏一致，不需要更改）----------------------------------------------

# 未裁剪的图片，也就是还没有打开过的图片就用这个来读取ocr,此时读取的应该是全地址。更改为判断游戏状态相关
def Pic_Ocr_Unshape(self):
    snapshot(filename='Game_Pic.jpg')
    Pic_Dir = self.Log_Dir + '/Game_Pic.jpg'
    Ocr_Pic = Image.open(Pic_Dir)
    Ocr_Text = pytesseract.image_to_string(Ocr_Pic, lang='jpn')
    return Ocr_Text


def Remove_Temp_File(self):
    for root, dirs, files in os.walk(self.Log_Dir, topdown=False):
        for name in files:
            try:
                os.remove(os.path.join(root, name))
            except:
                continue


def Exit_Game(self):
    print("游戏结束，退出游戏")
    stop_app(self.Game_Name)
    self.Remove_Temp_File()
    exit()


def Get_Pixel_Rgb(self, Coordinate):
    snapshot(filename='Game_Pic.jpg')
    Pic_Dir = self.Log_Dir + '/Game_Pic.jpg'
    Img_Pic = Image.open(Pic_Dir)
    r, g, b = Img_Pic.getpixel(Coordinate)
    return r, g, b


def Pic_Ocr_Shape(self, x1, y1, x2, y2):
    xx1 = min(x1, x2)
    xx2 = max(x1, x2)
    yy1 = min(y1, y2)
    yy2 = max(y1, y2)

    snapshot(filename='Game_Pic.jpg')
    Pic_Dir = self.Log_Dir + '/Game_Pic.jpg'
    Ocr_Pic = cv2.imread(Pic_Dir)
    Ocr_Auto_Pic = Ocr_Pic[yy1:yy2, xx1:xx2]
    Ocr_Text = pytesseract.image_to_string(Ocr_Auto_Pic, lang='eng')
    return Ocr_Text


def CV2_Show_Pic(self, Pic_Data):
    cv2.namedWindow("image")  # 创建一个image的窗口
    cv2.imshow("image", Pic_Data)  # 显示图像
    cv2.waitKey()  # 默认为0，无限等待


def CV2_Circle_Pic(self, Pic_Dir, Coordinate):
    # 此函数用于在截图上显示点
    Cv2_Img = cv2.imread(Pic_Dir)
    Cv2_Circle = cv2.circle(Cv2_Img, Coordinate, 5, (255, 0, 255), -1)
    CV2_Circle_Resize = cv2.resize(Cv2_Circle, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
    self.CV2_Show_Pic(CV2_Circle_Resize)
