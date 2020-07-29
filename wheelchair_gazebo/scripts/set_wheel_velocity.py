#!/usr/bin/env python

import rospkg
import os
import rospy
import csv
import time

rospack = rospkg.RosPack()
pkg_path = rospack.get_path('wheelchair_gazebo')

filename = os.path.join(pkg_path, 'scripts/StraightF_T1_WS64_Mahsa.csv')


def WheelVelControl():
	# initialize node
	rospy.init_node('LeftWheel_AngVel_Pub')	
	rospy.init_node('RightWheel_AngVel_Pub')	

	# start twist publisher
	angvelL_pub = rospy.Publisher('', ..., queue_size = 1)
	angvelR_pub = rospy.Publisher('', ..., queue_size = 1)

	with open(filename, 'rb') as csvfile:
		csvfile.readline()
		data = csv.reader(csvfile, delimiter=',')

		for row in data:
			print(row[1], row[2])
			angvel_L = float(row[1])
			angvel_R = float(row[2]

			# publish twist command to wheelchair
			twist_pub.publish(move_cmd)

			time.sleep(0.004167)

if __name__ == '__main__':
	try:
		WheelVelControl()
	except:
		"There was an error publihing angular velocity messages"