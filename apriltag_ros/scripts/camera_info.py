#! /usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import CameraInfo

rospy.init_node('camera_info', anonymous=True)

pub = rospy.Publisher('/camera_rect/camera_info', CameraInfo, queue_size=10)
rate = rospy.Rate(60)

while not rospy.is_shutdown():
    q = CameraInfo()

    q.header.frame_id = 'usb_cam'
    q.height = 0
    q.width = 0

    q.D = [0.0, 0.0, 0.0, 0.0, 0.0]
    q.K = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
    q.R = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
    q.P = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]

    q.binning_x = 0
    q.binning_y = 0
    q.roi.x_offset = 0
    q.roi.y_offset = 0
    q.roi.height = 0
    q.roi.width = 0
    q.roi.do_rectify = False
    pub.publish(q)
    rate.sleep()
