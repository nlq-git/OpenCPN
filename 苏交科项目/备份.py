#获取最危险船舶信息
class Get_Danger_Ship():
    def __init__(self,list_own,list_danger_ships):
        self.list_own=list_own #[x，y，航向,速度,船长，船宽]
        self.list_danger_ships=list_danger_ships #[[船舶1],[船舶2]...] 其中船舶：[x，y，航向,mmsi，速度,t_danger]
        self.time_danger=300
    def get_most_danger_ship(self):
        t_min=600
        list_most_danger_ship =[]
        s_min=1000000000000000
        x_own = self.list_own[0]
        y_own = self.list_own[1]
        ##通过时间筛选最危险船舶


        if len(self.list_danger_ships)==1:
            if self.list_danger_ships[0][5]<t_min:
                list_most_danger_ship=self.list_danger_ships[0]


        else:
            for item in self.list_danger_ships:

                if int(item[5])<t_min:
                    list_most_danger_ship=item
                    t_min=item[5]

                ##时间相同，通过距离判断
                elif item[5]==t_min:
                    x_ship = item[0]
                    y_ship = item[1]
                    s = math.sqrt((x_own - x_ship) ** 2 + (y_own - y_ship) ** 2)
                    if s < s_min:
                        list_most_danger_ship=item
                        s_min = s
                else:
                    continue

        return list_most_danger_ship #[x，y，航向,mmsi，速度,t_danger]

    def get_danger_ships(self):
        list_most_danger_ships = []

        for item_ship in list_danger_ships:

            if item_ship[-1]<self.time_danger:
                list_most_danger_ships.append(item_ship)


        return list_most_danger_ships  # [[x，y，航向,mmsi，速度,t_danger,point_x,point_y],[x，y，航向,mmsi，速度,t_danger,point_x,point_y]]

