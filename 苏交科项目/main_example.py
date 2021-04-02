"""
测试修改版本
"""
import xlrd
import math
from sympy import *
import time
import os
#从指定路径下的excel表格中获取静态信息
class Get_StaticData():
    """
    获取静态数据
    输入：无（通过读取指定路径的excel文件获取输入）
    输出：静态数据：[dataArea,dataChannel]
    """
    def __init__(self):
        self.path_rel=os.path.join(os.getcwd(),'数据配置文档')  #自适应相对路径



    #######################################################1、本船为小船(开发完成，待验证)##################################
    # 1.1获取当本船为小船时的区域数据
    def get_areaData_smallShip(self):
        """
        输入：读取路径为“D:/code/苏交科/数据配置文档/区域数据/小船”里的excel文件获取区域信息
        输出：[正常区域区域信息, 交汇区域区域信息,其他区域区域信息]-----正常区域区域信息=[区域1,区域2...]------区域i=[右上,右下,左上,左下,id]----左/右=[lon,lat]
        """

        #############################（1）获取正常区域信息####################################
        data_allArea = [] #存放正常区域信息
        for id_normalArea in range(1,12):#小船的正常区域有12个

            # 1)打开表
            path_abs="区域数据/小船区域/正常区域/区域%d.xlsx"%(id_normalArea)  #绝对路径
            path=os.path.join(self.path_rel,path_abs)

            #"D:/code/苏交科/数据配置文档/区域数据/小船区域/正常区域/区域%d.xlsx"%(id_normalArea)
            data_area = xlrd.open_workbook(r"%s" % (path))

            # 2)获取sheet（区域）中内容
            sheet = data_area.sheet_by_name("区域")

            # 3)处理经纬度，将分转换为°
            data_oneArea = []
            for i in range(1, sheet.nrows):
                rows01 = sheet.row_values(i)
                data_oneArea.append(
                    [int(rows01[1]) + float(rows01[2]) / 60, int(rows01[3]) + float(rows01[4]) / 60])
            data_oneArea.append([1,id_normalArea])
            data_allArea.append(data_oneArea)


        #############################（2）获取交叉区域信息####################################
        for id_specialArea in range(1, 6):
            #1） 打开表
            path_abs = "区域数据/小船区域/交叉区域/区域%d.xlsx" % (id_specialArea)  # 绝对路径
            path = os.path.join(self.path_rel, path_abs)
            #path="D:/code/苏交科/数据配置文档/区域数据/小船区域/交叉区域/区域%d.xlsx"%(id_specialArea)
            data_area = xlrd.open_workbook(r"%s" % (path))

            # 2）获取sheet（区域）中内容
            sheet = data_area.sheet_by_name("区域")

            # 3）处理经纬度，将分转换为°
            data_oneArea = []
            for i in range(1, sheet.nrows):
                rows01 = sheet.row_values(i)
                data_oneArea.append(
                    [int(rows01[1]) + float(rows01[2]) / 60, int(rows01[3]) + float(rows01[4]) / 60])
            data_oneArea.append([2,id_specialArea])
            data_allArea.append(data_oneArea)

        #############################（3）获取其他区域信息####################################
        for id_otherArea in range(1, 3):
            # 1） 打开表
            path_abs = "区域数据/小船区域/其他区域/区域%d.xlsx" % (id_otherArea)  # 绝对路径
            path = os.path.join(self.path_rel, path_abs)
            #path = "D:/code/苏交科/数据配置文档/区域数据/小船区域/其他区域/区域%d.xlsx" % (id_otherArea)
            data_area = xlrd.open_workbook(r"%s" % (path))

            # 2）获取sheet（区域）中内容
            sheet = data_area.sheet_by_name("区域")

            # 3）处理经纬度，将分转换为°
            data_oneArea = []
            for i in range(1, sheet.nrows):
                rows01 = sheet.row_values(i)
                data_oneArea.append(
                    [int(rows01[1]) + float(rows01[2]) / 60, int(rows01[3]) + float(rows01[4]) / 60])
            data_oneArea.append([3, id_otherArea])
            data_allArea.append(data_oneArea)

        return data_allArea

    # 1.2获取当本船为小船时的航道数据
    def get_channelData_smallShip(self):
        """
        输入：读取路径为“D:/code/苏交科/数据配置文档/航道数据/小船航道”里的excel文件获取航道信息
        输出：[正常区域航道信息, 交汇区域航道信息,其他区域航道信息]----正常区域航道信息=[区域1,区域2...]----区域i=[上行航线1,上行航线2,下行航线1,下行航线2,id]----- 上/下行航线=[点1,点2...]---点i=[lon,lat]
        """
        ###############################（1）、获取正常区域航道信息###########################
        data_allChannel = []  # 存放正常区域航道信息

        for id_normalChannel in range(1, 12):
            #########################1)打开表###################
            path_abs01 = "航道数据/小船航道/正常区域/区域%d/1.xlsx" % (id_normalChannel)  # 绝对路径
            path_abs02 = "航道数据/小船航道/正常区域/区域%d/2.xlsx" % (id_normalChannel)  # 绝对路径
            path_abs03 = "航道数据/小船航道/正常区域/区域%d/3.xlsx" % (id_normalChannel)  # 绝对路径
            path_abs04 = "航道数据/小船航道/正常区域/区域%d/4.xlsx" % (id_normalChannel)  # 绝对路径
            path01 = os.path.join(self.path_rel, path_abs01)
            path02 = os.path.join(self.path_rel, path_abs02)
            path03 = os.path.join(self.path_rel, path_abs03)
            path04 = os.path.join(self.path_rel, path_abs04)
            # path01 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/正常区域/区域%d/1.xlsx" % (id_normalChannel)
            # path02 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/正常区域/区域%d/2.xlsx" % (id_normalChannel)
            # path03 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/正常区域/区域%d/3.xlsx" % (id_normalChannel)
            # path04 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/正常区域/区域%d/4.xlsx" % (id_normalChannel)

            data_channelUp01 = xlrd.open_workbook(r"%s" % (path01))
            data_channelUp02 = xlrd.open_workbook(r"%s" % (path02))
            data_channelDown01 = xlrd.open_workbook(r"%s" % (path03))
            data_channelDown02 = xlrd.open_workbook(r"%s" % (path04))

            #####################2)获取sheet（区域）中内容######
            sheet_channelUp01 = data_channelUp01.sheet_by_name("航线")
            sheet_channelUp02 = data_channelUp02.sheet_by_name("航线")
            sheet_channelDown01 = data_channelDown01.sheet_by_name("航线")
            sheet_channelDown02 = data_channelDown02.sheet_by_name("航线")

            ####################3)处理经纬度，将分转换为°#######
            ######01、转换上行航道1（up01）的经纬度######
            channelUp01 = []
            for i in range(1, sheet_channelUp01.nrows):
                rows01 = sheet_channelUp01.row_values(i)
                lat = (int(rows01[1]) + float(rows01[2]) / 60)
                lon = (int(rows01[3]) + float(rows01[4]) / 60)
                channelUp01.append([lon, lat])
            id_areaMark=id_normalChannel+0.01
            channelUp01.append([1,id_areaMark ])

            ######02、转换上行航道2（up02）的经纬度######
            channelUp02 = []
            for i in range(1, sheet_channelUp02.nrows):
                rows02 = sheet_channelUp02.row_values(i)
                lat = (int(rows02[1]) + float(rows02[2]) / 60)
                lon = (int(rows02[3]) + float(rows02[4]) / 60)
                channelUp02.append([lon, lat])
            id_areaMark = id_normalChannel + 0.02
            channelUp02.append([1, id_areaMark])


            ######03、转换下行航道1（down01）的经纬度######
            channelDown01 = []
            for i in range(1, sheet_channelDown01.nrows):
                rows03 = sheet_channelDown01.row_values(i)
                lat = (int(rows03[1]) + float(rows03[2]) / 60)
                lon = (int(rows03[3]) + float(rows03[4]) / 60)
                channelDown01.append([lon, lat])

            id_areaMark = id_normalChannel + 0.11
            channelDown01.append([1, id_areaMark])


            ######04、转换下行航道2（down02）的经纬度######
            channelDown02 = []
            for i in range(1, sheet_channelDown02.nrows):
                rows04 = sheet_channelDown02.row_values(i)
                lat = (int(rows04[1]) + float(rows04[2]) / 60)
                lon = (int(rows04[3]) + float(rows04[4]) / 60)
                channelDown02.append([lon, lat])
            id_areaMark = id_normalChannel + 0.12
            channelDown02.append([1, id_areaMark])


            data_allChannel.append([channelUp01, channelUp02, channelDown01, channelDown02])

        ##############################（2）、获取交汇区域航道信息#############################

        ##########1)转换交汇区域1的航道数据#############
        path_abs01 = "航道数据/小船航道/交汇区域/区域1/1.xlsx"  # 绝对路径
        path_abs02 = "航道数据/小船航道/交汇区域/区域1/2.xlsx"   # 绝对路径
        path_abs03 = "航道数据/小船航道/交汇区域/区域1/3.xlsx"   # 绝对路径
        path_abs04 = "航道数据/小船航道/交汇区域/区域1/4.xlsx"   # 绝对路径
        path01 = os.path.join(self.path_rel, path_abs01)
        path02 = os.path.join(self.path_rel, path_abs02)
        path03 = os.path.join(self.path_rel, path_abs03)
        path04 = os.path.join(self.path_rel, path_abs04)
        # path01 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/交汇区域/区域1/1.xlsx"
        # path02 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/交汇区域/区域1/2.xlsx"
        # path03 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/交汇区域/区域1/3.xlsx"
        # path04 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/交汇区域/区域1/4.xlsx"


        data_channelUp01 = xlrd.open_workbook(r"%s" % (path01))
        data_channelUp02 = xlrd.open_workbook(r"%s" % (path02))
        data_channelDown01 = xlrd.open_workbook(r"%s" % (path03))
        data_channelDown02 = xlrd.open_workbook(r"%s" % (path04))

        sheet_channelUp01 = data_channelUp01.sheet_by_name("航线")
        sheet_channelUp02 = data_channelUp02.sheet_by_name("航线")
        sheet_channelDown01 = data_channelDown01.sheet_by_name("航线")
        sheet_channelDown02 = data_channelDown02.sheet_by_name("航线")

        ###01、转换上行航道1的经纬度####
        channelUp01 = []
        for i in range(1, sheet_channelUp01.nrows):
            rows01 = sheet_channelUp01.row_values(i)
            lat = (int(rows01[1]) + float(rows01[2]) / 60)
            lon = (int(rows01[3]) + float(rows01[4]) / 60)
            channelUp01.append([lon, lat])
        id_areaMark = 1 + 0.01
        channelUp01.append([2, id_areaMark])




        ###02、转换上行航道2的经纬度####
        channelUp02 = []
        for i in range(1, sheet_channelUp02.nrows):
            rows02 = sheet_channelUp02.row_values(i)
            lat = (int(rows02[1]) + float(rows02[2]) / 60)
            lon = (int(rows02[3]) + float(rows02[4]) / 60)
            channelUp02.append([lon, lat])

        id_areaMark = 1 + 0.02
        channelUp02.append([2, id_areaMark])


        ###03、转换下行航道1的经纬度####
        channelDown01 = []
        for i in range(1, sheet_channelDown01.nrows):
            rows05 = sheet_channelDown01.row_values(i)
            lat = (int(rows05[1]) + float(rows05[2]) / 60)
            lon = (int(rows05[3]) + float(rows05[4]) / 60)
            channelDown01.append([lon, lat])
        id_areaMark = 1 + 0.11
        channelDown01.append([2, id_areaMark])


        ###04、转换下行航道2的经纬度###
        channelDown02 = []
        for i in range(1, sheet_channelDown02.nrows):
            rows06 = sheet_channelDown02.row_values(i)
            lat = (int(rows06[1]) + float(rows06[2]) / 60)
            lon = (int(rows06[3]) + float(rows06[4]) / 60)
            channelDown02.append([lon, lat])
        id_areaMark = 1 + 0.12
        channelDown02.append([2, id_areaMark])
        data_allChannel.append([channelUp01, channelUp02,channelDown01, channelDown02])

        ##########2)转换交汇区域2的航道数据#############
        path_abs01 = "航道数据/小船航道/交汇区域/区域2/1.xlsx"  # 绝对路径
        path_abs02 = "航道数据/小船航道/交汇区域/区域2/2.xlsx"  # 绝对路径
        path_abs03 = "航道数据/小船航道/交汇区域/区域2/3.xlsx"  # 绝对路径
        path_abs04 = "航道数据/小船航道/交汇区域/区域2/4.xlsx"  # 绝对路径
        path_abs05 = "航道数据/小船航道/交汇区域/区域2/5.xlsx"  # 绝对路径
        path_abs06 = "航道数据/小船航道/交汇区域/区域2/6.xlsx"  # 绝对路径
        path01 = os.path.join(self.path_rel, path_abs01)
        path02 = os.path.join(self.path_rel, path_abs02)
        path03 = os.path.join(self.path_rel, path_abs03)
        path04 = os.path.join(self.path_rel, path_abs04)
        path05 = os.path.join(self.path_rel, path_abs05)
        path06 = os.path.join(self.path_rel, path_abs06)
        # path01 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/交汇区域/区域2/1.xlsx"
        # path02 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/交汇区域/区域2/2.xlsx"
        # path03 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/交汇区域/区域2/3.xlsx"
        # path04 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/交汇区域/区域2/4.xlsx"
        # path05 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/交汇区域/区域2/5.xlsx"
        # path06 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/交汇区域/区域2/6.xlsx"

        data_channelUp01 = xlrd.open_workbook(r"%s" % (path01))
        data_channelUp02 = xlrd.open_workbook(r"%s" % (path02))
        data_channelDown01 = xlrd.open_workbook(r"%s" % (path03))
        data_channelDown02 = xlrd.open_workbook(r"%s" % (path04))
        data_channelDown03 = xlrd.open_workbook(r"%s" % (path05))
        data_channelDown04 = xlrd.open_workbook(r"%s" % (path06))


        sheet_channelUp01 = data_channelUp01.sheet_by_name("航线")
        sheet_channelUp02 = data_channelUp02.sheet_by_name("航线")
        sheet_channelDown01 = data_channelDown01.sheet_by_name("航线")
        sheet_channelDown02 = data_channelDown02.sheet_by_name("航线")
        sheet_channelDown03 = data_channelDown03.sheet_by_name("航线")
        sheet_channelDown04 = data_channelDown04.sheet_by_name("航线")


        ###01、转换上行航道1的经纬度###
        channelUp01 = []
        for i in range(1, sheet_channelUp01.nrows):
            rows01 = sheet_channelUp01.row_values(i)
            lat = (int(rows01[1]) + float(rows01[2]) / 60)
            lon = (int(rows01[3]) + float(rows01[4]) / 60)
            channelUp01.append([lon, lat])
        id_areaMark = 2 + 0.01
        channelUp01.append([2, id_areaMark])

        ###02、转换上行航道2的经纬度###
        channelUp02 = []
        for i in range(1, sheet_channelUp02.nrows):
            rows02 = sheet_channelUp02.row_values(i)
            lat = (int(rows02[1]) + float(rows02[2]) / 60)
            lon = (int(rows02[3]) + float(rows02[4]) / 60)
            channelUp02.append([lon, lat])
        id_areaMark = 2 + 0.02
        channelUp02.append([2, id_areaMark])


        ###03、转换下行航道1的经纬度###
        channelDown01 = []
        for i in range(1, sheet_channelDown01.nrows):
            rows03 = sheet_channelDown01.row_values(i)
            lat = (int(rows03[1]) + float(rows03[2]) / 60)
            lon = (int(rows03[3]) + float(rows03[4]) / 60)
            channelDown01.append([lon, lat])
        id_areaMark = 2 + 0.11
        channelDown01.append([2, id_areaMark])

        ###04、转换下行航道2的经纬度###
        channelDown02 = []
        for i in range(1, sheet_channelDown02.nrows):
            rows04 = sheet_channelDown02.row_values(i)
            lat = (int(rows04[1]) + float(rows04[2]) / 60)
            lon = (int(rows04[3]) + float(rows04[4]) / 60)
            channelDown02.append([lon, lat])
        id_areaMark = 2 + 0.12
        channelDown02.append([2, id_areaMark])



        ###05、转换下行航道3的经纬度###
        channelDown03 = []
        for i in range(1, sheet_channelDown03.nrows):
            rows05 = sheet_channelDown03.row_values(i)
            lat = (int(rows05[1]) + float(rows05[2]) / 60)
            lon = (int(rows05[3]) + float(rows05[4]) / 60)
            channelDown03.append([lon, lat])
        id_areaMark = 2 + 0.13
        channelDown03.append([2, id_areaMark])



        ###06、转换下行航道4的经纬度###
        channelDown04 = []
        for i in range(1, sheet_channelDown04.nrows):
            rows06 = sheet_channelDown04.row_values(i)
            lat = (int(rows06[1]) + float(rows06[2]) / 60)
            lon = (int(rows06[3]) + float(rows06[4]) / 60)
            channelDown04.append([lon, lat])
        id_areaMark = 2 + 0.14
        channelDown04.append([2, id_areaMark])
        data_allChannel.append([channelUp01, channelUp02, channelDown01, channelDown02,channelDown03, channelDown04])

        ##########3)转换交汇区域3的航道数据#############
        path_abs01 = "航道数据/小船航道/交汇区域/区域3/1.xlsx"  # 绝对路径
        path_abs02 = "航道数据/小船航道/交汇区域/区域3/2.xlsx"  # 绝对路径
        path_abs03 = "航道数据/小船航道/交汇区域/区域3/3.xlsx"  # 绝对路径
        path_abs04 = "航道数据/小船航道/交汇区域/区域3/4.xlsx"  # 绝对路径
        path_abs05 = "航道数据/小船航道/交汇区域/区域3/5.xlsx"  # 绝对路径
        path_abs06 = "航道数据/小船航道/交汇区域/区域3/6.xlsx"  # 绝对路径
        path01 = os.path.join(self.path_rel, path_abs01)
        path02 = os.path.join(self.path_rel, path_abs02)
        path03 = os.path.join(self.path_rel, path_abs03)
        path04 = os.path.join(self.path_rel, path_abs04)
        path05 = os.path.join(self.path_rel, path_abs05)
        path06 = os.path.join(self.path_rel, path_abs06)
        # path01 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/交汇区域/区域3/1.xlsx"
        # path02 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/交汇区域/区域3/2.xlsx"
        # path03 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/交汇区域/区域3/3.xlsx"
        # path04 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/交汇区域/区域3/4.xlsx"
        # path05 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/交汇区域/区域3/5.xlsx"
        # path06 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/交汇区域/区域3/6.xlsx"

        data_channelUp01 = xlrd.open_workbook(r"%s" % (path01))
        data_channelUp02 = xlrd.open_workbook(r"%s" % (path02))
        data_channelDown01 = xlrd.open_workbook(r"%s" % (path03))
        data_channelDown02 = xlrd.open_workbook(r"%s" % (path04))
        data_channelDown03 = xlrd.open_workbook(r"%s" % (path05))
        data_channelDown04 = xlrd.open_workbook(r"%s" % (path06))

        sheet_channelUp01 = data_channelUp01.sheet_by_name("航线")
        sheet_channelUp02 = data_channelUp02.sheet_by_name("航线")
        sheet_channelDown01 = data_channelDown01.sheet_by_name("航线")
        sheet_channelDown02 = data_channelDown02.sheet_by_name("航线")
        sheet_channelDown03 = data_channelDown03.sheet_by_name("航线")
        sheet_channelDown04 = data_channelDown04.sheet_by_name("航线")

        ###01、转换上行航道1的经纬度###
        channelUp01 = []
        for i in range(1, sheet_channelUp01.nrows):
            rows01 = sheet_channelUp01.row_values(i)
            lat = (int(rows01[1]) + float(rows01[2]) / 60)
            lon = (int(rows01[3]) + float(rows01[4]) / 60)
            channelUp01.append([lon, lat])
        id_areaMark = 3 + 0.01
        channelUp01.append([2, id_areaMark])



        ###02、转换上行航道2的经纬度###
        channelUp02 = []
        for i in range(1, sheet_channelUp02.nrows):
            rows02 = sheet_channelUp02.row_values(i)
            lat = (int(rows02[1]) + float(rows02[2]) / 60)
            lon = (int(rows02[3]) + float(rows02[4]) / 60)
            channelUp02.append([lon, lat])
        id_areaMark = 3 + 0.02
        channelUp02.append([2, id_areaMark])


        ###03、转换下行航道1的经纬度###
        channelDown01 = []
        for i in range(1, sheet_channelDown01.nrows):
            rows03 = sheet_channelDown01.row_values(i)
            lat = (int(rows03[1]) + float(rows03[2]) / 60)
            lon = (int(rows03[3]) + float(rows03[4]) / 60)
            channelDown01.append([lon, lat])
        id_areaMark = 3 + 0.11
        channelDown01.append([2, id_areaMark])


        ###04、转换下行航道2的经纬度###
        channelDown02 = []
        for i in range(1, sheet_channelDown02.nrows):
            rows04 = sheet_channelDown02.row_values(i)
            lat = (int(rows04[1]) + float(rows04[2]) / 60)
            lon = (int(rows04[3]) + float(rows04[4]) / 60)
            channelDown02.append([lon, lat])
        id_areaMark = 3 + 0.12
        channelDown02.append([2, id_areaMark])


        ###05、转换下行航道3的经纬度###
        channelDown03 = []
        for i in range(1, sheet_channelDown03.nrows):
            rows05 = sheet_channelDown03.row_values(i)
            lat = (int(rows05[1]) + float(rows05[2]) / 60)
            lon = (int(rows05[3]) + float(rows05[4]) / 60)
            channelDown03.append([lon, lat])
        id_areaMark = 3 + 0.13
        channelDown03.append([2, id_areaMark])


        ###06、转换下行航道4的经纬度###
        channelDown04 = []
        for i in range(1, sheet_channelDown04.nrows):
            rows06 = sheet_channelDown04.row_values(i)
            lat = (int(rows06[1]) + float(rows06[2]) / 60)
            lon = (int(rows06[3]) + float(rows06[4]) / 60)
            channelDown04.append([lon, lat])
        id_areaMark = 3 + 0.14
        channelDown04.append([2, id_areaMark])


        data_allChannel.append( [channelUp01, channelUp02, channelDown01, channelDown02, channelDown03, channelDown04])

        ##########4)转换交汇区域4的航道数据#############
        path_abs01 = "航道数据/小船航道/交汇区域/区域4/1.xlsx"  # 绝对路径
        path_abs02 = "航道数据/小船航道/交汇区域/区域4/2.xlsx"  # 绝对路径
        path_abs03 = "航道数据/小船航道/交汇区域/区域4/3.xlsx"  # 绝对路径
        path_abs04 = "航道数据/小船航道/交汇区域/区域4/4.xlsx"  # 绝对路径

        path01 = os.path.join(self.path_rel, path_abs01)
        path02 = os.path.join(self.path_rel, path_abs02)
        path03 = os.path.join(self.path_rel, path_abs03)
        path04 = os.path.join(self.path_rel, path_abs04)

        # path01 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/交汇区域/区域4/1.xlsx"
        # path02 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/交汇区域/区域4/2.xlsx"
        # path03 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/交汇区域/区域4/3.xlsx"
        # path04 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/交汇区域/区域4/4.xlsx"

        data_channelUp01 = xlrd.open_workbook(r"%s" % (path01))
        data_channelUp02 = xlrd.open_workbook(r"%s" % (path02))
        data_channelDown01 = xlrd.open_workbook(r"%s" % (path03))
        data_channelDown02 = xlrd.open_workbook(r"%s" % (path04))

        sheet_channelUp01 = data_channelUp01.sheet_by_name("航线")
        sheet_channelUp02 = data_channelUp02.sheet_by_name("航线")
        sheet_channelDown01 = data_channelDown01.sheet_by_name("航线")
        sheet_channelDown02 = data_channelDown02.sheet_by_name("航线")

        ###01、转换上行航道1的经纬度###
        channelUp01 = []
        for i in range(1, sheet_channelUp01.nrows):
            rows01 = sheet_channelUp01.row_values(i)
            lat = (int(rows01[1]) + float(rows01[2]) / 60)
            lon = (int(rows01[3]) + float(rows01[4]) / 60)
            channelUp01.append([lon, lat])
        id_areaMark = 4 + 0.01
        channelUp01.append([2, id_areaMark])

        ###02、转换上行航道2的经纬度###
        channelUp02 = []
        for i in range(1, sheet_channelUp02.nrows):
            rows02 = sheet_channelUp02.row_values(i)
            lat = (int(rows02[1]) + float(rows02[2]) / 60)
            lon = (int(rows02[3]) + float(rows02[4]) / 60)
            channelUp02.append([lon, lat])
        id_areaMark = 4 + 0.02
        channelUp02.append([2, id_areaMark])


        ###03、转换下行航道1的经纬度###
        channelDown01 = []
        for i in range(1, sheet_channelDown01.nrows):
            rows05 = sheet_channelDown01.row_values(i)
            lat = (int(rows05[1]) + float(rows05[2]) / 60)
            lon = (int(rows05[3]) + float(rows05[4]) / 60)
            channelDown01.append([lon, lat])
        id_areaMark = 4 + 0.11
        channelDown01.append([2, id_areaMark])

        ###04、转换下行航道2的经纬度###
        channelDown02 = []
        for i in range(1, sheet_channelDown02.nrows):
            rows06 = sheet_channelDown02.row_values(i)
            lat = (int(rows06[1]) + float(rows06[2]) / 60)
            lon = (int(rows06[3]) + float(rows06[4]) / 60)
            channelDown02.append([lon, lat])
        id_areaMark = 4 + 0.12
        channelDown02.append([2, id_areaMark])

        data_allChannel.append([channelUp01, channelUp02, channelDown01, channelDown02])

        ##########5)转换交汇区域5的航道数据#############
        path_abs01 = "航道数据/小船航道/交汇区域/区域5/1.xlsx"  # 绝对路径
        path_abs02 = "航道数据/小船航道/交汇区域/区域5/2.xlsx"  # 绝对路径
        path_abs03 = "航道数据/小船航道/交汇区域/区域5/3.xlsx"  # 绝对路径
        path_abs04 = "航道数据/小船航道/交汇区域/区域5/4.xlsx"  # 绝对路径

        path01 = os.path.join(self.path_rel, path_abs01)
        path02 = os.path.join(self.path_rel, path_abs02)
        path03 = os.path.join(self.path_rel, path_abs03)
        path04 = os.path.join(self.path_rel, path_abs04)

        # path01 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/交汇区域/区域5/1.xlsx"
        # path02 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/交汇区域/区域5/2.xlsx"
        # path03 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/交汇区域/区域5/3.xlsx"
        # path04 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/交汇区域/区域5/4.xlsx"

        data_channelUp01 = xlrd.open_workbook(r"%s" % (path01))
        data_channelUp02 = xlrd.open_workbook(r"%s" % (path02))
        data_channelDown01 = xlrd.open_workbook(r"%s" % (path03))
        data_channelDown02 = xlrd.open_workbook(r"%s" % (path04))

        sheet_channelUp01 = data_channelUp01.sheet_by_name("航线")
        sheet_channelUp02 = data_channelUp02.sheet_by_name("航线")
        sheet_channelDown01 = data_channelDown01.sheet_by_name("航线")
        sheet_channelDown02 = data_channelDown02.sheet_by_name("航线")

        ###01、转换上行航道1的经纬度###
        channelUp01 = []
        for i in range(1, sheet_channelUp01.nrows):
            rows01 = sheet_channelUp01.row_values(i)
            lat = (int(rows01[1]) + float(rows01[2]) / 60)
            lon = (int(rows01[3]) + float(rows01[4]) / 60)
            channelUp01.append([lon, lat])
        id_areaMark = 5 + 0.01
        channelUp01.append([2, id_areaMark])


        ###02、转换上行航道2的经纬度###
        channelUp02 = []
        for i in range(1, sheet_channelUp02.nrows):
            rows02 = sheet_channelUp02.row_values(i)
            lat = (int(rows02[1]) + float(rows02[2]) / 60)
            lon = (int(rows02[3]) + float(rows02[4]) / 60)
            channelUp02.append([lon, lat])
        id_areaMark = 5 + 0.02
        channelUp02.append([2, id_areaMark])



        ###03、转换下行航道1的经纬度###
        channelDown01 = []
        for i in range(1, sheet_channelDown01.nrows):
            rows05 = sheet_channelDown01.row_values(i)
            lat = (int(rows05[1]) + float(rows05[2]) / 60)
            lon = (int(rows05[3]) + float(rows05[4]) / 60)
            channelDown01.append([lon, lat])
        id_areaMark = 5 + 0.11
        channelDown01.append([2, id_areaMark])


        ###04、转换下行航道2的经纬度###
        channelDown02 = []
        for i in range(1, sheet_channelDown02.nrows):
            rows06 = sheet_channelDown02.row_values(i)
            lat = (int(rows06[1]) + float(rows06[2]) / 60)
            lon = (int(rows06[3]) + float(rows06[4]) / 60)
            channelDown02.append([lon, lat])
        id_areaMark = 5 + 0.12
        channelDown02.append([2, id_areaMark])

        data_allChannel.append([channelUp01, channelUp02, channelDown01, channelDown02])

        ##############################（3）、获取其他区域航道信息#############################
        ##########1)转换其他区域1的航道数据#############
        path_abs01 = "航道数据/小船航道/其他区域/区域1/1.xlsx"  # 绝对路径
        path_abs02 = "航道数据/小船航道/其他区域/区域1/2.xlsx"  # 绝对路径
        path_abs03 = "航道数据/小船航道/其他区域/区域1/3.xlsx"  # 绝对路径
        path_abs04 = "航道数据/小船航道/其他区域/区域1/4.xlsx"  # 绝对路径
        path_abs05 = "航道数据/小船航道/其他区域/区域1/5.xlsx"  # 绝对路径
        path_abs06 = "航道数据/小船航道/其他区域/区域1/6.xlsx"  # 绝对路径
        path01 = os.path.join(self.path_rel, path_abs01)
        path02 = os.path.join(self.path_rel, path_abs02)
        path03 = os.path.join(self.path_rel, path_abs03)
        path04 = os.path.join(self.path_rel, path_abs04)
        path05 = os.path.join(self.path_rel, path_abs05)
        path06 = os.path.join(self.path_rel, path_abs06)
        # path01 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/其他区域/区域1/1.xlsx"
        # path02 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/其他区域/区域1/2.xlsx"
        # path03 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/其他区域/区域1/3.xlsx"
        # path04 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/其他区域/区域1/4.xlsx"
        # path05 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/其他区域/区域1/5.xlsx"
        # path06 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/其他区域/区域1/6.xlsx"

        data_channelUp01 = xlrd.open_workbook(r"%s" % (path01))
        data_channelUp02 = xlrd.open_workbook(r"%s" % (path02))
        data_channelDown01 = xlrd.open_workbook(r"%s" % (path03))
        data_channelDown02 = xlrd.open_workbook(r"%s" % (path04))
        data_channelDown03 = xlrd.open_workbook(r"%s" % (path05))
        data_channelDown04 = xlrd.open_workbook(r"%s" % (path06))

        sheet_channelUp01 = data_channelUp01.sheet_by_name("航线")
        sheet_channelUp02 = data_channelUp02.sheet_by_name("航线")
        sheet_channelDown01 = data_channelDown01.sheet_by_name("航线")
        sheet_channelDown02 = data_channelDown02.sheet_by_name("航线")
        sheet_channelDown03 = data_channelDown03.sheet_by_name("航线")
        sheet_channelDown04 = data_channelDown04.sheet_by_name("航线")

        ###01、转换上行航道1的经纬度###
        channelUp01 = []
        for i in range(1, sheet_channelUp01.nrows):
            rows01 = sheet_channelUp01.row_values(i)
            lat = (int(rows01[1]) + float(rows01[2]) / 60)
            lon = (int(rows01[3]) + float(rows01[4]) / 60)
            channelUp01.append([lon, lat])
        id_areaMark = 1 + 0.01
        channelUp01.append([3, id_areaMark])


        ###02、转换上行航道2的经纬度###
        channelUp02 = []
        for i in range(1, sheet_channelUp02.nrows):
            rows02 = sheet_channelUp02.row_values(i)
            lat = (int(rows02[1]) + float(rows02[2]) / 60)
            lon = (int(rows02[3]) + float(rows02[4]) / 60)
            channelUp02.append([lon, lat])
        id_areaMark = 1 + 0.02
        channelUp02.append([3, id_areaMark])


        ###03、转换下行航道1的经纬度###
        channelDown01 = []
        for i in range(1, sheet_channelDown01.nrows):
            rows03 = sheet_channelDown01.row_values(i)
            lat = (int(rows03[1]) + float(rows03[2]) / 60)
            lon = (int(rows03[3]) + float(rows03[4]) / 60)
            channelDown01.append([lon, lat])
        id_areaMark = 1 + 0.11
        channelDown01.append([3, id_areaMark])


        ###04、转换下行航道2的经纬度###
        channelDown02 = []
        for i in range(1, sheet_channelDown02.nrows):
            rows04 = sheet_channelDown02.row_values(i)
            lat = (int(rows04[1]) + float(rows04[2]) / 60)
            lon = (int(rows04[3]) + float(rows04[4]) / 60)
            channelDown02.append([lon, lat])
        id_areaMark = 1 + 0.12
        channelDown02.append([3, id_areaMark])


        ###05、转换下行航道3的经纬度###
        channelDown03 = []
        for i in range(1, sheet_channelDown03.nrows):
            rows05 = sheet_channelDown03.row_values(i)
            lat = (int(rows05[1]) + float(rows05[2]) / 60)
            lon = (int(rows05[3]) + float(rows05[4]) / 60)
            channelDown03.append([lon, lat])
        id_areaMark = 1 + 0.13
        channelDown03.append([3, id_areaMark])

        ###06、转换下行航道4的经纬度###
        channelDown04 = []
        for i in range(1, sheet_channelDown04.nrows):
            rows06 = sheet_channelDown04.row_values(i)
            lat = (int(rows06[1]) + float(rows06[2]) / 60)
            lon = (int(rows06[3]) + float(rows06[4]) / 60)
            channelDown04.append([lon, lat])
        id_areaMark = 1 + 0.14
        channelDown04.append([3, id_areaMark])

        data_allChannel.append([channelUp01, channelUp02, channelDown01, channelDown02, channelDown03, channelDown04])


        ##########2)转换其他区域2的航道数据#############
        path_abs01 = "航道数据/小船航道/其他区域/区域2/1.xlsx"  # 绝对路径
        path_abs02 = "航道数据/小船航道/其他区域/区域2/2.xlsx"  # 绝对路径
        path_abs03 = "航道数据/小船航道/其他区域/区域2/3.xlsx"  # 绝对路径
        path_abs04 = "航道数据/小船航道/其他区域/区域2/4.xlsx"  # 绝对路径
        path_abs05 = "航道数据/小船航道/其他区域/区域2/5.xlsx"  # 绝对路径
        path_abs06 = "航道数据/小船航道/其他区域/区域2/6.xlsx"  # 绝对路径
        path01 = os.path.join(self.path_rel, path_abs01)
        path02 = os.path.join(self.path_rel, path_abs02)
        path03 = os.path.join(self.path_rel, path_abs03)
        path04 = os.path.join(self.path_rel, path_abs04)
        path05 = os.path.join(self.path_rel, path_abs05)
        path06 = os.path.join(self.path_rel, path_abs06)
        # path01 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/其他区域/区域2/1.xlsx"
        # path02 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/其他区域/区域2/2.xlsx"
        # path03 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/其他区域/区域2/3.xlsx"
        # path04 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/其他区域/区域2/4.xlsx"
        # path05 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/其他区域/区域2/5.xlsx"
        # path06 = "D:/code/苏交科/数据配置文档/航道数据/小船航道/其他区域/区域2/6.xlsx"

        data_channelUp01 = xlrd.open_workbook(r"%s" % (path01))
        data_channelUp02 = xlrd.open_workbook(r"%s" % (path02))
        data_channelUp03 = xlrd.open_workbook(r"%s" % (path03))
        data_channelUp04 = xlrd.open_workbook(r"%s" % (path04))
        data_channelDown01 = xlrd.open_workbook(r"%s" % (path05))
        data_channelDown02 = xlrd.open_workbook(r"%s" % (path06))

        sheet_channelUp01 = data_channelUp01.sheet_by_name("航线")
        sheet_channelUp02 = data_channelUp02.sheet_by_name("航线")
        sheet_channelUp03 = data_channelUp03.sheet_by_name("航线")
        sheet_channelUp04 = data_channelUp04.sheet_by_name("航线")
        sheet_channelDown01 = data_channelDown01.sheet_by_name("航线")
        sheet_channelDown02 = data_channelDown02.sheet_by_name("航线")


        ###01、转换上行航道1的经纬度###
        channelUp01 = []
        for i in range(1, sheet_channelUp01.nrows):
            rows01 = sheet_channelUp01.row_values(i)
            lat = (int(rows01[1]) + float(rows01[2]) / 60)
            lon = (int(rows01[3]) + float(rows01[4]) / 60)
            channelUp01.append([lon, lat])
        id_areaMark = 2 + 0.01
        channelUp01.append([3, id_areaMark])

        ###02、转换上行航道2的经纬度###
        channelUp02 = []
        for i in range(1, sheet_channelUp02.nrows):
            rows02 = sheet_channelUp02.row_values(i)
            lat = (int(rows02[1]) + float(rows02[2]) / 60)
            lon = (int(rows02[3]) + float(rows02[4]) / 60)
            channelUp02.append([lon, lat])
        id_areaMark = 2 + 0.02
        channelUp02.append([3, id_areaMark])

        ###03、转换上行航道3的经纬度###
        channelUp03 = []
        for i in range(1, sheet_channelUp03.nrows):
            rows03 = sheet_channelUp03.row_values(i)
            lat = (int(rows03[1]) + float(rows03[2]) / 60)
            lon = (int(rows03[3]) + float(rows03[4]) / 60)
            channelUp03.append([lon, lat])
        id_areaMark = 2 + 0.03
        channelUp03.append([3, id_areaMark])

        ###04、转换上行航道4的经纬度###
        channelUp04 = []
        for i in range(1, sheet_channelUp04.nrows):
            rows04 = sheet_channelUp04.row_values(i)
            lat = (int(rows04[1]) + float(rows04[2]) / 60)
            lon = (int(rows04[3]) + float(rows04[4]) / 60)
            channelUp04.append([lon, lat])
        id_areaMark = 2 + 0.04
        channelUp04.append([3, id_areaMark])

        ###05、转换下行航道1的经纬度###
        channelDown01 = []
        for i in range(1, sheet_channelDown01.nrows):
            rows05 = sheet_channelDown01.row_values(i)
            lat = (int(rows05[1]) + float(rows05[2]) / 60)
            lon = (int(rows05[3]) + float(rows05[4]) / 60)
            channelDown01.append([lon, lat])
        id_areaMark = 2 + 0.11
        channelDown01.append([3, id_areaMark])

        ###06、转换下行航道2的经纬度###
        channelDown02 = []
        for i in range(1, sheet_channelDown02.nrows):
            rows06 = sheet_channelDown02.row_values(i)
            lat = (int(rows06[1]) + float(rows06[2]) / 60)
            lon = (int(rows06[3]) + float(rows06[4]) / 60)
            channelDown02.append([lon, lat])
        id_areaMark = 2 + 0.12
        channelDown02.append([3, id_areaMark])

        data_allChannel.append([channelUp01, channelUp02, channelUp03, channelUp04, channelDown01, channelDown02])
        return data_allChannel

    #1.3获取当本船为小船时的静态数据
    def get_data_smallShip(self):
        """
        输入：调用def get_areaData_smallShip和def get_channelData_smallShip方法，获取区域和航道信息
        输出：[区域信息, 航道信息]
        """


        dataArea = self.get_areaData_smallShip()
        dataChannel = self.get_channelData_smallShip()

        return [dataArea, dataChannel]


    ########################################################2、本船为大船（开发完成，待验证）##################################
    #2.1 获取当本船为大船时的区域数据
    def get_areaData_bigShip(self):
        """
            输入：读取路径为“D:/code/苏交科/数据配置文档/区域数据/大船”里的excel文件获取区域信息
            输出：[正常区域区域信息, 交汇区域区域信息,其他区域区域信息]-----正常区域区域信息=[区域1,区域2...]------区域i=[右上,右下,左上,左下,id]----左/右=[lon,lat]
        """

        #############################（1）获取正常区域信息####################################
        data_allArea = []  # 存放正常区域信息
        for id_normalArea in range(1, 10):
            # 1)打开表
            path_abs = "区域数据/大船区域/正常区域/区域%d.xlsx" % (id_normalArea)  # 绝对路径
            path = os.path.join(self.path_rel, path_abs)
            #path = "D:/code/苏交科/数据配置文档/区域数据/大船区域/正常区域/区域%d.xlsx" % (id_normalArea)
            data_area = xlrd.open_workbook(r"%s" % (path))

            # 2)获取sheet（区域）中内容
            sheet = data_area.sheet_by_name("区域")

            # 3)处理经纬度，将分转换为°
            data_oneArea = []
            for i in range(1, sheet.nrows):
                rows01 = sheet.row_values(i)
                data_oneArea.append([int(rows01[1]) + float(rows01[2]) / 60,int(rows01[3]) + float(rows01[4]) / 60])

            data_oneArea.append([1,id_normalArea])
            data_allArea.append(data_oneArea)

        #############################（2）获取交汇区域信息####################################
        for id_specialArea in range(1, 4):
            # 1） 打开表
            path_abs = "区域数据/大船区域/交汇区域/区域%d.xlsx" % (id_specialArea)  # 绝对路径
            path = os.path.join(self.path_rel, path_abs)
            #path = "D:/code/苏交科/数据配置文档/区域数据/大船区域/交汇区域/区域%d.xlsx"  % (id_specialArea)
            data_area = xlrd.open_workbook(r"%s" % (path))

            # 2）获取sheet（区域）中内容
            sheet = data_area.sheet_by_name("区域")

            # 3）处理经纬度，将分转换为°
            data_oneArea = []
            for i in range(1, sheet.nrows):
                rows01 = sheet.row_values(i)
                data_oneArea.append([int(rows01[1]) + float(rows01[2]) / 60,int(rows01[3]) + float(rows01[4]) / 60])
            data_oneArea.append([2, id_specialArea])
            data_allArea.append(data_oneArea)

        #############################（3）获取其他区域信息####################################
        data_otherArea = []  # 存放其他区域信息
        for id_otherArea in range(1, 3):
            # 1） 打开表
            path_abs = "区域数据/大船区域/其他区域/区域%d.xlsx" % (id_otherArea)  # 绝对路径
            path = os.path.join(self.path_rel, path_abs)
            #path = "D:/code/苏交科/数据配置文档/区域数据/大船区域/其他区域/区域%d.xlsx" % (id_otherArea)
            data_area = xlrd.open_workbook(r"%s" % (path))

            # 2）获取sheet（区域）中内容
            sheet = data_area.sheet_by_name("区域")

            # 3）处理经纬度，将分转换为°
            data_oneArea = []
            for i in range(1, sheet.nrows):
                rows01 = sheet.row_values(i)
                data_oneArea.append([int(rows01[1]) + float(rows01[2]) / 60,int(rows01[3]) + float(rows01[4]) / 60])
            data_oneArea.append([3, id_otherArea])
            data_allArea.append(data_oneArea)
        return data_allArea

    #2.2 获取当本船为大船时的航道数据
    def get_channelData_bigShip(self):
        """
           输入：读取路径为“D:/code/苏交科/数据配置文档/航道数据/大船航道”里的excel文件获取航道信息
           输出：[正常区域航道信息, 交汇区域航道信息,其他区域航道信息]----正常区域航道信息=[区域1,区域2...]----区域i=[上行航线1,上行航线2,下行航线1,下行航线2,id]----- 上/下行航线=[点1,点2...]---点i=[lon,lat]
        """
        ###############################（1）、获取正常区域航道信息###########################
        data_allChannel = []  # 存放正常区域航道信息
        for id_normalChannel in range(1, 10):
            #########################1)打开表###################
            path_abs01 = "航道数据/大船航道/正常区域/区域%d/1.xlsx" % (id_normalChannel)  # 绝对路径
            path_abs02 = "航道数据/大船航道/正常区域/区域%d/2.xlsx" % (id_normalChannel)  # 绝对路径
            path_abs03 = "航道数据/大船航道/正常区域/区域%d/3.xlsx" % (id_normalChannel)  # 绝对路径
            path_abs04 = "航道数据/大船航道/正常区域/区域%d/4.xlsx" % (id_normalChannel)  # 绝对路径
            path01 = os.path.join(self.path_rel, path_abs01)
            path02 = os.path.join(self.path_rel, path_abs02)
            path03 = os.path.join(self.path_rel, path_abs03)
            path04 = os.path.join(self.path_rel, path_abs04)
            # path01 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/正常区域/区域%d/1.xlsx" % (id_normalChannel)
            # path02 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/正常区域/区域%d/2.xlsx" % (id_normalChannel)
            # path03 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/正常区域/区域%d/3.xlsx" % (id_normalChannel)
            # path04 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/正常区域/区域%d/4.xlsx" % (id_normalChannel)
            data_channelUp01 = xlrd.open_workbook(r"%s" % (path01))
            data_channelUp02 = xlrd.open_workbook(r"%s" % (path02))
            data_channelDown01 = xlrd.open_workbook(r"%s" % (path03))
            data_channelDown02 = xlrd.open_workbook(r"%s" % (path04))

            ################2)获取sheet（区域）中内容###################
            sheet_channelUp01 = data_channelUp01.sheet_by_name("航线")
            sheet_channelUp02 = data_channelUp02.sheet_by_name("航线")
            sheet_channelDown01 = data_channelDown01.sheet_by_name("航线")
            sheet_channelDown02 = data_channelDown02.sheet_by_name("航线")


           ################3)处理经纬度，将分转换为°###################
            ######01、转换上行航道1（up01）的经纬度######
            channelUp01=[]
            for i in range(1, sheet_channelUp01.nrows):
                rows01 = sheet_channelUp01.row_values(i)
                lat=(int(rows01[1]) + float(rows01[2]) / 60)
                lon=(int(rows01[3]) + float(rows01[4]) / 60)
                channelUp01.append([lon,lat])
            id_areaMark = id_normalChannel + 0.01
            channelUp01.append([1, id_areaMark])

            ######02、转换上行航道2（up02）的经纬度######
            channelUp02 = []
            for i in range(1, sheet_channelUp02.nrows):
                rows02 = sheet_channelUp02.row_values(i)
                lat = (int(rows02[1]) + float(rows02[2]) / 60)
                lon = (int(rows02[3]) + float(rows02[4]) / 60)
                channelUp02.append([lon, lat])
            id_areaMark = id_normalChannel + 0.02
            channelUp02.append([1, id_areaMark])

            ######03、转换下行航道1（down01）的经纬度######
            channelDown01 = []
            for i in range(1, sheet_channelDown01.nrows):
                rows03 = sheet_channelDown01.row_values(i)
                lat = (int(rows03[1]) + float(rows03[2]) / 60)
                lon = (int(rows03[3]) + float(rows03[4]) / 60)
                channelDown01.append([lon, lat])
            id_areaMark = id_normalChannel + 0.11
            channelDown01.append([1, id_areaMark])

            ######04、转换下行航道2（down02）的经纬度######
            channelDown02 = []
            for i in range(1, sheet_channelDown02.nrows):
                rows04 = sheet_channelDown02.row_values(i)
                lat = (int(rows04[1]) + float(rows04[2]) / 60)
                lon = (int(rows04[3]) + float(rows04[4]) / 60)
                channelDown02.append([lon, lat])
            id_areaMark = id_normalChannel + 0.12
            channelDown02.append([1, id_areaMark])

            data_allChannel.append([channelUp01,channelUp02,channelDown01,channelDown02])


        ###############################（2）、获取交汇区域航道信息###########################
        ##########1)转换交汇区域1#############
        path_abs01 = "航道数据/大船航道/交汇区域/区域1/1.xlsx"  # 绝对路径
        path_abs02 = "航道数据/大船航道/交汇区域/区域1/2.xlsx"   # 绝对路径
        path_abs03 = "航道数据/大船航道/交汇区域/区域1/3.xlsx"   # 绝对路径
        path_abs04 = "航道数据/大船航道/交汇区域/区域1/4.xlsx"  # 绝对路径
        path_abs05 = "航道数据/大船航道/交汇区域/区域1/5.xlsx"   # 绝对路径
        path_abs06 = "航道数据/大船航道/交汇区域/区域1/6.xlsx"   # 绝对路径
        path01 = os.path.join(self.path_rel, path_abs01)
        path02 = os.path.join(self.path_rel, path_abs02)
        path03 = os.path.join(self.path_rel, path_abs03)
        path04 = os.path.join(self.path_rel, path_abs04)
        path05 = os.path.join(self.path_rel, path_abs05)
        path06 = os.path.join(self.path_rel, path_abs06)
        # path01 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/交汇区域/区域1/1.xlsx"
        # path02 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/交汇区域/区域1/2.xlsx"
        # path03 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/交汇区域/区域1/3.xlsx"
        # path04 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/交汇区域/区域1/4.xlsx"
        # path05 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/交汇区域/区域1/5.xlsx"
        # path06 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/交汇区域/区域1/6.xlsx"

        data_channelUp01 = xlrd.open_workbook(r"%s" % (path01))
        data_channelUp02 = xlrd.open_workbook(r"%s" % (path02))
        data_channelUp03 = xlrd.open_workbook(r"%s" % (path03))
        data_channelUp04 = xlrd.open_workbook(r"%s" % (path04))
        data_channelDown01 = xlrd.open_workbook(r"%s" % (path05))
        data_channelDown02 = xlrd.open_workbook(r"%s" % (path06))

        sheet_channelUp01 = data_channelUp01.sheet_by_name("航线")
        sheet_channelUp02 = data_channelUp02.sheet_by_name("航线")
        sheet_channelUp03 = data_channelUp03.sheet_by_name("航线")
        sheet_channelUp04 = data_channelUp04.sheet_by_name("航线")
        sheet_channelDown01 = data_channelDown01.sheet_by_name("航线")
        sheet_channelDown02 = data_channelDown02.sheet_by_name("航线")

        # 转换上行航道1的经纬度
        channelUp01 = []
        for i in range(1, sheet_channelUp01.nrows):
            rows01 = sheet_channelUp01.row_values(i)
            lat = (int(rows01[1]) + float(rows01[2]) / 60)
            lon = (int(rows01[3]) + float(rows01[4]) / 60)
            channelUp01.append([lon, lat])
        id_areaMark = 1 + 0.01
        channelUp01.append([2, id_areaMark])


        # 转换上行航道2的经纬度
        channelUp02 = []
        for i in range(1, sheet_channelUp02.nrows):
            rows02 = sheet_channelUp02.row_values(i)
            lat = (int(rows02[1]) + float(rows02[2]) / 60)
            lon = (int(rows02[3]) + float(rows02[4]) / 60)
            channelUp02.append([lon, lat])
        id_areaMark = 1 + 0.02
        channelUp02.append([2, id_areaMark])


        # 转换上行航道3的经纬度
        channelUp03 = []
        for i in range(1, sheet_channelUp03.nrows):
            rows03 = sheet_channelUp03.row_values(i)
            lat = (int(rows03[1]) + float(rows03[2]) / 60)
            lon = (int(rows03[3]) + float(rows03[4]) / 60)
            channelUp03.append([lon, lat])
        id_areaMark = 1 + 0.03
        channelUp03.append([2, id_areaMark])

        # 转换上行航道4的经纬度
        channelUp04 = []
        for i in range(1, sheet_channelUp04.nrows):
            rows04 = sheet_channelUp04.row_values(i)
            lat = (int(rows04[1]) + float(rows04[2]) / 60)
            lon = (int(rows04[3]) + float(rows04[4]) / 60)
            channelUp04.append([lon, lat])
        id_areaMark = 1 + 0.04
        channelUp04.append([2, id_areaMark])


        # 转换下行航道1的经纬度
        channelDown01 = []
        for i in range(1, sheet_channelDown01.nrows):
            rows05 = sheet_channelDown01.row_values(i)
            lat = (int(rows05[1]) + float(rows05[2]) / 60)
            lon = (int(rows05[3]) + float(rows05[4]) / 60)
            channelDown01.append([lon, lat])
        id_areaMark = 1 + 0.11
        channelDown01.append([2, id_areaMark])

        # 转换下行航道2的经纬度
        channelDown02 = []
        for i in range(1, sheet_channelDown02.nrows):
            rows06 = sheet_channelDown02.row_values(i)
            lat = (int(rows06[1]) + float(rows06[2]) / 60)
            lon = (int(rows06[3]) + float(rows06[4]) / 60)
            channelDown02.append([lon, lat])
        id_areaMark = 1 + 0.12
        channelDown02.append([2, id_areaMark])

        data_allChannel.append([channelUp01,channelUp02,channelUp03,channelUp04,channelDown01,channelDown02])

        ##########2)转换交汇区域2#############
        path_abs01 = "航道数据/大船航道/交汇区域/区域2/1.xlsx"  # 绝对路径
        path_abs02 = "航道数据/大船航道/交汇区域/区域2/2.xlsx"  # 绝对路径
        path_abs03 = "航道数据/大船航道/交汇区域/区域2/3.xlsx"  # 绝对路径
        path_abs04 = "航道数据/大船航道/交汇区域/区域2/4.xlsx"  # 绝对路径
        path_abs05 = "航道数据/大船航道/交汇区域/区域2/5.xlsx"  # 绝对路径
        path_abs06 = "航道数据/大船航道/交汇区域/区域2/6.xlsx"  # 绝对路径
        path_abs07 = "航道数据/大船航道/交汇区域/区域2/7.xlsx"  # 绝对路径
        path_abs08 = "航道数据/大船航道/交汇区域/区域2/8.xlsx"  # 绝对路径
        path01 = os.path.join(self.path_rel, path_abs01)
        path02 = os.path.join(self.path_rel, path_abs02)
        path03 = os.path.join(self.path_rel, path_abs03)
        path04 = os.path.join(self.path_rel, path_abs04)
        path05 = os.path.join(self.path_rel, path_abs05)
        path06 = os.path.join(self.path_rel, path_abs06)
        path07 = os.path.join(self.path_rel, path_abs07)
        path08 = os.path.join(self.path_rel, path_abs08)
        # path01 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/交汇区域/区域2/1.xlsx"
        # path02 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/交汇区域/区域2/2.xlsx"
        # path03 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/交汇区域/区域2/3.xlsx"
        # path04 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/交汇区域/区域2/4.xlsx"
        # path05 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/交汇区域/区域2/5.xlsx"
        # path06 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/交汇区域/区域2/6.xlsx"
        # path07 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/交汇区域/区域2/7.xlsx"
        # path08 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/交汇区域/区域2/8.xlsx"

        data_channelUp01 = xlrd.open_workbook(r"%s" % (path01))
        data_channelUp02 = xlrd.open_workbook(r"%s" % (path02))
        data_channelUp03 = xlrd.open_workbook(r"%s" % (path05))
        data_channelUp04 = xlrd.open_workbook(r"%s" % (path06))
        data_channelDown01 = xlrd.open_workbook(r"%s" % (path03))
        data_channelDown02 = xlrd.open_workbook(r"%s" % (path04))
        data_channelDown03 = xlrd.open_workbook(r"%s" % (path07))
        data_channelDown04 = xlrd.open_workbook(r"%s" % (path08))

        sheet_channelUp01 = data_channelUp01.sheet_by_name("航线")
        sheet_channelUp02 = data_channelUp02.sheet_by_name("航线")
        sheet_channelUp03 = data_channelUp03.sheet_by_name("航线")
        sheet_channelUp04 = data_channelUp04.sheet_by_name("航线")
        sheet_channelDown01 = data_channelDown01.sheet_by_name("航线")
        sheet_channelDown02 = data_channelDown02.sheet_by_name("航线")
        sheet_channelDown03 = data_channelDown03.sheet_by_name("航线")
        sheet_channelDown04 = data_channelDown04.sheet_by_name("航线")

        # 转换上行航道1的经纬度
        channelUp01 = []
        for i in range(1, sheet_channelUp01.nrows):
            rows01 = sheet_channelUp01.row_values(i)
            lat = (int(rows01[1]) + float(rows01[2]) / 60)
            lon = (int(rows01[3]) + float(rows01[4]) / 60)
            channelUp01.append([lon, lat])
        id_areaMark = 2 + 0.01
        channelUp01.append([2, id_areaMark])

        # 转换上行航道2的经纬度
        channelUp02 = []
        for i in range(1, sheet_channelUp02.nrows):
            rows02 = sheet_channelUp02.row_values(i)
            lat = (int(rows02[1]) + float(rows02[2]) / 60)
            lon = (int(rows02[3]) + float(rows02[4]) / 60)
            channelUp02.append([lon, lat])
        id_areaMark = 2 + 0.02
        channelUp02.append([2, id_areaMark])

        # 转换上行航道3的经纬度
        channelUp03 = []
        for i in range(1, sheet_channelUp03.nrows):
            rows03 = sheet_channelUp03.row_values(i)
            lat = (int(rows03[1]) + float(rows03[2]) / 60)
            lon = (int(rows03[3]) + float(rows03[4]) / 60)
            channelUp03.append([lon, lat])
        id_areaMark = 2 + 0.03
        channelUp03.append([2, id_areaMark])

        # 转换上行航道4的经纬度
        channelUp04 = []
        for i in range(1, sheet_channelUp04.nrows):
            rows04 = sheet_channelUp04.row_values(i)
            lat = (int(rows04[1]) + float(rows04[2]) / 60)
            lon = (int(rows04[3]) + float(rows04[4]) / 60)
            channelUp04.append([lon, lat])
        id_areaMark = 2 + 0.04
        channelUp04.append([2, id_areaMark])

        # 转换下行航道1的经纬度
        channelDown01 = []
        for i in range(1, sheet_channelDown01.nrows):
            rows05 = sheet_channelDown01.row_values(i)
            lat = (int(rows05[1]) + float(rows05[2]) / 60)
            lon = (int(rows05[3]) + float(rows05[4]) / 60)
            channelDown01.append([lon, lat])
        id_areaMark = 2 + 0.11
        channelDown01.append([2, id_areaMark])


        # 转换下行航道2的经纬度
        channelDown02 = []
        for i in range(1, sheet_channelDown02.nrows):
            rows06 = sheet_channelDown02.row_values(i)
            lat = (int(rows06[1]) + float(rows06[2]) / 60)
            lon = (int(rows06[3]) + float(rows06[4]) / 60)
            channelDown02.append([lon, lat])
        id_areaMark = 2 + 0.12
        channelDown02.append([2, id_areaMark])

        # 转换下行航道3的经纬度
        channelDown03 = []
        for i in range(1, sheet_channelDown03.nrows):
            rows07 = sheet_channelDown03.row_values(i)
            lat = (int(rows07[1]) + float(rows07[2]) / 60)
            lon = (int(rows07[3]) + float(rows07[4]) / 60)
            channelDown03.append([lon, lat])
        id_areaMark = 2 + 0.13
        channelDown03.append([2, id_areaMark])


        # 转换下行航道2的经纬度
        channelDown04 = []
        for i in range(1, sheet_channelDown04.nrows):
            rows08 = sheet_channelDown04.row_values(i)
            lat = (int(rows08[1]) + float(rows08[2]) / 60)
            lon = (int(rows08[3]) + float(rows08[4]) / 60)
            channelDown04.append([lon, lat])
        id_areaMark = 2 + 0.14
        channelDown04.append([2, id_areaMark])
        data_allChannel.append([channelUp01, channelUp02, channelUp03, channelUp04, channelDown01, channelDown02,channelDown03,channelDown04])

        ##########3)转换交汇区域3#############
        path_abs01 = "航道数据/大船航道/交汇区域/区域3/1.xlsx"  # 绝对路径
        path_abs02 = "航道数据/大船航道/交汇区域/区域3/2.xlsx"  # 绝对路径
        path_abs03 = "航道数据/大船航道/交汇区域/区域3/3.xlsx"  # 绝对路径
        path_abs04 = "航道数据/大船航道/交汇区域/区域3/4.xlsx"  # 绝对路径
        path_abs05 = "航道数据/大船航道/交汇区域/区域3/5.xlsx"  # 绝对路径
        path_abs06 = "航道数据/大船航道/交汇区域/区域3/6.xlsx"  # 绝对路径
        path_abs07 = "航道数据/大船航道/交汇区域/区域3/7.xlsx"  # 绝对路径
        path_abs08 = "航道数据/大船航道/交汇区域/区域3/8.xlsx"  # 绝对路径
        path01 = os.path.join(self.path_rel, path_abs01)
        path02 = os.path.join(self.path_rel, path_abs02)
        path03 = os.path.join(self.path_rel, path_abs03)
        path04 = os.path.join(self.path_rel, path_abs04)
        path05 = os.path.join(self.path_rel, path_abs05)
        path06 = os.path.join(self.path_rel, path_abs06)
        path07 = os.path.join(self.path_rel, path_abs07)
        path08 = os.path.join(self.path_rel, path_abs08)
        # path01 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/交汇区域/区域3/1.xlsx"
        # path02 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/交汇区域/区域3/2.xlsx"
        # path03 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/交汇区域/区域3/3.xlsx"
        # path04 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/交汇区域/区域3/4.xlsx"
        # path05 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/交汇区域/区域3/5.xlsx"
        # path06 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/交汇区域/区域3/6.xlsx"
        # path07 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/交汇区域/区域3/7.xlsx"
        # path08 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/交汇区域/区域3/8.xlsx"

        data_channelUp01 = xlrd.open_workbook(r"%s" % (path01))
        data_channelUp02 = xlrd.open_workbook(r"%s" % (path02))
        data_channelUp03 = xlrd.open_workbook(r"%s" % (path05))
        data_channelUp04 = xlrd.open_workbook(r"%s" % (path06))
        data_channelDown01 = xlrd.open_workbook(r"%s" % (path03))
        data_channelDown02 = xlrd.open_workbook(r"%s" % (path04))
        data_channelDown03 = xlrd.open_workbook(r"%s" % (path07))
        data_channelDown04 = xlrd.open_workbook(r"%s" % (path08))

        sheet_channelUp01 = data_channelUp01.sheet_by_name("航线")
        sheet_channelUp02 = data_channelUp02.sheet_by_name("航线")
        sheet_channelUp03 = data_channelUp03.sheet_by_name("航线")
        sheet_channelUp04 = data_channelUp04.sheet_by_name("航线")
        sheet_channelDown01 = data_channelDown01.sheet_by_name("航线")
        sheet_channelDown02 = data_channelDown02.sheet_by_name("航线")
        sheet_channelDown03 = data_channelDown03.sheet_by_name("航线")
        sheet_channelDown04 = data_channelDown04.sheet_by_name("航线")

        # 转换上行航道1的经纬度
        channelUp01 = []
        for i in range(1, sheet_channelUp01.nrows):
            rows01 = sheet_channelUp01.row_values(i)
            lat = (int(rows01[1]) + float(rows01[2]) / 60)
            lon = (int(rows01[3]) + float(rows01[4]) / 60)
            channelUp01.append([lon, lat])
        id_areaMark = 3 + 0.01
        channelUp01.append([2, id_areaMark])

        # 转换上行航道2的经纬度
        channelUp02 = []
        for i in range(1, sheet_channelUp02.nrows):
            rows02 = sheet_channelUp02.row_values(i)
            lat = (int(rows02[1]) + float(rows02[2]) / 60)
            lon = (int(rows02[3]) + float(rows02[4]) / 60)
            channelUp02.append([lon, lat])
        id_areaMark = 3 + 0.02
        channelUp02.append([2, id_areaMark])

        # 转换上行航道3的经纬度
        channelUp03 = []
        for i in range(1, sheet_channelUp03.nrows):
            rows03 = sheet_channelUp03.row_values(i)
            lat = (int(rows03[1]) + float(rows03[2]) / 60)
            lon = (int(rows03[3]) + float(rows03[4]) / 60)
            channelUp03.append([lon, lat])
        id_areaMark = 3 + 0.03
        channelUp03.append([2, id_areaMark])

        # 转换上行航道4的经纬度
        channelUp04 = []
        for i in range(1, sheet_channelUp04.nrows):
            rows04 = sheet_channelUp04.row_values(i)
            lat = (int(rows04[1]) + float(rows04[2]) / 60)
            lon = (int(rows04[3]) + float(rows04[4]) / 60)
            channelUp04.append([lon, lat])
        id_areaMark = 3 + 0.04
        channelUp04.append([2, id_areaMark])

        # 转换下行航道1的经纬度
        channelDown01 = []
        for i in range(1, sheet_channelDown01.nrows):
            rows05 = sheet_channelDown01.row_values(i)
            lat = (int(rows05[1]) + float(rows05[2]) / 60)
            lon = (int(rows05[3]) + float(rows05[4]) / 60)
            channelDown01.append([lon, lat])
        id_areaMark = 3 + 0.11
        channelDown01.append([2, id_areaMark])

        # 转换下行航道2的经纬度
        channelDown02 = []
        for i in range(1, sheet_channelDown02.nrows):
            rows06 = sheet_channelDown02.row_values(i)
            lat = (int(rows06[1]) + float(rows06[2]) / 60)
            lon = (int(rows06[3]) + float(rows06[4]) / 60)
            channelDown02.append([lon, lat])
        id_areaMark = 3 + 0.12
        channelDown02.append([2, id_areaMark])

        # 转换下行航道3的经纬度
        channelDown03 = []
        for i in range(1, sheet_channelDown03.nrows):
            rows07 = sheet_channelDown03.row_values(i)
            lat = (int(rows07[1]) + float(rows07[2]) / 60)
            lon = (int(rows07[3]) + float(rows07[4]) / 60)
            channelDown03.append([lon, lat])
        id_areaMark = 3 + 0.13
        channelDown03.append([2, id_areaMark])

        # 转换下行航道2的经纬度
        channelDown04 = []
        for i in range(1, sheet_channelDown04.nrows):
            rows08 = sheet_channelDown04.row_values(i)
            lat = (int(rows08[1]) + float(rows08[2]) / 60)
            lon = (int(rows08[3]) + float(rows08[4]) / 60)
            channelDown04.append([lon, lat])
        id_areaMark = 3 + 0.14
        channelDown04.append([2, id_areaMark])

        data_allChannel.append([channelUp01, channelUp02, channelUp03, channelUp04, channelDown01, channelDown02, channelDown03,channelDown04])

        ###############################（3）、获取其他区域航道信息###########################
        data_otherChannel = []  # 存放其他区域航道信息
        ##########1)转换其他区域1#############
        path_abs01 = "航道数据/大船航道/其他区域/区域1/1.xlsx"  # 绝对路径
        path_abs02 = "航道数据/大船航道/其他区域/区域1/2.xlsx"  # 绝对路径
        path_abs03 = "航道数据/大船航道/其他区域/区域1/3.xlsx"  # 绝对路径
        path_abs04 = "航道数据/大船航道/其他区域/区域1/4.xlsx"  # 绝对路径
        path_abs05 = "航道数据/大船航道/其他区域/区域1/5.xlsx"  # 绝对路径
        path_abs06 = "航道数据/大船航道/其他区域/区域1/6.xlsx"  # 绝对路径

        path01 = os.path.join(self.path_rel, path_abs01)
        path02 = os.path.join(self.path_rel, path_abs02)
        path03 = os.path.join(self.path_rel, path_abs03)
        path04 = os.path.join(self.path_rel, path_abs04)
        path05 = os.path.join(self.path_rel, path_abs05)
        path06 = os.path.join(self.path_rel, path_abs06)

        # path01 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/其他区域/区域1/1.xlsx"
        # path02 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/其他区域/区域1/2.xlsx"
        # path03 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/其他区域/区域1/3.xlsx"
        # path04 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/其他区域/区域1/4.xlsx"
        # path05 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/其他区域/区域1/5.xlsx"
        # path06 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/其他区域/区域1/6.xlsx"

        data_channelUp01 = xlrd.open_workbook(r"%s" % (path01))
        data_channelUp02 = xlrd.open_workbook(r"%s" % (path02))
        data_channelUp03 = xlrd.open_workbook(r"%s" % (path03))
        data_channelUp04 = xlrd.open_workbook(r"%s" % (path04))
        data_channelDown01 = xlrd.open_workbook(r"%s" % (path05))
        data_channelDown02 = xlrd.open_workbook(r"%s" % (path06))

        sheet_channelUp01 = data_channelUp01.sheet_by_name("航线")
        sheet_channelUp02 = data_channelUp02.sheet_by_name("航线")
        sheet_channelUp03 = data_channelUp03.sheet_by_name("航线")
        sheet_channelUp04 = data_channelUp04.sheet_by_name("航线")
        sheet_channelDown01 = data_channelDown01.sheet_by_name("航线")
        sheet_channelDown02 = data_channelDown02.sheet_by_name("航线")

        # 转换上行航道1的经纬度
        channelUp01 = []
        for i in range(1, sheet_channelUp01.nrows):
            rows01 = sheet_channelUp01.row_values(i)
            lat = (int(rows01[1]) + float(rows01[2]) / 60)
            lon = (int(rows01[3]) + float(rows01[4]) / 60)
            channelUp01.append([lon, lat])
        id_areaMark = 1 + 0.01
        channelUp01.append([3, id_areaMark])


        # 转换上行航道2的经纬度
        channelUp02 = []
        for i in range(1, sheet_channelUp02.nrows):
            rows02 = sheet_channelUp02.row_values(i)
            lat = (int(rows02[1]) + float(rows02[2]) / 60)
            lon = (int(rows02[3]) + float(rows02[4]) / 60)
            channelUp02.append([lon, lat])
        id_areaMark = 1 + 0.02
        channelUp02.append([3, id_areaMark])


        # 转换上行航道3的经纬度
        channelUp03 = []
        for i in range(1, sheet_channelUp03.nrows):
            rows03 = sheet_channelUp03.row_values(i)
            lat = (int(rows03[1]) + float(rows03[2]) / 60)
            lon = (int(rows03[3]) + float(rows03[4]) / 60)
            channelUp03.append([lon, lat])
        id_areaMark = 1 + 0.03
        channelUp03.append([3, id_areaMark])

        # 转换上行航道4的经纬度
        channelUp04 = []
        for i in range(1, sheet_channelUp04.nrows):
            rows04 = sheet_channelUp04.row_values(i)
            lat = (int(rows04[1]) + float(rows04[2]) / 60)
            lon = (int(rows04[3]) + float(rows04[4]) / 60)
            channelUp04.append([lon, lat])
        id_areaMark = 1 + 0.04
        channelUp04.append([3, id_areaMark])

        # 转换下行航道1的经纬度
        channelDown01 = []
        for i in range(1, sheet_channelDown01.nrows):
            rows05 = sheet_channelDown01.row_values(i)
            lat = (int(rows05[1]) + float(rows05[2]) / 60)
            lon = (int(rows05[3]) + float(rows05[4]) / 60)
            channelDown01.append([lon, lat])
        id_areaMark = 1 + 0.11
        channelDown01.append([3, id_areaMark])

        # 转换下行航道2的经纬度
        channelDown02 = []
        for i in range(1, sheet_channelDown02.nrows):
            rows06 = sheet_channelDown02.row_values(i)
            lat = (int(rows06[1]) + float(rows06[2]) / 60)
            lon = (int(rows06[3]) + float(rows06[4]) / 60)
            channelDown02.append([lon, lat])
        id_areaMark = 1 + 0.12
        channelDown02.append([3, id_areaMark])
        data_allChannel.append([channelUp01, channelUp02, channelUp03, channelUp04, channelDown01, channelDown02])

        ##########2)转换其他区域2#############
        path_abs01 = "航道数据/大船航道/其他区域/区域2/1.xlsx"  # 绝对路径
        path_abs02 = "航道数据/大船航道/其他区域/区域2/2.xlsx"  # 绝对路径
        path_abs03 = "航道数据/大船航道/其他区域/区域2/3.xlsx"  # 绝对路径
        path_abs04 = "航道数据/大船航道/其他区域/区域2/4.xlsx"  # 绝对路径
        path_abs05 = "航道数据/大船航道/其他区域/区域2/5.xlsx"  # 绝对路径
        path_abs06 = "航道数据/大船航道/其他区域/区域2/6.xlsx"  # 绝对路径
        path_abs07 = "航道数据/大船航道/其他区域/区域2/7.xlsx"  # 绝对路径
        path_abs08 = "航道数据/大船航道/其他区域/区域2/8.xlsx"  # 绝对路径

        path01 = os.path.join(self.path_rel, path_abs01)
        path02 = os.path.join(self.path_rel, path_abs02)
        path03 = os.path.join(self.path_rel, path_abs03)
        path04 = os.path.join(self.path_rel, path_abs04)
        path05 = os.path.join(self.path_rel, path_abs05)
        path06 = os.path.join(self.path_rel, path_abs06)
        path07 = os.path.join(self.path_rel, path_abs05)
        path08 = os.path.join(self.path_rel, path_abs06)
        # path01 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/其他区域/区域2/1.xlsx"
        # path02 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/其他区域/区域2/2.xlsx"
        # path03 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/其他区域/区域2/3.xlsx"
        # path04 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/其他区域/区域2/4.xlsx"
        # path05 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/其他区域/区域2/5.xlsx"
        # path06 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/其他区域/区域2/6.xlsx"
        # path07 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/其他区域/区域2/7.xlsx"
        # path08 = "D:/code/苏交科/数据配置文档/航道数据/大船航道/其他区域/区域2/8.xlsx"

        data_channelUp01 = xlrd.open_workbook(r"%s" % (path01))
        data_channelUp02 = xlrd.open_workbook(r"%s" % (path02))
        data_channelUp03 = xlrd.open_workbook(r"%s" % (path05))
        data_channelUp04 = xlrd.open_workbook(r"%s" % (path06))
        data_channelDown01 = xlrd.open_workbook(r"%s" % (path03))
        data_channelDown02 = xlrd.open_workbook(r"%s" % (path04))
        data_channelDown03 = xlrd.open_workbook(r"%s" % (path07))
        data_channelDown04 = xlrd.open_workbook(r"%s" % (path08))

        sheet_channelUp01 = data_channelUp01.sheet_by_name("航线")
        sheet_channelUp02 = data_channelUp02.sheet_by_name("航线")
        sheet_channelUp03 = data_channelUp03.sheet_by_name("航线")
        sheet_channelUp04 = data_channelUp04.sheet_by_name("航线")
        sheet_channelDown01 = data_channelDown01.sheet_by_name("航线")
        sheet_channelDown02 = data_channelDown02.sheet_by_name("航线")
        sheet_channelDown03 = data_channelDown03.sheet_by_name("航线")
        sheet_channelDown04 = data_channelDown04.sheet_by_name("航线")

        # 转换上行航道1的经纬度
        channelUp01 = []
        for i in range(1, sheet_channelUp01.nrows):
            rows01 = sheet_channelUp01.row_values(i)
            lat = (int(rows01[1]) + float(rows01[2]) / 60)
            lon = (int(rows01[3]) + float(rows01[4]) / 60)
            channelUp01.append([lon, lat])
        id_areaMark = 2 + 0.01
        channelUp01.append([3, id_areaMark])

        # 转换上行航道2的经纬度
        channelUp02 = []
        for i in range(1, sheet_channelUp02.nrows):
            rows02 = sheet_channelUp02.row_values(i)
            lat = (int(rows02[1]) + float(rows02[2]) / 60)
            lon = (int(rows02[3]) + float(rows02[4]) / 60)
            channelUp02.append([lon, lat])
        id_areaMark = 2 + 0.02
        channelUp02.append([3, id_areaMark])

        # 转换上行航道3的经纬度
        channelUp03 = []
        for i in range(1, sheet_channelUp03.nrows):
            rows03 = sheet_channelUp03.row_values(i)
            lat = (int(rows03[1]) + float(rows03[2]) / 60)
            lon = (int(rows03[3]) + float(rows03[4]) / 60)
            channelUp03.append([lon, lat])
        id_areaMark = 2 + 0.03
        channelUp03.append([3, id_areaMark])

        # 转换上行航道4的经纬度
        channelUp04 = []
        for i in range(1, sheet_channelUp04.nrows):
            rows04 = sheet_channelUp04.row_values(i)
            lat = (int(rows04[1]) + float(rows04[2]) / 60)
            lon = (int(rows04[3]) + float(rows04[4]) / 60)
            channelUp04.append([lon, lat])
        id_areaMark = 2 + 0.04
        channelUp04.append([3, id_areaMark])

        # 转换下行航道1的经纬度
        channelDown01 = []
        for i in range(1, sheet_channelDown01.nrows):
            rows05 = sheet_channelDown01.row_values(i)
            lat = (int(rows05[1]) + float(rows05[2]) / 60)
            lon = (int(rows05[3]) + float(rows05[4]) / 60)
            channelDown01.append([lon, lat])
        id_areaMark = 2 + 0.11
        channelDown01.append([3, id_areaMark])

        # 转换下行航道2的经纬度
        channelDown02 = []
        for i in range(1, sheet_channelDown02.nrows):
            rows06 = sheet_channelDown02.row_values(i)
            lat = (int(rows06[1]) + float(rows06[2]) / 60)
            lon = (int(rows06[3]) + float(rows06[4]) / 60)
            channelDown02.append([lon, lat])
        id_areaMark = 2 + 0.12
        channelDown02.append([3, id_areaMark])


        # 转换下行航道3的经纬度
        channelDown03 = []
        for i in range(1, sheet_channelDown03.nrows):
            rows07 = sheet_channelDown03.row_values(i)
            lat = (int(rows07[1]) + float(rows07[2]) / 60)
            lon = (int(rows07[3]) + float(rows07[4]) / 60)
            channelDown03.append([lon, lat])
        id_areaMark = 2 + 0.13
        channelDown03.append([3, id_areaMark])

        # 转换下行航道2的经纬度
        channelDown04 = []
        for i in range(1, sheet_channelDown04.nrows):
            rows08 = sheet_channelDown04.row_values(i)
            lat = (int(rows08[1]) + float(rows08[2]) / 60)
            lon = (int(rows08[3]) + float(rows08[4]) / 60)
            channelDown04.append([lon, lat])
        id_areaMark = 2 + 0.14
        channelDown04.append([3, id_areaMark])
        data_allChannel.append([channelUp01, channelUp02, channelUp03, channelUp04, channelDown01, channelDown02, channelDown03,channelDown04])
        return data_allChannel

    #2.3 获取当本船为大船时的静态数据
    def get_data_bigShip(self):
        dataArea = self.get_areaData_bigShip()
        dataChannel = self.get_channelData_bigShip()
        return [dataArea, dataChannel]

