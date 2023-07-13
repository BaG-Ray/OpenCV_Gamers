#----------------------------------引用部分（此部分所有脚本都一样，不需要修改）--------------------------------------------
# -*- encoding=utf8 -*-
#Version = 2.0
#Default_Scripts_Version = 2.4
#Update_Time = 2023.05.18

__author__ = "Ray"

import os
import shutil

import cv2
import pytesseract
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from PIL import Image

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["ios:///http+usbmux://00008020-001318C00A91002E",])

from poco.drivers.ios import iosPoco

poco = iosPoco()

#----------------------------------变量部分（需要改）--------------------------------------------

#-----以下为基础部分--------

Log_Dir = './AyakashiRanburu/log'
Game_Name = "com.dmm.games.ayarabu"


#----以下为图片--------------

Takamono_Now_Place_IsStory = Template(r"tpl1678944706838.png", record_pos=(-0.429, -0.059), resolution=(2224, 1668))
Takamono_Now_Place_IsQuest = Template(r"tpl1678948248497.png", record_pos=(-0.397, 0.069), resolution=(2224, 1668))
Takamono_Skip = Template(r"tpl1678947620600.png", record_pos=(0.446, -0.251), resolution=(2224, 1668))

#----以下为坐标--------------

Button_Close_News_Coordinate = (1123,1354)
Button_Get_Reward_Coordinate = (2096,732)
Button_Expedition_Coordinate = (1395,508)
Button_Expedition_Finish_Coordinate = (2033,1364)
Button_Expedition_First_Coordinate = (873,542)
Button_Expedition_Members_Coordinate = (1930,485)
Button_Expedition_Members_Determine_Coordinate = (2114,485)
Button_Return_Coordinate = (73,273)
Button_Summon_Coordinate = (2012,523)
Button_Summon_Up_Page_Coordinate = (289,386)
Button_Adventure_Coordinate = (1709,711)
Button_Training_Coordinate = (1567,1000)
Button_Daily_First_Coordinate = (236,884)
Button_Battle_Start_Coordinate = (1950,1187)
Button_Change_Team_Coordinate = (335,1377)
Button_Change_Party_Coordinate = (518,1338)
Button_Close_Energy_Shop_Coordinate = (1930,282)
Button_Present_Box_Coordinate = (88,771)
Button_Mission_Coordinate = (115,544)
Button_Get_Present_Coordinate = (1848,1346)


Team_Red_Coordinate = (1538,408)
Team_Green_Coordinate = (1648,408)
Team_Blue_Coordinate = (1759,408)
Team_Yellow_Coordinate = (1876,414)
Team_Purple_Coordinate = (1989,418)
Team_Weapon_Check_RGB_Coordinate = (496,608)

#------RGB颜色判定------------

Check_Game_Mode_RGB_Coordinate = (35,1292)
Game_Mode_Login_RGB = (29, 107, 145)
Game_Mode_Loading_RGB = (0, 0, 0)
Game_Mode_Login_Bonus_RGB =(24, 163, 222)
Game_Mode_Login_Bonus_Finish_RGB = (143, 42, 12)
Game_Mode_News_RGB = (82, 63, 48)
Game_Mode_Home_Page_1_RGB = (255, 238, 162)
Game_Mode_Home_Page_2_RGB = (255, 239, 155)
'''
Game_Mode_Home_Page_3_RGB = (255, 224, 166)
Game_Mode_Home_Page_4_RGB = (245, 234, 168)
Game_Mode_Home_Page_5_RGB = (255, 227, 166)
'''
Game_Mode_Expedition_Page_RGB = (174, 92, 55)
Game_Mode_Expedition_Finish_RGB = (145, 172, 141)
Game_Mode_Expedition_Member_RGB = (137, 97, 89)
Game_Mode_Summon_RGB = (149, 88, 67)
Game_Mode_Adventure_RGB = (169, 132, 103)
Game_Mode_Daily_RGB = (113, 51, 30)
Game_Mode_Team_Change_RGB = (45, 26, 11)
Game_Mode_Battle_Finish_RGB = (255, 226, 222)
Game_Mode_Get_Experience_RGB = (255, 235, 115)
Game_Mode_Null_Energy_RGB = (8, 8, 8)
Game_Mode_Present_Box_RGB = (149, 90, 46)

