#!/usr/bin/env python

# ROS getStatistics
from std_msgs.msg import String
# from my_ros_msgs import SpeakingNmber
from my_ros_msgs.msg import SpeakingNumber
# importing service GetCount
from my_ros_nodes.srv import GetCountResponse, GetCount
# rospy 
import rospy


#processing msg
def handleStatistics(msg):
#test
    rospy.loginfo(GetCountResponse(countmsgs, firstmsg, lastmsg))

#updates received msgcount, saves information of SpeakingNumber as global variables
def updateCount(msg):
    global firstmsg
    global lastmsg
    global countmsgs

    firstmsg = SpeakingNumber()
    lastmsg = SpeakingNumber()
    countmsgs = 0

    if firstmsg is None: 
        firstmsg = msg
        countmsgs = 1

    countmsgs += 1
    lastmsg = msg

#test    handleStatistics(msg)

#test
#    rospy.loginfo(firstmsg)
#    rospy.loginfo(lastmsg)

#
def getStatistic():
    rospy.init_node('getStatistic_node', anonymous=True)
    sub = rospy.Subscriber("speaking_numbers", SpeakingNumber, updateCount)
    service = rospy.Service("getCount", GetCount, handleStatistics)
# spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    getStatistic()