#转换经纬度坐标为固定坐标系坐标
class Convert_Data():
    """
    转换坐标
    输入：见具体函数
    输出：见具体函数
    """
    def __init__(self,list_staticData):
        self.list_areaData=list_staticData[0] #[正常区域区域信息, 交汇区域区域信息,其他区域区域信息]
        self.list_channelData=list_staticData[1] #[正常区域航道信息, 交汇区域航道信息,其他区域航道信息]

    def convert_method(self,float_lon,float_lat):
        """
         简单转换法
         输入的经纬度的分数为10分制
         """
        X_0 = 118.4  # 经度坐标原点
        Y_0 = 31.4  # 纬度坐标原点Y

        # 在大地坐标系的位置
        y = (float(float_lat) - Y_0) * 60 * 1852
        x = (float(float_lon) - X_0) * 60 * 1852 * math.cos(float(float_lat) * math.pi / 180)
        return [x, y]

    def convert_areaData(self):
        """
        输入：[正常区域区域信息, 交汇区域区域信息,其他区域区域信息]
            正常区域区域信息=[区域1,区域2...]
            区域i=[右上,右下,左上,左下,id]
            左/右=[lon,lat]
        输出：
        """
        for item_area in self.list_areaData:
            point_upRight=self.convert_method(item_area[0][0],item_area[0][1])
            item_area[0][0]= point_upRight[0]
            item_area[0][1] = point_upRight[1]

            point_downRight = self.convert_method(item_area[1][0], item_area[1][1])
            item_area[1][0] = point_downRight[0]
            item_area[1][1] = point_downRight[1]

            point_upLeft = self.convert_method(item_area[2][0], item_area[2][1])
            item_area[2][0] = point_upLeft[0]
            item_area[2][1] = point_upLeft[1]

            point_downLeft= self.convert_method(item_area[3][0], item_area[3][1])
            item_area[3][0] =point_downLeft[0]
            item_area[3][1] = point_downLeft[1]

        return self.list_areaData

    def convert_channelData(self):
        """
        转换静态数据的坐标
        输入：所有静态数据（具体格式待定）
        输出：坐标转换后的静态数据（具体格式待定）
        """
        for item_oneArea in self.list_channelData:
            for item_channel in item_oneArea:
                for item_onePoint in item_channel[:-1]:
                    onePoint_converted=self.convert_method(item_onePoint[0],item_onePoint[1])
                    item_onePoint[0]=onePoint_converted[0]
                    item_onePoint[1]=onePoint_converted[1]

        return self.list_channelData

    def convert_staticData(self):
        data_staticArea=self.convert_areaData()
        data_staticChnnel=self.convert_channelData()
        return [data_staticArea,data_staticChnnel]

    def convert_shipsData(self,list_ownship,list_targetships):
        """
        转换船舶数据的坐标
        输入：本船和目标船舶数据（具体格式待定）
        输出：坐标转换后的船舶数据（具体格式待定）
        """
        #################转换本船坐标#####################
        ownship_converted=self.convert_method(list_ownship[0],list_ownship[1])
        list_ownship[0]=ownship_converted[0]
        list_ownship[1]=ownship_converted[1]


        #################转换目标船舶坐标#####################
        for item_targetship in list_targetships:
            targetship_converted = self.convert_method(item_targetship[0], item_targetship[1])
            item_targetship[0]= targetship_converted[0]
            item_targetship[1]=targetship_converted[1]

        return [list_ownship,list_targetships]

