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

# -------------------------------------以下为坐标-----------------------------------------------


# --------------------------------------以下为变量--------------------------------------------


# --------------------------------------以下为RGB参数--------------------------------------------


# ----------------------------------基础程序部分（此部分所有游戏一致，不需要更改）--------------------------------------------


# ----------------------------------以下为启动部分--------------------------------------------

Game_Name = "com.bandainamcoent.shinycolors"
ShinyColors_Scripts_Class = Default_Scripts.OpencvGame(Game_Name)
# ShinyColors_Coordinate = ShinyColors_Class.Variable_Coordinate()
ShinyColors_RGB = ShinyColors_Class.Variable_RGB()


# ----------------------------------以下为内置程序部分--------------------------------------------


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
Skill_Page(0)
