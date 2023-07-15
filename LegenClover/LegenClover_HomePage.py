# -*- encoding=utf8 -*-
#   Version = 1.1
#   UpdateTime = 2023-07-20
#   本脚本界面为LegenClover的主界面，承担为各个模块承接的作用
# ----------------------------------1.0更新---------------------------------------------------
# UpdateTime = 2023-07-14
# 将原有模块进行拆分，方便后续的维护，以及当前界面的更好的识别
# ----------------------------------1.1更新---------------------------------------------------
# UpdateTime = 2023-07-20
# 应该没有什么问题了吧，下次再测测

__author__ = "BaG-Ray+"

# ----------------------------------引用部分（此部分所有脚本都一样，不需要修改）--------------------------------------------

from airtest.core.api import *

# 引入默认类脚本
import Default_Scripts
import LegenClover_Class
import LegenClover_Quest
import LegenClover_Story

# ----------------------------------变量部分（需要改）--------------------------------------------

# ------------------------------------以下为图片----------------------------------------------

# -------------------------------------以下为坐标-----------------------------------------------

Check_Game_Mode_Coordinate = (2333, 27)

Check_PresentBox_Coordinate = (203, 122)
Check_Mission_Coordinate = (315, 122)
Check_Daily_Coordinate = (135, 307)
Check_Mission_Status_Coordinate = (1788, 834)

Present_Box_Coordinate = (170, 147)
Mission_Box_Coordinate = (279, 149)
Daily_Coordinate = Check_Daily_Coordinate

Button_Get_Present = (1752, 929)
Button_Get_Mission = Check_Mission_Status_Coordinate

Stamina_HomePage_First_Coordinate = (465, 57)
Stamina_HomePage_Second_Coordinate = (633, 98)
Stamina_Mission_First_Coordinate = (1218, 20)
Stamina_Mission_Second_Coordinate = (1365, 60)

# --------------------------------------以下为变量--------------------------------------------


# --------------------------------------以下为RGB参数--------------------------------------------

Check_Game_Mode_Coordinate_Home_Page_RGB = (71, 153, 235)
Check_Game_Mode_Coordinate_Story_RGB = (178, 178, 178)
Check_Game_Mode_Coordinate_Quest_RGB = (207, 170, 141)
Check_Game_Mode_Coordinate_Mission_RGB = (175, 218, 225)

Check_Game_Mode_Coordinate_Result_RGB = (67, 86, 101)
Check_Game_Mode_Coordinate_Mission_Result_RGB = (93, 112, 127)

Check_PresentBox_Coordinate_RGB = (255, 188, 181)
Check_Mission_Coordinate_RGB = (255, 193, 188)
Check_Daily_Coordinate_RGB = (238, 242, 219)
Check_Mission_Status_Coordinate_RGB = (28, 92, 166)

# ----------------------------------基础程序部分（此部分所有游戏一致，不需要更改）--------------------------------------------


# ----------------------------------以下为启动部分--------------------------------------------

Game_Name = "com.dmm.games.legeclo"
LegendCloverScriptsClass = Default_Scripts.OpencvGame(Game_Name)
LegendCloverVariable = LegenClover_Class.Universal_Variable()


# -----------------------------以下为各游戏的不同部分--------------------------------------------


def Check_Game_Mode(Ocr_Text, Game_Process, Game_Mode_RGB):
    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Home_Page_RGB:
        print("当前在主页界面")
        return 0

    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Result_RGB:
        print("当前在领取完成界面")

        # 当前在礼物盒界面，若礼物盒中没有出现，证明礼物盒没有清空
        if "現在受け取れるプレゼントはありません" not in Ocr_Text:
            return 1
        else:
            # 表明礼物盒已经清空，目前已经可以回到主界面了
            # 或是每日一键完成的奖励界面
            return 2

    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Story_RGB:
        print("当前在故事界面")
        return 3

    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Quest_RGB:
        print("当前在战斗界面")
        return 4

    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Mission_RGB:
        print("当前在任务界面")
        return 5

    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Mission_Result_RGB:
        print("任务领取完成")
        return 6


