# ----------------------------------引用部分（此部分所有脚本都一样，不需要修改）--------------------------------------------
# -*- encoding=utf8 -*-
#   Version = 3.0
#   UpdateTime = 2023-05-18
__author__ = "Ray"

import datetime
import os
import shutil

import cv2
import pytesseract
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from PIL import Image

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["ios:///http+usbmux://00008020-001318C00A91002E", ])

from poco.drivers.ios import iosPoco

poco = iosPoco()

# ----------------------------------变量部分（需要改）--------------------------------------------

# ----以下为图片--------------
Nimue_Val_Pic = Template(r"tpl1684233899964.png", record_pos=(0.422, 0.073), resolution=(2224, 1668))
Nimue_Val_Q_Pic = Template(r"tpl1684233920975.png", record_pos=(-0.416, 0.081), resolution=(2224, 1668))
Hadesu_Sch_Pic = Template(r"tpl1684233955768.png", record_pos=(0.421, 0.094), resolution=(2224, 1668))
Hadesu_Sch_Q_Pic = Template(r"tpl1684233977140.png", record_pos=(-0.418, 0.104), resolution=(2224, 1668))
Master_White_Pic = Template(r"tpl1684234002464.png", record_pos=(0.418, 0.072), resolution=(2224, 1668))
Master_White_Q_Pic = Template(r"tpl1684234015710.png", record_pos=(-0.422, 0.096), resolution=(2224, 1668))
Master_Red_Pic = Template(r"tpl1678427716754.png", record_pos=(0.203, -0.072), resolution=(2224, 1668))
Master_Red_Q_Pic = Template(r"tpl1678423478458.png", record_pos=(-0.396, 0.124), resolution=(2224, 1668))
Soru_Pic = Template(r"tpl1684234059708.png", record_pos=(0.219, 0.073), resolution=(2224, 1668))
Soru_Q_Pic = Template(r"tpl1684234080980.png", record_pos=(-0.413, 0.102), resolution=(2224, 1668))
Izanami_Pic = Template(r"tpl1684234419942.png", record_pos=(0.319, 0.019), resolution=(2224, 1668))
Izanami_Q_Pic = Template(r"tpl1684234433684.png", record_pos=(-0.421, 0.095), resolution=(2224, 1668))
MansaMuusa_Pic = Template(r"tpl1684234493134.png", record_pos=(0.319, 0.032), resolution=(2224, 1668))
MansaMuusa_Q_Pic = Template(r"tpl1684234517140.png", record_pos=(-0.424, 0.102), resolution=(2224, 1668))

Home_Page_Pic = Template(r"tpl1678429454229.png", record_pos=(0.356, -0.352), resolution=(2224, 1668))
Present_Box_Pic = Template(r"tpl1678429619573.png", record_pos=(-0.291, 0.21), resolution=(2224, 1668))
Story_Pic = Template(r"tpl1678429671844.png", record_pos=(-0.44, -0.271), resolution=(2224, 1668))
Story_Character_Pic = Template(r"tpl1678429751918.png", record_pos=(0.26, 0.113), resolution=(2224, 1668))
Skip_Pic = Template(r"tpl1678431493179.png", record_pos=(0.082, 0.194), resolution=(2224, 1668))
Quest_Page_Pic = Template(r"tpl1678436934821.png", record_pos=(0.131, 0.104), resolution=(2224, 1668))
Quest_Daily_Pic = Template(r"tpl1678439969025.png", record_pos=(-0.003, -0.031), resolution=(2224, 1668))
Quest_JingYan_Pic = Template(r"tpl1678439997347.png", record_pos=(-0.346, -0.353), resolution=(2224, 1668))
Quest_HaoGan_Pic = Template(r"tpl1678440024744.png", record_pos=(-0.322, -0.35), resolution=(2224, 1668))
Quest_JinBi_Pic = Template(r"tpl1678440043013.png", record_pos=(-0.355, -0.353), resolution=(2224, 1668))
Quest_SiDa_Pic = Template(r"tpl1678440059060.png", record_pos=(-0.36, -0.356), resolution=(2224, 1668))
Quest_Event_Pic = Template(r"tpl1678518798688.png", record_pos=(0.402, 0.221), resolution=(2224, 1668))

