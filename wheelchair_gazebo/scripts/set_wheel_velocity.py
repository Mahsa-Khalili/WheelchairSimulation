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

def VelocityControl():
	# initialize node
	rospy.init_node('velocity_publisher')	

	# advertise velocity publisher
	velocity_left_pub = rospy.Publisher('/WheelL_velocity_controller/command', Float64, queue_size = 1)
	velocity_right_pub = rospy.Publisher('/WheelR_velocity_controller/command', Float64, queue_size = 1)

	# setting publishing rate in Hz
	rate = rospy.Rate(240)

	with open(filename, 'rb') as csvfile:
		csvfile.readline()
		data = csv.reader(csvfile, delimiter=',')
		
		for row in data:
			print(row[1], row[2])
			left_vel = float(row[1])
			right_vel = float(row[2])

			# publish twist command to wheelchair
			velocity_left_pub.publish(left_vel)
			velocity_right_pub.publish(right_vel)
			rate.sleep()

		left_vel = 0.0
		right_vel = 0.0

		while not rospy.is_shutdown():
			velocity_left_pub.publish(left_vel)
			velocity_right_pub.publish(right_vel)
			rate.sleep()

if __name__ == '__main__':
	try:
		VelocityControl()
	except:
		"There was an error publihing twist messages"
