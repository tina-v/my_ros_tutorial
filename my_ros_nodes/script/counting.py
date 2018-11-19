#!/usr/bin/env python

# ROS message
# from speakingNumbersNodes import everything
from my_ros_msgs.msg import SpeakingNumber
# rospy 
import rospy


# printing number on console and log

class SpeakingNumberNode(object):
    def __init__(self):
        """
        publishes SpeakingNumber msg through speaking_number topic.
        """
        topic = 'speaking_numbers'
        self.pub = rospy.Publisher(topic, SpeakingNumber,  queue_size=10)
        self.num = 0
        self.name_str = None
        self.rate = None

    def speaking(self):
        """
        starts to count in an 1 hz rate from 0 upwards and publishes it as SpeakingNumber.
        """
        rate = rospy.Rate(1) # speaking rate
        while not rospy.is_shutdown():
            self.num += 1
            self.name_str = "count:" + str(self.num)
            rospy.loginfo(self.num)
            rospy.loginfo(self.name_str)
            self.pub.publish(SpeakingNumber(self.name_str, self.num))
            rate.sleep()

if __name__ == "__main__":
    rospy.init_node('my_ros_node', anonymous=True)
    my_node = SpeakingNumberNode()
    rospy.sleep(1.0) # initial sleep time
    my_node.speaking()