#获取辅助决策（通过判断船头船尾）
class Get_support_decision():
   def get_decision_cross(self,targetShip,ownShip):
       """

       :param targetShip: [x，y，航向,mmsi，速度,t_danger,point_x,point_y]
       :param ownShip: [x，y，航向,速度,船长，船宽]
       :return:
       """
       course_own = ownShip[2]  # 真航向
       L = ownShip[4]  # 长半轴
       B = ownShip[3]  # 短半轴
       X_own = ownShip[0]
       Y_own = ownShip[1]
       X_danger = targetShip[6]
       Y_danger = targetShip[7]

       if 0 <= course_own < 90:
           C = course_own * math.pi / 180
           X_inv = X_own - sin(C) * 0.25 * L
           Y_inv = Y_own - cos(C) * 0.25 * L

           # 右舷
           X_right = X_inv + cos(C) * 0.5 * L
           Y_right = Y_inv - sin(C) * 0.5 * L

           # 左舷
           X_left = X_inv - cos(C) * 0.5 * L
           Y_left = Y_inv + sin(C) * 0.5 * L

           # 船头
           X_up = X_inv + sin(C) * 2 * L
           Y_up = Y_inv + cos(C) * 2 * L

           # 船尾
           X_down = X_inv - sin(C) * 2 * L
           Y_down = Y_inv - cos(C) * 2 * L

       elif 90 <= course_own < 180:
           C = (180 - course_own) * math.pi / 180
           X_inv = X_own - sin(C) * 0.25 * L
           Y_inv = Y_own + cos(C) * 0.25 * L

           # 右舷
           X_right = X_inv - cos(C) * 0.5 * L
           Y_right = Y_inv - sin(C) * 0.5 * L

           # 左舷
           X_left = X_inv + cos(C) * 0.5 * L
           Y_left = Y_inv + sin(C) * 0.5 * L

           # 船头
           X_up = X_inv + sin(C) * 2 * L
           Y_up = Y_inv - cos(C) * 2 * L

           # 船尾
           X_down = X_inv - sin(C) * 2 * L
           Y_down = Y_inv + cos(C) * 2 * L

       elif 180 <= course_own < 270:
           C = (course_own - 180) * math.pi / 180
           X_inv = X_own + sin(C) * 0.25 * L
           Y_inv = Y_own + cos(C) * 0.25 * L

           # 右舷
           X_right = X_inv - cos(C) * 0.5 * L
           Y_right = Y_inv + sin(C) * 0.5 * L

           # 左舷
           X_left = X_inv + cos(C) * 0.5 * L
           Y_left = Y_inv - sin(C) * 0.5 * L

           # 船头
           X_up = X_inv - sin(C) * 2 * L
           Y_up = Y_inv - cos(C) * 2 * L

           # 船尾
           X_down = X_inv + sin(C) * 2 * L
           Y_down = Y_inv + cos(C) * 2 * L

       else:
           C = (360 - course_own) * math.pi / 180
           X_inv = X_own + sin(C) * 0.25 * L
           Y_inv = Y_own - cos(C) * 0.25 * L

           # 右舷
           X_right = X_inv + cos(C) * 0.5 * L
           Y_right = Y_inv + sin(C) * 0.5 * L

           # 左舷
           X_left = X_inv - cos(C) * 0.5 * L
           Y_left = Y_inv - sin(C) * 0.5 * L

           # 船头
           X_up = X_inv - sin(C) * 2 * L
           Y_up = Y_inv + cos(C) * 2 * L

           # 船尾
           X_down = X_inv + sin(C) * 2 * L
           Y_down = Y_inv - cos(C) * 2 * L

       s_right = sqrt((X_danger - X_right) ** 2 + (Y_danger - Y_right) ** 2)
       s_left = sqrt((X_danger - X_left) ** 2 + (Y_danger - Y_left) ** 2)
       s_up = sqrt((X_danger - X_up) ** 2 + (Y_danger - Y_up) ** 2)
       s_down = sqrt((X_danger - X_down) ** 2 + (Y_danger - Y_down) ** 2)
       if s_right>s_left:#左侧来船
           if s_up>s_down:#左侧过船尾
               return [1,1]
           else:#左侧过船头
               return [2,2]
       else:                #右侧来船
           if s_up > s_down:  # 右侧过船尾
               return [2, 1]
           else:                # 右侧过船头
               return [1, 2]

   def get_decision_overtake(self,targetShip,ownShip,list_channel):

       """
       :param targetShip:[x，y，航向,速度,船长，船宽]
       :param ownShip:[x，y，航向,mmsi，速度,t_danger,t_danger,point_x,point_y]
       :param list_channel:【【lon,lat】,【lon,lat】，【lon,lat】，【lon,lat】,【course，value,id1,id2】】（右上，左上，右下，左下）
       :return:
       """
       x1 = list_channel[0][0]  # 右上
       y1 = list_channel[0][1]

       x2 = list_channel[1][0]  # 左上
       y2 = list_channel[1][1]

       x3 = list_channel[2][0]  # 右下
       y3 = list_channel[2][1]

       x4 = list_channel[3][0]  # 左下
       y4 = list_channel[3][1]
       c_channel=list_channel[4][0] #航道走向
       mark_channel=list_channel[4][3] #航道类型

       x_target = targetShip[0]  # 目标船x
       y_target = targetShip[1]  # 目标船y
       v_target = targetShip[4]  # 目标船速度

       x_own=ownShip[0]  #本船x
       y_own=ownShip[1]  #本船y
       v_own=ownShip[4]  #本船速度
       c_own=ownShip[2]  #本船航向

       if v_own>v_target:#本船追越
           pass
       else:  #本船被追越
           pass




       ###上边界直线方程###
       k_up = (y2 - y1) / (x2 - x1)
       b_up = y1 - k_up * x1

       ####下边界直线方程###
       k_down = (y4 - y3) / (x4 - x3)
       b_down = y3 - k_down * x3


       ###目标船舶与上边界距离###
       s_up = abs(y_target - k_up * x_target - b_up) / sqrt(1 + k_up ** 2)

       ###目标船舶与下边界距离###
       s_down = abs(y_target - k_down * x_target - b_down) / sqrt(1 + k_down ** 2)

       if  list_channel[4][3]>0: #上行航道
           if v_own > v_target:  # 本船追越
               if s_up > s_down: #目标船舶右侧宽裕
                   return [1,1]
               else:    #目标船舶左侧宽裕
                   return [2,1]
           else:  # 本船被追越
               return [3,3]

       else:                     #下行航道
           if v_own > v_target:  # 本船追越
               if s_up <s_down:  # 目标船舶右侧宽裕
                   return [1, 1]
               else:  # 目标船舶左侧宽裕
                   return [2, 1]
           else:  # 本船被追越
               return [3, 3]