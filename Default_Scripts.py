# -*- encoding=utf8 -*-
# Version = 3.4
# UpdateTime = 2023-09-23

# ----------------------------------2.4更新---------------------------------------------------
# UpdateTime = 2023-05-18
# 添加了CV2_Circle_Pic函数，此函数可以用来时间截图中的坐标标点

# ----------------------------------3.0更新---------------------------------------------------
# UpdateTime = 2023-07-13
# 本次在优化后，将之前的版本调整为类的模式，方便其他程序直接调用即可

# ----------------------------------3.1更新---------------------------------------------------
# UpdateTime = 2023-07-16
# 不知道为什么pillow和opencv在读取图片上出现了冲突，可能换了pycharm的原因吧
# 因此，在此将全部调整为opencv的模式

# ----------------------------------3.2更新---------------------------------------------------
# UpdateTime = 2023-07-18
# 修复CV2_Circle_Pic的bug
# 再次注意，所有的坐标务必确认

# ----------------------------------3.3更新---------------------------------------------------
# UpdateTime = 2023-07-21
# 将图片质量拉到最大，试下能否解决每次RGB值都在变化的问题

# ----------------------------------3.4更新---------------------------------------------------
# UpdateTime = 2023-09-23
# 将数字OCR添加了通过坐标的方式

__author__ = "BaG-Ray+"

# ----------------------------------引用部分（此部分所有脚本都一样，不需要修改）--------------------------------------------

import cv2
import pytesseract
from airtest.cli.parser import cli_setup
from airtest.core.api import *


class OpencvGame:
    # ----------------------------------变量部分（需要改）--------------------------------------------

    # -----以下为基础部分--------

    Log_Dir = '../log'
    Game_Name = ""
    Check_Game_Mode_RGB_Coordinate = []

    def __init__(self, Game_Name):
        self.Game_Name = Game_Name

        print(os.getcwd())

        if not cli_setup():
            auto_setup(__file__, logdir=True,
                       devices=[
                           "android://127.0.0.1:5037/aqwkhy95by4tgikb?cap_method=MINICAP&touch_method=MAXTOUCH&", ])

        start_app(self.Game_Name)

    # ----------------------------------基础程序部分（此部分所有游戏一致，不需要更改）--------------------------------------------

    # 未裁剪的图片，也就是还没有打开过的图片就用这个来读取ocr,此时读取的应该是全地址。更改为判断游戏状态相关
    def Snap_Read_Pic(self):
        # self.Remove_Temp_File()
        snapshot(filename='Game_Pic.jpg', quality=99)
        Pic_Dir = self.Log_Dir + '/Game_Pic.jpg'
        Ocr_Pic = cv2.imread(Pic_Dir)
        return Ocr_Pic

    def Pic_Ocr_Unshape(self):
        Ocr_Pic = self.Snap_Read_Pic()
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
        # self.Remove_Temp_File()
        exit()

    def Get_Pixel_Rgb(self, Coordinate):
        Img_Pic = self.Snap_Read_Pic()
        [b, g, r] = Img_Pic[Coordinate[1], Coordinate[0]]
        # self.CV2_Circle_Pic(Coordinate)
        return r, g, b

    def Pic_Ocr_Shape(self, x1, y1, x2, y2):

        xx1 = min(x1, x2)
        xx2 = max(x1, x2)
        yy1 = min(y1, y2)
        yy2 = max(y1, y2)

        Ocr_Pic = self.Snap_Read_Pic()
        Ocr_Auto_Pic = Ocr_Pic[yy1:yy2, xx1:xx2]
        self.CV2_Show_Pic(Ocr_Auto_Pic)
        Ocr_Text = pytesseract.image_to_string(Ocr_Auto_Pic, lang='eng',
                                               config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789/')
        return Ocr_Text

    def Pic_Ocr_Shape_Coordinate(self, Coordinate1, Coordinate2):

        x1 = Coordinate1[0]
        y1 = Coordinate1[1]
        x2 = Coordinate2[0]
        y2 = Coordinate2[1]

        xx1 = min(x1, x2)
        xx2 = max(x1, x2)
        yy1 = min(y1, y2)
        yy2 = max(y1, y2)

        Ocr_Pic = self.Snap_Read_Pic()
        Ocr_Auto_Pic = Ocr_Pic[yy1:yy2, xx1:xx2]
        self.CV2_Show_Pic(Ocr_Auto_Pic)
        Ocr_Text = pytesseract.image_to_string(Ocr_Auto_Pic, lang='eng',
                                               config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789/')
        return Ocr_Text

    def CV2_Show_Pic(self, Pic_Data):
        cv2.imshow("image", Pic_Data)  # 显示图像
        cv2.waitKey(0)

    def CV2_Circle_Pic(self, Coordinate):
        # 此函数用于在截图上显示点
        Cv2_Img = self.Snap_Read_Pic()
        Cv2_Circle = cv2.circle(Cv2_Img, Coordinate, 5, (255, 0, 255), -1)
        CV2_Circle_Resize = cv2.resize(Cv2_Circle, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
        self.CV2_Show_Pic(CV2_Circle_Resize)

    # -----------------------------以下为各游戏的不同部分--------------------------------------------
