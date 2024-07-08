#!/usr/bin/env python

import sys
import math
import rospy
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QDoubleSpinBox, QComboBox
from server_bridge.srv import LaunchGoal, LaunchGoalRequest
from sensor_msgs.msg import NavSatFix


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Load UI
        self.load_ui()
        self.gps_msg_robot1 = None
        self.gps_msg_robot2 = None
        # Connect button signal to function
        self.sendButton.clicked.connect(self.send_data)

        # ROS Node initialization
        rospy.init_node('service_interface')
        robot_name = 'robot1'
        service_name = "/{}/LaunchGoal".format(robot_name)
        #rospy.wait_for_service(service_name)
        self.service_client_1 = rospy.ServiceProxy(service_name, LaunchGoal)
        robot_name = 'robot2'
        service_name = "/{}/LaunchGoal".format(robot_name)
        #rospy.wait_for_service(service_name)
        self.service_client_2 = rospy.ServiceProxy(service_name, LaunchGoal)

        rospy.Subscriber("/robot1/gps", NavSatFix, self.cb_robot1_gps)
        rospy.Subscriber("/robot2/gps", NavSatFix, self.cb_robot2_gps)


    def cb_robot1_gps(self, msg):
        self.gps_msg_robot1 = msg
        # print('GPS INFO ROBOT 1')
        # print(msg.latitude)
        # print(msg.longitude)


    def cb_robot2_gps(self, msg):
        self.gps_msg_robot2 = msg
        # print('GPS INFO ROBOT 2')
        # print(msg.latitude)
        # print(msg.longitude)


    def load_ui(self):
        # Setup UI from converted file
        self.setWindowTitle('ROS Service Interface')
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.verticalLayout = QVBoxLayout(self.centralwidget)

        # Load ui attributes from designer
        from ui_main_window import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.centralwidget)
        self.verticalLayout.addWidget(self.ui.centralwidget)

        # Accessing elements from designer file
        self.float1SpinBox = self.ui.float1SpinBox
        self.float2SpinBox = self.ui.float2SpinBox
        self.robotComboBox = self.ui.robotComboBox
        self.sendButton = self.ui.sendButton


    def send_data(self):
        # Create request message
        req = LaunchGoalRequest()
        req.goal = [self.float1SpinBox.value(), self.float2SpinBox.value()]

        # Determine selected robot
        selected_robot = self.robotComboBox.currentText()
        if selected_robot == 'Robot1':
            rospy.loginfo("Robot1")
            client = self.service_client_1
        elif selected_robot == 'Robot2':
            rospy.loginfo("Robot2")
            client = self.service_client_2
        else:
            ## Calculate nearest distance
            if self.gps_msg_robot1 and self.gps_msg_robot2:
                distance_robot1 = haversine(self.gps_msg_robot1.latitude, self.gps_msg_robot1.longitude,
                    req.goal[0], req.goal[1])
                distance_robot2 = haversine(self.gps_msg_robot2.latitude, self.gps_msg_robot2.longitude,
                    req.goal[0], req.goal[1])
                if distance_robot1 < distance_robot2:
                    client = self.service_client_1
                else:
                    client = self.service_client_2
            else:
                rospy.loginfo("Checking distances error")
                return
            
        resp = client(req)
        rospy.loginfo("Sending goal")

        # Call ROS service
        try:
            resp = self.service_client(req)
            rospy.loginfo("Service call successful")
        except rospy.ServiceException as e:
            rospy.logerr("Service call failed:")



def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    
    # Convertir grados a radianes
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    # Diferencias de las coordenadas
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    
    a = math.sin(dlat / 2)*2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)*2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    distance = R * c
    return distance


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
