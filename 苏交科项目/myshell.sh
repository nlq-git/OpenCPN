#!/bin/bash
#~/anaconda3/envs/tfgpu/bin/python /home/sa/Project/sujiaoke/socket_client_UDP_SJK.py \r
#sleep 3
#pwd
filepath=$(cd "$(dirname "$0")"; pwd)"/main_example_connect.py \r"
echo $filepath
python3 $filepath

echo "执行完毕"
exit 0