#处理坐标转换后的航道数据，划分为若干个航段
class Deal_DataChannel():
    def __init__(self,list_channelData,int_type_channel):
        self.list_channelData=list_channelData  #[区域1、区域2、区域3...]
        self.int_type=int_type_channel #smallShip:小船 bigShip：大船

    def deal_bigChannel(self):
        channel_normalArea_dealed = []  # 处理过后的正常区域航道信息
        channel_crossArea_dealed = []  # 处理过后的交汇区域航道信息
        channel_otherArea_dealed = []  # 处理过后的其他区域航道信息

        for item_area in self.list_channelData:
            ###################正常区域###################
            if item_area[0][-1][0]==1:
                channel_up01 = item_area[0]  # 上行航道1
                channel_up02 = item_area[1]  # 上行航道2
                channel_down01 = item_area[2]  # 下行航道1
                channel_down02 = item_area[3]  # 下行航道2
                lenth_up = len(channel_up01)-2  # 上行航道拥有的转向点数
                lenth_down = len(channel_down01)-2  # 下行航道拥有的转向点数

                #####处理上行航道#####
                channel_up = []  # 上行航道数据
                for i in range(lenth_up):
                    list_upright = channel_up01[i]
                    list_upleft = channel_up01[i + 1]

                    list_downright = channel_up02[i]
                    list_downleft = channel_up02[i + 1]

                    #########计算航道走向##############
                    x_mid_right = (list_upright[0] + list_downright[0]) / 2
                    x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                    y_mid_right = (list_upright[1] + list_downright[1]) / 2
                    y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                    if y_mid_right == y_mid_left:
                        y_mid_right += 1
                    degree_channel = math.degrees(
                        math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                    ##较特殊的情况，
                    if x_mid_right <= x_mid_left:
                        if y_mid_right >= y_mid_left:
                            course_channel = 180 - degree_channel
                        else:
                            course_channel = degree_channel

                    else:

                        if y_mid_right >= y_mid_left:
                            course_channel = degree_channel
                        else:
                            course_channel = 180 - degree_channel

                    ####给出预定值和航道id##########
                    list_mark=[course_channel, 5, i + 1,1]   #预留值：5   i+1：航段id    1:上行航道
                    channel_up.append(
                        [list_upright, list_upleft, list_downright, list_downleft,list_mark])

                #####处理下行航道#####
                channel_down = []  # 下行航道数据
                for i in range(lenth_down):
                    list_upright = channel_down01[i + 1]
                    list_upleft = channel_down01[i]

                    list_downright = channel_down02[i + 1]
                    list_downleft = channel_down02[i]

                    #########计算航道走向##############
                    x_mid_right = (list_upright[0] + list_downright[0]) / 2
                    x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                    y_mid_right = (list_upright[1] + list_downright[1]) / 2
                    y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                    if y_mid_right == y_mid_left:
                        y_mid_right += 1
                    degree_channel = math.degrees(
                        math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                    ##较特殊的情况，
                    if x_mid_right <= x_mid_left:
                        if y_mid_right >= y_mid_left:
                            course_channel = 180 - degree_channel
                        else:
                            course_channel = degree_channel

                    else:

                        if y_mid_right >= y_mid_left:
                            course_channel = degree_channel
                        else:
                            course_channel = 180 - degree_channel

                    ####给出预定值和航道id##########
                    list_mark = [course_channel, 5, i + 1, -1]  # 预留值：5   i+1：航段id    -1:下行航道1
                    channel_down.append(
                        [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                channel_normalArea_dealed.append([channel_up, channel_down])


            ###################交汇区域###################
            elif item_area[0][-1][0]==2:
                #######交汇区域1########
                if int(item_area[0][-1][1])==1:
                    channel_up01 = item_area[0]  # 上行航道1
                    channel_up02 = item_area[1]  # 上行航道2
                    channel_up03 = item_area[2]  # 上行航道3
                    channel_up04 = item_area[3]  # 上行航道4
                    channel_down01 = item_area[4]  # 下行航道1
                    channel_down02 = item_area[5]  # 下行航道2
                    lenth_up01 = len(channel_up01) - 2  # 上行航道拥有的转向点数
                    lenth_up02 = len(channel_up03) - 2  # 上行航道拥有的转向点数
                    lenth_down = len(channel_down01) - 2  # 下行航道拥有的转向点数

                    #####处理上行航道1#####
                    channel_upOne = []  # 上行航道数据
                    for i in range(lenth_up01):
                        list_upright = channel_up01[i]
                        list_upleft = channel_up01[i + 1]

                        list_downright = channel_up02[i]
                        list_downleft = channel_up02[i + 1]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, 1]  # 预留值：5   i+1：航段id    1:上行航道
                        channel_upOne.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    #####处理上行航道2#####
                    channel_upTwo = []  # 上行航道数据
                    for i in range(lenth_up02):
                        list_upright = channel_up03[i]
                        list_upleft = channel_up03[i + 1]

                        list_downright = channel_up04[i]
                        list_downleft = channel_up04[i + 1]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, 2]  # 预留值：5   i+1：航段id    1:上行航道
                        channel_upTwo.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    #####处理下行航道1#####
                    channel_down = []  # 下行航道数据
                    for i in range(lenth_down):
                        list_upright = channel_down01[i + 1]
                        list_upleft = channel_down01[i]

                        list_downright = channel_down02[i + 1]
                        list_downleft = channel_down02[i]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, -1]  # 预留值：5   i+1：航段id    -1:下行航道1
                        channel_down.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    channel_crossArea_dealed.append([channel_upOne, channel_upTwo,channel_down])

                #######交汇区域2########
                elif int(item_area[0][-1][1])==2:
                    channel_up01 = item_area[0]  # 上行航道1
                    channel_up02 = item_area[1]  # 上行航道2
                    channel_up03 = item_area[2]  # 上行航道3
                    channel_up04 = item_area[3]  # 上行航道4
                    channel_down01 = item_area[4]  # 下行航道1
                    channel_down02 = item_area[5]  # 下行航道2
                    channel_down03 = item_area[6]  # 下行航道3
                    channel_down04 = item_area[7]  # 下行航道4

                    lenth_up01 = len(channel_up01) - 2  # 上行航道拥有的转向点数
                    lenth_up02 = len(channel_up03) - 2  # 上行航道拥有的转向点数
                    lenth_down01 = len(channel_down01) - 2  # 下行航道拥有的转向点数
                    lenth_down02 = len(channel_down03) - 2  # 下行航道拥有的转向点数
                    #####处理上行航道1#####
                    channel_upOne = []  # 上行航道数据
                    for i in range(lenth_up01):
                        list_upright = channel_up01[i]
                        list_upleft = channel_up01[i + 1]

                        list_downright = channel_up02[i]
                        list_downleft = channel_up02[i + 1]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, 1]  # 预留值：5   i+1：航段id    1:上行航道
                        channel_upOne.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    #####处理上行航道2#####
                    channel_upTwo = []  # 上行航道数据
                    for i in range(lenth_up02):
                        list_upright = channel_up03[i]
                        list_upleft = channel_up03[i + 1]

                        list_downright = channel_up04[i]
                        list_downleft = channel_up04[i + 1]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, 2]  # 预留值：5   i+1：航段id    1:上行航道
                        channel_upTwo.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    #####处理下行航道1#####
                    channel_downOne = []  # 下行航道数据
                    for i in range(lenth_down01):
                        list_upright = channel_down01[i + 1]
                        list_upleft = channel_down01[i]

                        list_downright = channel_down02[i + 1]
                        list_downleft = channel_down02[i]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, -1]  # 预留值：5   i+1：航段id    -1:下行航道1
                        channel_downOne.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    #####处理下行航道2#####
                    channel_downTwo = []  # 下行航道数据
                    for i in range(lenth_down02):
                        list_upright = channel_down03[i + 1]
                        list_upleft = channel_down03[i]

                        list_downright = channel_down04[i + 1]
                        list_downleft = channel_down04[i]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, -2]  # 预留值：5   i+1：航段id    -1:下行航道1
                        channel_downTwo.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])


                    channel_crossArea_dealed.append([channel_upOne, channel_upTwo, channel_downOne,channel_downTwo])

                #######交汇区域3########
                else:
                    channel_up01 = item_area[0]  # 上行航道1
                    channel_up02 = item_area[1]  # 上行航道2
                    channel_up03 = item_area[2]  # 上行航道3
                    channel_up04 = item_area[3]  # 上行航道4
                    channel_down01 = item_area[4]  # 下行航道1
                    channel_down02 = item_area[5]  # 下行航道2
                    channel_down03 = item_area[6]  # 下行航道3
                    channel_down04 = item_area[7]  # 下行航道4

                    lenth_up01 = len(channel_up01) - 2  # 上行航道拥有的转向点数
                    lenth_up02 = len(channel_up03) - 2  # 上行航道拥有的转向点数
                    lenth_down01 = len(channel_down01) - 2  # 下行航道拥有的转向点数
                    lenth_down02 = len(channel_down03) - 2  # 下行航道拥有的转向点数

                    #####处理上行航道1#####
                    channel_upOne = []  # 上行航道数据
                    for i in range(lenth_up01):
                        list_upright = channel_up01[i]
                        list_upleft = channel_up01[i + 1]

                        list_downright = channel_up02[i]
                        list_downleft = channel_up02[i + 1]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, 1]  # 预留值：5   i+1：航段id    1:上行航道
                        channel_upOne.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    #####处理上行航道2#####
                    channel_upTwo = []  # 上行航道数据
                    for i in range(lenth_up02):
                        list_upright = channel_up03[i]
                        list_upleft = channel_up03[i + 1]

                        list_downright = channel_up04[i]
                        list_downleft = channel_up04[i + 1]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, 2]  # 预留值：5   i+1：航段id    1:上行航道
                        channel_upTwo.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    #####处理下行航道1#####
                    channel_downOne = []  # 下行航道数据
                    for i in range(lenth_down01):
                        list_upright = channel_down01[i + 1]
                        list_upleft = channel_down01[i]

                        list_downright = channel_down02[i + 1]
                        list_downleft = channel_down02[i]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, -1]  # 预留值：5   i+1：航段id    -1:下行航道1
                        channel_downOne.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    #####处理下行航道2#####
                    channel_downTwo = []  # 下行航道数据
                    for i in range(lenth_down02):
                        list_upright = channel_down03[i + 1]
                        list_upleft = channel_down03[i]

                        list_downright = channel_down04[i + 1]
                        list_downleft = channel_down04[i]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, -2]  # 预留值：5   i+1：航段id    -1:下行航道1
                        channel_downTwo.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    channel_crossArea_dealed.append([channel_upOne, channel_upTwo, channel_downOne, channel_downTwo])


            ####################其他区域###################
            else:
                #######其他区域1########
                if int(item_area[0][-1][1]) == 1:
                    channel_up01 = item_area[0]  # 上行航道1
                    channel_up02 = item_area[1]  # 上行航道2
                    channel_up03 = item_area[2]  # 上行航道3
                    channel_up04 = item_area[3]  # 上行航道4
                    channel_down01 = item_area[4]  # 下行航道1
                    channel_down02 = item_area[5]  # 下行航道2

                    lenth_up01 = len(channel_up01) - 2  # 上行航道拥有的转向点数
                    lenth_up02 = len(channel_up03) - 2  # 上行航道拥有的转向点数
                    lenth_down01 = len(channel_down01) - 2  # 下行航道拥有的转向点数

                    #####处理上行航道1#####
                    channel_upOne = []  # 上行航道数据
                    for i in range(lenth_up01):
                        list_upright = channel_up01[i]
                        list_upleft = channel_up01[i + 1]

                        list_downright = channel_up02[i]
                        list_downleft = channel_up02[i + 1]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, 1]  # 预留值：5   i+1：航段id    1:上行航道
                        channel_upOne.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    #####处理上行航道2#####
                    channel_upTwo = []  # 上行航道数据
                    for i in range(lenth_up02):
                        list_upright = channel_up03[i]
                        list_upleft = channel_up03[i + 1]

                        list_downright = channel_up04[i]
                        list_downleft = channel_up04[i + 1]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, 2]  # 预留值：5   i+1：航段id    1:上行航道
                        channel_upTwo.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    #####处理下行航道1#####
                    channel_downOne = []  # 下行航道数据
                    for i in range(lenth_down01):
                        list_upright = channel_down01[i + 1]
                        list_upleft = channel_down01[i]

                        list_downright = channel_down02[i + 1]
                        list_downleft = channel_down02[i]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, -1]  # 预留值：5   i+1：航段id    -1:下行航道1
                        channel_downOne.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    channel_otherArea_dealed.append([channel_upOne, channel_upTwo, channel_downOne])

                #######其他区域2########
                elif int(item_area[0][-1][1]) == 2:

                    channel_up01 = item_area[0]  # 上行航道1
                    channel_up02 = item_area[1]  # 上行航道2
                    channel_up03 = item_area[2]  # 上行航道3
                    channel_up04 = item_area[3]  # 上行航道4
                    channel_down01 = item_area[4]  # 下行航道1
                    channel_down02 = item_area[5]  # 下行航道2
                    channel_down03 = item_area[6]  # 下行航道3
                    channel_down04 = item_area[7]  # 下行航道4

                    lenth_up01 = len(channel_up01) - 2  # 上行航道拥有的转向点数
                    lenth_up02 = len(channel_up03) - 2  # 上行航道拥有的转向点数
                    lenth_down01 = len(channel_down01) - 2  # 下行航道拥有的转向点数
                    lenth_down02 = len(channel_down03) - 2  # 下行航道拥有的转向点数

                    #####处理上行航道1#####
                    channel_upOne = []  # 上行航道数据
                    for i in range(lenth_up01):
                        list_upright = channel_up01[i]
                        list_upleft = channel_up01[i + 1]

                        list_downright = channel_up02[i]
                        list_downleft = channel_up02[i + 1]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, 1]  # 预留值：5   i+1：航段id    1:上行航道
                        channel_upOne.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    #####处理上行航道2#####
                    channel_upTwo = []  # 上行航道数据
                    for i in range(lenth_up02):
                        list_upright = channel_up03[i]
                        list_upleft = channel_up03[i + 1]

                        list_downright = channel_up04[i]
                        list_downleft = channel_up04[i + 1]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, 2]  # 预留值：5   i+1：航段id    1:上行航道
                        channel_upTwo.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    #####处理下行航道1#####
                    channel_downOne = []  # 下行航道数据
                    for i in range(lenth_down01):
                        list_upright = channel_down01[i + 1]
                        list_upleft = channel_down01[i]

                        list_downright = channel_down02[i + 1]
                        list_downleft = channel_down02[i]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, -1]  # 预留值：5   i+1：航段id    -1:下行航道1
                        channel_downOne.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    #####处理下行航道2#####
                    channel_downTwo = []  # 下行航道数据
                    for i in range(lenth_down02):
                        list_upright = channel_down03[i + 1]
                        list_upleft = channel_down03[i]

                        list_downright = channel_down04[i + 1]
                        list_downleft = channel_down04[i]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, -2]  # 预留值：5   i+1：航段id    -1:下行航道1
                        channel_downTwo.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    channel_otherArea_dealed.append([channel_upOne, channel_upTwo, channel_downOne, channel_downTwo])

        return [channel_normalArea_dealed,channel_crossArea_dealed,channel_otherArea_dealed]

    def deal_smallChannel(self):
        channel_normalArea_dealed = []  # 处理过后的正常区域航道信息
        channel_crossArea_dealed = []  # 处理过后的交汇区域航道信息
        channel_otherArea_dealed = []  # 处理过后的其他区域航道信息

        for item_area in self.list_channelData:
            ###################正常区域###################
            if item_area[0][-1][0]==1:
                channel_up01 = item_area[0]  # 上行航道1
                channel_up02 = item_area[1]  # 上行航道2
                channel_down01 = item_area[2]  # 下行航道1
                channel_down02 = item_area[3]  # 下行航道2
                lenth_up = len(channel_up01)-2  # 上行航道拥有的转向点数
                lenth_down = len(channel_down01)-2  # 下行航道拥有的转向点数

                #####处理上行航道#####
                channel_up = []  # 上行航道数据
                for i in range(lenth_up):
                    list_upright = channel_up01[i]
                    list_upleft = channel_up01[i + 1]

                    list_downright = channel_up02[i]
                    list_downleft = channel_up02[i + 1]

                    #########计算航道走向##############
                    x_mid_right = (list_upright[0] + list_downright[0]) / 2
                    x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                    y_mid_right = (list_upright[1] + list_downright[1]) / 2
                    y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                    if y_mid_right == y_mid_left:
                        y_mid_right += 1
                    degree_channel = math.degrees(
                        math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                    ##较特殊的情况，
                    if x_mid_right <= x_mid_left:
                        if y_mid_right >= y_mid_left:
                            course_channel = 180 - degree_channel
                        else:
                            course_channel = degree_channel

                    else:

                        if y_mid_right >= y_mid_left:
                            course_channel = degree_channel
                        else:
                            course_channel = 180 - degree_channel

                    ####给出预定值和航道id##########
                    list_mark=[course_channel, 5, i + 1,1]   #预留值：5   i+1：航段id    1:上行航道
                    channel_up.append(
                        [list_upright, list_upleft, list_downright, list_downleft,list_mark])

                #####处理下行航道#####
                channel_down = []  # 下行航道数据
                for i in range(lenth_down):
                    list_upright = channel_down01[i + 1]
                    list_upleft = channel_down01[i]

                    list_downright = channel_down02[i + 1]
                    list_downleft = channel_down02[i]

                    #########计算航道走向##############
                    x_mid_right = (list_upright[0] + list_downright[0]) / 2
                    x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                    y_mid_right = (list_upright[1] + list_downright[1]) / 2
                    y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                    if y_mid_right == y_mid_left:
                        y_mid_right += 1
                    degree_channel = math.degrees(
                        math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                    ##较特殊的情况，
                    if x_mid_right <= x_mid_left:
                        if y_mid_right >= y_mid_left:
                            course_channel = 180 - degree_channel
                        else:
                            course_channel = degree_channel

                    else:

                        if y_mid_right >= y_mid_left:
                            course_channel = degree_channel
                        else:
                            course_channel = 180 - degree_channel

                    ####给出预定值和航道id##########
                    list_mark = [course_channel, 5, i + 1, -1]  # 预留值：5   i+1：航段id    -1:下行航道1
                    channel_down.append(
                        [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                channel_normalArea_dealed.append([channel_up, channel_down])

            ###################交汇区域###################
            elif item_area[0][-1][0]==2:
                #######交汇区域1########
                if int(item_area[0][-1][1])==1 :
                    channel_up01 = item_area[0]  # 上行航道1
                    channel_up02 = item_area[1]  # 上行航道2
                    channel_down01 = item_area[2]  # 下行航道1
                    channel_down02 = item_area[3]  # 下行航道2
                    lenth_up = len(channel_up01) - 2  # 上行航道拥有的转向点数
                    lenth_down = len(channel_down01) - 2  # 下行航道拥有的转向点数

                    #####处理上行航道#####
                    channel_up = []  # 上行航道数据
                    for i in range(lenth_up):
                        list_upright = channel_up01[i]
                        list_upleft = channel_up01[i + 1]

                        list_downright = channel_up02[i]
                        list_downleft = channel_up02[i + 1]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, 1]  # 预留值：5   i+1：航段id    1:上行航道
                        channel_up.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    #####处理下行航道#####
                    channel_down = []  # 下行航道数据
                    for i in range(lenth_down):
                        list_upright = channel_down01[i + 1]
                        list_upleft = channel_down01[i]

                        list_downright = channel_down02[i + 1]
                        list_downleft = channel_down02[i]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, -1]  # 预留值：5   i+1：航段id    -1:下行航道1
                        channel_down.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    channel_crossArea_dealed.append([channel_up, channel_down])

                #######交汇区域2########
                elif int(item_area[0][-1][1])==2 :
                    channel_up01 = item_area[0]  # 上行航道1
                    channel_up02 = item_area[1]  # 上行航道2
                    channel_down01 = item_area[2]  # 下行航道1
                    channel_down02 = item_area[3]  # 下行航道2
                    channel_down03 = item_area[4]  # 下行航道3
                    channel_down04 = item_area[5]  # 下行航道4

                    lenth_up01 = len(channel_up01) - 2  # 上行航道拥有的转向点数
                    lenth_down01 = len(channel_down01) - 2  # 下行航道拥有的转向点数
                    lenth_down02 = len(channel_down03) - 2  # 下行航道拥有的转向点数
                    #####处理上行航道1#####
                    channel_upOne = []  # 上行航道数据
                    for i in range(lenth_up01):
                        list_upright = channel_up01[i]
                        list_upleft = channel_up01[i + 1]

                        list_downright = channel_up02[i]
                        list_downleft = channel_up02[i + 1]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, 1]  # 预留值：5   i+1：航段id    1:上行航道
                        channel_upOne.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])


                    #####处理下行航道1#####
                    channel_downOne = []  # 下行航道数据
                    for i in range(lenth_down01):
                        list_upright = channel_down01[i + 1]
                        list_upleft = channel_down01[i]

                        list_downright = channel_down02[i + 1]
                        list_downleft = channel_down02[i]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, -1]  # 预留值：5   i+1：航段id    -1:下行航道1
                        channel_downOne.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    #####处理下行航道2#####
                    channel_downTwo = []  # 下行航道数据
                    for i in range(lenth_down02):
                        list_upright = channel_down03[i + 1]
                        list_upleft = channel_down03[i]

                        list_downright = channel_down04[i + 1]
                        list_downleft = channel_down04[i]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, -2]  # 预留值：5   i+1：航段id    -1:下行航道1
                        channel_downTwo.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])


                    channel_crossArea_dealed.append([channel_upOne,  channel_downOne,channel_downTwo])

                #######交汇区域3########
                elif int(item_area[0][-1][1]) == 3:
                    channel_up01 = item_area[0]  # 上行航道1
                    channel_up02 = item_area[1]  # 上行航道2
                    channel_down01 = item_area[2]  # 下行航道1
                    channel_down02 = item_area[3]  # 下行航道2
                    channel_down03 = item_area[4]  # 下行航道3
                    channel_down04 = item_area[5]  # 下行航道4

                    lenth_up01 = len(channel_up01) - 2  # 上行航道拥有的转向点数
                    lenth_down01 = len(channel_down01) - 2  # 下行航道拥有的转向点数
                    lenth_down02 = len(channel_down03) - 2  # 下行航道拥有的转向点数
                    #####处理上行航道1#####
                    channel_upOne = []  # 上行航道数据
                    for i in range(lenth_up01):
                        list_upright = channel_up01[i]
                        list_upleft = channel_up01[i + 1]

                        list_downright = channel_up02[i]
                        list_downleft = channel_up02[i + 1]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, 1]  # 预留值：5   i+1：航段id    1:上行航道
                        channel_upOne.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    #####处理下行航道1#####
                    channel_downOne = []  # 下行航道数据
                    for i in range(lenth_down01):
                        list_upright = channel_down01[i + 1]
                        list_upleft = channel_down01[i]

                        list_downright = channel_down02[i + 1]
                        list_downleft = channel_down02[i]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, -1]  # 预留值：5   i+1：航段id    -1:下行航道1
                        channel_downOne.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    #####处理下行航道2#####
                    channel_downTwo = []  # 下行航道数据
                    for i in range(lenth_down02):
                        list_upright = channel_down03[i + 1]
                        list_upleft = channel_down03[i]

                        list_downright = channel_down04[i + 1]
                        list_downleft = channel_down04[i]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, -2]  # 预留值：5   i+1：航段id    -1:下行航道1
                        channel_downTwo.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    channel_crossArea_dealed.append([channel_upOne, channel_downOne, channel_downTwo])

                #######交汇区域4########
                elif int(item_area[0][-1][1]) == 4:
                    channel_up01 = item_area[0]  # 上行航道1
                    channel_up02 = item_area[1]  # 上行航道2
                    channel_down01 = item_area[2]  # 下行航道1
                    channel_down02 = item_area[3]  # 下行航道2
                    lenth_up = len(channel_up01) - 2  # 上行航道拥有的转向点数
                    lenth_down = len(channel_down01) - 2  # 下行航道拥有的转向点数

                    #####处理上行航道#####
                    channel_up = []  # 上行航道数据
                    for i in range(lenth_up):
                        list_upright = channel_up01[i]
                        list_upleft = channel_up01[i + 1]

                        list_downright = channel_up02[i]
                        list_downleft = channel_up02[i + 1]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, 1]  # 预留值：5   i+1：航段id    1:上行航道
                        channel_up.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    #####处理下行航道#####
                    channel_down = []  # 下行航道数据
                    for i in range(lenth_down):
                        list_upright = channel_down01[i + 1]
                        list_upleft = channel_down01[i]

                        list_downright = channel_down02[i + 1]
                        list_downleft = channel_down02[i]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, -1]  # 预留值：5   i+1：航段id    -1:下行航道1
                        channel_down.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    channel_crossArea_dealed.append([channel_up, channel_down])

                #######交汇区域5########
                elif int(item_area[0][-1][1]) == 5:
                    channel_up01 = item_area[0]  # 上行航道1
                    channel_up02 = item_area[1]  # 上行航道2
                    channel_down01 = item_area[2]  # 下行航道1
                    channel_down02 = item_area[3]  # 下行航道2
                    lenth_up = len(channel_up01) - 2  # 上行航道拥有的转向点数
                    lenth_down = len(channel_down01) - 2  # 下行航道拥有的转向点数

                    #####处理上行航道#####
                    channel_up = []  # 上行航道数据
                    for i in range(lenth_up):
                        list_upright = channel_up01[i]
                        list_upleft = channel_up01[i + 1]

                        list_downright = channel_up02[i]
                        list_downleft = channel_up02[i + 1]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, 1]  # 预留值：5   i+1：航段id    1:上行航道
                        channel_up.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    #####处理下行航道#####
                    channel_down = []  # 下行航道数据
                    for i in range(lenth_down):
                        list_upright = channel_down01[i + 1]
                        list_upleft = channel_down01[i]

                        list_downright = channel_down02[i + 1]
                        list_downleft = channel_down02[i]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, -1]  # 预留值：5   i+1：航段id    -1:下行航道1
                        channel_down.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    channel_crossArea_dealed.append([channel_up, channel_down])

            ####################其他区域###################
            else:
                #######其他区域1########
                if int(item_area[0][-1][1]) == 1:
                    channel_up01 = item_area[0]  # 上行航道1
                    channel_up02 = item_area[1]  # 上行航道2
                    channel_down01 = item_area[2]  # 下行航道1
                    channel_down02 = item_area[3]  # 下行航道2
                    channel_down03 = item_area[4]  # 下行航道3
                    channel_down04 = item_area[5]  # 下行航道4

                    lenth_up01 = len(channel_up01) - 2  # 上行航道拥有的转向点数
                    lenth_down01 = len(channel_down01) - 2  # 下行航道拥有的转向点数
                    lenth_down02 = len(channel_down03) - 2  # 下行航道拥有的转向点数
                    #####处理上行航道1#####
                    channel_upOne = []  # 上行航道数据
                    for i in range(lenth_up01):
                        list_upright = channel_up01[i]
                        list_upleft = channel_up01[i + 1]

                        list_downright = channel_up02[i]
                        list_downleft = channel_up02[i + 1]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, 1]  # 预留值：5   i+1：航段id    1:上行航道
                        channel_upOne.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    #####处理下行航道1#####
                    channel_downOne = []  # 下行航道数据
                    for i in range(lenth_down01):
                        list_upright = channel_down01[i + 1]
                        list_upleft = channel_down01[i]

                        list_downright = channel_down02[i + 1]
                        list_downleft = channel_down02[i]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, -1]  # 预留值：5   i+1：航段id    -1:下行航道1
                        channel_downOne.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    #####处理下行航道2#####
                    channel_downTwo = []  # 下行航道数据
                    for i in range(lenth_down02):
                        list_upright = channel_down03[i + 1]
                        list_upleft = channel_down03[i]

                        list_downright = channel_down04[i + 1]
                        list_downleft = channel_down04[i]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, -2]  # 预留值：5   i+1：航段id    -1:下行航道1
                        channel_downTwo.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    channel_otherArea_dealed.append([channel_upOne, channel_downOne, channel_downTwo])

                #######其他区域2########
                if int(item_area[0][-1][1]) == 2:
                    channel_up01 = item_area[0]  # 上行航道1
                    channel_up02 = item_area[1]  # 上行航道2
                    channel_up03 = item_area[2]  # 上行航道3
                    channel_up04 = item_area[3]  # 上行航道4
                    channel_down01 = item_area[4]  # 下行航道1
                    channel_down02 = item_area[5]  # 下行航道2
                    lenth_up01 = len(channel_up01) - 2  # 上行航道拥有的转向点数
                    lenth_up02 = len(channel_up03) - 2  # 上行航道拥有的转向点数
                    lenth_down = len(channel_down01) - 2  # 下行航道拥有的转向点数

                    #####处理上行航道1#####
                    channel_upOne = []  # 上行航道数据
                    for i in range(lenth_up01):
                        list_upright = channel_up01[i]
                        list_upleft = channel_up01[i + 1]

                        list_downright = channel_up02[i]
                        list_downleft = channel_up02[i + 1]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, 1]  # 预留值：5   i+1：航段id    1:上行航道
                        channel_upOne.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    #####处理上行航道2#####
                    channel_upTwo = []  # 上行航道数据
                    for i in range(lenth_up02):
                        list_upright = channel_up03[i]
                        list_upleft = channel_up03[i + 1]

                        list_downright = channel_up04[i]
                        list_downleft = channel_up04[i + 1]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, 2]  # 预留值：5   i+1：航段id    1:上行航道
                        channel_upTwo.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    #####处理下行航道1#####
                    channel_down = []  # 下行航道数据
                    for i in range(lenth_down):
                        list_upright = channel_down01[i + 1]
                        list_upleft = channel_down01[i]

                        list_downright = channel_down02[i + 1]
                        list_downleft = channel_down02[i]

                        #########计算航道走向##############
                        x_mid_right = (list_upright[0] + list_downright[0]) / 2
                        x_mid_left = (list_upleft[0] + list_downleft[0]) / 2
                        y_mid_right = (list_upright[1] + list_downright[1]) / 2
                        y_mid_left = (list_upleft[1] + list_downleft[1]) / 2
                        if y_mid_right == y_mid_left:
                            y_mid_right += 1
                        degree_channel = math.degrees(
                            math.atan(abs(x_mid_left - x_mid_right) / abs(y_mid_left - y_mid_right)))

                        ##较特殊的情况，
                        if x_mid_right <= x_mid_left:
                            if y_mid_right >= y_mid_left:
                                course_channel = 180 - degree_channel
                            else:
                                course_channel = degree_channel

                        else:

                            if y_mid_right >= y_mid_left:
                                course_channel = degree_channel
                            else:
                                course_channel = 180 - degree_channel

                        ####给出预定值和航道id##########
                        list_mark = [course_channel, 5, i + 1, -1]  # 预留值：5   i+1：航段id    -1:下行航道1
                        channel_down.append(
                            [list_upright, list_upleft, list_downright, list_downleft, list_mark])

                    channel_otherArea_dealed.append([channel_upOne, channel_upTwo, channel_down])

        return [channel_normalArea_dealed,channel_crossArea_dealed,channel_otherArea_dealed]

    def deal_channel(self):
        if self.int_type=="smallShip":
            return self.deal_smallChannel()
        else:
            return self.deal_bigChannel()