Quest_Xilai_Lv80_Pic = Template(r"tpl1684398881004.png", record_pos=(0.301, 0.026), resolution=(2224, 1668))
# ----以下为坐标---------------

Ok_Coordinate = (1245, 1027)
Ok_Present_Coordinate = (1102, 1115)
Close_Present_Coordinate = (2057, 373)
Present_Box_Coordinate = (202, 182)
Present_Get_Coordinate = (1764, 1288)
Close_PresentBox_Coordinate = (1897, 277)
Story_Coordinate = (800, 1600)
Sub_Heroine_Coordinate = (1529, 394)
Main_Heroine_Coordinate = (1353, 397)
Quest_Coordinate = (1102, 1584)
Fragment_Check_Coordinate = (1377, 1222)
Story_Character_Coordinate = (839, 1201)
Close_Fragment_Coordinate = (1540, 350)
Return_Coordinate = (78, 30)
Quest_Fragment_Coordinate = (1989, 1095)
Skip_Coordinate = (1283, 1258)
Close_Result_Coordinate = (1622, 317)
Close_Quest_Coordinate = (1814, 303)
Quest_Master_Coordinate = (169, 474)
Quest_Daily_Coordinate = (632, 1076)
Quest_Main_Coordinate = (723, 562)
Quest_Sub_Coordinate = (1441, 593)
Quest_Tower_Coordinate = (1403, 1050)
Quest_Event_Coordinate = (1883, 1038)
Quest_Master_2_Coordinate = (1069, 1307)
Quest_Daily_13_Coordinate = (1987, 1134)
Quest_JingYan_Coordinate = (352, 784)
Quest_HaoGan_Coordinate = (834, 784)
Quest_JinBi_Coordinate = (1341, 784)
Quest_SiDa_Coordinate = (1806, 784)
Close_JinBi_Result_Coordinate = (2047, 1364)
Quest_XiLai_Coordinate = (2087, 1348)
Quest_Xilai_Lv80_Coordinate = (1774, 1058)
Quest_XiLai_Fight_Coordinate = (1423, 1256)
Battle_Coordinate = (2074, 1501)
Battle_Next_Coordinate = (2012, 1369)
Quest_Sub_10_Coordinate = (1286, 1061)
Quest_Sub_1_Coordinate = (268, 889)
Quest_Sub_2_Coordinate = (536, 571)
Quest_Sub_3_Coordinate = (823, 884)
Quest_Sub_4_Coordinate = (1114, 566)
Quest_Sub_5_Coordinate = (1398, 891)
Quest_Sub_6_Coordinate = (1681, 564)
Quest_Sub_7_Coordinate = (1947, 884)
Home_Page_Coordinate = (161, 1603)
Mission_Coordinate = (314, 192)
Mission_Get_Coordinate = (1806, 1173)
Sub_Left_Coordinate = (86, 727)
Quest_Event_Quest_Coordinate = (1990, 1310)
Quest_Event_1_Coordinate = (249, 886)
Quest_Event_2_Coordinate = (660, 751)
Quest_Event_3_Coordinate = (1115, 900)
Quest_Event_4_Coordinate = (1540, 740)
Quest_Event_5_Coordinate = (1956, 977)
Daily_Finish_Button_Coordinate = (158, 365)
Close_News_Coordinate = (1700, 1208)
Check_Game_Mode_Coordinate = (214, 47)
Get_Fragment_Coordinate = (1116, 1136)
Button_Finish_Quest_Coordinate = (2019, 1584)

# ------以下为变量------------
# Log_Dir = './log'
Log_Dir = './LegenClover/log'
Game_Name = "com.dmm.games.legeclo"

Game_Process = 0
Fragment_Heroine = 0
Sub_Count = 0

Fragment_Heroine_List = [
    2, Nimue_Val_Pic, Nimue_Val_Q_Pic,
    2, Hadesu_Sch_Pic, Hadesu_Sch_Q_Pic,
    1, Master_White_Pic, Master_White_Q_Pic,
    1, Master_Red_Pic, Master_Red_Q_Pic,
    2, Soru_Pic, Soru_Q_Pic,
    2, Izanami_Pic, Izanami_Q_Pic,
    1, MansaMuusa_Pic, MansaMuusa_Q_Pic
]

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

