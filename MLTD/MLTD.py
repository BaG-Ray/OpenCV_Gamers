# ----------------------------------引用部分（此部分所有脚本都一样，不需要修改）--------------------------------------------
# -*- encoding=utf8 -*-
__author__ = "Ray"

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

Log_Dir = './MLTD/log'
# Log_Dir = './log'
Game_Name = "jp.co.bandainamcoent.BNEI0310"
Game_Process = 0

Default_Coordinate = (1116, 1134)
Present_Coordinate = (1097, 1296)
Present_Touch_Coordinate = (1487, 1436)
Ok_Button_Coordinate = (1460, 1130)
Close_Present_Coordinate = (750, 1445)
Live_Coordinate = (1116, 1544)
Live_Start_Coordinate = (1981, 1338)
Determine_Coordinate = (1460, 1345)
First_Help_Coordinate = (1895, 600)
Auto_Button_Coordinate = (1211, 1384)
Live_Real_Start_Coordinate = (1925, 1355)
Next_Coordinate = (1915, 1535)


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


# -----------------------------以下为各游戏的不同部分--------------------------------------------


def Check_Game_Mode(Ocr_Text):
    if "Connect" in Ocr_Text:
        print("等待中")
        return 0

    if "Loading" in Ocr_Text:
        print("等待中")
        return 0

    if "NAMCO" in Ocr_Text:
        print("开始界面")
        Default_Touch()
        return 1

    if "ログイン" in Ocr_Text and "獲得日時" not in Ocr_Text:
        print("奖励界面")
        sleep(5)
        Default_Touch()
        sleep(5)
        Default_Touch()
        sleep(5)
        Default_Touch()
        sleep(5)
        return 2

    if "Lv" in Ocr_Text and "チケツト使用" not in Ocr_Text and "アピール" not in Ocr_Text and "ボーナス適用中" not in Ocr_Text and "ファン数" not in Ocr_Text and "チケット使用" not in Ocr_Text and "覚醒ゲージ" not in Ocr_Text and "PERFECT" not in Ocr_Text and "楽曲Lv" not in Ocr_Text:
        print("当前在主界面")
        return 4

    if "受け取れるプレゼントはありません" in Ocr_Text:
        print("礼物接收完成")
        touch(Close_Present_Coordinate)
        return 5

    if "Wi-Fi" in Ocr_Text:
        print("需要更新")
        touch(Ok_Button_Coordinate)
        return 3

    if "閉じる" in Ocr_Text and "期限なし" not in Ocr_Text:
        print("关闭")
        touch(Template(r"tpl1678265858112.png", record_pos=(-0.161, 0.298), resolution=(2224, 1668)))
        return 6

    if "全て受け取る" in Ocr_Text:
        print("选择接收所有礼物")
        touch(Present_Touch_Coordinate)
        return 7

    if "よろしいですか?" in Ocr_Text:
        print("确认")
        touch(Ok_Button_Coordinate)
        return 8

    if "受け取りました" in Ocr_Text:
        print("接收完成")
        Default_Touch()
        return 9

    if "使用" in Ocr_Text:
        sleep(2)
        print("Live界面")
        sleep(2)
        touch(Live_Start_Coordinate)
        return 10

    if "選択した倍率を記憶する" in Ocr_Text:
        print("确定倍数界面")
        sleep(1)
        touch(Determine_Coordinate)
        sleep(2)
        return 11

    if "アピール" in Ocr_Text and "モード" not in Ocr_Text and "全ダイプのアピール" not in Ocr_Text:
        print("选人帮助界面")
        sleep(2)
        touch(First_Help_Coordinate)
        sleep(2)
        return 12

    if "モード" in Ocr_Text or "全ダイプのアピール" in Ocr_Text or "タイブの" in Ocr_Text:
        print("准备界面")
        sleep(2)
        touch(Auto_Button_Coordinate)
        sleep(2)
        touch(Live_Real_Start_Coordinate)
        sleep(5)
        return 13

    if "AUTO" in Ocr_Text and "PERFECT" not in Ocr_Text and "回復しました" not in Ocr_Text and "ミッシヨン達成報酬" not in Ocr_Text:
        print("正在自动打歌中")
        return 14

    if "PERFECT" in Ocr_Text:
        print("自动打歌完成")
        sleep(5)
        touch(Next_Coordinate)
        return 15

    if "回復しました" in Ocr_Text:
        print("等级提升")
        sleep(3)
        touch(Present_Coordinate)
        sleep(3)
        touch(Present_Coordinate)
        sleep(3)
        touch(Present_Coordinate)
        return 16

    if "ボーナス適用中" in Ocr_Text:
        print("歌曲完成奖励完成")
        sleep(1)
        touch(Next_Coordinate)
        return 17

    if "ミッシヨン達成報酬" in Ocr_Text:
        print("领取每日奖励")
        touch(Present_Touch_Coordinate)
        return 18

    if "ファン数" in Ocr_Text or "覚醒ゲージ" in Ocr_Text:
        print("好感度升级完成")
        touch(Next_Coordinate)
        Exit_Game()
        return 19

    if "明日は" in Ocr_Text:
        print("每日奖励领取完成")
        sleep(2)
        touch(Default_Coordinate)
        return 10


# mltd中的默认按钮
def Default_Touch():
    touch(Default_Coordinate)


# 接收礼物
def Get_Present():
    touch(Present_Coordinate)
    sleep(5)

    return 1


# 判断Auto卷还有多少张  识别不了，目前还不知道为什么，因此还是改成默认为1吧，也就不去考虑这个问题了
def Get_Auto_Quantity():
    Pic_Dir = Log_Dir + '/Game_Pic.jpg'
    Ocr_Pic = Image.open(Pic_Dir)
    Ocr_Auto_Pic = Ocr_Pic.crop((1363, 1358, 1441, 1408))
    Ocr_Text = pytesseract.image_to_string(Ocr_Auto_Pic, lang='equ')
    return (Ocr_Text)


# ----------------------------------主程序部分(不需要更改)--------------------------------------------


if __name__ == '__main__':
    start_app(Game_Name)
    while True:

        Game_Ocr_Text = Pic_Ocr_Unshape()
        try:
            print(Game_Ocr_Text)
        except:
            pass
        Game_Mode = Check_Game_Mode(Game_Ocr_Text)

        # --------------------------------以下部分为主程序中的专属部分-----------------------------

        if Game_Mode == 4 and Game_Process == 0:
            sleep(5)
            Game_Process = Get_Present()

        if Game_Mode == 4 and Game_Process == 1:
            sleep(5)
            touch(Live_Coordinate)
