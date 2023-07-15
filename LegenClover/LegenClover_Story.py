# -*- encoding=utf8 -*-
#   Version = 1.1
#   UpdateTime = 2023-07-16

# ----------------------------------1.0更新---------------------------------------------------
# UpdateTime = 2023-07-16
# 将原有模块进行拆分，方便后续的维护，以及当前界面的更好的识别
# 理论上这个脚本以后应该不会在需要大更新了，可能只有更新下刷碎片角色的小更新

# ----------------------------------1.1更新---------------------------------------------------
# UpdateTime = 2023-07-16
# 更新六个碎片信息，本来应该更多的，而且前两个也快满了，但截图的时候就忘了。
# 估计很快就会更行1.2了吧

__author__ = "BaG-Ray+"

# ----------------------------------引用部分（此部分所有脚本都一样，不需要修改）--------------------------------------------

from airtest.core.api import *

# 引入默认类脚本
import Default_Scripts
import LegenClover_Class

# ----------------------------------变量部分（需要改）--------------------------------------------

# ------------------------------------以下为图片----------------------------------------------

Soru_Pic = Template(r"tpl1689506462564.png", record_pos=(0.193, 0.03), resolution=(2400, 1080))
Soru_Q_Pic = Template(r"tpl1689506477625.png", record_pos=(-0.436, 0.076), resolution=(2400, 1080))
Morigan_Pic = Template(r"tpl1689506512391.png", record_pos=(0.355, 0.002), resolution=(2400, 1080))
Morigan_Q_Pic = Template(r"tpl1689506533213.png", record_pos=(-0.432, 0.08), resolution=(2400, 1080))
Zikufurito_Pic = Template(r"tpl1689506590196.png", record_pos=(0.275, 0.031), resolution=(2400, 1080))
Zikufurito_Q_Pic = Template(r"tpl1689506606643.png", record_pos=(-0.441, 0.081), resolution=(2400, 1080))
Yanmo_Pic = Template(r"tpl1689506674734.png", record_pos=(0.194, -0.036), resolution=(2400, 1080))
Yanmo_Q_Pic = Template(r"tpl1689506689563.png", record_pos=(-0.438, 0.055), resolution=(2400, 1080))
Katia_Pic = Template(r"tpl1689506815678.png", record_pos=(0.274, 0.065), resolution=(2400, 1080))
Katia_Q_Pic = Template(r"tpl1689506823333.png", record_pos=(-0.435, 0.077), resolution=(2400, 1080))
Tianjiang_Pic = Template(r"tpl1689506918618.png", record_pos=(0.435, 0.104), resolution=(2400, 1080))
Tianjiang_Q_Pic = Template(r"tpl1689506931529.png", record_pos=(-0.443, 0.065), resolution=(2400, 1080))

# ----------------------------------------------------以下为坐标-----------------------------------------------

Check_Game_Mode_Coordinate = (2333, 27)

Sub_Heroine_Coordinate = (1812, 164)
Main_Heroine_Coordinate = (1642, 162)
Get_Fragment_Coordinate = (1453, 788)
Close_Fragment_Coordinate = (1540, 350)

Swipe_Start_Coordinate = (1957, 777)
Swipe_End_Coordinate = (1957, 496)

Fragment_Pic_First_Coordinate = (1390, 693)
Fragment_Pic_Second_Coordinate = (1519, 723)
Times_Pic_First_Coordinate = (1920, 20)
Times_Pic_Second_Coordinate = (2020, 58)

# --------------------------------------以下为变量--------------------------------------------

Fragment_Heroine_List = [
    2, Soru_Pic, Soru_Q_Pic,
    2, Morigan_Pic, Morigan_Q_Pic,
    1, Zikufurito_Pic, Zikufurito_Q_Pic,
    1, Yanmo_Pic, Yanmo_Q_Pic,
    1, Katia_Pic, Katia_Q_Pic,
    2, Tianjiang_Pic, Tianjiang_Q_Pic
]

# --------------------------------------以下为RGB参数--------------------------------------------

Check_Game_Mode_Coordinate_Story_RGB = (178, 178, 178)
Check_Game_Mode_Coordinate_HomePage_RGB = (83, 167, 255)

Get_Fragment_RGB = (88, 88, 88)

# ----------------------------------基础程序部分（此部分所有游戏一致，不需要更改）--------------------------------------------


# ----------------------------------以下为启动部分--------------------------------------------

Game_Name = "com.dmm.games.legeclo"
LegendCloverScriptsClass = Default_Scripts.OpencvGame(Game_Name)
LegendCloverVariable = LegenClover_Class.Universal_Variable()


# -----------------------------以下为各游戏的不同部分--------------------------------------------

# 此函数为判断当前碎片个数，并给出如下逻辑，返回目前有的碎片数和当前升星所需要的碎片数，若需要升星的碎片数不为50或100，即为150，表明此时为五星，按照目前规划，不需要升级。因此
# 当前的个数不应该超过100，后续给出判断，若当前数大于100，就不跑这个碎片本。此函数应当在故事模块中个人页里的详细中进行查看。
def Get_Fragment_Num():
    Ocr_Text = LegendCloverScriptsClass.Pic_Ocr_Shape(Fragment_Pic_First_Coordinate[0],
                                                      Fragment_Pic_First_Coordinate[1],
                                                      Fragment_Pic_Second_Coordinate[0],
                                                      Fragment_Pic_Second_Coordinate[1])

    Fragment_List = Ocr_Text.split('/')
    Fragment_Need = Fragment_List[1]
    Fragment_Now = Fragment_List[0]
    return int(Fragment_Need), int(Fragment_Now)


