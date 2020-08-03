#!/usr/bin/env python
import rospy
from tf.transformations import euler_from_quaternion
from sum1.msg import quaternion, euler
import numpy as np

def compute(orientation_q):
	global roll, pitch, yaw
	orientation_list = np.array([orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w])
	(roll, pitch, yaw) = euler_from_quaternion (orientation_list)   
	output_eul= euler()
        output_eul.pitch=pitch
	output_eul.roll=roll
	output_eul.yaw=yaw
	
	pub = rospy.Publisher('topic2', euler, queue_size=10)
        rospy.init_node("my_conversion", anonymous=True)
	rospy.Rate(1).sleep()  # sleep for one second
	
	while not rospy.is_shutdown():
		pub.publish(output_eul)
		rospy.Rate(1).sleep()  # sleep for one second

def listener():	
	rospy.init_node("my_conversion")
	sub= rospy.Subscriber("topic1", quaternion, compute)

if __name__ == '__main__':
	try:
		listener()
	except rospy.ROSInterruptException: 
		pass


