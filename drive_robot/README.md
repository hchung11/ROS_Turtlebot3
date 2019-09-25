# Wheeled robot control: Motion
## Use odometry information to determine when to stop the robot!
![](gifFile/turnOn.gif)

This link to script 
https://github.com/hchung11/ROS_Turtlebot3/blob/master/drive_robot/src/Scripts/drive_robot.py
# Usage
``` python
import rospy
import math
import tf.transformations
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from turtlebot3_msgs.msg import SensorState
```
## Set global values
This global values can use in inside method.
Set all this global in method where you want to use
```python 
global poxitionX 
```
Put this on very top
``` python
positionX = 0
odom = Odometry()
msg = Twist()
linearX = 0
PI = math.pi
anglarZ = 0
linearZ = 0
count = 0
addth = 0

```
### Get data from turtlebot
``` python
	#get distance based obn odom
	positionX = int(odom.pose.pose.position.x)
	positionY = int(odom.pose.pose.position.y)
```
### Send data to turlebot
``` python
       	msg.linear.z = linearZ
        msg.linear.x = linearX
        msg.angular.z = anglarZ
        pub = rospy.Publisher('/cmd_vel', Twist, queue_size=30)   #line 45
        pub.publish(msg)
```
# Imporant Code in this assingment
``` python
#instead put angle value on permeter you put angular.z
def turnTo (anglar_Z):
	v_speed_theta = (anglar_Z *360) / (2*PI)
	return v_speed_theta
  
def distanceRobot(distance, x):
	if x == distance:
	return True
```
# How to it work
``` python 

```


