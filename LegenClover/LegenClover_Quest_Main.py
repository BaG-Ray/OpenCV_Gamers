# -*- encoding=utf8 -*-
#   Version = 1.1
#   UpdateTime = 2023-07-18

# ----------------------------------1.0更新---------------------------------------------------
# UpdateTime = 2023-07-18
# 将原有模块进行拆分，方便后续的维护，以及当前界面的更好的识别
# 本节太累了
# ----------------------------------1.1更新---------------------------------------------------
# UpdateTime = 2023-07-19
# 调整了战斗结束时的rgb值

__author__ = "BaG-Ray+"

# ----------------------------------引用部分（此部分所有脚本都一样，不需要修改）--------------------------------------------

from airtest.core.api import *

# 引入默认类脚本
import Default_Scripts
import LegenClover_Class

# ----------------------------------变量部分（需要改）--------------------------------------------

# ------------------------------------以下为图片----------------------------------------------

Quest_Xilai_Lv80_Pic = Template(r"tpl1689586003798.png", record_pos=(0.24, 0.02), resolution=(2400, 1080))

# -------------------------------------以下为坐标-----------------------------------------------

Check_Game_Mode_Coordinate = (2333, 19)

Check_Button_Xilai_Coordinate = (2258, 773)
Check_Xilai_Coordinate = (855, 225)
Check_Battle_Coordinate = (2028, 913)
Check_Button_Finish_Coordinate = (2100, 1007)

Button_Xilai_Coordinate = Check_Button_Xilai_Coordinate
Button_Xilai_Choose_Coordinate = (917, 282)
Button_Battle_Coordinate = Check_Battle_Coordinate
Button_Finish_Coordinate = Check_Button_Finish_Coordinate

# --------------------------------------以下为变量--------------------------------------------


# --------------------------------------以下为RGB参数--------------------------------------------

Check_Game_Mode_Coordinate_Main_RGB = (238, 242, 219)

Check_Game_Mode_Coordinate_Choose_RGB = (118, 118, 118)
Check_Game_Mode_Coordinate_Fight_RGB = (229, 188, 156)

Check_Button_Xilai_Coordinate_RGB = (103, 20, 134)
Check_Xilai_Coordinate_Yes_RGB = (248, 248, 248)
Check_Xilai_Coordinate_UnChoose_RGB = (248, 248, 248)
Check_Battle_Coordinate_RGB = (138, 119, 104)
Check_Button_Finish_Coordinate_RGB = (234, 203, 139)
Check_Button_Finish_Coordinate_0_RGB = (235, 213, 156)

# ----------------------------------基础程序部分（此部分所有游戏一致，不需要更改）--------------------------------------------


# ----------------------------------以下为启动部分--------------------------------------------

Game_Name = "com.dmm.games.legeclo"
LegendCloverScriptsClass = Default_Scripts.OpencvGame(Game_Name)
LegendCloverVariable = LegenClover_Class.Universal_Variable()


# -----------------------------以下为各游戏的不同部分--------------------------------------------

# 此函数用来判断袭来界面是否已经选中
def Check_Xilai_Status():
    Xilai_Status_RGB = LegendCloverScriptsClass.Get_Pixel_Rgb(Check_Xilai_Coordinate)
    if Xilai_Status_RGB == Check_Xilai_Coordinate_UnChoose_RGB:
        # 表明尚未选中了袭来关卡
        return 0
    else:
        # 表明已经选中袭来关卡
        return 1


def Check_Battle_Status():
    Battle_Status = LegendCloverScriptsClass.Get_Pixel_Rgb(Check_Battle_Coordinate)
    if Battle_Status == Check_Battle_Coordinate_RGB:
        # 表明还在战斗准备阶段
        return 0
    else:
        # 表明已经开始战斗
        return 1