Event_List = [
    Quest_Event_1_Coordinate,
    Quest_Event_2_Coordinate,
    Quest_Event_3_Coordinate,
    Quest_Event_4_Coordinate,
    Quest_Event_5_Coordinate,
]

Tower_R, Tower_G, Tower_B = 167, 130, 101
XiLai_R, XiLai_G, XiLai_B = 113, 163, 252
Tower_Pixel_X, Tower_Pixel_Y = 1377, 1182
XiLai_Pixel_X, XiLai_Pixel_Y = 991, 571
Main_2_XiLai_Pixel_X, Main_2_XiLai_Pixel_Y = 2087, 1348
Main_2_XiLai_Pixel_R, Main_2_XiLai_Pixel_G, Main_2_XiLai_Pixel_B = 74, 19, 102

Daily_Finish_Button_Coordinate_RGB = (227, 231, 208)
Check_Game_Mode_Coordinate_Home_Page_RGB = (160, 123, 218)
Check_Game_Mode_Coordinate_Story_RGB = (255, 255, 255)
Check_Game_Mode_Coordinate_Query_RGB = (82, 63, 48)
Check_Game_Mode_Coordinate_Main_Query_RGB = (173, 136, 231)
Check_Game_Mode_Coordinate_Sub_Query_RGB = (208, 125, 111)
Check_Game_Mode_Coordinate_Sub_Episode_RGB = (253, 196, 151)
Check_Game_Mode_Coordinate_Tower_RGB = (208, 204, 227)
Check_Game_Mode_Get_Login_Bonus_RGB = (73, 44, 92)
Check_Game_Mode_Quest_Finish_RGB = (131, 158, 123)
Check_Game_Mode_Mission_Finish_RGB = (39, 72, 125)

Quest_XiLai_Check_RGB_Coordinate = (2052, 1307)
Quest_XiLai_Check_RGB = (57, 2, 85)


# ----------------------------------基础程序部分（此部分所有游戏一致，不需要更改）--------------------------------------------

# 未裁剪的图片，也就是还没有打开过的图片就用这个来读取ocr,此时读取的应该是全地址。更改为判断游戏状态相关
def Pic_Ocr_Unshape():
    snapshot(filename='Game_Pic.jpg')
    Pic_Dir = Log_Dir + '/Game_Pic.jpg'
    Ocr_Pic = Image.open(Pic_Dir)
    Ocr_Text = pytesseract.image_to_string(Ocr_Pic, lang='jpn')
    return (Ocr_Text)


def Remove_Temp_File():
    for root, dirs, files in os.walk(Log_Dir, topdown=False):
        for name in files:
            try:
                os.remove(os.path.join(root, name))
            except:
                continue


def Exit_Game():
    print("游戏结束，退出游戏")
    stop_app(Game_Name)
    Remove_Temp_File()
    exit()


def Get_Pixel_Rgb(Coordinate):
    snapshot(filename='Game_Pic.jpg')
    Pic_Dir = Log_Dir + '/Game_Pic.jpg'
    Img_Pic = Image.open(Pic_Dir)
    r, g, b = Img_Pic.getpixel(Coordinate)
    return (r, g, b)


def Pic_Ocr_Shape(x1, y1, x2, y2):
    if x1 < x2:
        xx1 = x1
        xx2 = x2
    else:
        xx1 = x2
        xx2 = x1
    if y1 < y2:
        yy1 = y1
        yy2 = y2
    else:
        yy1 = y2
        yy2 = y1

    snapshot(filename='Game_Pic.jpg')
    Pic_Dir = Log_Dir + '/Game_Pic.jpg'
    Ocr_Pic = cv2.imread(Pic_Dir)
    Ocr_Auto_Pic = Ocr_Pic[yy1:yy2, xx1:xx2]
    # CV2_Show_Pic(Ocr_Auto_Pic)
    Ocr_Text = pytesseract.image_to_string(Ocr_Auto_Pic, config="-c tessedit_char_whitelist=0123456789/")
    return (Ocr_Text)


