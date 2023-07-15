from airtest.core.api import *


class Universal_Variable:
    Return_Coordinate = (78, 30)
    Check_Game_Mode_Coordinate = (214, 47)
    Skip_Coordinate = (1283, 1258)

    Quest_Coordinate = (1102, 1584)
    Story_Coordinate = (800, 1600)
    Home_Page_Coordinate = (383, 1020)

    Ok_Present_Coordinate = (1102, 1115)
    Close_Present_Coordinate = (2057, 373)
    Close_Result_Coordinate = (1622, 317)
    Close_Quest_Coordinate = (1814, 303)

    # 以下为新写的，以下面为主
    Close_Button_Coordinate = (1623, 277)
    OK_Two_Button_Coordinate = (1333, 710)
    OK_One_Button_Coordinate = (1195, 710)
    Ready_Quest_Button_Coordinate = (1461, 907)


class Quest:

    def Quest_Skip(self, Quest_Coordinate, Skip_Coordinate):
        sleep(5)
        touch(Quest_Coordinate)
        sleep(5)
        touch(Skip_Coordinate)
        sleep(5)
        touch(Universal_Variable.Close_Result_Coordinate)
        sleep(3)
        touch(Universal_Variable.Close_Quest_Coordinate)
        sleep(3)
        touch(Universal_Variable.Return_Coordinate)

    # 此函数中不带返回操作
    def Quest_Skip_NoReturn(self, Quest_Coordinate, Skip_Coordinate):
        sleep(3)
        touch(Quest_Coordinate)
        sleep(5)
        touch(Skip_Coordinate)
        sleep(5)
        touch(Universal_Variable.Close_Result_Coordinate)
        sleep(3)
        touch(Universal_Variable.Close_Quest_Coordinate)
