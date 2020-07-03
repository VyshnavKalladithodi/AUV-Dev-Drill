#!/usr/bin/env python
import rospy
from chat2.msg import usermsg


def callback(msg):
    print('User Message : ' + msg.textmsg)

def listener():

    rospy.init_node('listener')

    rospy.Subscriber('chatter', usermsg, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':

    listener()