def CV2_Show_Pic(Pic_Data):
    cv2.namedWindow("image")  # 创建一个image的窗口
    cv2.imshow("image", Pic_Data)  # 显示图像
    cv2.waitKey()  # 默认为0，无限等待


# -----------------------------以下为各游戏的不同部分--------------------------------------------


def Check_Game_Mode(Ocr_Text, Game_Process):
    if "詳細な情報につきましては公式Twitterをご確認ください" in Ocr_Text:
        print("正在更新中，请切换下个游戏")
        Exit_Game()
        return 0

    if "Loading" in Ocr_Text and "容量" not in Ocr_Text:
        print("等待中")
        return 1

    if "このゲームではサウンドが再生されます。" in Ocr_Text:
        print("音量设定")
        return 2

    if "CLOVER" in Ocr_Text:
        print("标题界面")
        return 3

    if "ログインボーナス" in Ocr_Text:
        print("领取完成")
        return 3.5

    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Home_Page_RGB:
        print("当前在主页界面")
        return 4

    if "マスターランク" in Ocr_Text:
        print("正在领取礼物")
        return 5
        '''
        if exists(Present_Box_Pic):
            print("正在领取礼物")
            touch(Present_Get_Coordinate)
            sleep(2)
            return 5
        '''

    if "以下のプレゼントを受け取りました" in Ocr_Text:
        print("礼物领取完成")
        return 6

    if "現在受け取れるプレゼントはありません" in Ocr_Text:
        print("关闭礼物盒子")

        return 6.5

    '''
    if  Game_Mode_RGB == Check_Game_Mode_Get_Login_Bonus_RGB:
        print("正在尝试进入主界面")
        touch(Close_Present_Coordinate)
        return 3
        '''

    if "フラグメント" in Ocr_Text:
        print("当前在判断碎片个数")
        return 7

    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Story_RGB and Game_Process != 0:
        print("故事界面")
        return 8
        '''
        if exists(Story_Pic):
            print("故事界面")
            return 8
        '''

    '''
    if "報酬" in Ocr_Text and "訓練" not in Ocr_Text and "13回" not in Ocr_Text and "ミルク" not in Ocr_Text and "獲得報酬" not in Ocr_Text:
        if exists(Quest_Daily_Pic):
            print("每日任务界面")
            return 9
    
    if "訓練場" in Ocr_Text:
        if exists(Quest_JingYan_Pic):
            print("经验本")
            Quest_Skip(Quest_Daily_13_Coordinate,Skip_Coordinate)
            return 10
    
    if "ケーキ" in Ocr_Text:
        if exists(Quest_HaoGan_Pic):
            print("好感本")
            Quest_Skip(Quest_Daily_13_Coordinate,Skip_Coordinate)
            return 11
    
    if "洞窟探索" in Ocr_Text:
        if exists(Quest_JinBi_Pic):
            print("金币本")
            Quest_Skip(Quest_Daily_13_Coordinate,Skip_Coordinate)
            sleep(5)
            touch(Close_JinBi_Result_Coordinate)
            sleep(5)
            touch(Return_Coordinate)
            return 12
    
    if "形態" in Ocr_Text:
        if exists(Quest_SiDa_Pic):
            print("厄神本")
            Quest_Skip(Quest_Daily_13_Coordinate,Skip_Coordinate)
            return 13
    
    '''

    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Tower_RGB:
        print("霸者之塔界面")
        return 14

    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Sub_Query_RGB and "挑戦" not in Ocr_Text:
        print("Sub关卡选择第几部")
        return 15

    '''
    if  "入手可能" in Ocr_Text:
        if exists(Story_Character_Pic):
            print("故事模块个人界面")
            return 16
        '''
    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Query_RGB:
        print("Quest界面")
        return 17

        '''
    if "クラスへの" in Ocr_Text:
        print("大师本界面")
        Quest_Skip(Quest_Master_2_Coordinate,Skip_Coordinate)
        return 16
    '''

    if Game_Mode_RGB == Check_Game_Mode_Coordinate_Main_Query_RGB:
        print("Main Quest界面")
        return 17.5

    if "リスト" in Ocr_Text:
        print("袭来界面")
        return 18

    if "おまかせ編成" in Ocr_Text:
        print("战斗界面")
        return 19

    if "TURN" in Ocr_Text or "オート解除" in Ocr_Text:
        print("战斗中")
        return 20

    if "上限" in Ocr_Text:
        print("战斗结束")
        return 21

    if Game_Mode_RGB == Check_Game_Mode_Quest_Finish_RGB and Game_Process == 10:
        print("Main_Quest完成")
        touch(Button_Finish_Quest_Coordinate)
        return 21

    if "挑戦" in Ocr_Text:
        print("Sub关卡选择")
        return 22

    if "ログインのみのミッションは含まない" in Ocr_Text:
        print("任务界面")
        return 23

    if "獲得報酬" in Ocr_Text and "索計獲得報酬" not in Ocr_Text:
        return 24

    if "累計イベントアイテム" in Ocr_Text:
        print("活动界面")
        return 25

    if "索計獲得報酬" in Ocr_Text:
        print("Event奖励获得")
        return 26

    '''
    if "本日あと" in Ocr_Text:
        print("活动挑战界面")
        return 27
    '''

    if "容量" in Ocr_Text:
        print("需要更新")
        return 28

    if "完了" in Ocr_Text:
        print("更新完成")
        return 29

    if "次回以降は表示しない" in Ocr_Text:
        print("公告界面")
        return 30

    if Game_Mode_RGB == Check_Game_Mode_Mission_Finish_RGB:
        print("每日任务领取完成")
        return 31


