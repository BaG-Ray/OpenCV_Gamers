# -*- encoding=utf8 -*-
#   Version = 1.0
#   UpdateTime = 2023-07-14

# ----------------------------------1.0更新---------------------------------------------------
# UpdateTime = 2023-07-14
# 将原有模块进行拆分，方便后续的维护，以及当前界面的更好的识别

__author__ = "BaG-Ray+"

# ----------------------------------引用部分（此部分所有脚本都一样，不需要修改）--------------------------------------------

from airtest.core.api import *

# 引入默认类脚本
import Default_Scripts
import LegenClover_Class

# ----------------------------------变量部分（需要改）--------------------------------------------

# ------------------------------------以下为图片----------------------------------------------

# -------------------------------------以下为坐标-----------------------------------------------

Check_Game_Mode_Coordinate = (1117, 521)

Check_Button_Skip_Coordinate = (1357, 903)

Button_Skip_Coordinate = Check_Button_Skip_Coordinate

Quest_Sub_10_Coordinate = (1471, 730)

Quest_Sub_1_Coordinate = (464, 581)
Quest_Sub_2_Coordinate = (714, 311)
Quest_Sub_3_Coordinate = (953, 581)
Quest_Sub_4_Coordinate = (1198, 298)
Quest_Sub_5_Coordinate = (1438, 581)
Quest_Sub_6_Coordinate = (1685, 309)
Quest_Sub_7_Coordinate = (1930, 584)

Sub_Left_Coordinate = (71, 144)

# --------------------------------------以下为变量--------------------------------------------

Sub_List = [
    Quest_Sub_1_Coordinate,
    Quest_Sub_2_Coordinate,
    Quest_Sub_3_Coordinate,
    Quest_Sub_4_Coordinate,
    Quest_Sub_5_Coordinate,
    Quest_Sub_6_Coordinate,
    Quest_Sub_7_Coordinate,
    Sub_Left_Coordinate
]

# --------------------------------------以下为RGB参数--------------------------------------------

Check_Game_Mode_Coordinate_Sub_RGB = (85, 106, 111)
Check_Game_Mode_Coordinate_Kuest_RGB = (156, 86, 255)

Check_Game_Mode_Coordinate_Sub_Decision_RGB = (238, 238, 238)
Check_Game_Mode_Coordinate_Quest_RGB = (205, 186, 171)
Check_Game_Mode_Coordinate_Result_RGB = (243, 225, 203)

Check_Button_Coordinate_RGB = (255, 225, 173)

# ----------------------------------基础程序部分（此部分所有游戏一致，不需要更改）--------------------------------------------


# ----------------------------------以下为启动部分--------------------------------------------

Game_Name = "com.dmm.games.legeclo"
LegendCloverScriptsClass = Default_Scripts.OpencvGame(Game_Name)
LegendCloverVariable = LegenClover_Class.Universal_Variable()
LegenCloverQuest = LegenClover_Class.Quest()


# -----------------------------以下为各游戏的不同部分--------------------------------------------

# 本程序用来判断当前还有多少体力
def Get_Stamina():
    Ocr_Text = LegendCloverScriptsClass.Pic_Ocr_Shape(1140, 63, 1285, 15)
    Ocr_Text_List = Ocr_Text.split('/')
    Stamina = Ocr_Text_List[0]
    return int(Stamina)


# 本程序用来判断该关卡是否需要执行
def Check_Quest_Status():
    Quest_Status = LegendCloverScriptsClass.Get_Pixel_Rgb(Check_Button_Skip_Coordinate)
    if Quest_Status == Check_Button_Coordinate_RGB:
        print("需要执行")
        return 0

    else:
        print("已经执行")
        return 1


# 本程序用来执行Sub的关卡
def Sub_Quest(Quest_Num):
    touch(Sub_List[Quest_Num])


def Check_Game_Mode(Ocr_Text, Game_Process, Game_Mode_RGB):
    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Sub_RGB:
        print("当前在Sub总界面")
        return 0

    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Sub_Decision_RGB:
        print("当前在Sub选择关卡界面")
        return 1

    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Quest_RGB:
        print("当前在Sub关卡界面")
        return 2

    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Result_RGB:
        print("当前在领取奖励界面")
        return 3

    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Kuest_RGB:
        print("当前在Quest界面")
        return 4


def Sub(Game_Process):
    Sub_Count = 0

    # 若目前不在主界面，证明脚本衔接之间出现了问题。
    # 因此将“Game_Process”原路返还，从哪来的回哪去，重新执行一遍前置脚本
    if LegendCloverScriptsClass.Get_Pixel_Rgb(Check_Game_Mode_Coordinate) != Check_Game_Mode_Coordinate_Sub_RGB:
        return Game_Process

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
            # Sub关卡选择第几部
            # 直接进入第十部
            touch(Quest_Sub_10_Coordinate)
            continue

        # 表明此时在关卡选择界面
        # 此时情况复杂
        # 如果是第一次进入，则需要打一关后退出Sub界面，回到主菜单一次
        # 这里的随机打就打第十部的第六个关卡吧
        if Game_Mode == 1:
            if Game_Process == 5:
                touch(Quest_Sub_6_Coordinate)
                sleep(2)
                if LegendCloverScriptsClass.Get_Pixel_Rgb(
                        Check_Game_Mode_Coordinate) == Check_Game_Mode_Coordinate_Quest_RGB:
                    Game_Process = 6
                continue

            # 表明此时已经执行过一次了
            # 这里返回Quest界面先
            if Game_Process == 6:
                touch(LegendCloverVariable.Quest_Coordinate)
                continue

            # 表明此时已经第二次了
            #
            if Game_Mode == 7:
                Stamina = Get_Stamina()
                if Stamina >= 10:
                    touch(Sub_List[Sub_Count])
                    Sub_Count = Sub_Count + 1
                    if Sub_Count == 8:
                        Sub_Count = 0
                else:
                    touch(LegendCloverVariable.Quest_Coordinate)
                    Game_Process = Game_Process + 1

        # 表明此时在关卡界面
        # 首先需要判断是否已经执行
        # 没有则执行
        # 有则返回,随便点击即可
        # 这里点击左键
        if Game_Mode == 2:
            Quest_Status = Check_Quest_Status()
            if Quest_Status == 0:
                touch(Check_Button_Skip_Coordinate)
                continue
            else:
                touch(Sub_Left_Coordinate)
                continue

        # 表明此时已经奖励领取完成
        # 随便点击即可，这里依旧点击左键
        if Game_Mode == 3:
            touch(Sub_Left_Coordinate)
            continue

        # 此时已经在Quest界面
        # 执行返回主界面的操作
        if Game_Mode == 4:
            return Game_Process

# ------------------------Test----------------------------------------------\
# print(LegendCloverScriptsClass.Get_Pixel_Rgb(Check_Game_Mode_Coordinate))
# Sub(0)
# LegendCloverScriptsClass.CV2_Circle_Pic(Check_Game_Mode_Coordinate)
# touch(Check_Button_Finish_Coordinate)
# print(Get_Stamina())