#判断本船所处区域
class Judge_Area():
    """
    判断本船所处的区域
    输入：每个区域的经纬度、本船XY坐标（具体格式待定）
    输出：本船所处的区域id
    """
    def __init__(self,dataArea_converted,x_ownship,y_ownship):
        self.dataArea_converted=dataArea_converted #[区域1,区域2,区域3......] ,区域：[[lon,lat],[lon,lat],[lon,lat],[lon,lat],[id_type,id_area]]
        self.x_ownship=x_ownship
        self.y_ownship=y_ownship

    def get_idArea(self):
        x=self.x_ownship
        y=self.y_ownship
        id_location = [0,0]
        for item in self.dataArea_converted:
            # 右上角
            x1 = item[0][0]
            y1 = item[0][1]

            # 右下角
            x2 = item[1][0]
            y2 = item[1][1]

            # 左上角
            x3 = item[2][0]
            y3 = item[2][1]

            # 左下角
            x4 = item[3][0]
            y4 = item[3][1]

            s1 = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
            s2 = math.sqrt((x - x2) ** 2 + (y - y2) ** 2)
            s3 = math.sqrt((x - x3) ** 2 + (y - y3) ** 2)
            s4 = math.sqrt((x - x4) ** 2 + (y - y4) ** 2)

            l1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            l2 = math.sqrt((x4 - x2) ** 2 + (y4 - y2) ** 2)
            l3 = math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
            l4 = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

            c1 = math.degrees(math.acos((s1 ** 2 + s2 ** 2 - l1 ** 2) / (2 * s1 * s2)))
            c2 = math.degrees(math.acos((s2 ** 2 + s4 ** 2 - l2 ** 2) / (2 * s2 * s4)))
            c3 = math.degrees(math.acos((s3 ** 2 + s4 ** 2 - l3 ** 2) / (2 * s3 * s4)))
            c4 = math.degrees(math.acos((s1 ** 2 + s3 ** 2 - l4 ** 2) / (2 * s1 * s3)))
            id_area = item[4]
            if 361 >= c1 + c2 + c3 + c4 > 359:
                id_location = id_area
                return id_location
        return id_location

#用速度障碍法计算危险船舶
class Warm_Danger_By_SOM():
    def __init__(self, list_own, list_ships):
        self.list_own = list_own  # [x，y，航向,速度,船长，船宽]
        self.list_ships = list_ships  # [[x，y，航向,mmsi，速度],[x，y，航向,mmsi，速度]...]
        self.time_danger = 1800

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

        # x = symbols('x')
        # y = k * x + b
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
        #print("虚拟船坐标",X_inv,Y_inv,w,L,B)

        point = []
        E_equation = k * cos(w) + sin(w)
        F_equation = b * cos(w) - Y_inv * cos(w) - X_inv * sin(w)
        C_equation = cos(w) - k * sin(w)
        D_equation = Y_inv * sin(w) - b * sin(w) - X_inv * cos(w)
        a_equation = B * B * E_equation * E_equation + L * L * C_equation * C_equation
        b_equation = 2 * B * B * E_equation * F_equation + 2 * L * L * C_equation * D_equation
        c_equation = B * B * F_equation * F_equation + L * L * D_equation * D_equation - L * L * B * B
        delta = b_equation * b_equation - 4 * a_equation * c_equation
        if delta<0:
            point_x = 0
            point_y = 0
        elif delta==0:
            point_x = -b_equation / (2 * a_equation)
            point_y = k * point_x + b
        else:
            x01 = (-b_equation + sqrt(delta)) / (2 * a_equation)
            x02 = (-b_equation - sqrt(delta)) / (2 * a_equation)
            y01 = k * x01 + b
            y02 = k * x02 + b
            if sqrt(((X_tar) - (x01)) ** 2 + ((Y_tar) - (y01)) ** 2) > sqrt(
                    ((X_tar) - (x02)) ** 2 + ((Y_tar) - (y02)) ** 2):
                point_x = x02
                point_y = y02
            else:
                point_x = x01
                point_y = y01


        # result01 = solve(((y - Y_inv) * math.cos(w) + (x - X_inv) * math.sin(w)) ** 2 / L ** 2 + (
        #          (x - X_inv) * math.cos(w) - (y - Y_inv) * math.sin(w)) ** 2 / B ** 2 - 1, x)
        # list_result = []
        # for item02 in result01:
        #     list_point = []
        #     if type(item02) == Float:
        #         list_point.append(item02)
        #         y = k * item02 + b
        #         list_point.append(y)
        #         list_result.append(list_point)
        #print("###",list_result)
        ###########分段分析他船进入船舶领域的点和时间###########################
        #确定他船进入船舶领域的点
        # point = []
        # if len(list_result) == 2:
        #
        #     x01 = list_result[0][0]  # 第一个交点x01
        #     y01 = list_result[0][1]
        #
        #     x02 = list_result[1][0]  # 第二个交点x02
        #     y02 = list_result[1][1]
        #
        #     if sqrt(((X_tar) - (x01)) ** 2 + ((Y_tar) - (y01)) ** 2) > sqrt(
        #             ((X_tar) - (x02)) ** 2 + ((Y_tar) - (y02)) ** 2):
        #         point_x = x02
        #     else:
        #         point_x = x01
        #
        #     if point_x == x01:
        #         point_y = list_result[0][1]
        #     else:
        #         point_y = list_result[1][1]
        #
        # elif len(list_result) == 1:
        #     point_x = list_result[0]
        #     point_y = list_result[1]
        #
        # elif len(list_result) == 0:
        #     point_x = 0
        #     point_y = 0

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
            #print("船舶%d进入本船船舶领域的点" % (list_ship[3]), point,t)
            return [1, t, point[0], point[1]]

    def start(self):
        list_danger_ships = []  # 危险船舶
        for item in self.list_ships:
            list_mark_ship = self.get_danger_ships(item)  # [0,0]/[1,t]

            if list_mark_ship[0] == 1:  # 目标船舶会进入本船船舶领域
                t_in = list_mark_ship[1]  # 目标船舶进入本船船舶领域的时间
                if t_in < self.time_danger:
                    list_danger_ships.append(item)

        return list_danger_ships

#判断本船/目标船与航道关系
class Which_Location():
    def __init__(self,list_own,list_channel_oneArea):
        self.list_own=list_own #[x，y，航向,速度,船长，船宽]/[x，y，航向,mmsi，速度,t_danger]
        self.list_channel_oneArea=list_channel_oneArea  #【上行航道01，上行航道02】

    ##########判别本船在航道内外#########
    def judge_ownShip_location(self):
        """
        return 非顺航道行驶：【[-1],【lon,lat】,【lon,lat】，【lon,lat】，【lon,lat】,【course，value,id1,id2】】
                航道外：[[0]]
                顺航道行驶【[1],【lon,lat】,【lon,lat】，【lon,lat】，【lon,lat】,【course，value,id1,id2】】（右上，左上，右下，左下）
        """
        for item_channel in  self.list_channel_oneArea:
            for item_oneChannel in item_channel:
                x1 = item_oneChannel[0][0]  # 右上
                y1 = item_oneChannel[0][1]

                x2 = item_oneChannel[1][0]  # 左上
                y2 = item_oneChannel[1][1]

                x3 = item_oneChannel[2][0]  # 右下
                y3 = item_oneChannel[2][1]

                x4 = item_oneChannel[3][0]  # 左下
                y4 = item_oneChannel[3][1]

                # x,y分别表示船舶的坐标
                x = self.list_own[0]
                y = self.list_own[1]

                s1 = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
                s2 = math.sqrt((x - x2) ** 2 + (y - y2) ** 2)
                s3 = math.sqrt((x - x3) ** 2 + (y - y3) ** 2)
                s4 = math.sqrt((x - x4) ** 2 + (y - y4) ** 2)

                l1 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
                l2 = math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
                l3 = math.sqrt((x4 - x2) ** 2 + (y4 - y2) ** 2)
                l4 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

                c1 = math.degrees(math.acos((s1 ** 2 + s3 ** 2 - l1 ** 2) / (2 * s1 * s3)))
                c2 = math.degrees(math.acos((s3 ** 2 + s4 ** 2 - l2 ** 2) / (2 * s3 * s4)))
                c3 = math.degrees(math.acos((s2 ** 2 + s4 ** 2 - l3 ** 2) / (2 * s2 * s4)))
                c4 = math.degrees(math.acos((s1 ** 2 + s2 ** 2 - l4 ** 2) / (2 * s1 * s2)))
                c_total = c1 + c2 + c3 + c4
                if 361 >= c_total >= 359:
                    C_channel = item_oneChannel[4][0]
                    C_own =  self.list_own[2]
                    value_channel = item_oneChannel[4][1]
                    #print("####",C_channel,C_own,value_channel)
                    if abs(C_channel - C_own) <= value_channel:
                        return [[1],item_oneChannel]

                    if abs(C_channel + 180 - C_own) <= value_channel:
                        return [[1],item_oneChannel]

                    return [[-1],item_oneChannel]
        return [[0]]

#获取航行预警信息
class Warm_Navigation():
    """
    输出：[warm_border,warm_yaw,warm_turn]
    """

    def __init__(self,list_own,list_channel):
        self.list_own=list_own #[x，y，航向,速度,船长，船宽]
        self.list_channel=list_channel #【【lon,lat】,【lon,lat】，【lon,lat】，【lon,lat】,【course，value,id1,id2】】
        self.s_border=20  #边界报警距离
        self.s_mid=20         #偏航报警距离
    def get_warm_navigation(self):

        x1 =  self.list_channel[0][0]  # 右上
        y1 =  self.list_channel[0][1]

        x2 =  self.list_channel[1][0]  # 左上
        y2 =  self.list_channel[1][1]

        x3 =  self.list_channel[2][0]  # 右下
        y3 =  self.list_channel[2][1]

        x4 =  self.list_channel[3][0]  # 左下
        y4 =  self.list_channel[3][1]

        x_own=list_ownship[0] #本船x
        y_own=list_ownship[1] #本船y
        id_mark=self.list_channel[4][3] #上行/下行
        v_own=list_ownship[3] #本船速度

        ###上边界直线方程###
        k_up = (y2 - y1) / (x2 - x1)
        b_up = y1 - k_up * x1

        ####下边界直线方程###
        k_down = (y4 - y3) / (x4 - x3)
        b_down = y3 - k_down * x3

        ####推荐航线直线方程###
        k_mid = ((y1 + y3)/2-(y2+y4)/2) / ((x1 + x3)/2-(x2+x4)/2)
        b_mid = (y1 + y3)/2 - k_mid * (x1 + x3)/2

        ####转向点所在直线方程###
        if id_mark>0: #上行
            k_turn = (y4 - y2) / (x4 - x2)
            b_turn = y2 - k_turn * x2
        else:
            k_turn = (y3 - y1) / (x3 - x1)
            b_turn = y1 - k_turn * x1

        ###本船与上边界距离###
        s_up=abs(y_own-k_up*x_own-b_up)/sqrt(1+k_up**2)

        ###本船与下边界距离###
        s_down = abs(y_own - k_down * x_own - b_down) / sqrt(1 + k_down ** 2)

        ###本船与推荐航线距离###
        s_mid = abs(y_own - k_mid * x_own - b_mid) / sqrt(1 + k_mid ** 2)

        ###本船与转向点距离和时间###
        s_turn = abs(y_own - k_turn * x_own - b_turn) / sqrt(1 + k_turn ** 2)
        t_turn=s_turn/v_own
        warm_turn=[s_turn,t_turn]
        ###返回边界预警信息###
        if id_mark > 0:  # 上行
            if s_up>=s_down:
                if s_down<self.s_border:
                    warm_border = [1,s_down]
                else:
                    warm_border = [0, 0]
            else:
                if s_up < self.s_border:
                    warm_border = [2, s_up]
                else:
                    warm_border = [0, 0]
        else:
            if s_up >= s_down:
                if s_down < self.s_border:
                    warm_border = [2, s_down]
                else:
                    warm_border = [0, 0]
            else:
                if s_up < self.s_border:
                    warm_border = [1, s_up]
                else:
                    warm_border = [0, 0]

        ###返回偏航预警信息###
        if s_mid>self.s_mid:
            if id_mark > 0:  # 上行
                if s_up >= s_down:
                    warm_yaw = [1, s_mid]
                else:
                    warm_yaw=[2,s_mid]
            else:
                if s_up >= s_down:
                    warm_yaw = [2, s_mid]
                else:
                    warm_yaw = [1, s_mid]
        else:
            warm_yaw=[0,0]


        return [warm_border,warm_yaw,warm_turn]