def Get_Stamina(x1, y1, x2, y2):
    Ocr_Text = LegendCloverScriptsClass.Pic_Ocr_Shape(x1, y1, x2, y2)
    Ocr_Text_List = Ocr_Text.split('/')
    Stamina = Ocr_Text_List[0]
    return int(Stamina)


def Home_Page_Status():
    PresentBox_RGB = LegendCloverScriptsClass.Get_Pixel_Rgb(Check_PresentBox_Coordinate)
    Mission_RGB = LegendCloverScriptsClass.Get_Pixel_Rgb(Check_Mission_Coordinate)
    Daily_RGB = LegendCloverScriptsClass.Get_Pixel_Rgb(Check_Daily_Coordinate)

    if PresentBox_RGB == Check_PresentBox_Coordinate_RGB:
        if Daily_RGB == Check_Daily_Coordinate_RGB:
            if Mission_RGB == Check_Mission_Coordinate_RGB:
                return 0
            else:
                return 1
        else:
            return 2
    else:
        return 3


def Home_Page_Status_Check():
    # 此函数用来在程序和设定出现矛盾时，手动确认目前脚本已经进行位置
    Process = input("当前逻辑出现错误，请手动输入目前脚本已经进行到了哪个位置")
    return Process


# 此程序用来表示在任务领取完成时，若体力已经满了，则直接返回
# 目前策略是直接放弃多余的任务奖励
def Check_Stamina_Status(Page):
    if Page == 1:
        Stamina = Get_Stamina(Stamina_Mission_First_Coordinate[0],
                              Stamina_Mission_First_Coordinate[1],
                              Stamina_Mission_Second_Coordinate[0],
                              Stamina_Mission_Second_Coordinate[1])
    else:
        Stamina = Get_Stamina(Stamina_HomePage_First_Coordinate[0],
                              Stamina_HomePage_First_Coordinate[1],
                              Stamina_HomePage_Second_Coordinate[0],
                              Stamina_HomePage_Second_Coordinate[1])
    if Stamina > 1800:
        return 1
    else:
        return 0


# 本程序
def Check_Mission_Status():
    Mission_Status = LegendCloverScriptsClass.Get_Pixel_Rgb(Check_Mission_Status_Coordinate)
    if Mission_Status == Check_Mission_Status_Coordinate_RGB:
        return 0
    else:
        return 1


