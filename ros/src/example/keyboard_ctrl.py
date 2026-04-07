#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import sys
import select
import termios
import tty

from airsim_ros_pkgs.msg import VelCmd, CarControls

def get_key():

    tty.setraw(sys.stdin.fileno())

    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)

    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

    return key

def main():

    rospy.init_node("keyboard_control")

    global settings
    settings = termios.tcgetattr(sys.stdin)

    # publisher
    drone_pub = rospy.Publisher(
        "/airsim_node/UAV/vel_cmd_body_frame",
        VelCmd,
        queue_size=1)

    car_pub = rospy.Publisher(
        "/airsim_node/Car/car_cmd",
        CarControls,
        queue_size=1)

    vel = VelCmd()
    car = CarControls()

    rate = rospy.Rate(20)

    print("Keyboard Control Start")
    print("-----------------------")
    print("UAV: w s a d f y")
    print("UGV: arrow keys")

    while not rospy.is_shutdown():

        key = get_key()

        # stop
        vel.twist.linear.x = 0
        vel.twist.linear.y = 0
        vel.twist.linear.z = 0
        vel.twist.angular.z = 0

        car.throttle = 0
        car.brake = 1
        car.steering = 0


        # ====================
        # UAV ctrl
        # ====================

        if key == 'w':
            vel.twist.linear.x = 2

        elif key == 's':
            vel.twist.linear.x = -2

        elif key == 'a':
            vel.twist.linear.y = 2

        elif key == 'd':
            vel.twist.linear.y = -2

        elif key == 'f':
            vel.twist.linear.z = -2   # NED frame

        elif key == 'b':
            vel.twist.linear.z = 2   # NED frame

        elif key == 'y':
            vel.twist.angular.z = 1


        # ====================
        # UGV ctrl
        # ====================

        elif key == '8':   # forward
            car.throttle = 0.7
            car.brake = 0
            car.steering = 0

        elif key == '2':   # backward
            car.throttle = -0.7
            car.brake = 0.0
            car.steering = 0.0

        elif key == '4':   # left
            car.throttle = 0.4
            car.steering = -0.4
            car.brake = 0

        elif key == '6':   # right
            car.throttle = 0.4
            car.steering = 0.4
            car.brake = 0

        elif key == '5':   # right
            car.throttle = 0.0
            car.steering = 0.0
            car.brake = 0


        elif key == 'q':
            print("Exit")
            break


        drone_pub.publish(vel)
        car_pub.publish(car)

        rate.sleep()


if __name__ == "__main__":
    main()