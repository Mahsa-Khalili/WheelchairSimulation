#!/usr/bin/env python

import rospy
import time
import os

from gazebo_msgs.srv import *
import rospkg
import csv

rospack = rospkg.RosPack()
pkg_path = rospack.get_path('wheelchair_gazebo')

filename = os.path.join(pkg_path, 'scripts/StraightF_T1_Experiment_Ref.csv')

if __name__ == '__main__':

	rospy.init_node('effort_srvcall')

	rospy.wait_for_service('/gazebo/apply_joint_effort')

	apply_joint_effort = rospy.ServiceProxy('/gazebo/apply_joint_effort', ApplyJointEffort)

	start_time = rospy.Duration.from_sec(0)
	duration = rospy.Duration.from_sec(0.00417)

	rate = rospy.Rate(240)

	with open(filename, 'rb') as csvfile:
		csvfile.readline()
		test_read = csv.reader(csvfile, delimiter=',')

		for data in test_read:

			print(data[5], data[6])
			effort_left = float(data[5])
			effort_right = float(data[6])

			# effort_left = 0.05*row_fl_left
			# effort_right = 0.05*row_fl_right

			try:
				resp1 = (apply_joint_effort('WheelL_cont', effort_left, start_time, duration))
				resp2 = (apply_joint_effort('WheelR_cont', effort_right, start_time, duration))

				rate.sleep()

			except rospy.ServiceException, e:
				print "Service did not process"