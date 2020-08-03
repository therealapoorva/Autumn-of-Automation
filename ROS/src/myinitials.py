#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from time import sleep


pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
rospy.init_node('myinitials',anonymous=True)
vel=Twist()
vel.linear.y=vel.linear.z=0
vel.angular.x=vel.angular.y=0

def loop():
	t0=rospy.Time.now().to_sec()
	while not rospy.is_shutdown():
		pub.publish(vel)
		if rospy.Time.now().to_sec()>1+t0:
			break 

def move(distance):
	vel.linear.x=distance
	vel.angular.z=0
	loop()
	vel.linear.x=0
	pub.publish(vel)

def rotate(angle):
	pi = 3.1415926535897
	vel.linear.x=0
	vel.angular.z=angle*pi/180
        loop()
	vel.angular.z=0
	pub.publish(vel)

def make_a():
	vel.linear.x=0
	vel.angular.z=0
	pub.publish(vel)
	sleep(1)
	rotate(120)
	move(4)
	rotate(120)
	move(4)
	move(-2)
	rotate(120)
	move(2)

if __name__ == '__main__':
	try:
		make_a()
	except rospy.ROSInterruptException: 
		pass


