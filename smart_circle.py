#!/usr/bin/env python3
import rospy
# import _thread
import threading
# TODO: Include the appropriate library for sending Twist messages.
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


# class sensor():
class sensor(threading.Thread):



    def __init__(self):
        self.distance=[]
        rospy.init_node(name="listener")
        rospy.Subscriber(name="front/scan",
                        data_class=LaserScan,
                        queue_size=100,
                        callback=self.setdistance)
    
    def setdistance(self, data):
        self.distance=data.distance    


class motion():
    def __init__(self):
        rospy.init_node(name='husky_controller')
        # TODO: Create a publisher that publishes to husky_velocity_controller/cmd_vel topic.
        self.pub = rospy.Publisher(name="husky_velocity_controller/cmd_vel", 
                            dataclass=Twist, 
                            queue_size=100)
        self.rate = rospy.Rate(10)  # 10hz

    def circle(self):
        # Allows the publisher to publish at 10 Hz.
        

        # TODO: Make Husky move in circles by publishing to husky_velocity_controller/cmd_vel topic.
        msg = Twist()
        msg.linear.x = 1.0
        msg.angular.z = 1.0
        self.pub.publish(msg)
        self.rate.sleep()

    def stop(self):
        msg = Twist()
        self.pub.publish(msg) #published a Twist msg with all zeros
        self.rate.sleep()



if __name__ == '__main__':
    try:
        # _thread.start_new_thread(sensor)

        while not rospy.is_shutdown():
            if len([dist for dist in sensor.distances if dist<1]) > 0:
                motion.stop()
            else:
                motion.circle()
    except rospy.ROSInterruptException:
        pass