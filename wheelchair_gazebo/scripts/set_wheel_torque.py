#!/usr/bin/env python

import rospy
import time
import os

from gazebo_msgs.srv import *
import rospkg
import csv

rospack = rospkg.RosPack()
pkg_path = rospack.get_path('wheelchair_gazebo')

filename = os.path.join(pkg_path, 'scripts/StraightF_T1_WS64_Mahsa.csv')

if __name__ == '__main__':

	rospy.init_node('set_wheel_torque')

	rospy.wait_for_service('/gazebo/apply_joint_effort')

	time.sleep(5)

	apply_joint_effort = rospy.ServiceProxy('/gazebo/apply_joint_effort', ApplyJointEffort)

	start_time = rospy.Duration.from_sec(0)
	duration = rospy.Duration.from_sec(20)

	with open(filename, 'rb') as csvfile:
		csvfile.readline()
		test_read = csv.reader(csvfile, delimiter=',')
		i = 0
		for data in test_read:
			i+=1
			print(data[5], data[6])
			row_fl_left = float(data[5])
			row_fl_right = float(data[6])

			effort_left = 0.01*row_fl_left
			effort_right = 0.01*row_fl_right

			try:
				resp1 = (apply_joint_effort('WheelL_cont', effort_left, start_time, duration))
				resp2 = (apply_joint_effort('WheelR_cont', effort_right, start_time, duration))

				time.sleep(1/300)

			except rospy.ServiceException, e:
				print "Sercice did not process"
		print(i)
