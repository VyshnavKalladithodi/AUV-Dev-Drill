#!/usr/bin/env python
import rospy
from chat2.msg import usermsg

rospy.init_node('talker')
pub = rospy.Publisher('chatter', usermsg)
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    msg = usermsg()
    msg.textmsg = raw_input('Enter your message \n')
    # rospy.loginfo(msg.textmsg)

    pub.publish(msg)

    rate.sleep()
