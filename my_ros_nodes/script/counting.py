#!/usr/bin/env python

# ROS message
# from speakingNumbersNodes import everything
from my_ros_msgs.msg import SpeakingNumber
# rospy 
import rospy


# printing number on console and log
def speaking():
    topic = 'speaking_numbers'
    pub = rospy.Publisher(topic, SpeakingNumber, queue_size=10)
    rospy.init_node('my_ros_node', anonymous=True)
    num = 0
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        num += 1
        name_str = "count:" + str(num)
        rospy.loginfo(num)
        rospy.loginfo(name_str)
        pub.publish(SpeakingNumber(name_str, num))
        rate.sleep()


if __name__ == "__main__":
        speaking()