#得到最危险船舶
class Get_Most_Danger_Ship():
    """
    return：【【0】】/[[159825.22148001133, 60701.85576000032, 90, 413782245, 4.372778], [45]]
    """

    def __init__(self, list_ownship, list_targetships,list_channel_oneArea):
        self.list_own = list_ownship  #[x，y，航向,速度,船长，船宽]
        self.list_ships = list_targetships #[[x，y，航向,mmsi，速度],[x，y，航向,mmsi，速度]...]
        self.list_channel_oneArea=list_channel_oneArea ##【上行航道01，上行航道02...】--上行/下行航道：【航段1，航段2，航段3。。。】
        # ---【【lon,lat】,【lon,lat】，【lon,lat】，【lon,lat】,【course，value,id1,id2】】（右上，左上，右下，左下）


    ##########判别目标船舶是否顺航道行驶（已验证）#########
    def judge_targetShips_follow(self,list_targetship):
        """
        return
        """
        for item_channel in self.list_channel_oneArea:
            for item_oneChannel in item_channel:
                x1 = item_oneChannel[0][0]  # 右上
                y1 = item_oneChannel[0][1]

                x2 = item_oneChannel[1][0]  # 左上
                y2 = item_oneChannel[1][1]

                x3 = item_oneChannel[2][0]  # 右下
                y3 = item_oneChannel[2][1]

                x4 = item_oneChannel[3][0]  # 左下
                y4 = item_oneChannel[3][1]

                C_channel = item_oneChannel[4][0]
                value_channel = item_oneChannel[4][1]
                id_channel=item_oneChannel[4][2]
                # x,y分别表示船舶的坐标
                x = list_targetship[0]
                y = list_targetship[1]
                C_ship = list_targetship[2] #船舶航向

                s1 = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
                s2 = math.sqrt((x - x2) ** 2 + (y - y2) ** 2)
                s3 = math.sqrt((x - x3) ** 2 + (y - y3) ** 2)
                s4 = math.sqrt((x - x4) ** 2 + (y - y4) ** 2)

                l1 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
                l2 = math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
                l3 = math.sqrt((x4 - x2) ** 2 + (y4 - y2) ** 2)
                l4 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

                c1 = math.degrees(math.acos((s1 ** 2 + s3 ** 2 - l1 ** 2) / (2 * s1 * s3)))
                c2 = math.degrees(math.acos((s3 ** 2 + s4 ** 2 - l2 ** 2) / (2 * s3 * s4)))
                c3 = math.degrees(math.acos((s2 ** 2 + s4 ** 2 - l3 ** 2) / (2 * s2 * s4)))
                c4 = math.degrees(math.acos((s1 ** 2 + s2 ** 2 - l4 ** 2) / (2 * s1 * s2)))
                c_total = c1 + c2 + c3 + c4
                #print("####",c_total)
                if 361 >= c_total >= 359: #目标船舶在航道内
                    if abs(C_channel - C_ship) <= value_channel or abs(C_channel + 180 - C_ship) <= value_channel:
                        list_targetship.append(id_channel)

                        return [list_targetship,item_channel]

        return [[0]]
        ######### 预测顺航道行驶船舶时间t后的位置

    ##########预测本船航道行驶轨迹#########
    def predict_track_ownShip(self, list_own_ship_channel, t):
        """

        :param list_own_ship_channel: [本船,航道]
                本船：[159481.40998267243, 60818.97624000031, 110.03, 4.6763, 45, 12, 15]
                航道：上行/下行一条航道
        :param t: 0-1800
        :return:
        """

        list_ship = list_own_ship_channel[0]
        list_channel = list_own_ship_channel[1]

        if t == 0:
            return list_ship

        x_ship = list_ship[0]
        y_ship = list_ship[1]
        speed_ship = list_ship[3]

        time_start = 0
        mark_channel = list_channel[0][4][3]  # 上行、下行航道
        id_channel = list_ship[-1]  # 所在航段id
        course_out = 0
        ##船舶下行
        if mark_channel < 0:
            ####（1)计算船舶通过航道的时间和点序列#########
            for item_channel in list_channel:
                if id_channel == item_channel[4][2]:
                    x1 = item_channel[1][0]  # 左上
                    x2 = item_channel[0][0]  # 右上
                    x3 = item_channel[3][0]  # 左下
                    x4 = item_channel[2][0]  # 右下

                    y1 = item_channel[1][1]  # 左上
                    y2 = item_channel[0][1]  # 右上
                    y3 = item_channel[3][1]  # 左下
                    y4 = item_channel[2][1]  # 右下

                    # 求本船驶出航段的末尾直线方程
                    x_out_up = x2
                    y_out_up = y2
                    x_out_down = x4
                    y_out_down = y4

                    k_channel = (y_out_up - y_out_down) / (x_out_up - x_out_down)
                    b_channel = y_out_up - k_channel * x_out_up

                    # 求本船在该航段的直线方程
                    course_ship = item_channel[4][0] + 180
                    #print(t,course_ship)

                    if 180 <= course_ship < 270:
                        k_ship = math.tan(math.radians(270 - course_ship))
                    else:
                        k_ship = -math.tan(math.radians(course_ship - 270))
                    b_ship = y_ship - k_ship * x_ship

                    # 求本船驶出航段点
                    x_cross = (b_channel - b_ship) / (k_ship - k_channel)
                    y_cross = k_channel * x_cross + b_channel
                    #print(x_cross,y_cross)
                    # 求本船驶出航段的时间
                    time_cross = math.sqrt(
                        (x_cross - x_ship) ** 2 + (y_cross - y_ship) ** 2) / speed_ship + time_start

                    # 判断预测时间是否在该段内
                    if time_start < t < time_cross:
                        course_ship = item_channel[4][0]
                        time = t - time_start

                        if 0 <= course_ship < 90:
                            speed_own_x = math.sin(course_ship * math.pi / 180) * speed_ship
                            speed_own_y = math.cos(course_ship * math.pi / 180) * speed_ship
                            x_ship += time * speed_own_x
                            y_ship += time * speed_own_y
                        elif 90 <= course_ship < 180:
                            speed_own_x = math.cos((course_ship - 90) * math.pi / 180) * speed_ship
                            speed_own_y = math.sin((course_ship - 90) * math.pi / 180) * speed_ship
                            x_ship += time * speed_own_x
                            y_ship -= time * speed_own_y
                        elif 180 <= course_ship < 270:
                            speed_own_x = math.sin((course_ship - 180) * math.pi / 180) * speed_ship
                            speed_own_y = math.cos((course_ship - 180) * math.pi / 180) * speed_ship
                            x_ship -= time * speed_own_x
                            y_ship -= time * speed_own_y
                        else:
                            speed_own_x = math.cos((course_ship - 270) * math.pi / 180) * speed_ship
                            speed_own_y = math.sin((course_ship - 270) * math.pi / 180) * speed_ship
                            x_ship -= time * speed_own_x
                            y_ship += time * speed_own_y

                        #print(t,time,x_ship, y_ship,course_ship, list_ship[3], list_ship[4], list_ship[5])
                        return [x_ship, y_ship,course_ship, list_ship[3], list_ship[4], list_ship[5]]
                    else:
                        id_channel += 1
                        x_ship = x_cross
                        y_ship = y_cross
                        time_start = time_cross
                        course_out = course_ship

            time = t - time_start
            if 0 <= course_out < 90:
                speed_x = math.sin(course_out * math.pi / 180) * speed_ship
                speed_y = math.cos(course_out * math.pi / 180) * speed_ship
                x_ship += time * speed_x
                y_ship += time * speed_y
            elif 90 <= course_out < 180:
                speed_x = math.cos((course_out - 90) * math.pi / 180) * speed_ship
                speed_y = math.sin((course_out - 90) * math.pi / 180) * speed_ship
                x_ship += time * speed_x
                y_ship -= time * speed_y
            elif 180 <= course_out < 270:
                speed_x = math.sin((course_out - 180) * math.pi / 180) * speed_ship
                speed_y = math.cos((course_out - 180) * math.pi / 180) * speed_ship
                x_ship -= time * speed_x
                y_ship -= time * speed_y
            else:
                speed_x = math.cos((course_out - 270) * math.pi / 180) * speed_ship
                speed_y = math.sin((course_out - 270) * math.pi / 180) * speed_ship
                x_ship -= time * speed_x
                y_ship += time * speed_y

            return [x_ship, y_ship,course_out, list_ship[3], list_ship[4], list_ship[5]]

        ##船舶上行
        else:
            ####（1)计算船舶通过航道的时间和点序列#########
            for item_channel in list_channel:
                if id_channel == item_channel[4][2]:
                    x1 = item_channel[0][0]  # 右上
                    x2 = item_channel[1][0]  # 左上
                    x3 = item_channel[2][0]  # 右下
                    x4 = item_channel[3][0]  # 左下

                    y1 = item_channel[0][1]  # 右上
                    y2 = item_channel[1][1]  # 左上
                    y3 = item_channel[2][1]  # 右下
                    y4 = item_channel[3][1]  # 左下

                    # 求本船驶出航段的末尾直线方程
                    x_out_up = x2
                    y_out_up = y2
                    x_out_down = x4
                    y_out_down = y4
                    k_channel = (y_out_up - y_out_down) / (x_out_up - x_out_down)
                    b_channel = y_out_up - k_channel * x_out_up

                    # 求本船在该航段的直线方程
                    course_ship = item_channel[4][0] + 180
                    if 180 <= course_ship < 270:
                        k_ship = math.tan(math.radians(270 - course_ship))
                    else:
                        k_ship = -math.tan(math.radians(course_ship - 270))
                    b_ship = y_ship - k_ship * x_ship

                    # 求本船驶出航段点
                    x_cross = (b_channel - b_ship) / (k_ship - k_channel)
                    y_cross = k_channel * x_cross + b_channel

                    # 求本船驶出航段的时间
                    time_cross = math.sqrt(
                        (x_cross - x_ship) ** 2 + (y_cross - y_ship) ** 2) / speed_ship + time_start

                    # 判断预测时间是否在该段内
                    if time_start < t < time_cross:
                        time = t - time_start
                        if 0 <= course_ship < 90:
                            speed_own_x = math.sin(course_ship * math.pi / 180) * speed_ship
                            speed_own_y = math.cos(course_ship * math.pi / 180) * speed_ship
                            x_ship += time * speed_own_x
                            y_ship += time * speed_own_y
                        elif 90 <= course_ship < 180:
                            speed_own_x = math.cos((course_ship - 90) * math.pi / 180) * speed_ship
                            speed_own_y = math.sin((course_ship - 90) * math.pi / 180) * speed_ship
                            x_ship += time * speed_own_x
                            y_ship -= time * speed_own_y
                        elif 180 <= course_ship < 270:
                            speed_own_x = math.sin((course_ship - 180) * math.pi / 180) * speed_ship
                            speed_own_y = math.cos((course_ship - 180) * math.pi / 180) * speed_ship
                            x_ship -= time * speed_own_x
                            y_ship -= time * speed_own_y
                        else:
                            speed_own_x = math.cos((course_ship - 270) * math.pi / 180) * speed_ship
                            speed_own_y = math.sin((course_ship - 270) * math.pi / 180) * speed_ship
                            x_ship -= time * speed_own_x
                            y_ship += time * speed_own_y

                        return [x_ship, y_ship, course_ship, list_ship[3], list_ship[4], list_ship[5]]
                    else:
                        id_channel += 1
                        x_ship = x_cross
                        y_ship = y_cross
                        time_start = time_cross
                        course_out = course_ship

                time = t - time_start
                if 0 <= course_out < 90:
                    speed_x = math.sin(course_out * math.pi / 180) * speed_ship
                    speed_y = math.cos(course_out * math.pi / 180) * speed_ship
                    x_ship += time * speed_x
                    y_ship += time * speed_y
                elif 90 <= course_out < 180:
                    speed_x = math.cos((course_out - 90) * math.pi / 180) * speed_ship
                    speed_y = math.sin((course_out - 90) * math.pi / 180) * speed_ship
                    x_ship += time * speed_x
                    y_ship -= time * speed_y
                elif 180 <= course_out < 270:
                    speed_x = math.sin((course_out - 180) * math.pi / 180) * speed_ship
                    speed_y = math.cos((course_out - 180) * math.pi / 180) * speed_ship
                    x_ship -= time * speed_x
                    y_ship -= time * speed_y
                else:
                    speed_x = math.cos((course_out - 270) * math.pi / 180) * speed_ship
                    speed_y = math.sin((course_out - 270) * math.pi / 180) * speed_ship
                    x_ship -= time * speed_x
                    y_ship += time * speed_y

                return [x_ship, y_ship,course_out, list_ship[3], list_ship[4], list_ship[5]]

    ##########预测目标船舶顺航道行驶船舶轨迹#########
    def predict_track_follow_channel(self, list_own_ship_channel, t):
        list_ship=list_own_ship_channel[0]
        list_channel=list_own_ship_channel[1]

        if t==0:
            return list_ship

        x_ship = list_ship[0]
        y_ship = list_ship[1]
        speed_ship = list_ship[4]

        time_start = 0
        mark_channel=list_channel[0][4][3]  #上行、下行航道
        id_channel= list_ship[-1]  #所在航段id
        course_out=0
        ##船舶下行
        if  mark_channel <0:
            ####（1)计算船舶通过航道的时间和点序列#########
            for item_channel in list_channel:
                if id_channel == item_channel[4][2]:

                    x1 = item_channel[1][0] # 左上
                    x2 = item_channel[0][0] # 右上
                    x3 = item_channel[3][0] # 左下
                    x4 = item_channel[2][0] # 右下

                    y1 = item_channel[1][1]  # 左上
                    y2 = item_channel[0][1]  # 右上
                    y3 = item_channel[3][1]  # 左下
                    y4 = item_channel[2][1]  # 右下


                    # 求本船驶出航段的末尾直线方程
                    x_out_up = x2
                    y_out_up = y2
                    x_out_down = x4
                    y_out_down = y4
                    k_channel = (y_out_up - y_out_down) / (x_out_up - x_out_down)
                    b_channel = y_out_up - k_channel * x_out_up

                    # 求本船在该航段的直线方程
                    course_ship = item_channel[4][0] + 180
                    if 180 <= course_ship < 270:
                        k_ship = math.tan(math.radians(270 - course_ship))
                    else:
                        k_ship = -math.tan(math.radians(course_ship - 270))
                    b_ship = y_ship - k_ship * x_ship

                    # 求本船驶出航段点
                    x_cross = (b_channel - b_ship) / (k_ship - k_channel)
                    y_cross = k_channel * x_cross + b_channel

                    # 求本船驶出航段的时间
                    time_cross = math.sqrt((x_cross - x_ship) ** 2 + (y_cross - y_ship) ** 2) / speed_ship + time_start

                    #判断预测时间是否在该段内
                    if time_start<t<time_cross:
                        course_ship= item_channel[4][0]
                        time = t - time_start
                        if 0 <= course_ship < 90:
                            speed_own_x = math.sin(course_ship * math.pi / 180) * speed_ship
                            speed_own_y = math.cos(course_ship * math.pi / 180) * speed_ship
                            x_ship += time * speed_own_x
                            y_ship += time * speed_own_y
                        elif 90 <= course_ship < 180:
                            speed_own_x = math.cos((course_ship - 90) * math.pi / 180) * speed_ship
                            speed_own_y = math.sin((course_ship - 90) * math.pi / 180) * speed_ship
                            x_ship += time * speed_own_x
                            y_ship -= time * speed_own_y
                        elif 180 <= course_ship < 270:
                            speed_own_x = math.sin((course_ship - 180) * math.pi / 180) * speed_ship
                            speed_own_y = math.cos((course_ship - 180) * math.pi / 180) * speed_ship
                            x_ship -= time * speed_own_x
                            y_ship -= time * speed_own_y
                        else:
                            speed_own_x = math.cos((course_ship - 270) * math.pi / 180) * speed_ship
                            speed_own_y = math.sin((course_ship - 270) * math.pi / 180) * speed_ship
                            x_ship -= time * speed_own_x
                            y_ship += time * speed_own_y


                        return [x_ship, y_ship, course_ship, list_ship[3], list_ship[4]]

                    else:
                        id_channel += 1
                        x_ship = x_cross
                        y_ship = y_cross
                        time_start = time_cross
                        course_out=course_ship

            time = t - time_start
            if 0 <= course_out < 90:
                speed_x = math.sin(course_out * math.pi / 180) * speed_ship
                speed_y = math.cos(course_out * math.pi / 180) * speed_ship
                x_ship += time * speed_x
                y_ship += time * speed_y
            elif 90 <= course_out < 180:
                speed_x = math.cos((course_out - 90) * math.pi / 180) * speed_ship
                speed_y = math.sin((course_out - 90) * math.pi / 180) * speed_ship
                x_ship += time * speed_x
                y_ship -= time * speed_y
            elif 180 <=course_out < 270:
                speed_x = math.sin((course_out - 180) * math.pi / 180) * speed_ship
                speed_y = math.cos((course_out - 180) * math.pi / 180) * speed_ship
                x_ship -= time * speed_x
                y_ship -= time * speed_y
            else:
                speed_x = math.cos((course_out - 270) * math.pi / 180) * speed_ship
                speed_y = math.sin((course_out - 270) * math.pi / 180) * speed_ship
                x_ship -= time * speed_x
                y_ship += time * speed_y

            return [x_ship, y_ship,course_out, list_ship[3], list_ship[4]]



        ##船舶上行
        else:
            ####（1)计算船舶通过航道的时间和点序列#########
            for item_channel in list_channel:
                if id_channel == item_channel[4][2]:
                    x1 = item_channel[0][0]  # 右上
                    x2 = item_channel[1][0]  # 左上
                    x3 = item_channel[2][0]  # 右下
                    x4 = item_channel[3][0]  # 左下

                    y1 = item_channel[0][1]  # 右上
                    y2 = item_channel[1][1]  # 左上
                    y3 = item_channel[2][1]  # 右下
                    y4 = item_channel[3][1]  # 左下


                    # 求本船驶出航段的末尾直线方程
                    x_out_up = x2
                    y_out_up = y2
                    x_out_down = x4
                    y_out_down = y4
                    k_channel = (y_out_up - y_out_down) / (x_out_up - x_out_down)
                    b_channel = y_out_up - k_channel * x_out_up

                    # 求本船在该航段的直线方程
                    course_ship = item_channel[4][0] + 180
                    if 180 <= course_ship < 270:
                        k_ship = math.tan(math.radians(270 - course_ship))
                    else:
                        k_ship = -math.tan(math.radians(course_ship - 270))
                    b_ship = y_ship - k_ship * x_ship

                    # 求本船驶出航段点
                    x_cross = (b_channel - b_ship) / (k_ship - k_channel)
                    y_cross = k_channel * x_cross + b_channel

                    # 求本船驶出航段的时间
                    time_cross = math.sqrt(
                        (x_cross - x_ship) ** 2 + (y_cross - y_ship) ** 2) / speed_ship + time_start

                    # 判断预测时间是否在该段内
                    if time_start < t < time_cross:
                        time = t - time_start
                        if 0 <= course_ship < 90:
                            speed_own_x = math.sin(course_ship * math.pi / 180) * speed_ship
                            speed_own_y = math.cos(course_ship * math.pi / 180) * speed_ship
                            x_ship += time * speed_own_x
                            y_ship += time * speed_own_y
                        elif 90 <= course_ship < 180:
                            speed_own_x = math.cos((course_ship - 90) * math.pi / 180) * speed_ship
                            speed_own_y = math.sin((course_ship - 90) * math.pi / 180) * speed_ship
                            x_ship += time * speed_own_x
                            y_ship -= time * speed_own_y
                        elif 180 <= course_ship < 270:
                            speed_own_x = math.sin((course_ship - 180) * math.pi / 180) * speed_ship
                            speed_own_y = math.cos((course_ship - 180) * math.pi / 180) * speed_ship
                            x_ship -= time * speed_own_x
                            y_ship -= time * speed_own_y
                        else:
                            speed_own_x = math.cos((course_ship - 270) * math.pi / 180) * speed_ship
                            speed_own_y = math.sin((course_ship - 270) * math.pi / 180) * speed_ship
                            x_ship -= time * speed_own_x
                            y_ship += time * speed_own_y


                        return [x_ship, y_ship, course_ship, list_ship[3], list_ship[4]]

                    else:
                        id_channel += 1
                        x_ship = x_cross
                        y_ship = y_cross
                        time_start = time_cross
                        course_out = course_ship

                time = t - time_start
                if 0 <= course_out < 90:
                    speed_x = math.sin(course_out * math.pi / 180) * speed_ship
                    speed_y = math.cos(course_out * math.pi / 180) * speed_ship
                    x_ship += time * speed_x
                    y_ship += time * speed_y
                elif 90 <= course_out < 180:
                    speed_x = math.cos((course_out - 90) * math.pi / 180) * speed_ship
                    speed_y = math.sin((course_out - 90) * math.pi / 180) * speed_ship
                    x_ship += time * speed_x
                    y_ship -= time * speed_y
                elif 180 <= course_out < 270:
                    speed_x = math.sin((course_out - 180) * math.pi / 180) * speed_ship
                    speed_y = math.cos((course_out - 180) * math.pi / 180) * speed_ship
                    x_ship -= time * speed_x
                    y_ship -= time * speed_y
                else:
                    speed_x = math.cos((course_out - 270) * math.pi / 180) * speed_ship
                    speed_y = math.sin((course_out - 270) * math.pi / 180) * speed_ship
                    x_ship -= time * speed_x
                    y_ship += time * speed_y


                return [x_ship, y_ship, course_out, list_ship[3], list_ship[4]]

    ##########预测非顺航道行驶船舶轨迹#########
    def predict_track_not_follow_channel(self,list_ship,time):
        """
        list_ship:[x，y，航向,mmsi，速度]
        """
        x = list_ship[0]  # 初始点x
        y = list_ship[1]  # 初始点y
        course_ship = list_ship[2]  # 船舶航向
        speed_ship = list_ship[4]  # 船舶速度
        mmsi=list_ship[3] #船舶编号
        if 0 <= course_ship < 90:
            speed_x = math.sin(course_ship * math.pi / 180) * speed_ship
            speed_y = math.cos(course_ship * math.pi / 180) * speed_ship
            x += time * speed_x
            y += time * speed_y
        elif 90 <= course_ship < 180:
            speed_x = math.cos((course_ship - 90) * math.pi / 180) * speed_ship
            speed_y = math.sin((course_ship - 90) * math.pi / 180) * speed_ship
            x += time * speed_x
            y -= time * speed_y
        elif 180 <= course_ship < 270:
            speed_x = math.sin((course_ship - 180) * math.pi / 180) * speed_ship
            speed_y = math.cos((course_ship - 180) * math.pi / 180) * speed_ship
            x -= time * speed_x
            y -= time * speed_y
        else:
            speed_x = math.cos((course_ship - 270) * math.pi / 180) * speed_ship
            speed_y = math.sin((course_ship - 270) * math.pi / 180) * speed_ship
            x -= time * speed_x
            y += time * speed_y

        ##替换为t时刻的坐标

        return [x,y,list_ship[2],list_ship[3],list_ship[4]]

    ########获取危险船舶##########
    def get_danger_ships(self, list_own, list_ships):
        list_danger_ships = []
        X_own = list_own[0]
        Y_own = list_own[1]
        course_own=list_own[2]
        w = math.radians(course_own)
        L = 3*list_own[4]  # 长半轴
        B = 1*list_own[4]  #短半轴

        if 0 <= course_own < 90:
            C = course_own * math.pi / 180
            X_inv = X_own + sin(C) * 0.25 * L
            Y_inv = Y_own + cos(C) * 0.25 * L


        elif 90 <= course_own < 180:
            C = (180 - course_own) * math.pi / 180
            X_inv = X_own + sin(C) * 0.25 * L
            Y_inv = Y_own - cos(C) * 0.25 * L


        elif 180 <= course_own < 270:
            C = (course_own - 180) * math.pi / 180
            X_inv = X_own - sin(C) * 0.25 * L
            Y_inv = Y_own - cos(C) * 0.25 * L


        else:
            C = (360 - course_own) * math.pi / 180
            X_inv = X_own - sin(C) * 0.25 * L
            Y_inv = Y_own + cos(C) * 0.25 * L

        for item in list_ships:
            mmsi_ship = item[3]
            X_ship = item[0]
            Y_ship = item[1]
            #print(X_ship,Y_ship,X_inv,Y_inv)
            result01 = ((Y_ship - Y_inv) * math.cos(w) + (X_ship - X_inv) * math.sin(w)) ** 2 / L ** 2 + (
                    (X_ship - X_inv) * math.cos(w) - (Y_ship - Y_inv) * math.sin(w)) ** 2 / B ** 2 - 1

            if result01 <= 0:
                list_danger_ships.append(item)
        return list_danger_ships

    def start(self,time):

        #####2、筛选出顺航道和非顺航道行驶船舶 ##########
        list_ships_follow = []  # 顺航道行驶船舶 [[船舶1，上/下行航道i],[船舶2，上/下行航道i],[船舶2，上/下行航道i]...]
        list_ships_not_follow=[] #非顺航道行驶船舶 [船舶1，船舶2，船舶3...]

        for item in self.list_ships:
            list_mark_ship = self.judge_targetShips_follow(item)
            if list_mark_ship[0][0]==0:
                list_ships_not_follow.append(item)
            else:
                list_ships_follow.append(list_mark_ship)
        # print("顺", list_ships_follow)
        # print("非顺", list_ships_not_follow)

        #####3、判断本船所处航道##########
        list_own_ship_channel = self.judge_targetShips_follow(self.list_own)


        #####4、获取最危险船舶##########
        for time_moment in range(0, time, 5):
            # 本船在时间t的状态
            list_own_new = self.predict_track_ownShip( list_own_ship_channel,time_moment)  # 本船经过时间t后的坐标

            #顺航道行驶船舶在时间t的状态
            list_targetShip_new=[]
            if len(list_ships_follow) > 0:
                for item in list_ships_follow:
                    list_follow_ship_new =self.predict_track_follow_channel(item,time_moment)
                    list_targetShip_new.append( list_follow_ship_new )

            #其他船舶在时间t的状态
            if len(list_ships_not_follow)>0:
                for item in list_ships_not_follow:
                    list_not_follow_ship_new=self.predict_track_not_follow_channel(item,time_moment)
                    list_targetShip_new.append(list_not_follow_ship_new)

            #####判断该时刻是否有危险船舶##########
            list_danger_ships=self.get_danger_ships(list_own_new ,list_targetShip_new)  #[]/[船舶1，船舶2...]
            #print(time_moment,list_danger_ships)
            if len(list_danger_ships)==0:
                continue
            else:
                for item_targetShip in self.list_ships:
                    if item_targetShip[3]==list_danger_ships[0][3]:
                        list_most_danger_ships = item_targetShip
                return [list_most_danger_ships,[time_moment]]
        return [[0]]

