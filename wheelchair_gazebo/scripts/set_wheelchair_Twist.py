#!/usr/bin/env python

import rospkg
import os
import rospy
from geometry_msgs.msg import Twist
import csv
import time

rospack = rospkg.RosPack()
pkg_path = rospack.get_path('wheelchair_gazebo')

filename = os.path.join(pkg_path, 'scripts/StraightF_T1_WS64_Mahsa.csv')


def TwistControl():
	# initialize node
	rospy.init_node('Twist_publisher')	

	# start twist publisher
	twist_pub = rospy.Publisher('/mobile_base_controller/cmd_vel', Twist, queue_size = 1)

	# create twist message, add linear x velocity and angular z velocity
	move_cmd = Twist()

	with open(filename, 'rb') as csvfile:
		csvfile.readline()
		data = csv.reader(csvfile, delimiter=',')

		for row in data:
			print(row[3], row[4])
			lin_vel = float(row[3])
			ang_vel = float(row[4])

			move_cmd.linear.x = lin_vel
			move_cmd.angular.z = ang_vel

			# publish twist command to wheelchair
			twist_pub.publish(move_cmd)

			time.sleep(0.004167)

if __name__ == '__main__':
	try:
		TwistControl()
	except:
		"There was an error publihing twist messages"