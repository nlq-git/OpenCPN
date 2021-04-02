/*
 * @Author: your name
 * @Date: 2021-03-25 16:40:27
 * @LastEditTime: 2021-03-27 17:02:37
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /OpenCPN-fork/plugins/aisradar_pi/src/ShipStatus.h
 */
#ifndef _SHIPSTATUS_H_
#define _SHIPSTATUS_H_

#include <unordered_map>

#ifndef  WX_PRECOMP
  #include "wx/wx.h"
#endif //precompiled headers

class tarShip;

//船舶所处位置
enum class ShipLocateArea{
    INIT,
    QT,  //其他区域
    JH,  //实验航段交汇区域
    ZC  //实验航段正常区域
};

//船舶行驶状态
enum class ShipTransportCondition{
    INIT, //其他区域qt为默认INIT
//下述状态只会存在于jh和zc船
    OUT, //实验航道外
    NOT, //非顺航道行驶
    IN   //顺航道行驶
};


//报警字段
//偏航报警 status01
enum class Yaw2Channel{
    INIT,
    R, //右侧偏航
    L, //左侧偏航
    K  //未偏离航道
};

//边界报警 status02
enum class Yaw2Boundary{
    INIT,
    R, //靠近右侧边界
    L, //靠近左侧边界
    K  //未靠近航道边界
};

//辅助决策字段
//转向决策 C
enum class DecisionOfTurn{
    INIT,
    R, //右转向
    L, //左转向
    K, //保向
    D, //正常行驶
    N  //危险，请注意避让
};

//减速决策 V
enum class DecisionOfSpeed{
    INIT,
    M, //减速
    A, //加速
    K, //保速
    D, //正常行驶
    N  //危险，请注意避让
};
class ShipStatus{
public:
    ShipStatus(){
        m_ShipLocateArea = ShipLocateArea::INIT;
        m_ShipTransportCondition = ShipTransportCondition::INIT;
        OtherShipNum = 0;
        m_OtherShipData.clear();
        m_Yaw2Channel = Yaw2Channel::INIT;
        Yaw2ChannelDistance = 0;
        m_Yaw2Boundary =  Yaw2Boundary::INIT;
        Yaw2BoundaryDistance = 0;
        Time2Corner = 0; 
        m_DecisionOfTurn = DecisionOfTurn::INIT;
        m_DecisionOfSpeed = DecisionOfSpeed::INIT;
    }
    ~ShipStatus(){}
    void SetStatusContent(wxArrayString &content);
    void ClearShipStatus()
    {
        m_ShipLocateArea = ShipLocateArea::INIT;
        m_ShipTransportCondition = ShipTransportCondition::INIT;
        OtherShipNum = 0;
        m_OtherShipData.clear();
        m_Yaw2Channel = Yaw2Channel::INIT;
        Yaw2ChannelDistance = 0;
        m_Yaw2Boundary =  Yaw2Boundary::INIT;
        Yaw2BoundaryDistance = 0;
        Time2Corner = 0; 
        m_DecisionOfTurn = DecisionOfTurn::INIT;
        m_DecisionOfSpeed = DecisionOfSpeed::INIT;
    };
    ShipLocateArea GetShipArea() {return m_ShipLocateArea;}

    
    ShipLocateArea m_ShipLocateArea;
    ShipTransportCondition m_ShipTransportCondition;
    //其他船舶总数
    int OtherShipNum; 
    //存放其他船舶信息< mmsi，<cog,sog> >
    std::unordered_map<int, OtherShipData> m_OtherShipData;
    //status01 偏航报警
    Yaw2Channel m_Yaw2Channel;
    int Yaw2ChannelDistance;
    //status02 边界报警
    Yaw2Boundary m_Yaw2Boundary;
    int Yaw2BoundaryDistance;
    //status03 转向点提示
    int Time2Corner;
    //辅助决策
    //转向决策 C
    DecisionOfTurn m_DecisionOfTurn;
    //速度决策 V
    DecisionOfSpeed m_DecisionOfSpeed;

private:
    void SetShipLocateArea(wxString type);
    void SetShipTransportCondition(wxString type);
    int  SetOtherShipNum(wxString type);
    void SetOtherShipData(wxString MMsi, wxString COG, wxString SOG);
    void SetYaw2Channel(wxString type);
    void SetYaw2ChannelDistance(wxString type);
    void SetYaw2Boundary(wxString type);
    void SetYaw2BoundaryDistance(wxString type);
    void SetTime2Corner(wxString type);
    void SetDecisionOfTurn(wxString type);
    void SetDecisionOfSpeed(wxString type);
    




};



class OtherShipData{
public:
    OtherShipData(int _mmsi = 0, double _cog = 0, double _sog = 0)
    :mmsi(_mmsi), cog(_cog),  sog(_sog){}
    void ClearOtherShipData(){ cog=0, sog=0;}
private:
    int mmsi;
    double cog, sog;
};

#endif