'''
Team_Red_Not_Choose_RGB = (244, 160, 98)
Team_Green_Not_Choose_RGB = (139, 205, 97)
Team_Blue_Not_Choose_RGB = (194, 212, 212)
Team_Yellow_Not_Choose_RGB =(255, 255, 194)
Team_Purple_Not_Choose_RGB = (206, 147, 253)
Team_Red_Choose_RGB = (139, 205, 97)
Team_Green_Choose_RGB = (214, 245, 214)
Team_Blue_Choose_RGB = (112, 162, 213)
Team_Yellow_Choose_RGB =(219, 175, 70)
Team_Purple_Choose_RGB = (247, 222, 244)
Team_Not_Weapon_RGB = (255, 205, 181)
'''

#------以下为变量------------

Game_Process = 0
Game_Course = 0

#----------------------------------基础程序部分（此部分所有游戏一致，不需要更改）--------------------------------------------

#未裁剪的图片，也就是还没有打开过的图片就用这个来读取ocr,此时读取的应该是全地址。更改为判断游戏状态相关
def Pic_Ocr_Unshape():
    snapshot(filename = 'Game_Pic.jpg')
    Pic_Dir = Log_Dir + '/Game_Pic.jpg'
    Ocr_Pic = Image.open(Pic_Dir)
    Ocr_Text = pytesseract.image_to_string(Ocr_Pic, lang='jpn')
    return(Ocr_Text)

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
    snapshot(filename = 'Game_Pic.jpg')
    Pic_Dir = Log_Dir + '/Game_Pic.jpg'
    Img_Pic = Image.open(Pic_Dir)
    r, g, b = Img_Pic.getpixel(Coordinate)
    #CV2_Circle_Pic(Pic_Dir,Coordinate)
    return (r,g,b)

def Pic_Ocr_Shape(x1,y1,x2,y2):
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

    snapshot(filename = 'Game_Pic.jpg')
    Pic_Dir = Log_Dir + '/Game_Pic.jpg'
    Ocr_Pic = cv2.imread(Pic_Dir)
    Ocr_Auto_Pic = Ocr_Pic[yy1:yy2,xx1:xx2]  
    Ocr_Text = pytesseract.image_to_string(Ocr_Auto_Pic, lang='eng')
    return(Ocr_Text)

def CV2_Show_Pic(Pic_Data):
        cv2.namedWindow("image")     # 创建一个image的窗口
        cv2.imshow("image", Pic_Data)    # 显示图像
        cv2.waitKey()               # 默认为0，无限等待

