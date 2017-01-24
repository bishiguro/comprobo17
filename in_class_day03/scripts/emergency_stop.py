#!/usr/bin/env python

from neato_node.msg import Bump
from geometry_msgs.msg import Twist

import rospy

pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1)

def bump_stop(msg):
	if (msg.leftFront or msg.rightFront or msg.leftSide or msg.rightSide):
		print "Bump!"

		twist = Twist()
		twist.linear.x = 0; 
		twist.linear.y = 0; 
		twist.linear.z = 0;
		
		twist.angular.x = 0; 
		twist.angular.y = 0; 
		twist.angular.z = 0;
		
		pub.publish(twist)

rospy.init_node('emergency_stop')

rospy.Subscriber('/bump', Bump, bump_stop)

r = rospy.Rate(20)
while not rospy.is_shutdown():
	r.sleep()