import math
from sympy import *

def get_danger_ships(self, list_ship):
    """
    输入：list_ship=[x，y，航向,mmsi，速度]
    输出：
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
    if abs(list_ship[2] - self.list_own[2]) <= 5:
        course_ship = self.list_own[2]
    else:
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
    # print("合速度方向",C)
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
    B = self.list_own[4] * 1  # 船宽
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
    # print("虚拟船坐标",X_inv,Y_inv)

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

        s = sqrt(((X_tar) - (point[0])) ** 2 + ((Y_tar) - (point[1])) ** 2)
        t = s / V
        # print("船舶%d进入本船船舶领域的点" % (list_ship[3]), point,t)
        return [1, t, point[0], point[1]]