#!/usr/bin/env python

# ROS message
# from my_ros_msgs import speakingNumber
from std_msgs.msg import String
# from speakingNumbersNodes import everything
from my_ros_msgs.msg import speakingNumber
# rospy 
import rospy


# printing number on console and log
def speaking():
    topic = 'speakingNumbers'
    pub = rospy.Publisher(topic, speakingNumber, queue_size=10)
    rospy.init_node('my_ros_node', anonymous=True)
    num = 0
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        num += 1
        name_str = "count:" + str(num)
        rospy.loginfo(num)
        rospy.loginfo(name_str)
        pub.publish(speakingNumber(name_str, num))
        rate.sleep()


if __name__ == "__main__":
        speaking()