#判断是否仍然有碰撞危险
class Judge_Danger():
    """
    return：【【0】】/[[159825.22148001133, 60701.85576000032, 90, 413782245, 4.372778], [45]]
    """

    def __init__(self, list_ownship, list_targetships,list_channel_oneArea):
        self.list_own = list_ownship  #[x，y，航向,速度,船长，船宽]
        self.list_ships = list_targetships #[[x，y，航向,mmsi，速度],[x，y，航向,mmsi，速度]...]
        self.list_channel_oneArea=list_channel_oneArea ##【上行航道01，上行航道02...】--上行/下行航道：【航段1，航段2，航段3。。。】
        # ---【【lon,lat】,【lon,lat】，【lon,lat】，【lon,lat】,【course，value,id1,id2】】（右上，左上，右下，左下）

    ##########赛选2*0.8nm内且速度大于1kn的船舶(已验证)#########
    def get_ships_near(self):
        list_ships_near = []

        X_own = self.list_own[0]  # 本船x
        Y_own = self.list_own[1]  # 本船y
        w = math.radians(self.list_own[2])  # 本船真航向
        L01 = 3704  # 长半轴，2nm
        B01 = 1481  # 短半轴，0.8nm

        for item in self.list_ships:
            if item[4] > 0.1:
                X_ship = item[0]  # 其他船舶x
                Y_ship = item[1]  # 其他船舶y

                result01 = ((Y_ship - Y_own) * math.cos(w) + (X_ship - X_own) * math.sin(w)) ** 2 / L01 ** 2 + (
                        (X_ship - X_own) * math.cos(w) - (Y_ship - Y_own) * math.sin(w)) ** 2 / B01 ** 2 - 1

                if result01 <= 0:
                    list_ships_near.append(item)
        return list_ships_near

    ##########判别本船航道（已验证）#########
    def judge_ownShip_channel(self, list_targetship):
        """
        return
        """
        for item_channel in self.list_channel_oneArea:
            for item_oneChannel in item_channel:
                x1 = item_oneChannel[0][0]  # 右上
                y1 = item_oneChannel[0][1]

                x2 = item_oneChannel[1][0]  # 左上
                y2 = item_oneChannel[1][1]

                x3 = item_oneChannel[2][0]  # 右下
                y3 = item_oneChannel[2][1]

                x4 = item_oneChannel[3][0]  # 左下
                y4 = item_oneChannel[3][1]

                C_channel = item_oneChannel[4][0]
                value_channel = item_oneChannel[4][1]
                id_channel = item_oneChannel[4][2]
                # x,y分别表示船舶的坐标
                x = list_targetship[0]
                y = list_targetship[1]
                C_ship = list_targetship[2]  # 船舶航向

                s1 = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
                s2 = math.sqrt((x - x2) ** 2 + (y - y2) ** 2)
                s3 = math.sqrt((x - x3) ** 2 + (y - y3) ** 2)
                s4 = math.sqrt((x - x4) ** 2 + (y - y4) ** 2)

                l1 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
                l2 = math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
                l3 = math.sqrt((x4 - x2) ** 2 + (y4 - y2) ** 2)
                l4 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

                c1 = math.degrees(math.acos((s1 ** 2 + s3 ** 2 - l1 ** 2) / (2 * s1 * s3)))
                c2 = math.degrees(math.acos((s3 ** 2 + s4 ** 2 - l2 ** 2) / (2 * s3 * s4)))
                c3 = math.degrees(math.acos((s2 ** 2 + s4 ** 2 - l3 ** 2) / (2 * s2 * s4)))
                c4 = math.degrees(math.acos((s1 ** 2 + s2 ** 2 - l4 ** 2) / (2 * s1 * s2)))
                c_total = c1 + c2 + c3 + c4

                if 361 >= c_total >= 359:  # 目标船舶在航道内
                    if list_targetship[-1] != id_channel:
                        list_targetship.append(id_channel)

                    return [list_targetship, item_channel]

        return [[0]]
        ######### 预测顺航道行驶船舶时间t后的位置

    ##########判别目标船舶是否顺航道行驶（已验证）#########
    def judge_targetShips_follow(self,list_targetship):
        """
        return
        """
        for item_channel in self.list_channel_oneArea:
            for item_oneChannel in item_channel:
                x1 = item_oneChannel[0][0]  # 右上
                y1 = item_oneChannel[0][1]

                x2 = item_oneChannel[1][0]  # 左上
                y2 = item_oneChannel[1][1]

                x3 = item_oneChannel[2][0]  # 右下
                y3 = item_oneChannel[2][1]

                x4 = item_oneChannel[3][0]  # 左下
                y4 = item_oneChannel[3][1]

                C_channel = item_oneChannel[4][0]
                value_channel = item_oneChannel[4][1]
                id_channel=item_oneChannel[4][2]
                # x,y分别表示船舶的坐标
                x = list_targetship[0]
                y = list_targetship[1]
                C_ship = list_targetship[2] #船舶航向

                s1 = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
                s2 = math.sqrt((x - x2) ** 2 + (y - y2) ** 2)
                s3 = math.sqrt((x - x3) ** 2 + (y - y3) ** 2)
                s4 = math.sqrt((x - x4) ** 2 + (y - y4) ** 2)

                l1 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
                l2 = math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
                l3 = math.sqrt((x4 - x2) ** 2 + (y4 - y2) ** 2)
                l4 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

                c1 = math.degrees(math.acos((s1 ** 2 + s3 ** 2 - l1 ** 2) / (2 * s1 * s3)))
                c2 = math.degrees(math.acos((s3 ** 2 + s4 ** 2 - l2 ** 2) / (2 * s3 * s4)))
                c3 = math.degrees(math.acos((s2 ** 2 + s4 ** 2 - l3 ** 2) / (2 * s2 * s4)))
                c4 = math.degrees(math.acos((s1 ** 2 + s2 ** 2 - l4 ** 2) / (2 * s1 * s2)))
                c_total = c1 + c2 + c3 + c4

                if 361 >= c_total >= 359: #目标船舶在航道内
                    if abs(C_channel - C_ship) <= value_channel or abs(C_channel + 180 - C_ship) <= value_channel:
                        if list_targetship[-1]!=id_channel:
                            list_targetship.append(id_channel)

                        return [list_targetship,item_channel]

        return [[0]]
        ######### 预测顺航道行驶船舶时间t后的位置

    ##########预测本船航道行驶轨迹#########
    def predict_track_ownShip(self, list_own_ship_channel, t):
        """

        :param list_own_ship_channel: [本船,航道]
                本船：[159481.40998267243, 60818.97624000031, 110.03, 4.6763, 45, 12, 15]
                航道：上行/下行一条航道
        :param t: 0-1800
        :return:
        """

        list_ship = list_own_ship_channel[0]
        list_channel = list_own_ship_channel[1]

        if t == 0:
            return list_ship

        x_ship = list_ship[0]
        y_ship = list_ship[1]
        speed_ship = list_ship[3]

        time_start = 0
        mark_channel = list_channel[0][4][3]  # 上行、下行航道
        id_channel = list_ship[-1]  # 所在航段id
        course_out = 0
        ##船舶下行
        if mark_channel < 0:

            ####（1)计算船舶通过航道的时间和点序列#########
            for item_channel in list_channel:
                if id_channel == item_channel[4][2]:
                    x1 = item_channel[1][0]  # 左上
                    x2 = item_channel[0][0]  # 右上
                    x3 = item_channel[3][0]  # 左下
                    x4 = item_channel[2][0]  # 右下

                    y1 = item_channel[1][1]  # 左上
                    y2 = item_channel[0][1]  # 右上
                    y3 = item_channel[3][1]  # 左下
                    y4 = item_channel[2][1]  # 右下

                    # 求本船驶出航段的末尾直线方程
                    x_out_up = x2
                    y_out_up = y2
                    x_out_down = x4
                    y_out_down = y4
                    k_channel = (y_out_up - y_out_down) / (x_out_up - x_out_down)
                    b_channel = y_out_up - k_channel * x_out_up

                    # 求本船在该航段的直线方程
                    if time_start==0:
                        course_ship=list_ship[2]
                    else:
                        course_ship = item_channel[4][0] + 180

                    if 180 <= course_ship < 270:
                        k_ship = math.tan(math.radians(270 - course_ship))
                    else:
                        k_ship = -math.tan(math.radians(course_ship - 270))
                    b_ship = y_ship - k_ship * x_ship

                    # 求本船驶出航段点
                    x_cross = (b_channel - b_ship) / (k_ship - k_channel)
                    y_cross = k_channel * x_cross + b_channel
                    #print(x_cross,y_cross)
                    # 求本船驶出航段的时间
                    time_cross = math.sqrt(
                        (x_cross - x_ship) ** 2 + (y_cross - y_ship) ** 2) / speed_ship + time_start
                    #print(time_cross)
                    # 判断预测时间是否在该段内
                    if time_start < t < time_cross:
                        if time_start == 0:
                            course_ship = list_ship[2]
                        else:
                            course_ship = item_channel[4][0]
                        time = t - time_start

                        if 0 <= course_ship < 90:
                            speed_own_x = math.sin(course_ship * math.pi / 180) * speed_ship
                            speed_own_y = math.cos(course_ship * math.pi / 180) * speed_ship
                            x_ship += time * speed_own_x
                            y_ship += time * speed_own_y
                        elif 90 <= course_ship < 180:
                            speed_own_x = math.cos((course_ship - 90) * math.pi / 180) * speed_ship
                            speed_own_y = math.sin((course_ship - 90) * math.pi / 180) * speed_ship
                            x_ship += time * speed_own_x
                            y_ship -= time * speed_own_y
                        elif 180 <= course_ship < 270:
                            speed_own_x = math.sin((course_ship - 180) * math.pi / 180) * speed_ship
                            speed_own_y = math.cos((course_ship - 180) * math.pi / 180) * speed_ship
                            x_ship -= time * speed_own_x
                            y_ship -= time * speed_own_y
                        else:
                            speed_own_x = math.cos((course_ship - 270) * math.pi / 180) * speed_ship
                            speed_own_y = math.sin((course_ship - 270) * math.pi / 180) * speed_ship
                            x_ship -= time * speed_own_x
                            y_ship += time * speed_own_y


                        return [x_ship, y_ship,course_ship, list_ship[3], list_ship[4], list_ship[5]]
                    else:
                        id_channel += 1
                        x_ship = x_cross
                        y_ship = y_cross
                        time_start = time_cross
                        course_out = course_ship

            time = t - time_start
            if 0 <= course_out < 90:
                speed_x = math.sin(course_out * math.pi / 180) * speed_ship
                speed_y = math.cos(course_out * math.pi / 180) * speed_ship
                x_ship += time * speed_x
                y_ship += time * speed_y
            elif 90 <= course_out < 180:
                speed_x = math.cos((course_out - 90) * math.pi / 180) * speed_ship
                speed_y = math.sin((course_out - 90) * math.pi / 180) * speed_ship
                x_ship += time * speed_x
                y_ship -= time * speed_y
            elif 180 <= course_out < 270:
                speed_x = math.sin((course_out - 180) * math.pi / 180) * speed_ship
                speed_y = math.cos((course_out - 180) * math.pi / 180) * speed_ship
                x_ship -= time * speed_x
                y_ship -= time * speed_y
            else:
                speed_x = math.cos((course_out - 270) * math.pi / 180) * speed_ship
                speed_y = math.sin((course_out - 270) * math.pi / 180) * speed_ship
                x_ship -= time * speed_x
                y_ship += time * speed_y
            return [x_ship, y_ship,course_out, list_ship[3], list_ship[4], list_ship[5]]

        ##船舶上行
        else:
            ####（1)计算船舶通过航道的时间和点序列#########
            for item_channel in list_channel:
                if id_channel == item_channel[4][2]:
                    x1 = item_channel[0][0]  # 右上
                    x2 = item_channel[1][0]  # 左上
                    x3 = item_channel[2][0]  # 右下
                    x4 = item_channel[3][0]  # 左下

                    y1 = item_channel[0][1]  # 右上
                    y2 = item_channel[1][1]  # 左上
                    y3 = item_channel[2][1]  # 右下
                    y4 = item_channel[3][1]  # 左下

                    # 求本船驶出航段的末尾直线方程
                    x_out_up = x2
                    y_out_up = y2
                    x_out_down = x4
                    y_out_down = y4
                    k_channel = (y_out_up - y_out_down) / (x_out_up - x_out_down)
                    b_channel = y_out_up - k_channel * x_out_up

                    # 求本船在该航段的直线方程
                    if time_start == 0:
                        course_ship = list_ship[2]
                    else:
                        course_ship = item_channel[4][0] + 180

                    if 180 <= course_ship < 270:
                        k_ship = math.tan(math.radians(270 - course_ship))
                    else:
                        k_ship = -math.tan(math.radians(course_ship - 270))
                    b_ship = y_ship - k_ship * x_ship

                    # 求本船驶出航段点
                    x_cross = (b_channel - b_ship) / (k_ship - k_channel)
                    y_cross = k_channel * x_cross + b_channel

                    # 求本船驶出航段的时间
                    time_cross = math.sqrt(
                        (x_cross - x_ship) ** 2 + (y_cross - y_ship) ** 2) / speed_ship + time_start

                    # 判断预测时间是否在该段内
                    if time_start < t < time_cross:
                        time = t - time_start
                        if 0 <= course_ship < 90:
                            speed_own_x = math.sin(course_ship * math.pi / 180) * speed_ship
                            speed_own_y = math.cos(course_ship * math.pi / 180) * speed_ship
                            x_ship += time * speed_own_x
                            y_ship += time * speed_own_y
                        elif 90 <= course_ship < 180:
                            speed_own_x = math.cos((course_ship - 90) * math.pi / 180) * speed_ship
                            speed_own_y = math.sin((course_ship - 90) * math.pi / 180) * speed_ship
                            x_ship += time * speed_own_x
                            y_ship -= time * speed_own_y
                        elif 180 <= course_ship < 270:
                            speed_own_x = math.sin((course_ship - 180) * math.pi / 180) * speed_ship
                            speed_own_y = math.cos((course_ship - 180) * math.pi / 180) * speed_ship
                            x_ship -= time * speed_own_x
                            y_ship -= time * speed_own_y
                        else:
                            speed_own_x = math.cos((course_ship - 270) * math.pi / 180) * speed_ship
                            speed_own_y = math.sin((course_ship - 270) * math.pi / 180) * speed_ship
                            x_ship -= time * speed_own_x
                            y_ship += time * speed_own_y

                        return [x_ship, y_ship, course_ship, list_ship[3], list_ship[4], list_ship[5]]
                    else:
                        id_channel += 1
                        x_ship = x_cross
                        y_ship = y_cross
                        time_start = time_cross
                        course_out = course_ship

                time = t - time_start
                if 0 <= course_out < 90:
                    speed_x = math.sin(course_out * math.pi / 180) * speed_ship
                    speed_y = math.cos(course_out * math.pi / 180) * speed_ship
                    x_ship += time * speed_x
                    y_ship += time * speed_y
                elif 90 <= course_out < 180:
                    speed_x = math.cos((course_out - 90) * math.pi / 180) * speed_ship
                    speed_y = math.sin((course_out - 90) * math.pi / 180) * speed_ship
                    x_ship += time * speed_x
                    y_ship -= time * speed_y
                elif 180 <= course_out < 270:
                    speed_x = math.sin((course_out - 180) * math.pi / 180) * speed_ship
                    speed_y = math.cos((course_out - 180) * math.pi / 180) * speed_ship
                    x_ship -= time * speed_x
                    y_ship -= time * speed_y
                else:
                    speed_x = math.cos((course_out - 270) * math.pi / 180) * speed_ship
                    speed_y = math.sin((course_out - 270) * math.pi / 180) * speed_ship
                    x_ship -= time * speed_x
                    y_ship += time * speed_y

                return [x_ship, y_ship,course_out, list_ship[3], list_ship[4], list_ship[5]]

    ##########预测目标船舶顺航道行驶船舶轨迹#########
    def predict_track_follow_channel(self, list_own_ship_channel, t):
        list_ship=list_own_ship_channel[0]
        list_channel=list_own_ship_channel[1]

        if t==0:
            return list_ship

        x_ship = list_ship[0]
        y_ship = list_ship[1]
        speed_ship = list_ship[4]

        time_start = 0
        mark_channel=list_channel[0][4][3]  #上行、下行航道
        id_channel= list_ship[-1]  #所在航段id
        course_out=0
        ##船舶下行
        if  mark_channel <0:
            ####（1)计算船舶通过航道的时间和点序列#########
            for item_channel in list_channel:
                if id_channel == item_channel[4][2]:

                    x1 = item_channel[1][0] # 左上
                    x2 = item_channel[0][0] # 右上
                    x3 = item_channel[3][0] # 左下
                    x4 = item_channel[2][0] # 右下

                    y1 = item_channel[1][1]  # 左上
                    y2 = item_channel[0][1]  # 右上
                    y3 = item_channel[3][1]  # 左下
                    y4 = item_channel[2][1]  # 右下


                    # 求本船驶出航段的末尾直线方程
                    x_out_up = x2
                    y_out_up = y2
                    x_out_down = x4
                    y_out_down = y4
                    k_channel = (y_out_up - y_out_down) / (x_out_up - x_out_down)
                    b_channel = y_out_up - k_channel * x_out_up

                    # 求本船在该航段的直线方程
                    course_ship = item_channel[4][0] + 180
                    if 180 <= course_ship < 270:
                        k_ship = math.tan(math.radians(270 - course_ship))
                    else:
                        k_ship = -math.tan(math.radians(course_ship - 270))
                    b_ship = y_ship - k_ship * x_ship

                    # 求本船驶出航段点
                    x_cross = (b_channel - b_ship) / (k_ship - k_channel)
                    y_cross = k_channel * x_cross + b_channel

                    # 求本船驶出航段的时间
                    time_cross = math.sqrt((x_cross - x_ship) ** 2 + (y_cross - y_ship) ** 2) / speed_ship + time_start

                    #判断预测时间是否在该段内
                    if time_start<t<time_cross:
                        course_ship= item_channel[4][0]
                        time = t - time_start
                        if 0 <= course_ship < 90:
                            speed_own_x = math.sin(course_ship * math.pi / 180) * speed_ship
                            speed_own_y = math.cos(course_ship * math.pi / 180) * speed_ship
                            x_ship += time * speed_own_x
                            y_ship += time * speed_own_y
                        elif 90 <= course_ship < 180:
                            speed_own_x = math.cos((course_ship - 90) * math.pi / 180) * speed_ship
                            speed_own_y = math.sin((course_ship - 90) * math.pi / 180) * speed_ship
                            x_ship += time * speed_own_x
                            y_ship -= time * speed_own_y
                        elif 180 <= course_ship < 270:
                            speed_own_x = math.sin((course_ship - 180) * math.pi / 180) * speed_ship
                            speed_own_y = math.cos((course_ship - 180) * math.pi / 180) * speed_ship
                            x_ship -= time * speed_own_x
                            y_ship -= time * speed_own_y
                        else:
                            speed_own_x = math.cos((course_ship - 270) * math.pi / 180) * speed_ship
                            speed_own_y = math.sin((course_ship - 270) * math.pi / 180) * speed_ship
                            x_ship -= time * speed_own_x
                            y_ship += time * speed_own_y


                        return [x_ship, y_ship, course_ship, list_ship[3], list_ship[4]]

                    else:
                        id_channel += 1
                        x_ship = x_cross
                        y_ship = y_cross
                        time_start = time_cross
                        course_out=course_ship

            time = t - time_start
            if 0 <= course_out < 90:
                speed_x = math.sin(course_out * math.pi / 180) * speed_ship
                speed_y = math.cos(course_out * math.pi / 180) * speed_ship
                x_ship += time * speed_x
                y_ship += time * speed_y
            elif 90 <= course_out < 180:
                speed_x = math.cos((course_out - 90) * math.pi / 180) * speed_ship
                speed_y = math.sin((course_out - 90) * math.pi / 180) * speed_ship
                x_ship += time * speed_x
                y_ship -= time * speed_y
            elif 180 <=course_out < 270:
                speed_x = math.sin((course_out - 180) * math.pi / 180) * speed_ship
                speed_y = math.cos((course_out - 180) * math.pi / 180) * speed_ship
                x_ship -= time * speed_x
                y_ship -= time * speed_y
            else:
                speed_x = math.cos((course_out - 270) * math.pi / 180) * speed_ship
                speed_y = math.sin((course_out - 270) * math.pi / 180) * speed_ship
                x_ship -= time * speed_x
                y_ship += time * speed_y

            return [x_ship, y_ship,course_out, list_ship[3], list_ship[4]]



        ##船舶上行
        else:
            ####（1)计算船舶通过航道的时间和点序列#########
            for item_channel in list_channel:
                if id_channel == item_channel[4][2]:
                    x1 = item_channel[0][0]  # 右上
                    x2 = item_channel[1][0]  # 左上
                    x3 = item_channel[2][0]  # 右下
                    x4 = item_channel[3][0]  # 左下

                    y1 = item_channel[0][1]  # 右上
                    y2 = item_channel[1][1]  # 左上
                    y3 = item_channel[2][1]  # 右下
                    y4 = item_channel[3][1]  # 左下


                    # 求本船驶出航段的末尾直线方程
                    x_out_up = x2
                    y_out_up = y2
                    x_out_down = x4
                    y_out_down = y4
                    k_channel = (y_out_up - y_out_down) / (x_out_up - x_out_down)
                    b_channel = y_out_up - k_channel * x_out_up

                    # 求本船在该航段的直线方程
                    course_ship = item_channel[4][0] + 180
                    if 180 <= course_ship < 270:
                        k_ship = math.tan(math.radians(270 - course_ship))
                    else:
                        k_ship = -math.tan(math.radians(course_ship - 270))
                    b_ship = y_ship - k_ship * x_ship

                    # 求本船驶出航段点
                    x_cross = (b_channel - b_ship) / (k_ship - k_channel)
                    y_cross = k_channel * x_cross + b_channel

                    # 求本船驶出航段的时间
                    time_cross = math.sqrt(
                        (x_cross - x_ship) ** 2 + (y_cross - y_ship) ** 2) / speed_ship + time_start

                    # 判断预测时间是否在该段内
                    if time_start < t < time_cross:
                        time = t - time_start
                        if 0 <= course_ship < 90:
                            speed_own_x = math.sin(course_ship * math.pi / 180) * speed_ship
                            speed_own_y = math.cos(course_ship * math.pi / 180) * speed_ship
                            x_ship += time * speed_own_x
                            y_ship += time * speed_own_y
                        elif 90 <= course_ship < 180:
                            speed_own_x = math.cos((course_ship - 90) * math.pi / 180) * speed_ship
                            speed_own_y = math.sin((course_ship - 90) * math.pi / 180) * speed_ship
                            x_ship += time * speed_own_x
                            y_ship -= time * speed_own_y
                        elif 180 <= course_ship < 270:
                            speed_own_x = math.sin((course_ship - 180) * math.pi / 180) * speed_ship
                            speed_own_y = math.cos((course_ship - 180) * math.pi / 180) * speed_ship
                            x_ship -= time * speed_own_x
                            y_ship -= time * speed_own_y
                        else:
                            speed_own_x = math.cos((course_ship - 270) * math.pi / 180) * speed_ship
                            speed_own_y = math.sin((course_ship - 270) * math.pi / 180) * speed_ship
                            x_ship -= time * speed_own_x
                            y_ship += time * speed_own_y


                        return [x_ship, y_ship, course_ship, list_ship[3], list_ship[4]]

                    else:
                        id_channel += 1
                        x_ship = x_cross
                        y_ship = y_cross
                        time_start = time_cross
                        course_out = course_ship

                time = t - time_start
                if 0 <= course_out < 90:
                    speed_x = math.sin(course_out * math.pi / 180) * speed_ship
                    speed_y = math.cos(course_out * math.pi / 180) * speed_ship
                    x_ship += time * speed_x
                    y_ship += time * speed_y
                elif 90 <= course_out < 180:
                    speed_x = math.cos((course_out - 90) * math.pi / 180) * speed_ship
                    speed_y = math.sin((course_out - 90) * math.pi / 180) * speed_ship
                    x_ship += time * speed_x
                    y_ship -= time * speed_y
                elif 180 <= course_out < 270:
                    speed_x = math.sin((course_out - 180) * math.pi / 180) * speed_ship
                    speed_y = math.cos((course_out - 180) * math.pi / 180) * speed_ship
                    x_ship -= time * speed_x
                    y_ship -= time * speed_y
                else:
                    speed_x = math.cos((course_out - 270) * math.pi / 180) * speed_ship
                    speed_y = math.sin((course_out - 270) * math.pi / 180) * speed_ship
                    x_ship -= time * speed_x
                    y_ship += time * speed_y


                return [x_ship, y_ship, course_out, list_ship[3], list_ship[4]]

    ##########预测非顺航道行驶船舶轨迹#########
    def predict_track_not_follow_channel(self,list_ship,time):
        """
        list_ship:[x，y，航向,mmsi，速度]
        """
        x = list_ship[0]  # 初始点x
        y = list_ship[1]  # 初始点y
        course_ship = list_ship[2]  # 船舶航向
        speed_ship = list_ship[4]  # 船舶速度
        mmsi=list_ship[3] #船舶编号
        if 0 <= course_ship < 90:
            speed_x = math.sin(course_ship * math.pi / 180) * speed_ship
            speed_y = math.cos(course_ship * math.pi / 180) * speed_ship
            x += time * speed_x
            y += time * speed_y
        elif 90 <= course_ship < 180:
            speed_x = math.cos((course_ship - 90) * math.pi / 180) * speed_ship
            speed_y = math.sin((course_ship - 90) * math.pi / 180) * speed_ship
            x += time * speed_x
            y -= time * speed_y
        elif 180 <= course_ship < 270:
            speed_x = math.sin((course_ship - 180) * math.pi / 180) * speed_ship
            speed_y = math.cos((course_ship - 180) * math.pi / 180) * speed_ship
            x -= time * speed_x
            y -= time * speed_y
        else:
            speed_x = math.cos((course_ship - 270) * math.pi / 180) * speed_ship
            speed_y = math.sin((course_ship - 270) * math.pi / 180) * speed_ship
            x -= time * speed_x
            y += time * speed_y

        ##替换为t时刻的坐标

        return [x,y,list_ship[2],list_ship[3],list_ship[4]]

    ########获取危险船舶##########
    def get_danger_ships(self, list_own, list_ships):

        list_danger_ships = []
        X_own = list_own[0]
        Y_own = list_own[1]
        course_own=list_own[2]
        w = math.radians(course_own)
        L = 3*list_own[4]  # 长半轴
        B = 1*list_own[4]  #短半轴

        if 0 <= course_own < 90:
            C = course_own * math.pi / 180
            X_inv = X_own + sin(C) * 0.25 * L
            Y_inv = Y_own + cos(C) * 0.25 * L


        elif 90 <= course_own < 180:
            C = (180 - course_own) * math.pi / 180
            X_inv = X_own + sin(C) * 0.25 * L
            Y_inv = Y_own - cos(C) * 0.25 * L


        elif 180 <= course_own < 270:
            C = (course_own - 180) * math.pi / 180
            X_inv = X_own - sin(C) * 0.25 * L
            Y_inv = Y_own - cos(C) * 0.25 * L


        else:
            C = (360 - course_own) * math.pi / 180
            X_inv = X_own - sin(C) * 0.25 * L
            Y_inv = Y_own + cos(C) * 0.25 * L

        for item in list_ships:
            mmsi_ship = item[3]
            X_ship = item[0]
            Y_ship = item[1]

            result01 = ((Y_ship - Y_inv) * math.cos(w) + (X_ship - X_inv) * math.sin(w)) ** 2 / L ** 2 + (
                    (X_ship - X_inv) * math.cos(w) - (Y_ship - Y_inv) * math.sin(w)) ** 2 / B ** 2 - 1

            if result01 <= 0:

                list_danger_ships.append(item)

        return list_danger_ships

    def start(self,time):
        #####1、筛选附近2*0.8nm内的目标船舶 ##########
        list_ships_near = self.get_ships_near()  # #[[x，y，航向,mmsi，速度],[x，y，航向,mmsi，速度]...]

        #####2、筛选出顺航道和非顺航道行驶船舶 ##########
        list_ships_follow = []  # 顺航道行驶船舶 [[船舶1，上/下行航道i],[船舶2，上/下行航道i],[船舶2，上/下行航道i]...]
        list_ships_not_follow=[] #非顺航道行驶船舶 [船舶1，船舶2，船舶3...]

        for item in list_ships_near:
            list_mark_ship = self.judge_targetShips_follow(item)
            if list_mark_ship[0][0]==0:
                list_ships_not_follow.append(item)
            else:
                list_ships_follow.append(list_mark_ship)
        # print("顺", list_ships_follow)
        # print("非顺", list_ships_not_follow)

        #####3、判断本船所处航道##########
        #print("@@",self.list_own)
        list_own_ship_channel = self.judge_ownShip_channel(self.list_own)
        #print("###",list_own_ship_channel)

        #####4、获取最危险船舶##########
        for time_moment in range(0, time, 5):
            # 本船在时间t的状态
            list_own_new = self.predict_track_ownShip( list_own_ship_channel,time_moment)  # 本船经过时间t后的坐标

            #顺航道行驶船舶在时间t的状态
            list_targetShip_new=[]
            if len(list_ships_follow) > 0:
                for item in list_ships_follow:
                    list_follow_ship_new =self.predict_track_follow_channel(item,time_moment)
                    list_targetShip_new.append( list_follow_ship_new )

            #其他船舶在时间t的状态
            if len(list_ships_not_follow)>0:
                for item in list_ships_not_follow:
                    list_not_follow_ship_new=self.predict_track_not_follow_channel(item,time_moment)
                    list_targetShip_new.append(list_not_follow_ship_new)
            # print("#################",time_moment)
            # print(list_own_new)
            # print(list_targetShip_new)
            # if self.list_own[2]==110.46 and self.list_own[3]==4.691733 and time_moment==100:
            #     print("##########",110.46,time_moment)
            #     print("本船：",list_own_new)
            #     print("目标船：", list_targetShip_new)
            # elif self.list_own[2]==114.46 and self.list_own[3]==4.691733 and time_moment==100:
            #     print("##########",114.46)
            #     print("本船：",list_own_new)
            #     print("目标船：", list_targetShip_new)
            # else:
            #     pass
            #####判断该时刻是否有危险船舶##########
            # print(time_moment,"######################################")
            # print(list_own_new)
            # print(list_targetShip_new)


            list_danger_ships=self.get_danger_ships(list_own_new ,list_targetShip_new)  #[]/[船舶1，船舶2...]

            if len(list_danger_ships)==0:
                continue
            else:
                # print("##############")
                # print(time_moment)
                # print(list_own_new)
                # print(list_targetShip_new)
                for item_targetShip in self.list_ships:
                    if item_targetShip[3]==list_danger_ships[0][3]:
                        list_most_danger_ships = item_targetShip
                return [list_most_danger_ships,[time_moment]]
        return [[0]]

