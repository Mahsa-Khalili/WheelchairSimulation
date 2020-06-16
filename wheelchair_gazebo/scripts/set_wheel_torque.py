#!/usr/bin/env python

import rospy
import time

from gazebo_msgs.srv import *

if __name__ == '__main__':

	rospy.init_node('set_wheel_torque')

	rospy.wait_for_service('/gazebo/apply_joint_effort')

	time.sleep(10)

	apply_joint_effort = rospy.ServiceProxy('/gazebo/apply_joint_effort', ApplyJointEffort)

	joint_name = 'WheelR_cont'
	effort = 46.0
	start_time = rospy.Duration.from_sec(0)
	duration = rospy.Duration.from_sec(20)

	try:
		resp1 = (apply_joint_effort(joint_name, effort, start_time, duration))

	except rospy.ServiceException, e:
		print "Sercice did not process"