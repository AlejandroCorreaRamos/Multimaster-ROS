#!/usr/bin/env python

import rospy
from server_bridge.srv import LaunchGoal, LaunchGoalRequest
from sys import argv



def call_launch_goal_service(x, y, robot_name):
    service_name = "/{}/LaunchGoal".format(robot_name)
    rospy.wait_for_service(service_name)
    try:
        launch_goal_service = rospy.ServiceProxy(service_name, LaunchGoal)
        req = LaunchGoalRequest()
        req.goal = [x, y]
        resp = launch_goal_service(req)
        return resp.success, resp.message
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: ")
        return False, str(e)


if __name__ == '__main__':
    if len(argv) < 4:
        print("Usage: rosrun your_package_name your_node_name.py x_value y_value")
        exit(1)

    x_value = float(argv[1])
    y_value = float(argv[2])
    robot_name = argv[3]

    rospy.init_node('launch_goal_client')
    success, message = call_launch_goal_service(x_value, y_value, robot_name)

    if success:
        rospy.loginfo("Service call succeeded.")
    else:
        rospy.logerr("Service call failed")