#获取辅助决策
class Get_Support_Decision():
    """
    return [list_ships_follow,list_ships_not_follow] :
    list_ships_follow--[[x，y，航向,mmsi，速度,id_type,id_channel],[x，y，航向,mmsi，速度,id_type,id_channel]...]
    list_ships_not_follow--[[x，y，航向,mmsi，速度],[x，y，航向,mmsi，速度]...]
    """
    def __init__(self, list_ownship, list_targetship,list_channel_oneArea, list_targetships,time):
        self.list_own = list_ownship  #[x，y，航向,速度,船长，船宽]
        self.list_ship = list_targetship #[x，y，航向,mmsi，速度,time]
        self.list_channel_oneArea=list_channel_oneArea ##【上行航道01，上行航道02...】--上行/下行航道：【航段1，航段2，航段3。。。】
        # ---【【lon,lat】,【lon,lat】，【lon,lat】，【lon,lat】,【course，value,id1,id2】】（右上，左上，右下，左下）
        self.ships=list_targetships#[[x，y，航向,mmsi，速度,time],[x，y，航向,mmsi，速度,time]]
        self.time=time[0]
        self.speed_max=5.14 #最大速度m/s
        self.speed_min=0.1   #最小速度m/s
    ##########判断本船在上行/下行航道#########
    def judge_ownShip_channel(self):
        """
        return
        """
        for item_channel in self.list_channel_oneArea:
            for item_oneChannel in item_channel:
                x1 = item_oneChannel[0][0]  # 右上
                y1 = item_oneChannel[0][1]

                x2 = item_oneChannel[1][0]  # 左上
                y2 = item_oneChannel[1][1]

                x3 = item_oneChannel[2][0]  # 右下
                y3 = item_oneChannel[2][1]

                x4 = item_oneChannel[3][0]  # 左下
                y4 = item_oneChannel[3][1]


                mark_channel = item_oneChannel[4][3]  # 上行/下行标记
                # x,y分别表示船舶的坐标
                x = self.list_own [0]
                y = self.list_own [1]
                C_ship = self.list_own [2] #船舶航向

                s1 = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
                s2 = math.sqrt((x - x2) ** 2 + (y - y2) ** 2)
                s3 = math.sqrt((x - x3) ** 2 + (y - y3) ** 2)
                s4 = math.sqrt((x - x4) ** 2 + (y - y4) ** 2)

                l1 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
                l2 = math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
                l3 = math.sqrt((x4 - x2) ** 2 + (y4 - y2) ** 2)
                l4 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

                c1 = math.degrees(math.acos((s1 ** 2 + s3 ** 2 - l1 ** 2) / (2 * s1 * s3)))
                c2 = math.degrees(math.acos((s3 ** 2 + s4 ** 2 - l2 ** 2) / (2 * s3 * s4)))
                c3 = math.degrees(math.acos((s2 ** 2 + s4 ** 2 - l3 ** 2) / (2 * s2 * s4)))
                c4 = math.degrees(math.acos((s1 ** 2 + s2 ** 2 - l4 ** 2) / (2 * s1 * s2)))
                c_total = c1 + c2 + c3 + c4

                if 361 >= c_total >= 359: #目标船舶在航道内
                    return item_oneChannel


        ######### 预测顺航道行驶船舶时间t后的位置

    ##########局面辨识#########
    def identify_situation(self,mark_channel):
        """
        return
        """
        ##########航道内的船舶局面辨识###########
        for item_channel in self.list_channel_oneArea:
            for item_oneChannel in item_channel:
                x1 = item_oneChannel[0][0]  # 右上
                y1 = item_oneChannel[0][1]

                x2 = item_oneChannel[1][0]  # 左上
                y2 = item_oneChannel[1][1]

                x3 = item_oneChannel[2][0]  # 右下
                y3 = item_oneChannel[2][1]

                x4 = item_oneChannel[3][0]  # 左下
                y4 = item_oneChannel[3][1]

                C_channel = item_oneChannel[4][0]
                value_channel = item_oneChannel[4][1]
                id_channel = item_oneChannel[4][2]  #航段
                mark_channel=item_oneChannel[4][3]  #上行/下行标记

                # x,y分别表示本船的坐标
                x_own = self.list_own[0]
                y_own = self.list_own[1]
                C_own = self.list_own[2]

                # x,y分别表示目标船舶的坐标
                x =  self.list_ship[0]
                y =  self.list_ship[1]
                C_ship =  self.list_ship[2]  # 船舶航向

                s1 = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
                s2 = math.sqrt((x - x2) ** 2 + (y - y2) ** 2)
                s3 = math.sqrt((x - x3) ** 2 + (y - y3) ** 2)
                s4 = math.sqrt((x - x4) ** 2 + (y - y4) ** 2)

                l1 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
                l2 = math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
                l3 = math.sqrt((x4 - x2) ** 2 + (y4 - y2) ** 2)
                l4 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

                c1 = math.degrees(math.acos((s1 ** 2 + s3 ** 2 - l1 ** 2) / (2 * s1 * s3)))
                c2 = math.degrees(math.acos((s3 ** 2 + s4 ** 2 - l2 ** 2) / (2 * s3 * s4)))
                c3 = math.degrees(math.acos((s2 ** 2 + s4 ** 2 - l3 ** 2) / (2 * s2 * s4)))
                c4 = math.degrees(math.acos((s1 ** 2 + s2 ** 2 - l4 ** 2) / (2 * s1 * s2)))
                c_total = c1 + c2 + c3 + c4

                if 361 >= c_total >= 359:  # 目标船舶在航道内
                    if abs(C_channel - C_ship) <= value_channel or abs(C_channel + 180 - C_ship) <= value_channel: #顺航道行驶船舶
                        if  mark_channel<0:  #下行
                            x_mid_out=(x1+x3)/2
                            y_mid_out=(y1+y3)/2
                            s_own=sqrt((x_own-x_mid_out)**2+(y_own-y_mid_out)**2)
                            s_ship=sqrt((x-x_mid_out)**2+(y-y_mid_out)**2)
                            s_own_ship=sqrt((x-x_own)**2+(y-y_own)**2)
                        else:#上行
                            x_mid_out = (x2 + x4) / 2
                            y_mid_out = (y2 + y4) / 2
                            s_own = sqrt((x_own - x_mid_out) ** 2 + (y_own - y_mid_out) ** 2)
                            s_ship = sqrt((x - x_mid_out) ** 2 + (y - y_mid_out) ** 2)
                            s_own_ship = sqrt((x - x_own) ** 2 + (y - y_own) ** 2)
                        if s_own -s_own_ship >0 and s_own-s_ship>0:
                            status_ship = 1  # 目标船舶是被追越船
                        else:
                            status_ship = -1  # 目标船舶是追越船
                    elif abs(C_channel - C_ship) <=30 or abs(C_channel + 180 - C_ship) <= 30: #特殊船舶

                        X=x-x_own
                        Y=y-y_own
                        if X==0 and Y>0: #目标船在Y轴正半轴
                            C_relative=0
                        elif X==0 and Y<0: #目标船在Y轴负半轴
                            C_relative = 180
                        elif Y==0 and X>0:#目标船在X轴正半轴
                            C_relative = 90
                        elif Y==0 and X<0: #目标船在X轴负半轴
                            C_relative = 270
                        elif X>0 and Y>0: #第一象限
                            C_relative = math.degrees(math.atan(abs(X / Y)))
                        elif X>0 and Y<0: #第四象限
                            C_relative = 180-math.degrees(math.atan(abs(X / Y)))
                        elif X<0 and Y>0: #第二象限
                            C_relative = 180 + math.degrees(math.atan(abs(X / Y)))
                        else:               #第三象限
                            C_relative = 360 - math.degrees(math.atan(abs(X / Y)))

                        if C_relative-C_own>0: #判断相对方位
                            status_ship = 2  # 目标船舶是右侧特殊船
                            #print("航道内右侧特殊船")
                        else:
                            status_ship = -2  # 目标船舶是左侧特殊船


                    else:
                        status_ship=0  #目标船舶是横越船舶
                    return status_ship


        ##########航道外的船舶局面辨识###########
        for item_channel in self.list_channel_oneArea:
            if item_channel[0][4][3]==mark_channel:
                channel_messege=item_channel

        x_ship = self.list_ship[0]
        y_ship = self.list_ship[1]
        C_ship = self.list_ship[2]


        for item_oneChannel in channel_messege:  #每一航段
            x1 = item_oneChannel[0][0]  # 右上
            y1 = item_oneChannel[0][1]

            x2 = item_oneChannel[1][0]  # 左上
            y2 = item_oneChannel[1][1]

            x3 = item_oneChannel[2][0]  # 右下
            y3 = item_oneChannel[2][1]

            x4 = item_oneChannel[3][0]  # 左下
            y4 = item_oneChannel[3][1]

            C_channel = item_oneChannel[4][0]
            x_mid=(x1+x2)/2
            y_mid=(y1+y2)/2

            s=sqrt((x_mid-x_ship)**2+(y_mid-y_ship)**2)

            if 45<=C_channel<=135:
                if min(x2,x1)<=x_ship<=max(x1,x2)  and s<=3000:
                    if abs(C_channel - C_ship) <= 30 or abs(C_channel + 180 - C_ship) <= 30:  # 特殊船舶
                        ###上边界直线方程###
                        k_up = (y2 - y1) / (x2 - x1)
                        b_up = y1 - k_up * x1

                        ####下边界直线方程###
                        k_down = (y4 - y3) / (x4 - x3)
                        b_down = y3 - k_down * x3

                        ###目标船与上边界距离###
                        s_up = abs(y_ship - k_up * x_ship - b_up) / sqrt(1 + k_up ** 2)

                        ###目标船与下边界距离###
                        s_down = abs(y_ship - k_down * x_ship - b_down) / sqrt(1 + k_down ** 2)
                        if s_up>s_down:
                            status_ship=2
                        else:
                            status_ship=-2
                    else:
                        status_ship = 0  # 目标船舶是横越船舶
                    return status_ship
                else:
                    pass


            else:
                if min(y2,y1)<=y_ship<=max(y1,y2) and s <= 3000:
                    if abs(C_channel - C_ship) <= 30 or abs(C_channel + 180 - C_ship) <= 30:  # 特殊船舶
                        ###上边界直线方程###
                        k_up = (y2 - y1) / (x2 - x1)
                        b_up = y1 - k_up * x1

                        ####下边界直线方程###
                        k_down = (y4 - y3) / (x4 - x3)
                        b_down = y3 - k_down * x3

                        ###目标船与上边界距离###
                        s_up = abs(y_ship - k_up * x_ship - b_up) / sqrt(1 + k_up ** 2)

                        ###目标船与下边界距离###
                        s_down = abs(y_ship - k_down * x_ship - b_down) / sqrt(1 + k_down ** 2)
                        if s_up > s_down:
                            status_ship = 2
                        else:
                            status_ship = -2
                    else:
                        status_ship = 0  # 目标船舶是横越船舶
                    return status_ship
                else:
                    pass

    ##########获取最大改向区间#########
    def get_section_condition(self,channel_ownShip):
        x_own = self.list_own[0]
        y_own = self.list_own[1]
        #print(channel_ownShip)
        course_own = self.list_own[2]  # 本船航向


        if 0<=course_own<90:
            course_own=channel_ownShip[4][0]
            x_out_up = channel_ownShip[0][0]
            y_out_up = channel_ownShip[0][1]
            x_out_down = channel_ownShip[2][0]
            y_out_down = channel_ownShip[2][1]

            X_left=abs(x_out_up-x_own)
            Y_left=abs(y_out_up-y_own)
            X_right=abs(x_out_down-x_own)
            Y_right=abs(y_out_down-y_own)

            c_left=abs(math.degrees(math.atan(X_left/Y_left))-course_own)
            c_right=abs(math.degrees(math.atan(X_right/Y_right))-course_own)

        elif 90<=course_own<180:
            course_own = channel_ownShip[4][0]
            x_out_up = channel_ownShip[0][0]
            y_out_up = channel_ownShip[0][1]
            x_out_down = channel_ownShip[2][0]
            y_out_down = channel_ownShip[2][1]

            X_left = abs(x_out_up - x_own)
            Y_left = abs(y_out_up - y_own)
            X_right = abs(x_out_down - x_own)
            Y_right = abs(y_out_down - y_own)

            c_left = abs(180-math.degrees(math.atan(X_left / Y_left)) - course_own)
            c_right = abs(180-math.degrees(math.atan(X_right / Y_right)) - course_own)

        elif 180<=course_own<270:
            course_own = channel_ownShip[4][0]+180
            x_out_up = channel_ownShip[1][0]
            y_out_up = channel_ownShip[1][1]

            x_out_down = channel_ownShip[3][0]
            y_out_down = channel_ownShip[3][0]

            X_left = abs(x_out_down - x_own)
            Y_left = abs(y_out_down - y_own)
            X_right = abs(x_out_up - x_own)
            Y_right = abs(y_out_up - y_own)

            c_left = abs(180 + math.degrees(math.atan(X_left / Y_left)) - course_own)
            c_right = abs(180 + math.degrees(math.atan(X_right / Y_right)) - course_own)
        else:
            course_own = channel_ownShip[4][0]+180
            x_out_up = channel_ownShip[1][0]
            y_out_up = channel_ownShip[1][1]

            x_out_down = channel_ownShip[3][0]
            y_out_down = channel_ownShip[3][0]

            X_left = abs(x_out_down - x_own)
            Y_left = abs(y_out_down - y_own)
            X_right = abs(x_out_up - x_own)
            Y_right = abs(y_out_up - y_own)

            c_left = abs(360- math.degrees(math.atan(X_left / Y_left)) - course_own)
            c_right = abs(360- math.degrees(math.atan(X_right / Y_right)) - course_own)

        return [c_left,c_right]

    def get_decision(self,remark,section_course):
        """

        :param remark: ["R/L/K","A/M/K"]
        :return:
        """
        x_own = self.list_own[0]
        y_own = self.list_own[1]
        speed_own = self.list_own[3]
        course_own = self.list_own[2]
        L_own = self.list_own[4]
        B_own = self.list_own[5]

        #########右转########
        if remark[0]=="R" and remark[1]=="K":
            c_right = section_course[1]
            list_own = [x_own, y_own, course_own + c_right, speed_own, L_own, B_own]
            result_danger = Judge_Danger(list_own, self.ships, self.list_channel_oneArea).start(1800)
            if result_danger == [[0]]:
                return ["R", "K"]
            else:
                return ["N", "N"]

        #########左转########
        elif remark[0] == "L" and remark[1] == "K":

            c_left = section_course[0]
            list_own = [x_own, y_own, course_own - c_left, speed_own, L_own, B_own]
            result_danger = Judge_Danger(list_own, self.ships, self.list_channel_oneArea).start(1800)
            if result_danger == [[0]]:
                return ["L", "K"]
            else:
                return ["N", "N"]

        #########加速########
        elif remark[0]=="K" and remark[1]=="A":

            list_own = [x_own, y_own, course_own, self.speed_max, L_own, B_own]

            result_danger = Judge_Danger(list_own, self.ships, self.list_channel_oneArea).start(1800)
            if result_danger ==[[0]]:
                return ["K", "A"]
            else:
                return ["N", "N"]

        #########减速########
        elif remark[0] == "K" and remark[1] == "M":

            list_own = [x_own, y_own, course_own, self.speed_min, L_own, B_own]

            result_danger =Judge_Danger(list_own, self.ships, self.list_channel_oneArea).start(1800)

            if result_danger == [[0]]:
                return ["K", "M"]
            else:
                return ["N", "N"]

        #########减速加右转########
        elif remark[0] == "R" and remark[1] == "M":
            c_right = section_course[1]
            list_own = [x_own, y_own, course_own + c_right,  self.speed_min, L_own, B_own]

            result_danger = Judge_Danger(list_own, self.ships, self.list_channel_oneArea).start(1800)
            if result_danger == [[0]]:
                return ["R", "M"]
            else:
                return ["N","N"]


        #########减速加左转########
        elif remark[0] == "L" and remark[1] == "M":
            c_left = section_course[0]
            list_own = [x_own, y_own, course_own - c_left, self.speed_min, L_own, B_own]
            result_danger = Judge_Danger(list_own, self.ships, self.list_channel_oneArea).start(
                1800)
            if result_danger == [[0]]:
                return ["L", "M"]
            else:
                return ["N", "N"]


        #########加速加右转########
        elif remark[0] == "R" and remark[1] == "A":
            c_right = section_course[1]
            list_own = [x_own, y_own, course_own + c_right, self.speed_max, L_own, B_own]

            result_danger = Judge_Danger(list_own, self.ships, self.list_channel_oneArea).start(1800)
            if result_danger == [[0]]:
                return ["R", "A"]
            else:
                return ["N", "N"]



        #########加速加左转########
        elif remark[0] == "L" and remark[1] == "A":
            c_right = section_course[0]
            list_own = [x_own, y_own, course_own - c_right, self.speed_max, L_own, B_own]

            result_danger = Judge_Danger(list_own, self.ships, self.list_channel_oneArea).start(1800)
            if result_danger == [[0]]:
                return ["L", "A"]
            else:
                return ["N", "N"]

    ##########开始程序#########
    def start(self):
        channel_ownShip=self.judge_ownShip_channel() #本船所处航段
        mark_channel=channel_ownShip[4][3] #上行/下行

        status=self.identify_situation(mark_channel) #局面
        print("局面",status)
        section_course=self.get_section_condition(channel_ownShip) #[c_left,c_right]
        print("改向角",section_course)

        #########开始决策逻辑######
        #目标船舶为横越船舶(与航道夹角大于30)
        if status==0:
            if self.time<=600:
                ########右转向######
                remark=["R","K"]
                result=self.get_decision(remark,section_course)
                if result!=["N","N"]:
                    return result

                ########加速######
                remark = ["K", "A"]
                result = self.get_decision(remark, section_course)
                if result != ["N", "N"]:
                    return result

                ########减速######
                remark = ["K", "M"]
                result = self.get_decision(remark, section_course)
                if result != ["N", "N"]:
                    return result

                ########减速加右转######
                remark = ["R", "M"]
                result = self.get_decision(remark, section_course)

                return result

            else:
                return ["K","K"]

        #目标船舶是被追越船
        elif status==1:
            ########左转向######
            remark = ["L", "K"]
            result = self.get_decision(remark, section_course)
            if result != ["N", "N"]:
                return result

            ########减速######
            remark = ["K", "M"]
            result = self.get_decision(remark, section_course)
            return result

        # 目标船舶是追越船
        elif status == -1:
            if self.time <= 600:
                ########右转向######
                remark = ["R", "K"]
                result = self.get_decision(remark, section_course)
                return result
            else:
                return ["K", "K"]

        # 目标船舶是左侧特殊船(与航道夹角小于30，位于本船左侧)
        elif status == -2:
            if self.time <= 600:
                ########右转向######
                remark = ["R", "K"]
                result = self.get_decision(remark, section_course)
                if result != ["N", "N"]:
                    return result

                ########加速######
                remark = ["K", "A"]
                result = self.get_decision(remark, section_course)
                if result != ["N", "N"]:
                    return result

                ########减速######
                remark = ["K", "M"]
                result = self.get_decision(remark, section_course)
                if result != ["N", "N"]:
                    return result

                ########减速加右转######
                remark = ["R", "M"]
                result = self.get_decision(remark, section_course)

                return result

            else:
                return ["K", "K"]

        # 目标船舶是右侧特殊船(与航道夹角小于30，位于本船右侧)
        elif status == 2:
            if self.time <= 600:
                ########左转向######
                remark = ["L", "K"]
                result = self.get_decision(remark, section_course)
                if result != ["N", "N"]:
                    return result

                ########加速######
                remark = ["K", "A"]
                result = self.get_decision(remark, section_course)
                if result != ["N", "N"]:
                    return result

                ########减速######
                remark = ["K", "M"]
                result = self.get_decision(remark, section_course)
                if result != ["N", "N"]:
                    return result

                ########减速加左转######
                remark = ["L", "M"]
                result = self.get_decision(remark, section_course)
                return result
            else:
                return ["K", "K"]

#筛选重复、速度小于0.3m/s以及附近2*0.8nm的船舶
class Get_Near_Ships():
    def __init__(self,list_own,list_ships):
        self.list_own=list_own
        self.list_ships=list_ships
        ##########赛选2*0.8nm内且速度大于1kn的船舶(已验证)#########

    def get_ships_near(self):
        list_ships_near = []

        X_own = self.list_own[0]  # 本船x
        Y_own = self.list_own[1]  # 本船y
        w = math.radians(self.list_own[2])  # 本船真航向
        L01 = 3704  # 长半轴，2nm
        B01 = 1481  # 短半轴，0.8nm

        for item in self.list_ships:
            if item[4] > 0.3:
                X_ship = item[0]  # 其他船舶x
                Y_ship = item[1]  # 其他船舶y

                result01 = ((Y_ship - Y_own) * math.cos(w) + (X_ship - X_own) * math.sin(w)) ** 2 / L01 ** 2 + (
                        (X_ship - X_own) * math.cos(w) - (Y_ship - Y_own) * math.sin(w)) ** 2 / B01 ** 2 - 1

                if result01 <= 0:
                    list_ships_near.append(item)

        return list_ships_near


###############################################一、获取静态信息并进行坐标转换（区域和航道信息）##################################################
########################（一）获取小船航行时静态信息###################################
staticData_smallShip=Get_StaticData().get_data_smallShip()  #从excel表格内获取小船静态信息
staticData_smallShip_converted=Convert_Data(staticData_smallShip).convert_staticData() #转换从excel表格内获取的小船静态信息的坐标
dataArea_smallShip_converted=staticData_smallShip_converted[0] #坐标转换后的小船区域信息
dataChannel_smallShip_converted=staticData_smallShip_converted[1] #坐标转换后的小船航道信息


#########################（二）获取大船航行时静态信息###################################
staticData_bigShip=Get_StaticData().get_data_bigShip()  #从excel表格内获取大船静态信息
staticData_bigShip_converted=Convert_Data(staticData_bigShip).convert_staticData() #转换从excel表格内获取大船静态信息的坐标
dataArea_bigShip_converted=staticData_bigShip_converted[0] #坐标转换后的大船区域信息
dataChannel_bigShip_converted=staticData_bigShip_converted[1] #坐标转换后的大船航道信息


########################（三）处理坐标转换后的航道信息，划分为若干个航段##################
dataChannel_bigShip_dealed=Deal_DataChannel(dataChannel_bigShip_converted,"bigShip").deal_channel()
dataChannel_smallShip_dealed=Deal_DataChannel(dataChannel_smallShip_converted,"smallShip").deal_channel()
print(dataChannel_bigShip_dealed)
print(dataChannel_smallShip_dealed)

