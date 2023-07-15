# -*- encoding=utf8 -*-
#   Version = 1.0
#   UpdateTime = 2023-07-14
#   本脚本为LegenClover的Quest界面，通过此界面联系各个战斗关卡
#   为先运行勇者之塔，然后Main,最后Sub关卡有两种情况需要执行
#   目前尚未想到有什么好的方法处理活动界面，先搁置

# ----------------------------------1.0更新---------------------------------------------------
# UpdateTime = 2023-07-14
# 将原有模块进行拆分，方便后续的维护，以及当前界面的更好的识别

__author__ = "BaG-Ray+"

# ----------------------------------引用部分（此部分所有脚本都一样，不需要修改）--------------------------------------------

from airtest.core.api import *

# 引入默认类脚本
import Default_Scripts
import LegenClover_Class
import LegenClover_Quest_Main
import LegenClover_Quest_Sub
import LegenClover_Quest_Tower

# ----------------------------------变量部分（需要改）--------------------------------------------

# ------------------------------------以下为图片----------------------------------------------

# -------------------------------------以下为坐标-----------------------------------------------

Check_Game_Mode_Coordinate = (1297, 868)

Quest_Main_Coordinate = (874, 264)
Quest_Sub_Coordinate = (1478, 320)
Quest_Tower_Coordinate = (1447, 727)

# --------------------------------------以下为变量--------------------------------------------


# --------------------------------------以下为RGB参数--------------------------------------------

Check_Game_Mode_Coordinate_Quest_RGB = (207, 170, 141)
Check_Game_Mode_Coordinate_Quest_Main_RGB = (133, 117, 81)  # 随着主线的进行可能需要修改
Check_Game_Mode_Coordinate_Quest_Sub_RGB = (228, 232, 209)
Check_Game_Mode_Coordinate_Quest_Tower_RGB = (248, 248, 248)
# Check_Game_Mode_Coordinate_HomePage_RGB = (169, 197, 236)

# ----------------------------------基础程序部分（此部分所有游戏一致，不需要更改）--------------------------------------------


# ----------------------------------以下为启动部分--------------------------------------------

Game_Name = "com.dmm.games.legeclo"
LegendCloverScriptsClass = Default_Scripts.OpencvGame(Game_Name)
LegendCloverVariable = LegenClover_Class.Universal_Variable()


# -----------------------------以下为各游戏的不同部分--------------------------------------------


def Check_Game_Mode(Ocr_Text, Game_Process, Game_Mode_RGB):
    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Quest_RGB:
        print("Quest界面")
        return 0

    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Quest_Tower_RGB:
        print("Tower界面")
        return 1

    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Quest_Main_RGB:
        print("Main界面")
        return 2

    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Quest_Sub_RGB:
        print("Sub界面")
        return 3

    '''
    if Game_Mode_RGB == Check_Game_Mode_Coordinate_HomePage_RGB:
        print("主界面")
        return 4
    '''


def Quest_Page(Game_Process):
    # 若目前不在主界面，证明脚本衔接之间出现了问题。
    # 因此将“Game_Process”原路返还，从哪来的回哪去，重新执行一遍前置脚本
    if LegendCloverScriptsClass.Get_Pixel_Rgb(Check_Game_Mode_Coordinate) != Check_Game_Mode_Coordinate_Quest_RGB:
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

        # 目前在Quest界面
        if Game_Mode == 0:

            # 若Process为3，表明是第一次进入到Quest界面
            # 此时先打勇者之塔
            # 转入勇者之塔脚本运行
            if Game_Process == 3:
                touch(Quest_Tower_Coordinate)
                continue

            # 若Process为4，表明已经是第二次进入Quest界面
            # 勇者之塔部分已经结束
            # 接下来完成Main完成袭来
            if Game_Process == 4:
                touch(Quest_Main_Coordinate)
                continue

            # 接下来完成Sub,此时为Sub的第一次执行
            # 或者第二次进入Sub关卡
            if Game_Process == 5 or Game_Process == 7:
                touch(Quest_Sub_Coordinate)
                continue

            # 此处表明已经执行过一次Sub了，返回主界面领取每日任务
            if Game_Process == 6:
                touch(LegendCloverVariable.Home_Page_Coordinate)
                return Game_Process

        # 目前在勇者之塔界面
        # Process为从3变成4
        if Game_Mode == 1:
            sleep(2)
            if Game_Mode_RGB == Check_Game_Mode_Coordinate_Quest_Tower_RGB:
                # 似乎已经进入勇者之塔界面，接下来转到勇者之塔界面脚本文件
                # 如果切换脚本后发现仍处于错误界面，则返回，继续在此运行
                Game_Process = LegenClover_Quest_Tower.Tower(Game_Process)
            else:
                # 不是主界面，重来
                continue

        # 目前在主战斗界面
        # Process为从4到5
        if Game_Mode == 2:
            sleep(2)
            if Game_Mode_RGB == Check_Game_Mode_Coordinate_Quest_Main_RGB:
                # 似乎已经进入勇者之塔界面，接下来转到勇者之塔界面脚本文件
                # 如果切换脚本后发现仍处于错误界面，则返回，继续在此运行
                Game_Process = LegenClover_Quest_Main.Main(Game_Process)
            else:
                # 不是主界面，重来
                continue

        # 目前在次战斗界面
        # Process为从5到6
        if Game_Mode == 3:
            sleep(2)
            if Game_Mode_RGB == Check_Game_Mode_Coordinate_Quest_Sub_RGB:
                # 似乎已经进入Sub界面，接下来转到Sub脚本文件
                # 如果切换脚本后发现仍处于错误界面，则返回，继续在此运行
                Game_Process = LegenClover_Quest_Sub.Sub(Game_Process)
            else:
                # 不是主界面，重来
                continue

        # 目前已经回到主界面
        # if Game_Mode == 4:
        # return Game_Process

# -----------------------------------测试部分--------------------------------------------
# Quest_Page(0)
# print(LegendCloverScriptsClass.Get_Pixel_Rgb(Check_Game_Mode_Coordinate))
# LegendCloverScriptsClass.CV2_Circle_Pic(Check_Game_Mode_Coordinate)