def Home_Page(Game_Process):
    print("当前已进入主界面脚本")

    # 若目前不在主界面，证明脚本衔接之间出现了问题。
    # 因此将“Game_Process”原路返还，从哪来的回哪去，重新执行一遍前置脚本
    # if LegendCloverScriptsClass.Get_Pixel_Rgb(Check_Game_Mode_Coordinate) != Check_Game_Mode_Coordinate_Home_Page_RGB:
    # return Game_Process

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
            # 当前在主界面

            # 第一次在主界面是刚登录的时候，此时先收礼物
            # 此时，礼物，任务和一键完成指令都应该是未点击状态
            if Game_Process == 0:

                Home_Status = Home_Page_Status()
                if Home_Status == 0:
                    touch(Present_Box_Coordinate)
                    continue
                else:
                    Game_Process = Home_Page_Status_Check()
                    continue

            # 第二次在主界面是礼物领取完成的时候
            # 此时，礼物应该是已领取状态，剩余的两个应该是未点击状态
            # 若已经没有问题，则进入故事界面打碎片
            if Game_Process == 1:
                Home_Status = Home_Page_Status()
                if Home_Status == 1:
                    touch(LegendCloverVariable.Story_Coordinate)
                    continue
                else:
                    Game_Process = Home_Page_Status_Check()
                    continue

            # 第三次在主界面是故事本已经刷完的时候，先点击每日一键完成按钮吧
            if Game_Process == 2:
                touch(Daily_Coordinate)
                sleep(5)
                continue

            # 第四次在主界面是一键完成每日活动的奖励已经领取完成的时候
            # 先进行判断，每日一键是否已经完成
            # 若没问题就进入战斗本吧
            # 否则还是回到远处
            if Game_Process == 3:
                Home_Status = Home_Page_Status()
                if Home_Status == 2:
                    touch(LegendCloverVariable.Quest_Coordinate)
                    continue
                else:
                    Game_Process = Home_Page_Status_Check()
                    continue

            # 第五次在主界面是在已经打过一次Sub关卡
            # 回来领任务奖励的时候
            # Process应为从6至7
            if Game_Process == 6:
                touch(Mission_Box_Coordinate)
                continue

            # 第六次在主界面是领取完成任务奖励
            # 检测三个点
            # 理论上而言，此时应该三个点都已经点击完成
            # 除非体力已满
            if Game_Process == 7:
                Home_Status = Home_Page_Status()
                Stamina_Status = Check_Stamina_Status(0)
                if Home_Status == 3 or Stamina_Status == 0:
                    touch(LegendCloverVariable.Quest_Coordinate)
                else:
                    Game_Process = 6
                continue

        # 当前在礼物盒界面，不管领礼物进行到何处，反正当前为之还没出现"現在受け取れるプレゼントはありません"
        # 代表现在礼物盒还没有空，那就一直点领取即可
        # 此时Process在执行前后都应该是0
        if Game_Mode == 1:
            touch(Present_Box_Coordinate)
            continue

        # 表明目前礼物已经领取完成，可以关掉礼物盒回到主界面了,随便点即可，这里点击测试点
        # 此时Process执行前应该是0，执行后应该是1
        # 或者是执行每日任务时的2，执行后变成3
        if Game_Mode == 2:
            touch(Check_Game_Mode_Coordinate)
            Game_Process = Game_Process + 1
            continue

        # 目前在故事界面，切换至故事界面脚本
        # 执行前应该是1，执行后应该变为2
        if Game_Mode == 3:
            sleep(2)
            if Game_Mode_RGB == Check_Game_Mode_Coordinate_Story_RGB:
                # 似乎已经进入故事界面，接下来转到故事界面脚本文件
                # 如果切换脚本后发现仍处于错误界面，则返回1，继续在此运行
                Game_Process = LegenClover_Story.Story_Page(Game_Process)
            else:
                # 不是故事界面，重来
                continue

        # 目前在战斗界面，切换至战斗界面脚本
        # 执行前应该为3，执行后变为
        if Game_Mode == 4:
            sleep(2)
            if Game_Mode_RGB == Check_Game_Mode_Coordinate_Quest_RGB:
                # 似乎已经进入战斗界面，接下来转到战斗界面脚本文件
                # 如果切换脚本后发现仍处于错误界面，则返回，继续在此运行
                Game_Process = LegenClover_Quest.Quest_Page(Game_Process)
            else:
                # 不是主界面，重来
                continue

        # 目前在任务界面，点击领取任务
        # 或者需要返回
        # 这里通过检测
        # 但如果体力满了，同样返回
        if Game_Mode == 5:
            Mission_Status = Check_Mission_Status()

            if Mission_Status == 0:

                Stamina_Status = Check_Stamina_Status(1)
                if Stamina_Status == 0:
                    touch(Button_Get_Mission)
                    continue

                if Stamina_Status == 1:
                    touch(LegendCloverVariable.Home_Page_Coordinate)
                    Game_Process = 7
                    continue

            if Mission_Status == 1:
                touch(LegendCloverVariable.Home_Page_Coordinate)
                Game_Process = 7
                continue

        # 目前已经领取完任务
        # 点击任何点位即可返回任务界面
        # 这里点击检测点位
        if Game_Mode == 6:
            touch(Check_Game_Mode_Coordinate)
            continue

        # -------------------------------以下为旧程序-------------------------------------


# -----------------------------------测试部分--------------------------------------------
# print(LegendCloverScriptsClass.Get_Pixel_Rgb(Button_Get_Mission))
# LegendCloverScriptsClass.CV2_Circle_Pic(Button_Get_Mission)
# print(LegendCloverScriptsClass.Get_Pixel_Rgb(Check_Mission_Coordinate))
# print(LegendCloverScriptsClass.Get_Pixel_Rgb(Check_Daily_Coordinate))
Home_Page(0)
# Get_Stamina(1218, 20, 1365, 60)
