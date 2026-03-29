#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class drawcircleNode(Node):
    def __init__(self):
        super().__init__("draw_circle")
        
        self.cmd_vel_pub_ =self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.timer_=self.create_timer(0.6,self.send_vel_crcl)
        self.get_logger().info("Drawing circle")
    def send_vel_crcl(self):
        msg=Twist()
        msg.linear.x=1.0
        msg.angular.z=1.0
        self.cmd_vel_pub_.publish(msg)
def main(args=None):
    rclpy.init(args=args)
    node=drawcircleNode()
    for i in range(10):
        rclpy.spin_once(node)
    rclpy.shutdown()