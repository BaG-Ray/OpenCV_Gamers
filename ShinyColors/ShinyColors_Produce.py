# -*- encoding=utf8 -*-
#   Version = 1.0
#   UpdateTime = 2023-09-24

__author__ = "BaG-Ray+"

# ----------------------------------引用部分（此部分所有脚本都一样，不需要修改）--------------------------------------------

# 引入默认类脚本
import Default_Scripts
# 引入各界面脚本
import ShinyColors_Class


# ----------------------------------变量部分（需要改）--------------------------------------------

# ------------------------------------以下为图片----------------------------------------------

class Pic:
    Num1 = 1
    Num2 = 2
    Num3 = 3
    Num4 = 0
    Num5 = 0
    Num6 = 6
    Num7 = 7
    Num8 = 8


Num_Pic_List = [Pic.Num1,
                Pic.Num2,
                Pic.Num3,
                Pic.Num4,
                Pic.Num5,
                Pic.Num6,
                Pic.Num7,
                Pic.Num8]


# -------------------------------------以下为坐标-----------------------------------------------
class Coordinate:
    OCR_Season_1 = (864, 40)
    OCR_Season_2 = (894, 80)

    OCR_ErrorRate_1 = (1880, 285)
    OCR_ErrorRate_2 = (1980, 350)

    OCR_Sp_1 = (1625, 590)
    OCR_Sp_2 = (1706, 622)

    OCR_Stamina_1 = (1489, 590)
    OCR_Stamina_2 = (1570, 622)

    OCR_Rank_1 = (1220, 75)
    OCR_Rank_2 = (1255, 120)

    Button_Lesson = (466, 322)

    Button_Vi_Lesson = (1245, 750)
    Button_Vo_Lesson = (788, 750)
    Button_Da_Lesson = (1030, 750)
    Button_Radio = (1518, 750)
    Button_Talk = (1735, 750)

    Button_OK = (1988, 947)

    RGB_Support = (1642, 950)

    PicCom_Week_1 = ()
    PicCom_Week_2 = ()


# --------------------------------------以下为变量--------------------------------------------


# --------------------------------------以下为RGB参数--------------------------------------------

class RGB:
    Support = (86, 121, 203)


# ----------------------------------基础程序部分（此部分所有游戏一致，不需要更改）--------------------------------------------


# ----------------------------------以下为启动部分--------------------------------------------

Game_Name = "com.bandainamcoent.shinycolors"
ShinyColors_Scripts_Class = Default_Scripts.OpencvGame(Game_Name)
# ShinyColors_Coordinate = ShinyColors_Class.Variable_Coordinate()
ShinyColors_RGB = ShinyColors_Class.Variable_RGB()


# ----------------------------------以下为内置程序部分--------------------------------------------

def Get_Season():
    Season = ShinyColors_Scripts_Class.Pic_Ocr_Shape_Coordinate(Coordinate.OCR_Season_1, Coordinate.OCR_Season_2)
    return int(Season)


def Get_ErrorRate():
    ErrorRate = ShinyColors_Scripts_Class.Pic_Ocr_Shape_Coordinate(Coordinate.OCR_ErrorRate_1,
                                                                   Coordinate.OCR_ErrorRate_2)
    return int(ErrorRate)


def Get_Sp():
    Sp = ShinyColors_Scripts_Class.Pic_Ocr_Shape_Coordinate(Coordinate.OCR_Sp_1,
                                                            Coordinate.OCR_Sp_2)
    return int(Sp)


def Get_Stamina():
    Stamina = ShinyColors_Scripts_Class.Pic_Ocr_Shape_Coordinate(Coordinate.OCR_Stamina_1,
                                                                 Coordinate.OCR_Stamina_2)
    return int(Stamina)


def Check_Support():
    Support_Status = ShinyColors_Scripts_Class.Get_Pixel_Rgb(Coordinate.RGB_Support)
    if ShinyColors_Scripts_Class.RGB_Compare(Support_Status, RGB.Support):
        return 1
    else:
        return 0


def Get_Rank():
    Rank = ShinyColors_Scripts_Class.Pic_Ocr_Shape_Rank_Coordinate(Coordinate.OCR_Rank_1, Coordinate.OCR_Rank_2)
    return Rank


def Get_Week():
    for Num in range(0, 7):
        if ShinyColors_Scripts_Class.Pic_Compare_Coordinate(Coordinate.PicCom_Week_1, Coordinate.PicCom_Week_2,
                                                            Num_Pic_List[Num]):
            return Num + 1
        else:
            return 999


# ----------------------------------以下为标准程序部分--------------------------------------------
def Check_Game_Mode(Ocr_Text, Game_Process, Game_Mode_RGB):
    pass


def Skill_Page(Game_Process):
    Skill_List_Num = 0

    while True:

        Game_Ocr_Text = ShinyColors_Scripts_Class.Pic_Ocr_Unshape()
        try:
            print(Game_Ocr_Text)
        except:
            pass

        Game_Mode_RGB = ShinyColors_Scripts_Class.Get_Pixel_Rgb(0)
        print(Game_Mode_RGB)

        Game_Mode = Check_Game_Mode(Game_Ocr_Text, Game_Process, Game_Mode_RGB)
        print(Game_Mode)

        if Game_Mode == 0:
            pass


# ----------------------------------以下为主程序部分--------------------------------------------

# ----------------------------------test-------------------------------------------
print(Get_Week())