# 本函数使用方法特殊，由于在战斗界面，实在是没有什么能识别的了
# 在本界面识别不到任何东西时，就执行此函数来判断是否结束了吧
def Check_Battle_Finish_Stauts():
    Finish_Status = LegendCloverScriptsClass.Get_Pixel_Rgb(Check_Button_Finish_Coordinate)
    if Finish_Status == Check_Button_Finish_Coordinate_RGB:
        return 2
    elif Finish_Status == Check_Button_Finish_Coordinate_0_RGB:
        return 1
    else:
        return 0


def Check_Game_Mode(Ocr_Text, Game_Process, Game_Mode_RGB):
    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Main_RGB:
        print("Main Quest界面")
        return 0

    # 当前表明已经进入袭来按键部分了，但是此部分仍有两种情况
    # 一种是还没选中该打的袭来关卡
    # 一种是已经选择了，还没选择等级
    # 实际上是三种了，准备战斗也包含在内
    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Choose_RGB:
        print("袭来界面")

        if "する" in Ocr_Text:
            print("准备出击")
            return 3

        Xilai_Status = Check_Xilai_Status()
        if Xilai_Status == 0:
            print("目前尚未选中关卡")
            return 1

        if Xilai_Status == 1:
            print("目前已经选中关卡")
            return 2

    # 目前按照此方法，战斗界面包括了战斗中和战斗前准备的部分
    # 因此需要做出个条件判断
    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Fight_RGB:
        print("战斗界面")

        Fight_Status = Check_Battle_Status()
        if Fight_Status == 0:
            print("还未开始战斗")
            return 4

        if Fight_Status == 1:
            print("战斗中")
        return 5

    Finish_Status = Check_Battle_Finish_Stauts()
    if Finish_Status == 1:
        print("战斗完成，领取奖励")
        return 6

    elif Finish_Status == 2:
        print("战斗完全结束")
        return 7


def Main(Game_Process):
    # 若目前不在主界面，证明脚本衔接之间出现了问题。
    # 因此将“Game_Process”原路返还，从哪来的回哪去，重新执行一遍前置脚本
    if LegendCloverScriptsClass.Get_Pixel_Rgb(Check_Game_Mode_Coordinate) != Check_Game_Mode_Coordinate_Main_RGB:
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

        if Game_Mode == 0.5:
            # 已进入Main Quest界面
            # 首先判断是否需要打袭来
            Quest_XiLai_Check_Now_RGB = LegendCloverScriptsClass.Get_Pixel_Rgb(Check_Xilai_Coordinate)

            if Quest_XiLai_Check_Now_RGB == Check_Button_Xilai_Coordinate_RGB:
                # 当前需要执行袭来
                touch(Button_Xilai_Coordinate)
                continue

            else:
                # 当前不需要执行袭来
                Game_Process = 5
                return Game_Process

        if Game_Mode == 1.5:
            # 袭来界面
            # 但尚未选中关卡
            touch(Button_Xilai_Choose_Coordinate)
            continue

        if Game_Mode == 2.5:
            # 袭来界面，且已经选中关卡
            # 接下俩只需要选择lv80按键即可
            touch(Quest_Xilai_Lv80_Pic)
            sleep(5)
            continue

        if Game_Mode == 3.5:
            # 准备出击，点击出击即可
            touch(LegendCloverVariable.Ready_Quest_Button_Coordinate)
            sleep(2)
            continue

        if Game_Mode == 4.5:
            # 战斗界面
            # 开始战斗
            touch(Button_Battle_Coordinate)
            continue

        if Game_Mode == 6.5 or Game_Mode == 7.5:
            # 战斗完成，点击结束
            # 此处的坐标可能需要更改
            touch(Check_Button_Finish_Coordinate)
            continue

# ------------------------Test----------------------------------------------\
# print(LegendCloverScriptsClass.Get_Pixel_Rgb(Check_Button_Finish_Coordinate))
# Main(0)
# LegendCloverScriptsClass.CV2_Circle_Pic(Check_Button_Finish_Coordinate)
# touch(Check_Button_Finish_Coordinate)
