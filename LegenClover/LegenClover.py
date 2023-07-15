# -*- encoding=utf8 -*-
#   Version = 4.1
#   UpdateTime = 2023-07-21

# ----------------------------------4.0更新---------------------------------------------------
# UpdateTime = 2023-07-15
# 本次在优化后，将之前的版本调整为类的模式，方便其他程序直接调用即可

# ----------------------------------4.1更新---------------------------------------------------
# UpdateTime = 2023-07-21
# 更新RGB值

__author__ = "BaG-Ray+"

# ----------------------------------引用部分（此部分所有脚本都一样，不需要修改）--------------------------------------------

from airtest.core.api import *

# 引入默认类脚本
import Default_Scripts
# 引入各界面脚本
import LegenClover_Class
import LegenClover_HomePage

# ----------------------------------变量部分（需要改）--------------------------------------------

# ------------------------------------以下为图片----------------------------------------------


# ----------------------------------------------------以下为坐标-----------------------------------------------

Check_Game_Mode_Coordinate = (50, 1010)

# --------------------------------------以下为RGB参数--------------------------------------------

Game_Start_Page_RGB = (95, 148, 216)
Announce_Bonus_RGB = (108, 112, 89)
Home_Page_RGB = (237, 221, 195)

# --------------------------------------以下为变量--------------------------------------------
# Log_Dir = './log'
Log_Dir = './LegenClover/log'
Game_Name = "com.dmm.games.legeclo"

Game_Process = 0
Fragment_Heroine = 0
Sub_Count = 0

# ----------------------------------基础程序部分（此部分所有游戏一致，不需要更改）--------------------------------------------

LegendCloverScriptsClass = Default_Scripts.OpencvGame(Game_Name)
LegendCloverVariable = LegenClover_Class.Universal_Variable()
LegenCloverQuest = LegenClover_Class.Quest()


# -----------------------------以下为各游戏的不同部分--------------------------------------------

def Check_Game_Mode(Ocr_Text, Mode_Process, Mode_RGB):
    if "詳細な情報につきましては公式Twitterをご確認ください" in Ocr_Text:
        print("正在更新中，请切换下个游戏")
        LegendCloverScriptsClass.Exit_Game()
        return 0

    if "音量の設定" in Ocr_Text:
        print("音量设定")
        return 1

    if "CLOVER" in Ocr_Text or Mode_RGB == Game_Start_Page_RGB:
        print("标题界面")
        return 2

    if "容量" in Ocr_Text:
        print("需要更新")
        return 3

    if "完了" in Ocr_Text:
        print("更新完成")
        return 4

    if "Loading" in Ocr_Text:
        print("等待中")
        return 5

    if Mode_RGB == Announce_Bonus_RGB:
        print("在公告界面或登录奖励界面")
        return 6

    if Mode_RGB == Home_Page_RGB:
        print("当前已进入游戏主界面")
        return 7


# ----------------------------------主程序部分(不需要更改)--------------------------------------------


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

    if Game_Process == 0:
        # 由于目前采用的是多脚本联动的方式进行，因此采用此变量来推进流程
        # 采用此方法，可以防止多脚本的联动之间出现问题

        if Game_Mode == 0:
            # 需要更新安装包
            continue

        if Game_Mode == 1:
            # 音量设定
            touch(LegendCloverVariable.Close_Button_Coordinate)
            sleep(2)
            touch(LegendCloverVariable.Close_Button_Coordinate)
            continue

        if Game_Mode == 2:
            # 标题界面
            touch(LegendCloverVariable.OK_Two_Button_Coordinate)
            continue

        if Game_Mode == 3:
            # 更新
            touch(LegendCloverVariable.OK_Two_Button_Coordinate)
            continue

        if Game_Mode == 4:
            # 更新完成
            touch(LegendCloverVariable.OK_One_Button_Coordinate)
            continue

        if Game_Mode == 5:
            # 等待中
            continue

        if Game_Mode == 6:
            # 正在登录奖励界面或者公告界面
            # 此时点击任何非公告或奖励的地方即可
            # 因此这里设置成点击检测点位置
            touch(Check_Game_Mode_Coordinate)
            continue

        if Game_Mode == 7:
            # 目前已经进入主界面？
            # 不一定，也有可能是奖励或者公告界面的加载中，因此这里设置5秒的等待时间
            # 若是确认确实是在主界面，就进入主界面的脚本文件进行
            sleep(2)
            if Game_Mode_RGB == Home_Page_RGB:
                # 似乎已经进入主界面，接下来转到主界面脚本文件
                # 如果切换脚本后发现仍处于错误界面，则返回0，继续在此运行
                Game_Process = LegenClover_HomePage.Home_Page(Game_Process)
            else:
                # 不是主界面，重来
                continue
