# -*- encoding=utf8 -*-
#   Version = 1.0
#   UpdateTime = 2023-09-24

__author__ = "BaG-Ray+"

# ----------------------------------引用部分（此部分所有脚本都一样，不需要修改）--------------------------------------------
from airtest.core.api import *

# 引入默认类脚本
import Default_Scripts
# 引入各界面脚本
import ShinyColors_Class

# ----------------------------------变量部分（需要改）--------------------------------------------

# ------------------------------------以下为图片----------------------------------------------

# -------------------------------------以下为坐标-----------------------------------------------

Coordinate_Page_Coordinate_Skill = (495, 185)

Coordinate_OCR_SP_1 = (630, 180)
Coordinate_OCR_SP_2 = (730, 222)

Coordinate_Button_Skill = (1856, 941)
Coordinate_Button_OK = (1345, 750)
Coordinate_Button_Minus = (2040, 656)
Coordinate_Button_Back = (360, 950)

Coordinate_Clear = (1870, 495)

# --------------------------------------以下为变量--------------------------------------------
Skill_List_Vi_Wing = [
    # Mamimi
    ShinyColors_Class.Variable_Coordinate_Get_Skill.Coordinate_Get_Skill_East_1,
    ShinyColors_Class.Variable_Coordinate_Get_Skill.Coordinate_Get_Skill_East_2,
    ShinyColors_Class.Variable_Coordinate_Get_Skill.Coordinate_Get_Skill_East_4,
    ShinyColors_Class.Variable_Coordinate_Get_Skill.Coordinate_Get_Skill_East_7,
    ShinyColors_Class.Variable_Coordinate_Get_Skill.Coordinate_Get_Skill_East_8,
    ShinyColors_Class.Variable_Coordinate_Get_Skill.Coordinate_Get_Skill_East_9,

    # Kohane
    ShinyColors_Class.Variable_Coordinate_Get_Skill.Coordinate_Get_Skill_SouthWest_1,

    # Amana
    ShinyColors_Class.Variable_Coordinate_Get_Skill.Coordinate_Get_Skill_SouthEast_1,
    ShinyColors_Class.Variable_Coordinate_Get_Skill.Coordinate_Get_Skill_SouthEast_2,
    ShinyColors_Class.Variable_Coordinate_Get_Skill.Coordinate_Get_Skill_SouthEast_4,
    ShinyColors_Class.Variable_Coordinate_Get_Skill.Coordinate_Get_Skill_SouthEast_7,

    # Si
    ShinyColors_Class.Variable_Coordinate_Get_Skill.Coordinate_Get_Skill_NorthWest_1,
    ShinyColors_Class.Variable_Coordinate_Get_Skill.Coordinate_Get_Skill_NorthWest_2,
    ShinyColors_Class.Variable_Coordinate_Get_Skill.Coordinate_Get_Skill_NorthWest_4,
    ShinyColors_Class.Variable_Coordinate_Get_Skill.Coordinate_Get_Skill_NorthWest_7,

    # Mamimi
    ShinyColors_Class.Variable_Coordinate_Get_Skill.Coordinate_Get_Skill_East_10,
    ShinyColors_Class.Variable_Coordinate_Get_Skill.Coordinate_Get_Skill_East_3,
    ShinyColors_Class.Variable_Coordinate_Get_Skill.Coordinate_Get_Skill_East_5,

    # Kohane
    ShinyColors_Class.Variable_Coordinate_Get_Skill.Coordinate_Get_Skill_SouthWest_3,
]

# --------------------------------------以下为RGB参数--------------------------------------------

RGB_Button_Skill = (255, 155, 197)
RGB_Button_Skill_Off = (173, 107, 135)

RGB_Page_Coordinate_Skill = (238, 192, 158)
RGB_Page_Determine = (124, 97, 76)

# ----------------------------------基础程序部分（此部分所有游戏一致，不需要更改）--------------------------------------------


# ----------------------------------以下为启动部分--------------------------------------------

Game_Name = "com.bandainamcoent.shinycolors"
ShinyColors_Scripts_Class = Default_Scripts.OpencvGame(Game_Name)
# ShinyColors_Coordinate = ShinyColors_Class.Variable_Coordinate()
ShinyColors_RGB = ShinyColors_Class.Variable_RGB()


# ----------------------------------以下为内置程序部分--------------------------------------------
def OCR_Get_Sp():
    Sp = ShinyColors_Scripts_Class.Pic_Ocr_Shape_Coordinate(Coordinate_OCR_SP_1, Coordinate_OCR_SP_2)
    return int(Sp)


def RGB_Check_Skill_Status():
    RGB_Status = ShinyColors_Scripts_Class.Get_Pixel_Rgb(Coordinate_Button_Skill)

    if ShinyColors_Scripts_Class.RGB_Compare(RGB_Status, RGB_Button_Skill):
        print("技能尚未点击，即将点击")
        return 1

    elif ShinyColors_Scripts_Class.RGB_Compare(RGB_Status, RGB_Button_Skill_Off):
        print("技能已经点击，即将跳过")
        return 0

    else:
        print("未选中技能")
        return -1


def Get_Skill(Coordinate):
    while True:
        touch(Coordinate_Clear)
        sleep(1)
        touch(Coordinate)
        Skill_Status = RGB_Check_Skill_Status()
        if Skill_Status == 1:
            touch(Coordinate_Button_Skill)
            break

        elif Skill_Status == 0:
            break

        else:
            continue


# ----------------------------------以下为标准程序部分--------------------------------------------
def Check_Game_Mode(Ocr_Text, Game_Process, Game_Mode_RGB):
    if ShinyColors_Scripts_Class.RGB_Compare(Game_Mode_RGB, RGB_Page_Coordinate_Skill):
        print("当前在技能界面")
        return 0

    if ShinyColors_Scripts_Class.RGB_Compare(Game_Mode_RGB, RGB_Page_Determine):
        print("当前在确认界面")
        return 1


def Skill_Page(Game_Process):
    Skill_List_Num = 0

    while True:

        Game_Ocr_Text = ShinyColors_Scripts_Class.Pic_Ocr_Unshape()
        try:
            print(Game_Ocr_Text)
        except:
            pass

        Game_Mode_RGB = ShinyColors_Scripts_Class.Get_Pixel_Rgb(Coordinate_Page_Coordinate_Skill)
        print(Game_Mode_RGB)

        Game_Mode = Check_Game_Mode(Game_Ocr_Text, Game_Process, Game_Mode_RGB)
        print(Game_Mode)

        if Game_Mode == 0:
            touch(Coordinate_Button_Minus)
            Sp = OCR_Get_Sp()
            if Sp > 20:
                Get_Skill(Skill_List_Vi_Wing[Skill_List_Num])
                Skill_List_Num = Skill_List_Num + 1

            else:
                touch(Coordinate_Button_Back)
                sleep(2)
                break

        if Game_Mode == 1:
            touch(Coordinate_Button_OK)
            sleep(5)


# ----------------------------------以下为主程序部分--------------------------------------------

# ----------------------------------test-------------------------------------------
Skill_Page(0)
