#!usr/bin/env python3

import rclpy
from rclpy.node import Node

from turtlesim.msg import Pose
import math
from geometry_msgs.msg import Twist


class Controller(Node):
    def __init__(self):
        super().__init__("contoller")
        self.get_logger().info("Controller is now spinning...")
        self.declare_parameter("x",3)
        self.declare_parameter("y",3)
        self.target_x=self.get_parameter("x").value
        self.target_y=self.get_parameter("y").value
        self.current_pose = None
        self.pose_subscriber=self.create_subscription(Pose,"/turtle1/pose",self.pose_callback,10)
        self.velocity_publisher=self.create_publisher(Twist,"turtle1/cmd_vel",10)
        self.control_timer = self.create_timer(2.0, self.control_loop)

    def pose_callback(self,msg):
        self.current_pose=msg

    def control_loop(self):
        if self.current_pose==None:
            return
        
        distance_error=math.sqrt((self.target_x-self.current_pose.x)**2 + (self.target_y-self.current_pose.y)**2)
        angle_to_target=math.atan2(self.target_y-self.current_pose.y,self.target_x-self.current_pose.x)
        angle_error=angle_to_target-self.current_pose.theta
        angle_error = math.atan2(math.sin(angle_error), math.cos(angle_error))

        # velocity in action

        k_linear=1
        k_angular=1

        twist_msg=Twist()
        if abs(angle_error)>0.03:
            twist_msg.linear.x=0.0
            twist_msg.angular.z=k_angular*angle_error
        elif distance_error>0.3:
            twist_msg.linear.x=k_linear*distance_error
            twist_msg.angular.z=k_angular*angle_error
        else:
            twist_msg.linear.x=0.0
            twist_msg.angular.z=0.0
            self.get_logger().info("Turtle has reached the destination!")
            self.destroy_timer(self.control_timer)

        self.velocity_publisher.publish(twist_msg)





def main(args=None):
    rclpy.init(args=args)
    node = Controller()
    rclpy.spin(node)
    rclpy.shutdown()
    



if __name__=="__main__":
    main()