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

def EffortVelocityControl():
	# initialize node
	rospy.init_node('effort_velocity_publisher')	

	# advertise effort publisher
	effort_left_pub = rospy.Publisher('/WheelL_effort_controller/command', Float64, queue_size = 1)
	effort_right_pub = rospy.Publisher('/WheelR_effort_controller/command', Float64, queue_size = 1)

	# advertise velocity publisher
	velocity_left_pub = rospy.Publisher('/WheelL_velocity_controller/command', Float64, queue_size = 1)
	velocity_right_pub = rospy.Publisher('/WheelR_velocity_controller/command', Float64, queue_size = 1)

	# setting publishing rate in Hz
	rate = rospy.Rate(240)

	with open(filename, 'rb') as csvfile:
		csvfile.readline()
		data = csv.reader(csvfile, delimiter=',')
		# rowcount = sum(1 for row in data)
		# print(rowcount)
		
		for row in data:
			print(row[1], row[2], row[5], row[6])

			left_vel = float(row[1])
			right_vel = float(row[2])

			left_torque = float(row[5])
			right_torque = float(row[6])

			velocity_left_pub.publish(left_vel)
			velocity_right_pub.publish(right_vel)

			effort_left_pub.publish(left_torque)
			effort_right_pub.publish(right_torque)

			rate.sleep()

		left_torque = 0.0
		right_torque = 0.0

		left_vel = 0.0
		right_vel = 0.0

		while not rospy.is_shutdown():
			velocity_left_pub.publish(left_vel)
			velocity_right_pub.publish(right_vel)

			effort_left_pub.publish(left_torque)
			effort_right_pub.publish(right_torque)
			rate.sleep()

if __name__ == '__main__':
	try:
		EffortVelocityControl()
	except:
		"There was an error publihing twist messages"