# 此函数为判断当前碎片个数，并给出如下逻辑，返回目前有的碎片数和当前升星所需要的碎片数，若需要升星的碎片数不为50或100，即为150，表明此时为五星，按照目前规划，不需要升级。因此
# 当前的个数不应该超过100，后续给出判断，若当前数大于100，就不跑这个碎片本。此函数应当在故事模块中个人页里的详细中进行查看。
def Get_Fragment_Num():
    Ocr_Text = Pic_Ocr_Shape(1060, 1010, 1190, 1045)

    Fragent_List = Ocr_Text.split('/')
    Fragent_Need = Fragent_List[1]
    Fragent_Now = Fragent_List[0]
    return (int(Fragent_Need), int(Fragent_Now))


# 以下两个函数用来在角色碎片中滑动
def Heroine_Swipe():
    swipe((1671, 1098), (1674, 840))


def Heroine_Swipe_Count():
    swipe((1674, 840), (1671, 1098))


# 此函数用来获取今日可以打几次故事模式
def Get_Fragment_Times():
    Ocr_Text = Pic_Ocr_Shape(1940, 9, 2065, 70)

    Fragent_List = Ocr_Text.split('/')
    Fragent_Now_Times = Fragent_List[0]
    return (int(Fragent_Now_Times))


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
                touch(Return_Coordinate)
                continue
            else:
                # Quest_Skip(Quest_Fragment_Coordinate,Skip_Coordinate)
                touch(Get_Fragment_Coordinate)
                sleep(1)
                touch(Close_Fragment_Coordinate)
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
        elif SwipeCount < 7:
            Heroine_Swipe()
            sleep(5)
            SwipeCount = SwipeCount + 1
        else:
            Heroine_Swipe_Count()
            sleep(5)


# 此函数用于所有跳过
def Quest_Skip(Quest_Coordinate, Skip_Coordinate):
    sleep(5)
    touch(Quest_Coordinate)
    sleep(5)
    touch(Skip_Coordinate)
    sleep(5)
    touch(Close_Result_Coordinate)
    sleep(3)
    touch(Close_Quest_Coordinate)
    sleep(3)
    touch(Return_Coordinate)


# 此函数中不带返回操作
def Quest_Skip_NoReturn(Quest_Coordinate, Skip_Coordinate):
    sleep(3)
    touch(Quest_Coordinate)
    sleep(5)
    touch(Skip_Coordinate)
    sleep(5)
    touch(Close_Result_Coordinate)
    sleep(3)
    touch(Close_Quest_Coordinate)


def Get_Stamina():
    Ocr_Text = Pic_Ocr_Shape(1041, 63, 1211, 8)
    Ocr_Text_List = Ocr_Text.split('/')
    Stamina = Ocr_Text_List[0]
    return (int(Stamina))


