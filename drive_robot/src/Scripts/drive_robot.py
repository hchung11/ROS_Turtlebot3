#!/usr/bin/env python
import rospy
import math
import tf.transformations
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from turtlebot3_msgs.msg import SensorState

#global values
positionX = 0
odom = Odometry()
msg = Twist()
linearX = 0
PI = math.pi
anglarZ = 0
linearZ = 0
count = 0
addth = 0


def distanceRobot(distance, x):
	if x == distance:
		return True

#instead put angle value on permeter you put angular.z
def turnTo (anglar_Z):
	v_speed_theta = (anglar_Z *360) / (2*PI)
	return v_speed_theta
	
	
def callback(data):
     rospy.loginfo("%d is age: %s" % (data.id, data.message))


def callbacko(datao):
    
     global odom 
     odom = datao
     rospy.loginfo("x : %d ==== y : %d ===== z : %d" % (datao.pose.pose.position.x, datao.pose.pose.position.y,  datao.pose.pose.position.z))



def listener():
     rospy.init_node('custom_listener', anonymous=True)
     pub = rospy.Publisher('/cmd_vel', Twist, queue_size=30)
     rospy.Subscriber("/odom", Odometry, callbacko)
     r = rospy.Rate(1) #1hz mean every one secound
     


     global linearX
     global anglarZ
     global linearZ
     #speed of turning
     ADDTH= turnTo(0.2)

     while not rospy.is_shutdown():
	r.sleep()
	global count
	global addth
	
	#get distance based obn odom
	positionX = int(odom.pose.pose.position.x)
	positionY = int(odom.pose.pose.position.y)

	#set the final destination
	if distanceRobot(2,int(positionX)) and distanceRobot(2, int(positionY)):
		#if IS reach destination		
		linearX = 0
		print ("done====================================================")
		rospy.is_shutdown()
		break
	 
	else:
		#NOT reach final destination ,Yes, if reached linear.x(X) reach "2"
		if distanceRobot(2,int(positionX)):
			#stop a robot
			linearX = 0
			# less than 90 True
			if  int(addth) <= 90:
				#keep on add until the "addth" reach 90 and will turn 0.2 speed.
				addth += ADDTH
				print ("print add thetha========", addth)
				anglarZ = 0.2
			#NOT reach destination, Yes: reached linear.x , YES: turn 90
			#So keep going stright UNITL reach final destination.
			else:
				anglarZ = 0
				linearX = 0.2
		#NOT reached linear.x(X)	
		else:
			linearX = 0.2

			
	



	
	#print ("SSTTTOP", stop)
	
	global msg
      	msg.linear.z = linearZ
        msg.linear.x = linearX
        msg.angular.z = anglarZ
        pub.publish(msg)
   	# spin() simply keeps python from exiting until this node is stopped
    

if __name__ == '__main__':
     try:

         listener()
     except rospy.ROSInterruptException: pass