# 以下两个函数用来在角色碎片中滑动
def Heroine_Swipe():
    swipe(Swipe_Start_Coordinate, Swipe_End_Coordinate)


def Heroine_Swipe_Count():
    swipe(Swipe_End_Coordinate, Swipe_Start_Coordinate)


# 此函数用来获取今日可以打几次故事模式
def Get_Fragment_Times():
    Ocr_Text = LegendCloverScriptsClass.Pic_Ocr_Shape(Times_Pic_First_Coordinate[0],
                                                      Times_Pic_First_Coordinate[1],
                                                      Times_Pic_Second_Coordinate[0],
                                                      Times_Pic_Second_Coordinate[1])

    Fragent_List = Ocr_Text.split('/')
    Fragent_Now_Times = Fragent_List[0]
    return int(Fragent_Now_Times)


# 此函数用来进入角色的碎片界面：总共分为三个步骤，首先是通过Fragment_Heroine_List中第一位为区分main还是sub角色，第二步再找到角色，第三步判断找到角色后的界面是否正确，正确则执行，否则重新来一次
def Query_Fragment():
    Heroine_Now = 0
    Fragment_Times = Get_Fragment_Times()
    Heroine_Times = (Fragment_Times - 1) / 3

    while Heroine_Now <= Heroine_Times:

        if Fragment_Heroine_List[Heroine_Now * 3] == 1:
            touch(Main_Heroine_Coordinate)
        else:
            touch(Sub_Heroine_Coordinate)

        Heroine_Find(Heroine_Now)

        if exists(Fragment_Heroine_List[Heroine_Now * 3 + 2]):
            '''
            while not exists(Story_Character_Pic):
                touch(Story_Character_Coordinate)
            #此时进入到个人页面,先检查碎片个数
            '''

            # touch(Fragment_Check_Coordinate)
            Fragent_Need, Fragent_Now = Get_Fragment_Num()
            # touch(Close_Fragment_Coordinate)

            if Fragent_Need == 150 or Fragent_Now > 100:
                Heroine_Times = Heroine_Times + 1
                Heroine_Now = Heroine_Now + 1
                touch(LegendCloverVariable.Return_Coordinate)
                continue

            else:
                # Quest_Skip(Quest_Fragment_Coordinate,Skip_Coordinate)
                touch(Get_Fragment_Coordinate)

                while True:
                    Fragment_Status = LegendCloverScriptsClass.Get_Pixel_Rgb(Check_Game_Mode_Coordinate)
                    if Fragment_Status == Get_Fragment_RGB:
                        # 确保已经拿到碎片，点击即可
                        # 这里就点击检测点吧
                        touch(Check_Game_Mode_Coordinate)
                        break

                Heroine_Now = Heroine_Now + 1

        else:
            pass

    # 碎片本跑完，


# 此函数用来寻找对应角色，判断逻辑如下：如果当前页面存在则点击，否则往下划，直到新的两行出现在最上面。当划了七次后，如果还没有，证明可能是在原来位置的上面，再往上滑找
def Heroine_Find(Heroine_Now):
    SwipeCount = 0
    while True:
        if exists(Fragment_Heroine_List[Heroine_Now * 3 + 1]):
            touch(Fragment_Heroine_List[Heroine_Now * 3 + 1])
            break
        elif SwipeCount < 20:
            Heroine_Swipe()
            sleep(3)
            SwipeCount = SwipeCount + 1
        else:
            Heroine_Swipe_Count()
            sleep(3)


def Check_Game_Mode(Ocr_Text, Game_Process, Game_Mode_RGB):
    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Story_RGB:
        print("目前在故事界面")
        return 0

    if Game_Mode_RGB == Get_Fragment_RGB:
        print("碎片领取完成")
        return 1

    if Game_Mode_RGB == Check_Game_Mode_Coordinate_HomePage_RGB:
        print("目前在主界面")
        return 2


def Story_Page(Game_Process):
    # 若目前不在主界面，证明脚本衔接之间出现了问题。
    # 因此将“Game_Process”原路返还，从哪来的回哪去，重新执行一遍前置脚本
    if LegendCloverScriptsClass.Get_Pixel_Rgb(Check_Game_Mode_Coordinate) != Check_Game_Mode_Coordinate_Story_RGB:
        return Game_Process

    while True:

        Game_Ocr_Text = LegendCloverScriptsClass.Pic_Ocr_Unshape()
        try:
            print(Game_Ocr_Text)
        except:
            pass

        Game_Mode_RGB = LegendCloverScriptsClass.Get_Pixel_Rgb(Check_Game_Mode_Coordinate)
        print(Game_Mode_RGB)

        # --------------------------------以下部分为主程序中的专属部分-----------------------------

        # ------------------------    测试代码可在上面写,下面为正式代码----------------------------
        Game_Mode = Check_Game_Mode(Game_Ocr_Text, Game_Process, Game_Mode_RGB)
        print(Game_Mode)

        if Game_Mode == 0:
            # 执行即可
            Query_Fragment()

            # 故事页只需要跑碎片即可，因此只要确认碎片次数为0即可返回主界面
            # 否则报错，进行人工判断
            Times = Get_Fragment_Times()

            if Times == 0:
                pass
            else:
                Times = input("请输入目前故事脚本的运行情况，若返回主界面则输入0")

            # 返回主界面
            touch(LegendCloverVariable.Home_Page_Coordinate)
            sleep(2)

        if Game_Mode == 2:
            # 目前在主界面
            Game_Process = 2
            return Game_Process
