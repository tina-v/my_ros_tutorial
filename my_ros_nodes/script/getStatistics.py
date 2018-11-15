#!/usr/bin/env python

# ROS getStatistics
from std_msgs.msg import String
# from my_ros_msgs import SpeakingNmber
from my_ros_msgs.msg import SpeakingNumber
# importing service GetCount
from my_ros_nodes.srv import GetCountResponse
# rospy 
import rospy


#processing msg
#def handleStatistics():
#   count = my_ros_nodes.svr.GetCount(lastmsg)
#   rospy.loginfo(firstmsg + lastmsg + count)
#test
#    rospy.loginfo("")

#updatesCount
def updateCount(msg):
    global firstmsg 
    global lastmsg
    firstmsg = SpeakingNumber()
    lastmsg = SpeakingNumber()

    if firstmsg is None: 
        firstmsg = msg

    lastmsg = msg

#test    rospy.loginfo(firstmsg)
#test    rospy.loginfo(lastmsg)

#
def getStatistic():
    rospy.init_node('getStatistic_node', anonymous=True)
    sub = rospy.Subscriber("speaking_numbers", SpeakingNumber, updateCount)
    service = rospy.Service("getCount", GetCountResponse, updateCount)
# spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    getStatistic()
