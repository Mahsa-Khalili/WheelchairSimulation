#!/usr/bin/env python
import rospy
import rospkg
import csv
import time
import os
from std_msgs.msg import Float64

rospack = rospkg.RosPack()
pkg_path = rospack.get_path('wheelchair_gazebo')

filename = os.path.join(pkg_path, 'scripts/StraightF_T1_WS64_Mahsa.csv')

if __name__ == '__main__':

	pub_left = rospy.Publisher('/joint_velocity_controller_left/command', Float64, queue_size=1)
	pub_right = rospy.Publisher('/joint_velocity_controller_right/command', Float64, queue_size=1)
	rospy.init_node('set_left_wheel_vel')
	rate = rospy.Rate(10)
	rate.sleep()
	with open(filename, 'rb') as csvfile:
		csvfile.readline()
		test_read = csv.reader(csvfile, delimiter=',')
		i = 0
		for data in test_read:
			i+=1
			print(data[1])
			pub_left.publish(float(data[1]))
			pub_right.publish(float(data[2]))
			time.sleep(0.05)
		print(i)
