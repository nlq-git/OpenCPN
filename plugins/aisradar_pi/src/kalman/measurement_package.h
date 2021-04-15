/*
 * @Author: your name
 * @Date: 2020-11-11 17:14:14
 * @LastEditTime: 2021-04-10 10:32:37
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /OpenCPN-fork/plugins/aisradar_pi/src/kalman/measurement_package.h
 */
#ifndef MEASUREMENT_PACKAGE_H_
#define MEASUREMENT_PACKAGE_H_

#include "Eigen/Dense"

class MeasurementPackage {
public:
  long long timestamp_; //时间戳

  enum SensorType{
    LASER,
    RADAR
  } sensor_type_;

  Eigen::VectorXd raw_measurements_; //原始测量数据
};

#endif /* MEASUREMENT_PACKAGE_H_ */