while True:

    ###############################################二、获取坐标转换后的船舶信息##############################################
    list_ownship=[120.089673, 31.947848, 109.3, 4.702022, 150, 12.0]
    list_ships_resv =[[120.037384, 31.960627, 108.3, 413862638, 5.093], [120.225908, 31.926201, 216.8, 538003960, 0.051444], [120.120205, 31.942028, 107.9, 413834715, 3.755444], [120.102138, 31.958726, 278.0, 413992013, 1.903444], [120.090619, 31.946393, 110.6, 413951104, 3.961222], [120.140448, 31.937153, 101.4, 440875000, 6.687778], [120.09856, 31.941565, 0.0, 413772986, 0.051444], [120.113007, 31.957851, 285.8, 413763531, 2.057778], [120.008293, 31.99052, 360.0, 413316960, 0.0], [120.016186, 31.978641, 296.6, 413779588, 1.749111], [120.072051, 31.952161, 105.7, 413990923, 4.218444], [120.097283, 31.961983, 84.2, 413832279, 0.0], [120.142348, 31.925479, 194.3, 413787314, 0.051444], [120.15322, 31.935046, 101.5, 636018711, 6.945], [120.108507, 31.958533, 0.0, 413950217, 0.0], [120.189383, 31.946439, 275.7, 413794877, 1.749111], [120.157407, 31.949325, 58.6, 413555555, 0.0], [120.060422, 31.968505, 100.2, 413505920, 0.0], [120.091054, 31.945827, 112.2, 413816588, 3.909778], [120.078979, 31.949999, 107.9, 413974828, 3.909778], [120.230822, 31.933285, 251.8, 374269000, 3.806889], [120.084967, 31.944433, 208.0, 413995557, 0.0], [120.054696, 31.95719, 106.1, 413933692, 4.938667], [120.175013, 31.938923, 0.0, 413859025, 0.0], [120.089802, 31.94582, 16.2, 413818205, 4.064111], [120.065371, 31.954261, 103.1, 413974849, 3.961222], [120.138939, 31.954355, 345.0, 413839395, 0.720222], [120.15715, 31.941333, 280.4, 413800061, 0.0], [120.210467, 31.93972, 0.0, 413833231, 0.0], [120.104615, 31.959261, 285.8, 413792333, 1.903444], [120.021504, 31.979051, 294.6, 413980124, 1.286111], [120.042213, 31.955397, 229.9, 413358940, 0.0], [120.096707, 31.9623, 0.0, 413983708, 0.0], [120.097042, 31.958953, 295.9, 413789571, 1.286111], [120.061299, 31.962555, 281.7, 412418190, 2.829444], [120.139825, 31.934192, 215.9, 413795507, 1.646222], [120.007817, 31.990017, 175.7, 413861845, 0.0], [120.090608, 31.963332, 69.1, 413983151, 0.0], [120.104115, 31.945569, 108.1, 413810824, 3.961222], [120.175412, 31.94716, 0.0, 413834669, 0.0], [119.956132, 32.026875, 144.8, 413827822, 5.093], [119.969585, 32.005957, 132.7, 412997000, 6.224778], [120.164627, 31.942883, 0.0, 413842047, 0.0], [120.089277, 31.963797, 202.4, 413780344, 0.0], [120.160948, 31.924757, 264.0, 413960287, 0.0], [120.083273, 31.96348, 279.4, 413833499, 3.241], [120.08884, 31.9633, 0.0, 413854681, 0.0], [119.999334, 31.981112, 127.5, 440353000, 5.761778], [120.168615, 31.948067, 0.0, 215673000, 0.0], [120.137627, 31.918263, 326.9, 413819161, 0.0], [120.076398, 31.954867, 286.3, 413441940, 2.932333], [120.133723, 31.953132, 302.8, 412000000, 0.0], [120.08564, 31.944917, 0.0, 413860618, 0.0], [120.160259, 31.945228, 207.7, 413853923, 0.051444], [120.101677, 31.946079, 108.0, 412359650, 4.372778], [120.088813, 31.963147, 0.0, 413853528, 0.0], [120.097535, 31.962837, 360.0, 600021348, 0.0], [119.963429, 32.018151, 139.5, 440432000, 5.298778], [120.099982, 31.957505, 279.3, 413783708, 1.800556], [120.217513, 31.924588, 260.3, 538008891, 0.0], [120.085691, 31.947884, 110.5, 413771952, 3.755444], [120.105534, 31.9576, 283.0, 413813324, 2.160667], [120.143155, 31.926418, 0.0, 413966212, 0.0], [120.144003, 31.926655, 0.0, 413764146, 0.0], [120.114068, 31.939977, 113.3, 413834231, 3.704], [120.219342, 31.935059, 263.1, 412380020, 2.880889], [120.090489, 31.962377, 283.3, 413853968, 3.395333], [120.089133, 31.96345, 164.7, 413862297, 0.0], [120.109053, 31.958733, 0.0, 413854109, 0.0], [120.13655, 31.91735, 193.7, 412434140, 0.0], [120.083998, 31.944328, 205.5, 413807318, 0.0], [120.067997, 31.959223, 282.6, 413379030, 3.909778], [120.090431, 31.958548, 290.2, 413832607, 1.440444], [120.157783, 31.9239, 285.7, 413818604, 0.0], [120.135516, 31.930482, 186.0, 354097000, 0.051444], [120.148468, 31.950817, 0.0, 413775828, 0.0], [120.170887, 31.943805, 14.1, 413832234, 0.0], [120.225035, 31.931022, 52.2, 413794502, 2.366444], [120.167102, 31.947432, 282.8, 413763382, 2.109222], [120.074704, 31.950528, 107.5, 413802674, 4.372778], [120.023433, 31.965289, 114.1, 413808125, 3.806889], [120.02488, 31.963276, 299.0, 413358830, 2.469333], [120.107527, 31.95921, 280.4, 413959447, 3.292444], [120.136295, 31.919512, 253.2, 413780118, 0.0], [120.157147, 31.941883, 0.0, 413855586, 0.0], [120.0428, 31.95085, 68.0, 413850141, 0.0], [120.116592, 31.954012, 92.2, 413794516, 0.463], [120.14225, 31.9251, 195.2, 413774682, 0.0], [120.12936, 31.954257, 300.1, 413993301, 0.0], [120.106357, 31.953179, 354.9, 412361840, 0.051444], [120.162054, 31.945126, 210.1, 413816313, 0.051444], [120.1356, 31.918867, 6.4, 412751620, 0.0], [120.160445, 31.941487, 0.0, 413958301, 0.0], [120.01098, 31.981214, 295.2, 413791036, 1.337556], [119.996378, 31.988053, 316.4, 413800763, 1.183222], [120.13258, 31.935027, 104.8, 413774314, 3.292444], [120.096085, 31.960623, 278.9, 413990989, 3.395333], [120.142565, 31.926008, 273.5, 413834612, 0.0], [120.157998, 31.924558, 138.9, 413798827, 0.0], [120.135432, 31.918437, 182.7, 412359140, 0.0], [120.08959, 31.962576, 279.7, 413785995, 2.469333], [120.142923, 31.92514, 72.4, 413792998, 0.0], [120.128217, 31.940953, 113.2, 147258369, 8.385444], [120.179782, 31.946264, 119.4, 413991779, 0.514444], [120.15653, 31.943845, 132.8, 413817127, 0.0], [120.071663, 31.961678, 335.5, 412362670, 0.0], [120.14062, 31.951246, 325.4, 413953681, 1.697667], [120.13868, 31.927593, 207.6, 413842039, 0.0], [119.929078, 32.060539, 158.0, 354383000, 7.562333], [120.13706, 31.917727, 0.0, 412750130, 0.0], [120.054335, 31.957005, 105.9, 413812489, 4.012667], [120.142448, 31.923698, 109.8, 413817547, 0.0], [120.171392, 31.939306, 169.9, 413838166, 0.051444], [120.18398, 31.938396, 190.7, 413405990, 3.909778], [119.996223, 31.974054, 64.4, 413839727, 4.578556], [120.106525, 31.941165, 109.0, 413828057, 3.241], [120.133053, 31.953287, 0.0, 787878787, 0.0], [120.09316, 31.963267, 4.6, 413817167, 0.0], [120.155903, 31.939727, 0.0, 413794608, 0.0], [120.289644, 31.959115, 240.2, 413459680, 1.543333], [120.103302, 31.940025, 5.5, 413996508, 0.0], [120.273241, 31.948885, 243.7, 249807000, 4.424222], [120.045758, 31.959221, 103.4, 413990286, 4.269889], [120.072945, 31.951937, 105.2, 413770894, 4.167], [120.155888, 31.939942, 42.9, 413789572, 0.0], [120.154431, 31.933612, 100.1, 413458150, 5.813222], [120.161373, 31.945608, 6.1, 413839373, 0.051444], [120.071191, 31.951261, 105.7, 413793866, 4.784333], [120.05858, 31.966139, 281.5, 413829273, 1.697667], [120.16665, 31.943767, 0.0, 413797767, 0.0], [120.097787, 31.962348, 360.0, 413241110, 0.0], [120.105812, 31.959538, 281.0, 413796603, 3.035222], [120.155683, 31.939433, 206.6, 413840952, 0.0], [120.138193, 31.921223, 73.9, 413832006, 0.0], [120.096029, 31.956646, 5.4, 413826173, 3.343889], [120.158478, 31.945207, 0.0, 413802061, 0.0], [120.205378, 31.935557, 0.0, 413832017, 0.0], [120.162033, 31.943067, 203.3, 413826574, 0.0], [119.964063, 32.005448, 228.0, 413998516, 0.0], [120.038306, 31.961014, 108.2, 412809355, 3.395333], [120.090354, 31.946946, 110.5, 413782245, 4.424222], [120.0854, 31.943827, 227.0, 413783805, 0.0], [120.118877, 31.938418, 105.5, 413792366, 4.269889], [120.02576, 31.975023, 299.7, 412554180, 3.035222], [119.933867, 32.0372, 206.0, 538006685, 0.0], [119.990229, 31.991824, 304.5, 413793552, 2.623667], [120.097255, 31.942077, 291.8, 477711700, 0.0], [120.166637, 31.94395, 312.7, 413819228, 0.051444], [120.192433, 31.93875, 22.1, 413834792, 0.0], [120.147395, 31.950843, 193.2, 413780721, 0.0], [120.157223, 31.941477, 0.0, 413829348, 0.0], [120.196478, 31.923088, 180.4, 413000000, 0.0], [120.096058, 31.954435, 16.9, 413795506, 4.064111], [120.140548, 31.9285, 261.4, 413214730, 0.0], [120.083944, 31.963808, 283.1, 413964336, 2.572222], [120.16695, 31.9449, 103.8, 413826639, 0.0], [119.976483, 31.995384, 334.3, 412372950, 0.051444], [120.16335, 31.922499, 222.7, 413979913, 0.051444], [120.07134, 31.952916, 107.8, 413827818, 3.086667], [120.065759, 31.965423, 290.4, 413794364, 1.337556], [120.168221, 31.943341, 45.8, 413980307, 0.051444], [120.171027, 31.921313, 360.0, 414352590, 0.0], [120.077463, 31.944738, 217.2, 413775707, 0.0], [120.054323, 31.968046, 283.9, 413771429, 1.749111], [120.066114, 31.953186, 103.4, 413965932, 3.858333], [120.074753, 31.963452, 279.8, 413789326, 1.800556], [120.087863, 31.947268, 114.0, 413778047, 3.909778], [120.058565, 31.955965, 106.3, 413825117, 4.115556], [120.144331, 31.939366, 185.6, 413795943, 3.138111], [120.149198, 31.951549, 234.5, 413813842, 0.051444], [120.086226, 31.962712, 299.6, 413854688, 2.263556], [120.229893, 31.934857, 260.3, 413798287, 1.440444], [120.151695, 31.927095, 71.2, 413769118, 0.0], [120.160062, 31.922715, 0.0, 300800019, 0.0], [120.160495, 31.941742, 278.2, 413827082, 0.0], [119.995, 31.970533, 218.7, 412361720, 0.0], [120.1203, 31.956231, 147.6, 413841868, 0.102889], [120.14292, 31.925593, 0.0, 413772242, 0.0], [120.073247, 31.951504, 105.9, 413798695, 3.961222], [120.10865, 31.958717, 201.4, 413795585, 0.0], [120.134668, 31.952338, 288.2, 413795202, 1.389], [120.119834, 31.955842, 293.2, 413791315, 2.675111], [120.083837, 31.943907, 227.5, 413795986, 0.102889], [120.140867, 31.92865, 187.7, 414351090, 0.0], [120.183922, 31.928075, 100.9, 413815826, 4.990111], [120.085385, 31.947434, 110.5, 413989712, 4.012667], [120.091302, 31.954031, 297.9, 413827502, 1.800556], [120.098945, 31.961024, 272.7, 413813111, 2.880889], [120.08925, 31.964717, 145.8, 413793664, 0.0], [120.048332, 31.969599, 289.0, 413965992, 1.903444], [120.008462, 31.980456, 302.7, 413527980, 5.247333], [120.145853, 31.935844, 207.2, 413815072, 3.652556], [120.166377, 31.945325, 184.6, 413803412, 0.0], [120.226828, 31.941933, 273.5, 413836091, 1.491889]]
    t1=time.time()
    #list_ownship= [120.088218, 31.948277, 109.46, 1.691733, 75, 12] #本船信息，使用指针从内存获取[x，y，航向,速度,船长，船宽]
    # list_ships_resv=  [[120.064117, 31.960633, 281.7, 412418190, 2.829444], [120.13655, 31.91735, 195.3, 412434140, 0.0], [120.089587, 31.94488, 8.8, 413818205, 3.858333], [120.070878, 31.952413, 106.2, 413990923, 4.218444], [120.083998, 31.944328, 205.5, 413807318, 0.0], [120.065096, 31.962069, 282.7, 413379030, 3.858333], [120.090405, 31.958535, 290.2, 413832607, 1.440444], [120.157783, 31.9239, 285.7, 413818604, 0.0], [120.09971, 31.944073, 108.1, 413810824, 3.961222], [120.090608, 31.963332, 69.1, 413983151, 0.0], [120.190764, 31.944755, 275.7, 413794877, 1.749111], [120.144, 31.92665, 0.0, 413764146, 0.0], [120.08564, 31.944917, 0.0, 413860618, 0.0], [120.135478, 31.930425, 186.0, 354097000, 0.051444], [120.14847, 31.950812, 0.0, 413775828, 0.0], [120.170887, 31.943807, 14.1, 413832234, 0.0], [120.2258, 31.928981, 46.9, 413794502, 2.109222], [120.1671, 31.947383, 282.8, 413763382, 2.109222], [120.07879, 31.947205, 109.1, 413802674, 4.424222], [120.023815, 31.964855, 111.7, 413808125, 3.755444], [120.026357, 31.963093, 297.1, 413358830, 2.520778], [120.104713, 31.95601, 280.4, 413959447, 3.292444], [120.136295, 31.919512, 253.2, 413780118, 0.0], [120.230787, 31.933207, 251.8, 374269000, 3.806889], [120.15716, 31.941847, 0.0, 413855586, 0.0], [120.0428, 31.950817, 43.9, 413850141, 0.0], [120.084711, 31.948286, 108.6, 413771952, 3.858333], [120.116421, 31.953815, 92.2, 413794516, 0.463], [120.142233, 31.925083, 213.2, 413774682, 0.0], [120.106363, 31.953108, 354.9, 412361840, 0.051444], [120.162033, 31.945036, 210.1, 413816313, 0.051444], [120.1356, 31.918867, 6.4, 412751620, 0.0], [120.160443, 31.941485, 0.0, 413958301, 0.0], [120.011387, 31.981407, 290.6, 413791036, 1.286111], [119.996397, 31.98804, 315.1, 413800763, 1.183222], [120.131217, 31.933508, 104.8, 413774314, 3.241], [120.09834, 31.961807, 276.5, 413990989, 3.395333], [120.142565, 31.926008, 273.5, 413834612, 0.0], [120.097283, 31.961983, 84.2, 413832279, 0.0], [120.157998, 31.924558, 138.9, 413798827, 0.0], [120.007817, 31.990017, 175.7, 413861845, 0.0], [120.135432, 31.918437, 182.7, 412359140, 0.0], [120.087613, 31.964448, 282.7, 413785995, 2.469333], [120.11328, 31.940177, 113.2, 413834231, 3.704], [120.142923, 31.92514, 72.4, 413792998, 0.0], [120.128003, 31.942145, 114.5, 147258369, 8.385444], [120.179782, 31.946252, 119.4, 413991779, 0.514444], [120.060422, 31.968505, 100.2, 413505920, 0.0], [120.104396, 31.960074, 283.0, 413981668, 2.263556], [120.166142, 31.944728, 55.7, 413832683, 0.0], [120.036358, 31.961052, 108.5, 413862638, 5.093], [120.15653, 31.943845, 132.8, 413817127, 0.0], [120.021583, 31.978941, 294.6, 413980124, 1.286111], [120.160948, 31.924757, 264.0, 413960287, 0.0], [120.217513, 31.924588, 260.3, 538008891, 0.0], [120.071677, 31.961675, 326.4, 412362670, 0.0], [120.139909, 31.953674, 333.0, 413953681, 2.417889], [120.13868, 31.927593, 207.6, 413842039, 0.0], [119.934388, 32.062262, 158.0, 354383000, 7.562333], [120.084223, 31.948337, 108.9, 199200010, 3.806889], [120.164627, 31.94288, 0.0, 413842047, 0.0], [120.1686, 31.94808, 0.0, 215673000, 0.0], [120.109053, 31.95874, 0.0, 413854109, 0.0], [120.13706, 31.917727, 0.0, 412750130, 0.0], [120.054398, 31.956948, 105.9, 413812489, 4.012667], [120.142453, 31.923698, 126.7, 413817547, 0.0], [120.171408, 31.939376, 169.9, 413838166, 0.051444], [120.166347, 31.925, 188.0, 414350480, 0.0], [120.084731, 31.963306, 284.5, 413833499, 3.241], [120.097538, 31.962823, 360.0, 600021348, 0.0], [120.099421, 31.95961, 279.3, 413783708, 1.800556], [120.187787, 31.935172, 190.7, 413405990, 3.909778], [120.17541, 31.947152, 83.7, 413834669, 0.0], [120.109717, 31.938561, 109.0, 413828057, 3.241], [120.133042, 31.953293, 265.1, 787878787, 0.0], [119.996076, 31.976141, 42.8, 413839727, 4.115556], [120.09316, 31.963267, 4.6, 413817167, 0.0], [120.155903, 31.939728, 0.0, 413794608, 0.0], [120.109633, 31.958567, 234.9, 413771271, 0.0], [120.089133, 31.96345, 164.7, 413862297, 0.0], [120.15716, 31.941347, 280.4, 413800061, 0.0], [120.017079, 31.968404, 119.2, 413972389, 4.938667], [120.10332, 31.940043, 5.5, 413996508, 0.0], [120.108507, 31.958533, 0.0, 413950217, 0.0], [120.275574, 31.950801, 245.5, 249807000, 4.424222], [120.04959, 31.9553, 103.0, 413990286, 4.321333], [120.042218, 31.955385, 228.9, 413358940, 0.0], [120.070156, 31.951043, 104.3, 413770894, 4.167], [120.096215, 31.957511, 295.9, 413789571, 1.286111], [120.155888, 31.939942, 42.9, 413789572, 0.0], [120.153253, 31.93368, 101.1, 413458150, 5.813222], [120.161362, 31.945678, 6.1, 413839373, 0.051444], [120.071277, 31.951212, 105.7, 413793866, 4.784333], [120.116257, 31.939623, 107.9, 413834715, 3.755444], [120.114081, 31.957351, 285.0, 413763531, 2.057778], [120.008267, 31.990537, 360.0, 413316960, 0.0], [120.106078, 31.95779, 282.5, 413813324, 2.212111], [120.058768, 31.96638, 288.2, 413829273, 1.697667], [120.129378, 31.953351, 286.8, 413770147, 2.417889], [120.137627, 31.918263, 326.9, 413819161, 0.0], [120.096707, 31.962293, 0.0, 413983708, 0.0], [120.16665, 31.943767, 0.0, 413797767, 0.0], [120.097793, 31.962342, 360.0, 413241110, 0.0], [120.102247, 31.958812, 281.0, 413796603, 3.035222], [120.139415, 31.9535, 345.0, 413839395, 0.720222], [120.155683, 31.939433, 206.6, 413840952, 0.0], [120.138193, 31.921223, 73.9, 413832006, 0.0], [120.143155, 31.926418, 0.0, 413966212, 0.0], [120.104952, 31.959232, 281.1, 413792333, 1.954889], [120.158478, 31.945207, 0.0, 413802061, 0.0], [120.097287, 31.944017, 108.0, 412359650, 4.372778], [120.162161, 31.943209, 259.9, 413997341, 0.051444], [120.205387, 31.935548, 0.0, 413832017, 0.0], [120.162033, 31.943067, 203.3, 413826574, 0.0], [120.15089, 31.935327, 103.8, 636018711, 6.893556], [120.069705, 31.96764, 117.9, 413797795, 0.051444], [120.126717, 31.930367, 242.3, 413802075, 0.0], [120.0372, 31.961317, 109.3, 412809355, 3.395333], [120.089039, 31.946114, 109.9, 413782245, 4.424222], [120.0854, 31.943827, 227.0, 413783805, 0.0], [120.117177, 31.938651, 105.2, 413792366, 4.269889], [120.026663, 31.97465, 297.2, 412554180, 2.983778], [120.225908, 31.926212, 216.8, 538003960, 0.051444], [120.142353, 31.925485, 188.4, 413787314, 0.0], [119.933867, 32.0372, 206.0, 538006685, 0.0], [119.990941, 31.98827, 304.5, 413793552, 2.623667], [120.210467, 31.93972, 0.0, 413833231, 0.0], [120.097255, 31.942077, 291.8, 477711700, 0.0], [120.078259, 31.950206, 108.5, 413974828, 3.909778], [120.166638, 31.94395, 312.7, 413819228, 0.051444], [120.043052, 31.971392, 288.5, 413965494, 1.646222], [120.147415, 31.95084, 180.0, 413780721, 0.0], [120.192433, 31.93875, 22.1, 413834792, 0.0], [120.089427, 31.946853, 110.0, 413951104, 3.961222], [120.006133, 31.99398, 360.0, 413000000, 0.0], [120.157223, 31.941477, 0.0, 413829348, 0.0], [120.095867, 31.953767, 18.8, 413795506, 4.064111], [120.14054, 31.928497, 360.0, 413214730, 0.0], [120.140275, 31.934676, 202.3, 413795507, 1.646222], [120.084763, 31.963588, 282.6, 413964336, 2.572222], [120.089273, 31.963797, 194.6, 413780344, 0.0], [120.16695, 31.966981, 0.0, 413826639, 52.627667], [120.064554, 31.896529, 102.7, 413974849, 3.961222], [119.97654, 31.995403, 334.3, 412372950, 0.051444], [120.163372, 31.922432, 222.7, 413979913, 0.051444], [120.067317, 31.965788, 290.4, 413794364, 1.337556], [120.070352, 31.953127, 106.7, 413827818, 3.138111], [120.168281, 31.943324, 45.8, 413980307, 0.051444], [119.956061, 32.02657, 144.8, 413827822, 5.093], [120.129337, 31.936139, 108.1, 413778031, 4.064111], [120.017111, 31.97831, 297.1, 413779588, 1.800556], [120.077692, 31.958288, 286.3, 413441940, 2.932333], [120.171027, 31.921313, 360.0, 414352590, 0.0], [120.138453, 31.938649, 101.6, 440875000, 6.636333], [120.077463, 31.944738, 217.2, 413775707, 0.0], [120.056221, 31.969027, 283.9, 413771429, 1.749111], [120.098533, 31.94158, 0.0, 413772986, 0.154333], [120.067519, 31.950175, 104.1, 413965932, 3.858333], [120.07528, 31.963423, 277.7, 413789326, 1.800556], [120.091544, 31.950641, 114.0, 413778047, 3.909778], [120.088853, 31.963303, 0.0, 413854681, 0.0], [120.249302, 31.933573, 67.0, 413941039, 3.858333], [120.14432, 31.940377, 171.1, 413795943, 3.909778], [120.149197, 31.95155, 234.5, 413813842, 0.051444], [120.0838, 31.962613, 280.8, 413854688, 2.212111], [120.230654, 31.933052, 260.3, 413798287, 1.440444], [120.088813, 31.963147, 0.0, 413853528, 0.0], [120.157412, 31.949303, 141.1, 413555555, 0.051444], [120.151695, 31.927095, 71.2, 413769118, 0.0], [120.160062, 31.922715, 0.0, 300800019, 0.0], [120.160497, 31.941742, 278.2, 413827082, 0.0], [120.160262, 31.945232, 147.4, 413853923, 0.0], [119.995, 31.970533, 218.7, 412361720, 0.0], [120.120307, 31.956088, 147.6, 413841868, 0.102889], [119.998848, 31.981395, 129.6, 440353000, 5.864667], [120.142933, 31.925583, 0.0, 413772242, 0.0], [120.089483, 31.946434, 112.0, 413816588, 3.961222], [120.072142, 31.951732, 105.4, 413798695, 3.961222], [120.10865, 31.958717, 201.4, 413795585, 0.0], [120.135426, 31.951549, 286.2, 413795202, 1.440444], [120.21917, 31.935251, 263.1, 412380020, 2.880889], [120.121015, 31.954524, 280.2, 413791315, 2.623667], [120.085777, 31.944821, 339.5, 413858612, 0.051444], [120.083956, 31.943945, 227.5, 413795986, 0.102889], [120.05324, 31.95749, 105.8, 413933692, 4.938667], [120.140867, 31.92865, 187.7, 414351090, 0.0], [120.185692, 31.933334, 100.9, 413815826, 4.990111], [120.084093, 31.94793, 110.4, 413989712, 4.012667], [120.0918, 31.953833, 300.9, 413827502, 1.852], [120.099126, 31.961373, 281.7, 413813111, 2.778], [120.08925, 31.964717, 65.9, 413793664, 0.0], [120.1318, 31.9532, 0.0, 999414103, 0.0], [120.048273, 31.972249, 289.0, 413965992, 1.903444], [120.13285, 31.952967, 0.0, 999414104, 0.0], [120.084967, 31.944433, 208.0, 413995557, 0.0], [120.012987, 31.978766, 303.2, 413527980, 5.195889], [119.973831, 32.002672, 131.3, 413976499, 3.498222], [120.135983, 31.9522, 0.0, 999414108, 0.0], [119.958246, 32.016199, 139.5, 440432000, 5.298778], [119.968098, 32.00696, 132.8, 412997000, 6.173333], [120.175013, 31.938913, 0.0, 413859025, 0.0], [120.09156, 31.962117, 280.6, 413853968, 3.446778], [120.144644, 31.933234, 204.7, 413815072, 1.646222], [120.133717, 31.953117, 0.0, 412000000, 0.0], [120.166377, 31.945325, 184.6, 413803412, 0.0], [120.226504, 31.939889, 273.5, 413836091, 1.491889], [120.168628, 31.939764, 185.8, 413827938, 0.051444], [120.191817, 31.936233, 334.0, 413830289, 0.0], [120.12936, 31.954267, 300.1, 413993301, 0.0], [120.029362, 31.975033, 354.1, 413798043, 0.0], [120.111154, 31.9497, 297.0, 413791049, 1.131778], [120.14028, 31.928877, 0.0, 413840883, 0.0], [120.291103, 31.959341, 240.2, 413459680, 1.543333], [120.01566, 31.98586, 0.0, 636017510, 0.0], [120.093562, 31.959011, 5.4, 413826173, 3.343889], [120.10961, 31.958488, 0.0, 413820731, 0.0], [119.964063, 32.005448, 228.0, 413998516, 0.0], [120.128787, 31.931503, 0.0, 413827006, 0.0], [120.061054, 31.958574, 107.2, 413851127, 3.961222], [120.132, 31.9536, 330.0, 412000655, 0.0], [120.06588, 31.966757, 220.8, 268268268, 0.0], [120.129367, 31.932083, 228.0, 413955000, 0.0], [120.109741, 31.943506, 106.9, 413822747, 3.909778], [120.096442, 31.946745, 107.6, 413811079, 4.167], [120.161765, 31.923918, 176.1, 413778807, 0.0], [120.056633, 31.959958, 106.3, 413825117, 4.115556], [120.084692, 31.94406, 0.0, 413950385, 0.0], [120.171972, 31.937215, 304.0, 413802192, 0.0], [120.039744, 31.964102, 106.4, 413862154, 4.167], [120.132613, 31.9515, 285.7, 413971079, 2.623667], [120.12067, 31.953688, 186.4, 413965466, 2.675111], [120.144309, 31.931964, 270.8, 413982665, 2.623667], [120.143967, 31.92545, 311.0, 413853971, 0.0], [120.16176, 31.92338, 0.0, 413963031, 0.0], [120.090542, 31.95639, 301.5, 413831618, 1.852], [120.177617, 31.936312, 36.9, 413798178, 0.0], [120.150406, 31.927461, 220.3, 636016377, 0.051444], [120.089597, 31.964343, 351.1, 413788749, 0.0], [120.157487, 31.92357, 121.5, 413770952, 0.0], [120.158335, 31.945816, 34.9, 413834563, 0.051444], [120.165026, 31.947084, 278.3, 413971516, 1.389], [120.08897, 31.96339, 150.4, 413790316, 0.0], [120.156467, 31.945477, 0.0, 413858076, 0.0], [120.195707, 31.938483, 0.0, 413953476, 0.0], [120.088693, 31.94271, 81.3, 413815897, 0.0], [120.143275, 31.945933, 20.8, 413841734, 4.475667], [120.16915, 31.9244, 52.7, 413828773, 0.0], [120.102723, 31.958638, 281.8, 413992013, 1.903444], [120.155238, 31.931902, 94.5, 413839256, 4.115556], [120.1384, 31.95323, 103.7, 413772844, 0.0], [120.155536, 31.927867, 104.3, 413818025, 3.806889], [120.130918, 31.955825, 0.0, 413788554, 0.0], [119.998125, 31.972083, 275.8, 413825255, 0.0], [120.13649, 31.917422, 176.3, 413425340, 0.0], [120.099213, 31.96074, 275.6, 413815153, 1.852], [120.160536, 31.947247, 279.1, 413812651, 2.006333], [120.092893, 31.963377, 218.3, 413862106, 0.0], [119.975213, 31.978007, 288.8, 413553650, 0.0]]

    #右侧横越0：[120.089587, 31.94488, 8.8, 413818205, 4]   ,本船：[120.088218, 31.948277, 109.46, 4.691733, 75, 12]
    #左侧横越0：[120.089587, 31.95288, 180.8, 413818206, 6.5] ,本船：[120.088218, 31.948277, 109.46, 2.691733, 75, 12]
    #本船追越1：[120.088218, 31.948277, 109, 412418190, 2.629444],本船改为：[120.064117, 31.955033, 109.46, 4.829444, 75, 12]
    #本船被追越-1：[120.064117, 31.955033, 109, 412418190, 4.829444] 本船： [120.088218, 31.948277, 109.46, 1.829444, 75, 12]
    # 左侧特殊-2：[120.084117, 31.951033, 120, 412418190, 4.8]  本船：[120.088218, 31.948277, 109.46, 2.691733, 75, 12]

    #右侧特殊2：[120.080117, 31.947033, 90, 412418190, 5]，本船改为：[120.088218, 31.948277, 109.46, 1.691733, 75, 12]
    #list_ships_resv =[[120.080117, 31.947033, 90, 412418190, 5]]


    shipsData_conveted=Convert_Data([[],[]]).convert_shipsData(list_ownship,list_ships_resv) #转换船舶信息的坐标
    ownshipData_converted=shipsData_conveted[0] #坐标转换后的本船信息
    targetShipData_converted =shipsData_conveted[1] #坐标转换后的目标船舶信息

    #################筛选重复、速度小于0.3m/s以及附近2*0.8nm的船舶###############
    list_targetships = Get_Near_Ships(ownshipData_converted,targetShipData_converted).get_ships_near()

    print("转换后的本船信息：",ownshipData_converted)
    print("转换后的其他船舶信息：",list_targetships)

    ###############################################三、提取对应船舶航道和区域信息##############################################
    lenth_ownShip=list_ownship[4] #船舶长度
    if lenth_ownShip<80:#船长小于80m
        data_area=dataArea_smallShip_converted
        data_channel=dataChannel_smallShip_dealed
    else:
        data_area = dataArea_bigShip_converted
        data_channel = dataChannel_bigShip_dealed


    ###############################################四、获取本船所处区域id##############################################
    id_area = Judge_Area(data_area, ownshipData_converted[0],
                         ownshipData_converted[1]).get_idArea()  # 获取本船所处区域的id:[id_type,id_area]
    print("本船所处区域：",id_area)

    ###############################################五、获取预警和辅助决策信息################################################
    # 本船处于浏河口-南京以外的区域
    if id_area[0] == 0:
        ########################（一）用速度障碍法计算危险船舶#########################
        list_danger_ships=Warm_Danger_By_SOM(ownshipData_converted,list_targetships).start() #[船舶1,船舶2,船舶3.......] ，船舶：[x，y，航向,mmsi，速度,t_in]

        ########################（二）获取危险预警###################################
        len_danger_ships = len(list_danger_ships)  # 危险船舶数量
        warm_danger = "%d" % (len_danger_ships)
        for item in list_danger_ships:
            warm_danger += "-%d" % (item[3])

        #########################（三）生成回传信息##################################
        if warm_danger == "0":
            danger_messege = warm_danger
        else:
            mmsi_danger_ship = warm_danger.split("-")
            danger_messege = mmsi_danger_ship[0]
            lenth_mmsi = len(mmsi_danger_ship)
            i = 1
            while i < lenth_mmsi:
                mmsi = int(mmsi_danger_ship[i])
                for ship in list_targetships:
                    if mmsi == ship[3]:
                        cog = ship[2]
                        sog = round(ship[4] / 0.514, 1)
                        danger_messege += "-%d" % (mmsi) + "-%0.1f" % (cog) + "-%0.1f" % (sog)
                i += 1
        data_send = "qt-" + danger_messege


    # 本船处于浏河口-南京以内的交汇区域
    elif id_area[0] == 2:
        ########################（一）判断本船与航道位置关系#########################
        list_channel_messege=data_channel[1][id_area[1]-1]
        status_ownShip = Which_Location(ownshipData_converted, list_channel_messege).judge_ownShip_location()

        ########################（二）本船在航道外#########################
        if status_ownShip[0][0] == 0:

            ########################1、用速度障碍法计算危险船舶#########################
            list_danger_ships = Warm_Danger_By_SOM(ownshipData_converted,
                                                   list_targetships).start()  # [船舶1,船舶2,船舶3.......] ，船舶：[x，y，航向,mmsi，速度,t_in]

            ########################2、获取危险预警###################################
            len_danger_ships = len(list_danger_ships)  # 危险船舶数量
            warm_danger = "%d" % (len_danger_ships)
            for item in list_danger_ships:
                warm_danger += "-%d" % (item[3])

            #########################3、生成回传信息##################################
            if warm_danger == "0":
                danger_messege = warm_danger
            else:
                mmsi_danger_ship = warm_danger.split("-")
                danger_messege = mmsi_danger_ship[0]
                lenth_mmsi = len(mmsi_danger_ship)
                i = 1
                while i < lenth_mmsi:
                    mmsi = int(mmsi_danger_ship[i])
                    for ship in list_targetships:
                        if mmsi == ship[3]:
                            cog = ship[2]
                            sog = round(ship[4] / 0.514, 1)
                            danger_messege += "-%d" % (mmsi) + "-%0.1f" % (cog) + "-%0.1f" % (sog)
                    i += 1
            data_send = "jh-out-" + danger_messege


        ########################（三）本船在航道内且非顺航道行驶#########################
        elif status_ownShip[0][0] == -1:
            ########################1、求边界预警#########################
            warm_navigation = Warm_Navigation(ownshipData_converted, status_ownShip[1]).get_warm_navigation()
            warm_border = warm_navigation[0]
            if warm_border[0] == 1:
                status01 = "L"
            elif warm_border[0] == 2:
                status01 = "R"
            else:
                status01 = "K"
            s01 = "%d" % (warm_border[1])

            ########################2、用速度障碍法计算危险船舶#########################
            list_danger_ships = Warm_Danger_By_SOM(ownshipData_converted,
                                                   list_targetships).start()  # [船舶1,船舶2,船舶3.......] ，船舶：[x，y，航向,mmsi，速度,t_in]

            ########################3、获取危险预警###################################
            len_danger_ships = len(list_danger_ships)  # 危险船舶数量
            warm_danger = "%d" % (len_danger_ships)
            for item in list_danger_ships:
                warm_danger += "-%d" % (item[3])

            #########################4、生成回传信息##################################
            if warm_danger == "0":
                danger_messege = warm_danger
            else:
                mmsi_danger_ship = warm_danger.split("-")
                danger_messege = mmsi_danger_ship[0]
                lenth_mmsi = len(mmsi_danger_ship)
                i = 1
                while i < lenth_mmsi:
                    mmsi = int(mmsi_danger_ship[i])
                    for ship in list_targetships:
                        if mmsi == ship[3]:
                            cog = ship[2]
                            sog = round(ship[4] / 0.514, 1)
                            danger_messege += "-%d" % (mmsi) + "-%0.1f" % (cog) + "-%0.1f" % (sog)
                    i += 1
            data_send = "jh-not-" + danger_messege + "-" + status01+ "-" + str(s01)


        ########################（四）本船在航道内且顺航道行驶#########################
        else:
            ########################1、求预警信息#########################
            warm_navigation = Warm_Navigation(ownshipData_converted, status_ownShip[1]).get_warm_navigation()
            warm_border = warm_navigation[0]
            warm_yaw = warm_navigation[1]

            # 处理偏航报警
            if warm_yaw[0] == 1:
                status01 = "L"
            elif warm_yaw[0] == 2:
                status01 = "R"
            else:
                status01 = "K"
            s01 = "%d" % (warm_yaw[1])

            # 处理边界报警
            if warm_border[0] == 1:
                status02 = "L"
            elif warm_border[0] == 2:
                status02 = "R"
            else:
                status02 = "K"
            s02 = "%d" % (warm_border[1])



            ########################2、用速度障碍法计算危险船舶#########################
            list_danger_ships = Warm_Danger_By_SOM(ownshipData_converted,
                                                   list_targetships).start()  # [船舶1,船舶2,船舶3.......] ，船舶：[x，y，航向,mmsi，速度,t_in]

            ########################3、获取危险预警###################################
            len_danger_ships = len(list_danger_ships)  # 危险船舶数量
            warm_danger = "%d" % (len_danger_ships)
            for item in list_danger_ships:
                warm_danger += "-%d" % (item[3])

            #########################4、生成回传信息##################################
            if warm_danger == "0":
                danger_messege = warm_danger
            else:
                mmsi_danger_ship = warm_danger.split("-")
                danger_messege = mmsi_danger_ship[0]
                lenth_mmsi = len(mmsi_danger_ship)
                i = 1
                while i < lenth_mmsi:
                    mmsi = int(mmsi_danger_ship[i])
                    for ship in list_targetships:
                        if mmsi == ship[3]:
                            cog = ship[2]
                            sog = round(ship[4] / 0.514, 1)
                            danger_messege += "-%d" % (mmsi) + "-%0.1f" % (cog) + "-%0.1f" % (sog)
                    i += 1
            data_send = "jh-in-" + danger_messege + "-" + status01 + "-" + str(s01)+ "-" + status02 + "-" + str(s02)



    # 本船处于浏河口-南京以内的正常区域/其他区域
    else:
        if id_area[0] == 1:
            list_channel_messege = data_channel[0][id_area[1] - 1]  # 取出本船所在区域的航道数据
        else:
            list_channel_messege = data_channel[2][id_area[1] - 1]  # 取出本船所在区域的航道数据

        ########################（一）判断本船与航道位置关系#########################
        status_ownShip = Which_Location(ownshipData_converted,list_channel_messege).judge_ownShip_location()

        ########################（二）本船在航道外#########################
        if status_ownShip[0][0] == 0:
            ########################1、用速度障碍法计算危险船舶#########################
            list_danger_ships = Warm_Danger_By_SOM(ownshipData_converted,
                                                   list_targetships).start()  # [船舶1,船舶2,船舶3.......] ，船舶：[x，y，航向,mmsi，速度,t_in]

            ########################2、获取危险预警###################################
            len_danger_ships = len(list_danger_ships)  # 危险船舶数量
            warm_danger = "%d" % (len_danger_ships)
            for item in list_danger_ships:
                warm_danger += "-%d" % (item[3])

            #########################3、生成回传信息##################################
            if warm_danger == "0":
                danger_messege = warm_danger
            else:
                mmsi_danger_ship = warm_danger.split("-")
                danger_messege = mmsi_danger_ship[0]
                lenth_mmsi = len(mmsi_danger_ship)
                i = 1
                while i < lenth_mmsi:
                    mmsi = int(mmsi_danger_ship[i])
                    for ship in list_targetships:
                        if mmsi == ship[3]:
                            cog = ship[2]
                            sog = round(ship[4] / 0.514, 1)
                            danger_messege += "-%d" % (mmsi) + "-%0.1f" % (cog) + "-%0.1f" % (sog)
                    i += 1
            data_send = "zc-out-" + danger_messege

        ########################（三）本船在航道内且非顺航道行驶#########################
        elif status_ownShip[0][0] == -1:
            ########################1、求预警信息#########################
            warm_navigation = Warm_Navigation(ownshipData_converted, status_ownShip[1]).get_warm_navigation()
            warm_border = warm_navigation[0]

            # 处理边界报警
            if warm_border[0] == 1:
                status01 = "L"
            elif warm_border[0] == 2:
                status01 = "R"
            else:
                status01 = "K"
            s01 = "%d" % (warm_border[1])

            ########################2、用速度障碍法计算危险船舶#########################
            list_danger_ships = Warm_Danger_By_SOM(ownshipData_converted,
                                                   list_targetships).start()  # [船舶1,船舶2,船舶3.......] ，船舶：[x，y，航向,mmsi，速度,t_in]

            ########################3、获取危险预警###################################
            len_danger_ships = len(list_danger_ships)  # 危险船舶数量
            warm_danger = "%d" % (len_danger_ships)
            for item in list_danger_ships:
                warm_danger += "-%d" % (item[3])

            #########################4、生成回传信息##################################
            if warm_danger == "0":
                danger_messege = warm_danger
            else:
                mmsi_danger_ship = warm_danger.split("-")
                danger_messege = mmsi_danger_ship[0]
                lenth_mmsi = len(mmsi_danger_ship)
                i = 1
                while i < lenth_mmsi:
                    mmsi = int(mmsi_danger_ship[i])
                    for ship in list_targetships:
                        if mmsi == ship[3]:
                            cog = ship[2]
                            sog = round(ship[4] / 0.514, 1)
                            danger_messege += "-%d" % (mmsi) + "-%0.1f" % (cog) + "-%0.1f" % (sog)
                    i += 1
            data_send = "zc-not-" + danger_messege + "-" + status01 + "-" + str(s01)


        ########################（四）本船在航道内且顺航道行驶#########################
        else:
            ###1、获取航行预警########
            warm_navigation = Warm_Navigation(ownshipData_converted, status_ownShip[1]).get_warm_navigation()
            warm_border = warm_navigation[0]
            warm_yaw = warm_navigation[1]
            warm_turn = warm_navigation[2]

            # 处理偏航报警
            if warm_yaw[0] == 1:
                status01 = "L"
            elif warm_yaw[0] == 2:
                status01 = "R"
            else:
                status01 = "K"
            s01 = "%d" % (warm_yaw[1])

            # 处理边界报警
            if warm_border[0] == 1:
                status02 = "L"
            elif warm_border[0] == 2:
                status02 = "R"
            else:
                status02 = "K"
            s02 = "%d" % (warm_border[1])

            # 处理转向报警
            status03 = str(int(warm_turn[1]))


            ###2、获取危险船舶########
            list_danger_ships = Warm_Danger_By_SOM(ownshipData_converted, list_targetships
                                                   ).start()  # [船舶1,船舶2,船舶3.......] ，船舶：[x，y，航向,mmsi，速度,t_in]
            print("VO",list_danger_ships)

            ###3、获取最危险船舶########
            list_most_danger_ship=Get_Most_Danger_Ship(ownshipData_converted,list_targetships,list_channel_messege).start(1800)
            print("最危险",list_most_danger_ship)

            if list_most_danger_ship[0][0]==0:  #无危险船舶
                warm_decision = ["D","D"]
                len_danger_ships = len(list_danger_ships)
                warm_danger = "%d" % (len_danger_ships)
                for item in list_danger_ships:
                    warm_danger += "-%d" % (item[3])


            else:     #有危险船舶
                most_danger_ship=list_most_danger_ship[0] #危险船舶信息
                danger_time=list_most_danger_ship[1]    #危险时间

                ###4、获取危险船舶提示########
                mark=0
                for item_dangerShip in list_danger_ships:
                    if most_danger_ship[3]==item_dangerShip[3]:
                        mark=1
                if mark==0:
                    list_danger_ships.append(most_danger_ship)
                len_danger_ships = len(list_danger_ships)
                warm_danger = "%d" % (len_danger_ships)
                for item in list_danger_ships:
                    warm_danger += "-%d" % (item[3])

                warm_decision = Get_Support_Decision(ownshipData_converted, most_danger_ship, list_channel_messege,
                                                     targetShipData_converted, danger_time).start()

            #########################4、生成回传信息##################################
            if warm_danger == "0":
                danger_messege = warm_danger
            else:
                mmsi_danger_ship = warm_danger.split("-")
                danger_messege = mmsi_danger_ship[0]
                lenth_mmsi = len(mmsi_danger_ship)
                i = 1
                while i < lenth_mmsi:
                    mmsi = int(mmsi_danger_ship[i])
                    for ship in list_targetships:
                        if mmsi == ship[3]:
                            cog = ship[2]
                            sog = round(ship[4] / 0.514, 1)
                            danger_messege += "-%d" % (mmsi) + "-%0.1f" % (cog) + "-%0.1f" % (sog)
                    i += 1

            C=warm_decision[0]
            V = warm_decision[1]

            data_send = "zc-in-" + danger_messege + "-" + status01 + "-" + str(s01) + "-" + status02 + "-" + str(s02) + "-" + status03 + "-" + C + "-" + V


    print("#######################回传信息：###################",data_send )













