/*
 * @Author: your name
 * @Date: 2021-03-25 16:39:10
 * @LastEditTime: 2021-03-27 17:55:37
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /OpenCPN-fork/plugins/aisradar_pi/src/ShipStatus.cpp
 */
#include "ShipStatus.h"

using namespace std;



void ShipStatus::SetStatusContent(wxArrayString &content) //wxstring 的 数组
{
    SetShipLocateArea(content[0]);
    if(m_ShipLocateArea == ShipLocateArea::QT)
    {
        for(int i=0; i<SetOtherShipNum(content[1]); ++i)
            SetOtherShipData(content[i*3+2], content[i*3+3],content[i*3+4]);
        return ;   
    }
    else if(m_ShipLocateArea == ShipLocateArea::JH || m_ShipLocateArea == ShipLocateArea::ZC)
    {
        SetShipTransportCondition(content[1]);
        for(int i=0; i<SetOtherShipNum(content[2]); ++i)
            SetOtherShipData(content[i*3+3], content[i*3+4],content[i*3+5]);
        if(m_ShipTransportCondition == ShipTransportCondition::OUT)
            return;
        else if(m_ShipTransportCondition == ShipTransportCondition::NOT){
            SetYaw2Boundary(content[OtherShipNum * 3 + 3]);
            SetYaw2BoundaryDistance(content[OtherShipNum * 3 + 4]);
            return;
        }
        else if(m_ShipTransportCondition == ShipTransportCondition::IN){
            SetYaw2Channel(content[OtherShipNum * 3 + 3]);
            SetYaw2ChannelDistance(content[OtherShipNum * 3 + 4]);
            SetYaw2Boundary(content[OtherShipNum * 3 + 5]);
            SetYaw2BoundaryDistance(content[OtherShipNum * 3 + 6]);
            if(m_ShipLocateArea == ShipLocateArea::ZC)
            {
                SetDecisionOfTurn(content[OtherShipNum * 3 + 7]);
                SetDecisionOfSpeed(content[OtherShipNum * 3 + 8]);
            }
        }
    }

    
}

void ShipStatus::SetShipLocateArea(wxString type)
{
    if(type == "qt")
        m_ShipLocateArea = ShipLocateArea::QT;
    else if(type == "jh")
        m_ShipLocateArea = ShipLocateArea::JH;
    else if(type == "zc")
        m_ShipLocateArea = ShipLocateArea::ZC;
    else
        m_ShipLocateArea = ShipLocateArea::INIT;
}

void ShipStatus::SetShipTransportCondition(wxString type)
{
    if(type == "out")
        m_ShipTransportCondition = ShipTransportCondition::OUT;
    else if(type == "not")
        m_ShipTransportCondition = ShipTransportCondition::NOT;
    else if(type == "in")
        m_ShipTransportCondition = ShipTransportCondition::IN;
    else
        m_ShipTransportCondition = ShipTransportCondition::INIT;
}

int ShipStatus::SetOtherShipNum(wxString type)
{
    OtherShipNum = wxAtoi(type);
    return OtherShipNum;
}

void ShipStatus::SetOtherShipData(wxString MMSI, wxString COG, wxString SOG)
{
    OtherShipData Others(wxAtoi(MMSI), wxAtof(COG), wxAtof(SOG));
    //m_OtherShipData.insert(unordered_map<string, OtherShipData>::value_type(wxAtoi(MMSI),Others));
    m_OtherShipData[wxAtoi(MMSI)] = Others;
}

void ShipStatus::SetYaw2Channel(wxString type)
{
    if(type == "R")
        m_Yaw2Channel = Yaw2Channel::R;
    else if(type == "L")
        m_Yaw2Channel = Yaw2Channel::L;
    else if(type == "K")
        m_Yaw2Channel = Yaw2Channel::K;
    else
        m_Yaw2Channel = Yaw2Channel::INIT;
}

void ShipStatus::SetYaw2ChannelDistance(wxString type)
{
    Yaw2ChannelDistance = wxAtoi(type);
}

void ShipStatus::SetYaw2Boundary(wxString type)
{
    if(type == "R")
        m_Yaw2Boundary = Yaw2Boundary::R;
    else if(type == "L")
        m_Yaw2Boundary = Yaw2Boundary::L;
    else if(type == "K")
        m_Yaw2Boundary = Yaw2Boundary::K;
    else
        m_Yaw2Boundary = Yaw2Boundary::INIT;
}

void ShipStatus::SetYaw2BoundaryDistance(wxString type)
{
    Yaw2BoundaryDistance = wxAtoi(type);
}

void ShipStatus::SetTime2Corner(wxString type)
{
    Time2Corner = wxAtoi(type);
}

void ShipStatus::SetDecisionOfTurn(wxString type)
{
    if(type == "R")
        m_DecisionOfTurn = DecisionOfTurn::R;
    else if(type == "L")
        m_DecisionOfTurn = DecisionOfTurn::L;
    else if(type == "K")
        m_DecisionOfTurn = DecisionOfTurn::K;
    else if(type == "D")
        m_DecisionOfTurn = DecisionOfTurn::D;
    else if(type == "N")
        m_DecisionOfTurn = DecisionOfTurn::N;
    else
        m_DecisionOfTurn = DecisionOfTurn::INIT;
}

void ShipStatus::SetDecisionOfSpeed(wxString type)
{
    if(type == "M")
        m_DecisionOfSpeed = DecisionOfSpeed::M;
    else if(type == "A")
        m_DecisionOfSpeed = DecisionOfSpeed::A;
    else if(type == "K")
        m_DecisionOfSpeed = DecisionOfSpeed::K;
    else if(type == "D")
        m_DecisionOfSpeed = DecisionOfSpeed::D;
    else if(type == "N")
        m_DecisionOfSpeed = DecisionOfSpeed::N;
    else
        m_DecisionOfSpeed = DecisionOfSpeed::INIT;
}