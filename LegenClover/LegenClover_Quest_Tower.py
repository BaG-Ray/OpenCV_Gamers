# -*- encoding=utf8 -*-
#   Version = 1.0
#   UpdateTime = 2023-07-17

# ----------------------------------1.0更新---------------------------------------------------
# UpdateTime = 2023-07-17
# 将原有模块进行拆分，方便后续的维护，以及当前界面的更好的识别
# 理论上该脚本应该不再需要更新，除非大版本更新

__author__ = "BaG-Ray+"

# ----------------------------------引用部分（此部分所有脚本都一样，不需要修改）--------------------------------------------

from airtest.core.api import *

# 引入默认类脚本
import Default_Scripts
import LegenClover_Class

# ----------------------------------变量部分（需要改）--------------------------------------------

# ------------------------------------以下为图片----------------------------------------------

# -------------------------------------以下为坐标-----------------------------------------------

Check_Game_Mode_Coordinate = (2276, 153)

Button_Skip_Coordinate = (1810, 843)

# --------------------------------------以下为变量--------------------------------------------


# --------------------------------------以下为RGB参数--------------------------------------------

Check_Game_Mode_Coordinate_Tower_RGB = (243, 224, 209)
Check_Game_Mode_Coordinate_Quest_RGB = (207, 170, 141)

Check_Game_Mode_Coordinate_IsSkip_RGB = (118, 122, 99)

Check_Button_SKip_Coordinate_RGB = (239, 209, 136)

# ----------------------------------基础程序部分（此部分所有游戏一致，不需要更改）--------------------------------------------


# ----------------------------------以下为启动部分--------------------------------------------

Game_Name = "com.dmm.games.legeclo"
LegendCloverScriptsClass = Default_Scripts.OpencvGame(Game_Name)
LegendCloverVariable = LegenClover_Class.Universal_Variable()


# -----------------------------以下为各游戏的不同部分--------------------------------------------


def Check_Game_Mode(Ocr_Text, Game_Process, Game_Mode_RGB):
    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Tower_RGB:
        print("霸者之塔界面")
        return 0

    # 这里表明两种情况，一种是确认跳过，或者是已经领取完成
    if Game_Mode_RGB == Check_Game_Mode_Coordinate_IsSkip_RGB:
        if "結果" in Ocr_Text:
            print("勇者之塔跳过完成")
            return 2

        else:
            print("确认跳过勇者之塔")
            return 1

    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Quest_RGB:
        # 勇者之塔脚本执行完成
        print("当前在Quest界面")
        return 3


def Tower(Game_Process):
    while True:

        Game_Ocr_Text = LegendCloverScriptsClass.Pic_Ocr_Unshape()
        try:
            print(Game_Ocr_Text)
        except:
            pass

        Game_Mode_RGB = LegendCloverScriptsClass.Get_Pixel_Rgb(Check_Game_Mode_Coordinate)
        print(Game_Mode_RGB)

        Game_Mode = Check_Game_Mode(Game_Ocr_Text, Game_Process, Game_Mode_RGB)
        print(Game_Mode)

        # --------------------------------以下部分为主程序中的专属部分-----------------------------

        # ------------------------    测试代码可在上面写,下面为正式代码----------------------------

        if Game_Mode == 0:
            # 霸者之塔界面
            # 检测是否需要执行勇者之塔
            Button_Skip_Coordinate_RGB = LegendCloverScriptsClass.Get_Pixel_Rgb(Button_Skip_Coordinate)

            if Button_Skip_Coordinate_RGB == Check_Game_Mode_Coordinate_Tower_RGB:
                # 需要执行勇者之塔
                touch(Button_Skip_Coordinate)
                sleep(1)
                continue
            else:
                # 表明不需要执行勇者之塔，或者说已经执行完成了
                # 返回Quest界面
                touch(LegendCloverVariable.Quest_Coordinate)
                continue

        if Game_Mode == 1:
            # 确认跳过勇者之塔
            # 这里点击的按键和有两个按键的ok键相同
            touch(LegendCloverVariable.OK_Two_Button_Coordinate)
            sleep(5)
            continue

        if Game_Mode == 2:
            # 确认结果
            # 随便点击任何位置即可，这里点击监测点
            touch(Check_Game_Mode_Coordinate)
            continue

        if Game_Mode == 3:
            # 勇者之塔脚本执行完成，返回Quest脚本
            Game_Process = 4
            return Game_Process

# -----------------------------------测试部分--------------------------------------------