def CV2_Circle_Pic(Pic_Dir,Coordinate):
    Cv2_Img = cv2.imread(Pic_Dir)
    Cv2_Circle = cv2.circle(Cv2_Img,Coordinate,5,(255, 0, 255),-1)
    CV2_Circle_Resize = cv2.resize(Cv2_Circle, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
    CV2_Show_Pic(CV2_Circle_Resize)
#-----------------------------以下为各游戏的不同部分--------------------------------------------
'''
def Get_Team_Advice():
    #此函数用来判断推荐属性
    Team_Red_Now_RGB = Get_Pixel_Rgb(Team_Red_Coordinate)
    Team_Green_Now_RGB = Get_Pixel_Rgb(Team_Green_Coordinate)
    Team_Blue_Now_RGB = Get_Pixel_Rgb(Team_Blue_Coordinate)
    Team_Yellow_Now_RGB = Get_Pixel_Rgb(Team_Yellow_Coordinate)
    Team_Purple_Now_RGB = Get_Pixel_Rgb(Team_Purple_Coordinate)

    if Team_Red_Now_RGB == Team_Red_Choose_RGB:
        return 1
    elif Team_Green_Now_RGB == Team_Green_Choose_RGB:
        return 2
    elif Team_Blue_Now_RGB == Team_Blue_Choose_RGB:
        return 3
    elif Team_Yellow_Now_RGB == Team_Yellow_Choose_RGB:
        return 4
    elif Team_Purple_Now_RGB == Team_Purple_Choose_RGB:
        return 5
    
def Get_Team_Weapon():
    #此函数用来判断武器在谁身上
    #通过每个队伍的第一位角色的武器栏来判断武器目前在哪个队伍身上
    
    touch(Team_Red_Coordinate)
    Team_Weapon_Check_RGB = Get_Pixel_Rgb(Team_Weapon_Check_RGB_Coordinate)
    if Team_Weapon_Check_RGB != Team_Not_Weapon_RGB:
        return 1
    
    touch(Team_Green_Coordinate)
    Team_Weapon_Check_RGB = Get_Pixel_Rgb(Team_Weapon_Check_RGB_Coordinate)
    if Team_Weapon_Check_RGB != Team_Not_Weapon_RGB:
        return 2
    
    touch(Team_Blue_Coordinate)
    Team_Weapon_Check_RGB = Get_Pixel_Rgb(Team_Weapon_Check_RGB_Coordinate)
    if Team_Weapon_Check_RGB != Team_Not_Weapon_RGB:
        return 3
    
    touch(Team_Yellow_Coordinate)
    Team_Weapon_Check_RGB = Get_Pixel_Rgb(Team_Weapon_Check_RGB_Coordinate)
    if Team_Weapon_Check_RGB != Team_Not_Weapon_RGB:
        return 4
    
    touch(Team_Purple_Coordinate)
    Team_Weapon_Check_RGB = Get_Pixel_Rgb(Team_Weapon_Check_RGB_Coordinate)
    if Team_Weapon_Check_RGB != Team_Not_Weapon_RGB:
        return 5
        

#突然发现每个队伍是可以保存武器的，因此就不需要此函数来切换了
def Team_Change():
    #此函数用来实现将队伍切换成推荐属性的队伍，并装备上武器
    #先说下思路，首先由于点击战斗时，弹出的队伍窗口就是推荐的队伍。因此没有必要去识别
    #推荐属性的颜色，只需要判断目前打开的是哪个队伍的界面即可。因此通过识别五种队伍的
    #颜色来判断。之后在通过每个队伍的第一位角色的武器栏来判断武器目前在哪个队伍身上
    #之后在切换即可

    #首先第一步来判断推荐属性
    Team_Advice = Get_Team_Advice()
    #然后判断武器在哪个队伍上
    Team_Weapon = Get_Team_Weapon()

    #由于Get_Team_Weapon()中，在判断出了哪个队伍有武器后，就不再改变了，因此
    #此时停留的队伍就是有武器的那个队伍
    if Team_Advice != Team_Weapon:
        #如果两个是相同的，则不需要再改变队伍了
        touch(Button_Change_Team_Coordinate)
'''

def Check_Game_Mode():
    if Game_Mode_RGB == Game_Mode_Login_RGB:
        print("登陆界面")
        return 0
    
    if Game_Mode_RGB == Game_Mode_Loading_RGB or "oadjing" in Game_Ocr_Text:
        print("等待中")
        return 1
    
    if Game_Mode_RGB == Game_Mode_Login_Bonus_RGB:
        print("领取每日奖励")
        return 2
    
    if Game_Mode_RGB == Game_Mode_Login_Bonus_Finish_RGB:
        print("每日奖励领取完成")
        return 3
    
    if Game_Mode_RGB == Game_Mode_News_RGB:
        print("公告界面")
        return 4
    
    if Game_Mode_RGB == Game_Mode_Home_Page_1_RGB or \
        Game_Mode_RGB == Game_Mode_Home_Page_2_RGB:
        print("主界面")
        return 5
    
    if Game_Mode_RGB == Game_Mode_Expedition_Page_RGB:
        print("远征界面")
        return 6
    
    if Game_Mode_RGB == Game_Mode_Expedition_Finish_RGB:
        print("远征完成")
        return 7
    
    if Game_Mode_RGB == Game_Mode_Expedition_Member_RGB:
        print("远征选人")
        return 8
    
    if Game_Mode_RGB == Game_Mode_Summon_RGB:
        print("召唤界面")
        return 9
    
    if Game_Mode_RGB == Game_Mode_Adventure_RGB:
        print("冒险菜单选择界面")
        return 10
    
    if Game_Mode_RGB == Game_Mode_Daily_RGB:
        print("每日挑战界面")
        return 11
    
    if Game_Mode_RGB == Game_Mode_Team_Change_RGB:
        print("队伍选择界面")
        return 12
    
    if Game_Mode_RGB == Game_Mode_Battle_Finish_RGB:
        print("战斗结束")
        return 13
    
    if Game_Mode_RGB == Game_Mode_Get_Experience_RGB:
        print("战后奖励")
        return 14
    
    if Game_Mode_RGB == Game_Mode_Null_Energy_RGB:
        print("体力用完")
        return 15
    
    if Game_Mode_RGB == Game_Mode_Present_Box_RGB:
        print("礼物界面或任务界面")
        return 16

#----------------------------------主程序部分(不需要更改)--------------------------------------------
        
    
if __name__ == '__main__':
    start_app(Game_Name)

    while True:
        
        Game_Ocr_Text = Pic_Ocr_Unshape()
        Game_Mode_RGB = Get_Pixel_Rgb(Check_Game_Mode_RGB_Coordinate)

        try:
            print(Game_Ocr_Text)
        except:
            pass

        print(Game_Mode_RGB)
        #print(Get_Pixel_Rgb())
        Game_Mode = Check_Game_Mode()
        print(Game_Mode)

#--------------------------------以下部分为主程序中的专属部分-----------------------------
        
        if Game_Mode == 0 or Game_Mode == 2 or Game_Mode == 3:
            #登陆界面和每日登陆界面，随便点击进入即可
            touch(Check_Game_Mode_RGB_Coordinate)
            continue

        if Game_Mode == 4:
            #公告界面，点击关闭
            touch(Button_Close_News_Coordinate)
            continue

        if Game_Mode == 5:
            #主界面
            if Game_Process == 0:
                #第一次进入主界面，首先完成远征
                touch(Button_Expedition_Coordinate)
                Game_Process = Game_Process + 1
                continue

            if Game_Process == 5:
                #第二次进入主界面，点击冒险菜单
                touch(Button_Adventure_Coordinate)
                Game_Process = Game_Process + 1
                continue

            if Game_Process == 6:
                #领取礼物
                touch(Button_Present_Box_Coordinate)
                Game_Process = Game_Process + 1
                continue

            if Game_Process == 7:
                #领取任务奖励
                touch(Button_Mission_Coordinate)
                Game_Process = Game_Process + 1
                continue


        
    ###############################远征部分################################
        if Game_Mode == 6:
            #远征界面
            if Game_Process == 1:
                #首次进入远征界面，领取报酬
                touch(Button_Get_Reward_Coordinate)
                Game_Process = Game_Process + 1
                #由于每次远征完成的情况都不同，这里直接跳过
                sleep(5)
                touch(Button_Expedition_Finish_Coordinate)
                continue

            #接下来是三次的远征挂起
            if Game_Process < 5:
                #默认选择第一个进行远征
                touch(Button_Expedition_First_Coordinate)
                Game_Process = Game_Process + 1
                continue

            #远征任务结束，返回主界面
            if Game_Process == 5:
                touch(Button_Return_Coordinate)
                continue


        if Game_Mode == 7:
            #完成远征，选择第一个
            touch(Button_Expedition_Finish_Coordinate)
            continue

        if Game_Mode == 8:
            #远征选人，默认编程
            touch(Button_Expedition_Members_Coordinate)
            sleep(1)
            touch(Button_Expedition_Members_Determine_Coordinate)
            continue

        ###############################召唤部分################################
        
        ###############################日常部分################################
        
        if Game_Mode == 10:
            #在冒险菜单界面，选择修炼场完成日常
            touch(Button_Training_Coordinate)
            continue

        if Game_Mode == 11:
            #每日挑战界面,打开后默认就是推荐属性的队伍
            touch(Button_Daily_First_Coordinate)
            continue

        if Game_Mode == 12:
            #队伍选择界面，由于目前已经不再需要切换队伍来切换武器了，因此直接
            #开始战斗即可
            touch(Button_Battle_Start_Coordinate)
            continue

        if Game_Mode == 13:
            #战斗结束
            touch(Button_Expedition_Finish_Coordinate)
            continue

        if Game_Mode == 14:
            #领取战后奖励
            touch(Button_Expedition_Finish_Coordinate)
            continue

        if Game_Mode == 15:
            #体力用完，将返回主界面进行下一项操作
            touch(Button_Close_Energy_Shop_Coordinate)
            sleep(2)
            touch(Button_Return_Coordinate)
            sleep(2)
            touch(Button_Return_Coordinate)
            Game_Process = Game_Process + 1
            continue

       ###############################每日部分################################

        if Game_Mode == 16:
            #当前在礼物界面,同任务界面
            touch(Button_Get_Present_Coordinate)
            sleep(5)
            touch(Button_Get_Present_Coordinate)
            sleep(2)
            touch(Button_Return_Coordinate)
            continue