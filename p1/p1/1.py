#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
class P1Node(Node):
    def __init__(self):
        self.cmd_vel_pub_ =self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        super().__init__('p1_node')
        self.create_timer(1,self.timer_callback)
    def send_vel_crcl(self):
        now=self.get_clock().now()
        elapsed_time = (now -self.start_time).nanoseconds / 1e9
        msg=Twist()    
        if elapsed_time< self.timetocircle:
            msg.linear.x=2.0
            msg.angular.z=1.1
        else:
            msg.linear.x=0.0
            msg.angular.z=0.0
        self.timer.cancel()
        self.cmd_vel_pub_.publish(msg)
    def timer_callback(self):
        #self.get_logger().info("Hello world %d" %i)
        self.timer_=self.create_timer(0.1,self.send_vel_crcl)

def main(args=None):
    rclpy.init(args=args) 
    node = P1Node()
    for i in range (1):
        rclpy.spin_once(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()