# ----------------------------------主程序部分(不需要更改)--------------------------------------------

if __name__ == '__main__':
    start_app(Game_Name)

    now = datetime.datetime.now()
    weekday = now.weekday()

    while True:

        Game_Ocr_Text = Pic_Ocr_Unshape()
        try:
            print(Game_Ocr_Text)
        except:
            pass

        Game_Mode_RGB = Get_Pixel_Rgb(Check_Game_Mode_Coordinate)
        print(Game_Mode_RGB)

        # --------------------------------以下部分为主程序中的专属部分-----------------------------

        # ------------------------    测试代码可在上面写,下面为正式代码----------------------------
        Game_Mode = Check_Game_Mode(Game_Ocr_Text, Game_Process)
        print(Game_Mode)
        if Game_Mode == 2:
            # 音量设定
            touch(Ok_Coordinate)
            sleep(2)
            touch(Ok_Coordinate)
            continue

        if Game_Mode == 3:
            # 标题界面
            touch(Ok_Coordinate)
            continue

        if Game_Mode == 3.5:
            # 每日奖励领取完成
            touch(Ok_Present_Coordinate)
            sleep(6)
            touch(Close_Present_Coordinate)
            touch(Close_Present_Coordinate)
            Game_Process = 0

        # 第一次在主界面是刚登录的时候，此时先收礼物
        if Game_Mode == 4 and Game_Process == 0:
            touch(Present_Box_Coordinate)
            Game_Process = Game_Process + 1
            continue

        # 第二次在主界面是收取完成礼物后，此时先打碎片
        if Game_Mode == 4 and Game_Process == 1:
            touch(Story_Coordinate)
            Game_Process = 8
            continue

        if Game_Mode == 5:
            # 正在领取礼物
            touch(Present_Get_Coordinate)
            sleep(2)
            continue

        if Game_Mode == 6:
            # 礼物领取完成
            sleep(1)
            touch(Ok_Present_Coordinate)
            continue

        if Game_Mode == 6.5:
            # 关闭礼物盒子
            touch(Close_PresentBox_Coordinate)
            continue

        if Game_Mode == 7:
            # 判断碎片个数
            Get_Fragment_Num()
            continue

        # 进入角色碎片界面,打完后进入Quest界面
        if Game_Mode == 8:
            Query_Fragment()
            sleep(2)
            touch(Quest_Coordinate)
            continue

        '''
        #进入Quest界面，总共有六个步骤需要进行，首先打Master本
        if Game_Mode == 17 and  Game_Process == 2:
            touch(Quest_Master_Coordinate)
            Game_Process = 3
            continue

        #打每日本，每日本中有四个，因此分开进行
        if Game_Mode == 17 and Game_Process == 3:
            touch(Quest_Daily_Coordinate)
            continue

        if Game_Mode == 9 and Game_Process < 8:
            if Game_Process == 3:
                touch(Quest_JingYan_Coordinate)
            if Game_Process == 4:
                touch(Quest_HaoGan_Coordinate)
            if Game_Process == 5:
                touch(Quest_JinBi_Coordinate)
            if Game_Process == 6:
                touch(Quest_SiDa_Coordinate)
            if Game_Process == 7:
                touch(Return_Coordinate)
            Game_Process = Game_Process + 1
            continue
        '''

        if Game_Mode == 14:
            # 霸者之塔界面
            Tower_Now_R, Tower_Now_G, Tower_Now_B = Get_Pixel_Rgb((Tower_Pixel_X, Tower_Pixel_Y))
            if Tower_Now_R == Tower_R and Tower_Now_G == Tower_G and Tower_Now_B == Tower_B:
                touch(Return_Coordinate)
            continue

        if Game_Mode == 15:
            # Sub关卡选择第几部
            touch(Quest_Sub_10_Coordinate)
            continue

        # 查看勇者之塔
        if Game_Mode == 17 and Game_Process == 8:
            touch(Quest_Tower_Coordinate)
            Game_Process = Game_Process + 1
            continue

        # Main Quest打袭来
        if Game_Mode == 17 and Game_Process == 9:
            touch(Quest_Main_Coordinate)
            continue

        if Game_Mode == 17.5:
            # 已进入Main Quest界面
            Quest_XiLai_Check_Now_RGB = Get_Pixel_Rgb(Quest_XiLai_Check_RGB_Coordinate)
            if Quest_XiLai_Check_Now_RGB != Quest_XiLai_Check_RGB:
                touch(Quest_XiLai_Coordinate)
            else:
                touch(Quest_Coordinate)
                Game_Process = Game_Process + 1
                sleep(5)
            continue

        # 打Sub
        if Game_Mode == 17 and Game_Process == 10:
            touch(Quest_Sub_Coordinate)
            continue

        if Game_Mode == 18:
            # 袭来界面
            XiLai_Now_R, XiLai_Now_G, XiLai_Now_B = Get_Pixel_Rgb((XiLai_Pixel_X, XiLai_Pixel_Y))
            if XiLai_Now_R == XiLai_R and XiLai_Now_G == XiLai_G and XiLai_Now_B == XiLai_B:
                touch((XiLai_Pixel_X, XiLai_Pixel_Y))
                sleep(1)
                touch(Quest_Xilai_Lv80_Pic)
                sleep(5)
                touch(Quest_XiLai_Fight_Coordinate)
            continue

        if Game_Mode == 19:
            # 战斗界面
            touch(Battle_Coordinate)
            continue

        if Game_Mode == 21:
            # 战斗界面
            touch(Battle_Next_Coordinate)
            sleep(10)
            touch(Button_Finish_Quest_Coordinate)
            continue

        # 打一关sub然后去拿每日任务
        if Game_Mode == 22 and Game_Process == 10:
            Quest_Skip_NoReturn(Quest_Sub_6_Coordinate, Skip_Coordinate)
            sleep(2)
            touch(Home_Page_Coordinate)
            Game_Process = Game_Process + 1
            continue

        if Game_Mode == 4 and Game_Process == 11:
            touch(Daily_Finish_Button_Coordinate)
            Game_Process = Game_Process + 1
            continue

        if Game_Mode == 4 and Game_Process == 12:
            touch(Mission_Coordinate)
            Game_Process = Game_Process - 1
            continue

        if Game_Mode == 31:
            touch(Quest_Coordinate)
            sleep(1)
            touch(Quest_Coordinate)
            continue

        if Game_Mode == 17 and Game_Process == 11:
            touch(Quest_Sub_Coordinate)
            continue

        # 只有体力大于10的时候才跑sub，否则回到Quest界面执行下个操作
        if Game_Mode == 22 and Game_Process == 11:
            Stamina = Get_Stamina()
            if Stamina >= 10:
                Quest_Skip_NoReturn(Sub_List[Sub_Count], Skip_Coordinate)
                Sub_Count = Sub_Count + 1
                if Sub_Count == 8:
                    Sub_Count = 0
            else:
                touch(Quest_Coordinate)
                Game_Process = Game_Process + 1
            continue

        if Game_Mode == 17 and Game_Process == 12:
            touch(Quest_Event_Coordinate)
            continue

        if Game_Mode == 23:
            # 领取每日任务
            touch(Mission_Get_Coordinate)
            sleep(5)
            touch(Close_PresentBox_Coordinate)
            continue

        if Game_Mode == 24:
            # 领取奖励
            touch(Ok_Present_Coordinate)
            sleep(2)
            touch(Ok_Present_Coordinate)
            sleep(3)
            touch(Quest_Coordinate)
            continue

        if Game_Mode == 25:
            if exists(Quest_Event_Pic):
                touch(Quest_Event_Quest_Coordinate)
                print("现在是活动时间")
            continue

        if Game_Mode == 27:
            for Event_Num in Event_List:
                Quest_Skip_NoReturn(Event_Num, Skip_Coordinate)
                touch(Return_Coordinate)
            Exit_Game()
            continue

        if Game_Mode == 28:
            # 更新
            touch(Ok_Coordinate)
            continue

        if Game_Mode == 29:
            # 更新完成
            touch(Ok_Present_Coordinate)
            continue

        if Game_Mode == 30:
            # 公告
            touch(Close_News_Coordinate)
            continue
