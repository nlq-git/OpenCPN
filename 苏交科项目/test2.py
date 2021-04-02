# 获取浏河口至南京以外区域的辅助决策（完成开发，待验证）
import math
from math import *
from numpy import *
from sympy import *

class Warm_Danger_By_SOM():
    def __init__(self, list_own, list_ships):
        self.list_own = list_own  # [x，y，航向,速度,船长，船宽]
        self.list_ships = list_ships  # [[x，y，航向,mmsi，速度],[x，y，航向,mmsi，速度]...]
        self.time_danger = 1800

    def get_ships_near(self):
        list_ships_near = []

        X_own = self.list_own[0]  # 本船x
        Y_own = self.list_own[1]  # 本船y
        w = math.radians(self.list_own[2])  # 本船真航向
        L01 = 3704  # 长半轴，2nm
        B01 = 1481  # 短半轴，0.8nm

        for item in self.list_ships:
            if item[4] > 0.5:
                X_ship = item[0]  # 其他船舶x
                Y_ship = item[1]  # 其他船舶y

                result01 = ((Y_ship - Y_own) * math.cos(w) + (X_ship - X_own) * math.sin(w)) ** 2 / L01 ** 2 + (
                        (X_ship - X_own) * math.cos(w) - (Y_ship - Y_own) * math.sin(w)) ** 2 / B01 ** 2 - 1

                if result01 <= 0:
                    list_ships_near.append(item)
        return list_ships_near

    def get_danger_ships(self, list_ship):
        """
        list_ship=[x，y，航向,mmsi，速度]
        """
        ###########################计算速度大小########################
        #########本船的速度分量大小##########
        course_own = self.list_own[2]
        speed_own = self.list_own[3]

        if 0 <= course_own < 90:
            V0_x = -math.sin(course_own * math.pi / 180) * speed_own
            V0_y = -math.cos(course_own * math.pi / 180) * speed_own

        elif 90 <= course_own < 180:
            V0_x = -math.cos((course_own - 90) * math.pi / 180) * speed_own
            V0_y = math.sin((course_own - 90) * math.pi / 180) * speed_own

        elif 180 <= course_own < 270:
            V0_x = math.cos((270 - course_own) * math.pi / 180) * speed_own
            V0_y = math.sin((270 - course_own) * math.pi / 180) * speed_own

        else:
            V0_x = math.sin((360 - course_own) * math.pi / 180) * speed_own
            V0_y = -math.cos((360 - course_own) * math.pi / 180) * speed_own

        #########他船的速度分量大小##########
        course_ship = list_ship[2]
        speed_ship = list_ship[4]

        if 0 <= course_ship < 90:
            Vt_x = math.sin(course_ship * math.pi / 180) * speed_ship
            Vt_y = math.cos(course_ship * math.pi / 180) * speed_ship

        elif 90 <= course_ship < 180:
            Vt_x = math.cos((course_ship - 90) * math.pi / 180) * speed_ship
            Vt_y = -math.sin((course_ship - 90) * math.pi / 180) * speed_ship

        elif 180 <= course_ship < 270:
            Vt_x = -math.cos((270 - course_ship) * math.pi / 180) * speed_ship
            Vt_y = -math.sin((270 - course_ship) * math.pi / 180) * speed_ship

        else:
            Vt_x = -math.sin((360 - course_ship) * math.pi / 180) * speed_ship
            Vt_y = math.cos((360 - course_ship) * math.pi / 180) * speed_ship

        #########合速度分量大小##########

        V_x = V0_x + Vt_x
        V_y = V0_y + Vt_y

        V = math.sqrt(V_x ** 2 + V_y ** 2)
        # print("本船速度",V0_x,V0_y)
        # print("目标船速度", Vt_x, Vt_y)
        # print("合速度分量",V_x,V_y,V)
        ###########################计算速度方向########################
        # 速度方向
        if V_y != 0:
            if V_x == 0:
                if V_y < 0:
                    C = 180

                elif V_y > 0:
                    C = 0

            elif V_x < 0:
                if V_y < 0:
                    C = math.degrees(math.asin(abs(V_x) / V)) + 180

                elif V_y >= 0:
                    C = math.degrees(math.asin(abs(V_y) / V)) + 270


            else:
                if V_y < 0:
                    C = math.degrees(math.asin(abs(V_y) / V)) + 90

                elif V_y >= 0:
                    C = math.degrees(math.asin(abs(V_x) / V))

        if V_y == 0:
            if V_x < 0:
                C = 180

            elif V_x >= 0:
                C = 0
        #print("合速度方向",C)
        # 直线与X轴正半轴夹角rc
        if 0 <= C < 90:
            rc = 90 - C

        elif 90 <= C < 180:
            rc = 90 - C

        elif 180 <= C < 270:
            rc = 90 - (C - 180)

        else:
            rc = 90 - (C - 180)

        X_tar = list_ship[0]
        Y_tar = list_ship[1]

        k = math.tan(rc * math.pi / 180)
        b = Y_tar - k * X_tar

        w = math.radians(course_own)
        x = symbols('x')
        y = k * x + b
        ###########判断是否进入本船船舶领域
        L = self.list_own[4] * 3  # 船长
        B = self.list_own[4] * 0.5  # 船宽
        X_own = self.list_own[0]
        Y_own = self.list_own[1]

        if 0 <= course_own < 90:
            c_own = course_own * math.pi / 180
            X_inv = X_own + sin(c_own) * 0.25 * L
            Y_inv = Y_own + cos(c_own) * 0.25 * L

        elif 90 <= course_own < 180:
            c_own = (180 - course_own) * math.pi / 180
            X_inv = X_own + sin(c_own) * 0.25 * L
            Y_inv = Y_own - cos(c_own) * 0.25 * L

        elif 180 <= course_own < 270:
            c_own = (course_own - 180) * math.pi / 180
            X_inv = X_own - sin(c_own) * 0.25 * L
            Y_inv = Y_own - cos(c_own) * 0.25 * L

        else:
            c_own = (360 - course_own) * math.pi / 180
            X_inv = X_own - sin(c_own) * 0.25 * L
            Y_inv = Y_own + cos(c_own) * 0.25 * L
        #print("虚拟船坐标",X_inv,Y_inv)

        result01 = solve(((y - Y_inv) * math.cos(w) + (x - X_inv) * math.sin(w)) ** 2 / L ** 2 + (
                (x - X_inv) * math.cos(w) - (y - Y_inv) * math.sin(w)) ** 2 / B ** 2 - 1, x)

        list_result = []
        for item02 in result01:
            list_point = []
            if type(item02) == Float:
                list_point.append(item02)
                y = k * item02 + b
                list_point.append(y)
                list_result.append(list_point)

        ############分段分析他船进入船舶领域的点和时间###########################
        # 确定他船进入船舶领域的点
        point = []
        if len(list_result) == 2:

            x01 = list_result[0][0]  # 第一个交点x01
            y01 = list_result[0][1]

            x02 = list_result[1][0]  # 第二个交点x02
            y02 = list_result[1][1]

            if sqrt(((X_tar) - (x01)) ** 2 + ((Y_tar) - (y01)) ** 2) > sqrt(
                    ((X_tar) - (x02)) ** 2 + ((Y_tar) - (y02)) ** 2):
                point_x = x02
            else:
                point_x = x01

            if point_x == x01:
                point_y = list_result[0][1]
            else:
                point_y = list_result[1][1]

        elif len(list_result) == 1:
            point_x = list_result[0]
            point_y = list_result[1]

        elif len(list_result) == 0:
            point_x = 0
            point_y = 0

        ########再次筛选交叉点################
        if 0 <= C < 90:
            if X_tar <= point_x and Y_tar <= point_y:
                point.append(point_x)
                point.append(point_y)
            else:
                point = [0, 0]
        elif 90 <= C < 180:
            if X_tar <= point_x and Y_tar >= point_y:
                point.append(point_x)
                point.append(point_y)
            else:
                point = [0, 0]

        elif 180 <= C < 270:
            if X_tar >= point_x and Y_tar >= point_y:

                point.append(point_x)
                point.append(point_y)
            else:
                point = [0, 0]
        else:
            if X_tar >= point_x and Y_tar <= point_y:
                point.append(point_x)
                point.append(point_y)
            else:
                point = [0, 0]

        #######计算他船进入船舶领域的时间###########

        if point[0] == point[1] == 0:
            t = 0
            return [0, 0]
        else:
            print("船舶%d进入本船船舶领域的点" % (list_ship[3]), point)
            s = sqrt(((X_tar) - (point[0])) ** 2 + ((Y_tar) - (point[1])) ** 2)
            t = s / V
            return [1, t, point[0], point[1]]

    def start(self):
        list_ships_near = self.get_ships_near()  # 附近2*0.8nm内的目标船舶
        list_danger_ships = []  # 危险船舶
        for item in list_ships_near:
            list_mark_ship = self.get_danger_ships(item)  # [0,0]/[1,t]

            if list_mark_ship[0] == 1:  # 目标船舶会进入本船船舶领域
                t_in = list_mark_ship[1]  # 目标船舶进入本船船舶领域的时间
                if t_in < self.time_danger:
                    item.append(list_mark_ship[2])
                    item.append(list_mark_ship[3])
                    item.append(t_in)
                    list_danger_ships.append(item)
        return list_danger_ships

list_own=[100,100,45,24,4,2]
list_ship=[[1,1,45,88888,24],[0,0,0,6666,1]]
if __name__ == '__main__':
    print(Warm_Danger_By_SOM(list_own,list_ship).start())