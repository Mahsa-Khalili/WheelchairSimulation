#!/usr/bin/env python

import rospkg
import os
import rospy
from std_msgs.msg import Float64
import csv
import time

rospack = rospkg.RosPack()
pkg_path = rospack.get_path('wheelchair_gazebo')
filename = os.path.join(pkg_path, 'scripts/StraightF_T1_Experiment_Ref.csv')

def EffortControl():
	# initialize node
	rospy.init_node('effort_publisher')	

	# advertise effort publisher
	effort_left_pub = rospy.Publisher('/WheelL_effort_controller/command', Float64, queue_size = 1)
	effort_right_pub = rospy.Publisher('/WheelR_effort_controller/command', Float64, queue_size = 1)

	# setting publishing rate in Hz
	rate = rospy.Rate(240)

	with open(filename, 'rb') as csvfile:
		csvfile.readline()
		data = csv.reader(csvfile, delimiter=',')
		# rowcount = sum(1 for row in data)
		# print(rowcount)
		
		for row in data:
			# print(row[5], row[6])
			left_torque = float(row[5])
			right_torque = float(row[6])

			# publish twist command to wheelchair
			effort_left_pub.publish(left_torque)
			effort_right_pub.publish(right_torque)

			rate.sleep()

		left_torque = 0.0
		right_torque = 0.0

		while not rospy.is_shutdosn():
			effort_left_pub.publish(left_torque)
			effort_right_pub.publish(right_torque)
			rate.sleep()

if __name__ == '__main__':
	try:
		EffortControl()
	except:
		"There was an error publihing twist messages"