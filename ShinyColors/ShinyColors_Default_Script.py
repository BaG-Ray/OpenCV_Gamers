# -*- encoding=utf8 -*-
#   Version = 1.0
#   UpdateTime = 2023-09-23

__author__ = "BaG-Ray+"

# ----------------------------------引用部分（此部分所有脚本都一样，不需要修改）--------------------------------------------

# 引入默认类脚本
import Default_Scripts
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
ShinyColors_Coordinate = ShinyColors_Class.Variable_Coordinate()
ShinyColors_RGB = ShinyColors_Class.Variable_RGB()


# -----------------------------以下为各游戏的不同部分--------------------------------------------


def Check_Game_Mode(Ocr_Text, Game_Process, Game_Mode_RGB):
    pass


def Home_Page(Game_Process):
    while True:

        Game_Ocr_Text = ShinyColors_Scripts_Class.Pic_Ocr_Unshape()
        try:
            print(Game_Ocr_Text)
        except:
            pass

        # Game_Mode_RGB = ShinyColors_Scripts_Class.Get_Pixel_Rgb(ShinyColorsVariable.Check_Game_Mode_Coordinate)
        # print(Game_Mode_RGB)

        # Game_Mode = Check_Game_Mode(Game_Ocr_Text, Game_Process, Game_Mode_RGB)
        # print(Game_Mode)

        # --------------------------------以下部分为主程序中的专属部分-----------------------------

        # ------------------------    测试代码可在上面写,下面为正式代码----------------------------

        pass


Home_Page(0)
