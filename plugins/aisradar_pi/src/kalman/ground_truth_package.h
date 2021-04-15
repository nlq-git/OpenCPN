/*
 * @Author: your name
 * @Date: 2020-11-11 17:14:14
 * @LastEditTime: 2021-04-10 10:33:21
 * @LastEditors: your name
 * @Description: In User Settings Edit
 * @FilePath: /OpenCPN-fork/plugins/aisradar_pi/src/kalman/ground_truth_package.h
 */
#ifndef GROUND_TRUTH_PACKAGE_H_
#define GROUND_TRUTH_PACKAGE_H_

#include "Eigen/Dense"

class GroundTruthPackage { //地面真值
public:
  long long timestamp_;

  enum SensorType{
    LASER,
    RADAR
  } sensor_type_;

  Eigen::VectorXd gt_values_;

};

#endif /* GROUND_TRUTH_PACKAGE_H_ */
