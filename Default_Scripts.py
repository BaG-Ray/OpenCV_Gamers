# ----------------------------------引用部分（此部分所有脚本都一样，不需要修改）--------------------------------------------
# -*- encoding=utf8 -*-
# Version = 3.0
# UpdateTime = 2023-07-13

#################################2.4更新###################################
# UpdateTime = 2023-05-18
# 添加了CV2_Circle_Pic函数，此函数可以用来时间截图中的坐标标点

#################################3.0更新###################################
# UpdateTime = 2023-07-13
# 本次在优化后，将之前的版本调整为类的模式，方便其他程序直接调用即可

__author__ = "BaG-Ray+"

import os
import shutil

import cv2
import pytesseract
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from PIL import Image


class OpencvGame:

    if not cli_setup():
        auto_setup(__file__, logdir=True,
                   devices=["android://127.0.0.1:5037/aqwkhy95by4tgikb?cap_method=MINICAP&touch_method=MAXTOUCH&", ])

    from poco.drivers.ios import iosPoco

    poco = iosPoco()

    # ----------------------------------变量部分（需要改）--------------------------------------------

    # -----以下为基础部分--------

    Log_Dir = ''
    Game_Name = ""
    Game_Process = 0

    # ----以下为图片--------------

    # ----以下为坐标--------------

    # ------RGB颜色判定------------

    Check_Game_Mode_RGB_Coordinate = ()

    # ----以下为变量--------------

    # ----------------------------------基础程序部分（此部分所有游戏一致，不需要更改）--------------------------------------------

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

    # -----------------------------以下为各游戏的不同部分--------------------------------------------

    def Check_Game_Mode(self, Ocr_Text):
        if "" in Ocr_Text:
            return

        # ----------------------------------主程序部分(不需要更改)--------------------------------------------

    if __name__ == '__main__':
        start_app(Game_Name)
        while True:

            Game_Ocr_Text = Pic_Ocr_Unshape()
            Game_Mode_RGB = Get_Pixel_Rgb(Check_Game_Mode_RGB_Coordinate)

            try:
                print(Game_Ocr_Text)
            except:
                pass

            print(Game_Mode_RGB)

            Game_Mode = Check_Game_Mode(Game_Ocr_Text)

    # --------------------------------以下部分为主程序中的专属部分-----------------------------
