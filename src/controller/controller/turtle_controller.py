#!usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
import math
from geometry_msgs.msg import Twist
from custom_interfaces.msg import NewTurtlePose
from turtlesim.srv import Kill

class Controller(Node):
    def __init__(self):
        super().__init__("controller")
        self.get_logger().info("Controller is now spinning...")
        
        # Target position for the turtle to move towards
        self.target_x = 0.0
        self.target_y = 0.0

        # Current pose of the turtle
        self.current_pose = None

        # List to store the received target poses
        self.new_poses = []
        
        # Flag to determine whether to prioritize the closest target
        self.closest_flag = True

        # Used to track the index of poses
        self.index = 0

        # Subscribes to the current turtle pose topic
        self.pose_subscriber = self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)
        
        # Subscribes to custom target poses
        self.new_turtle_poses = self.create_subscription(NewTurtlePose, "poses", self.new_poses_callback, 10)

        # Publisher for velocity commands
        self.velocity_publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)

        # Timer for the control loop to ensure the turtle keeps moving toward the target
        self.timer = self.create_timer(0.05, self.control_loop)

        # Service client for killing a turtle once its target is reached
        self.kill_client = self.create_client(Kill, "/kill")

    def pose_callback(self, msg):
        """Callback to update the current pose of the turtle."""
        self.current_pose = msg

    def new_poses_callback(self, msg):
        """Callback to receive and add new target poses to the list."""
        # Convert incoming NewTurtlePose message into a simple list format
        plist = [msg.name, msg.x, msg.y, msg.theta]
        self.new_poses.append(plist)

        # Set the next target if there are poses available
        if self.new_poses:
            self.set_next_target()

    def set_next_target(self):
        """Select the next target based on the closest_flag."""
        if not self.new_poses:
            return  # If there are no poses, do nothing

        if self.closest_flag:
            # Find the closest target based on Euclidean distance
            min_distance = float('inf')
            closest_pose_index = -1

            # Iterate through the list to find the closest pose
            for index, pose in enumerate(self.new_poses):
                distance = math.sqrt((pose[1] - self.current_pose.x) ** 2 + (pose[2] - self.current_pose.y) ** 2)
                if distance < min_distance:
                    min_distance = distance
                    closest_pose_index = index
            
            # Move the closest pose to the front of the list for processing
            closest_pose = self.new_poses.pop(closest_pose_index)
            self.new_poses.insert(0, closest_pose)
            
            # Set the target using the pose at index 0
            self.target_x = self.new_poses[0][1]
            self.target_y = self.new_poses[0][2]
            self.get_logger().info(f"New closest target set: {self.new_poses[0][0]} at ({self.target_x}, {self.target_y})")
        else:
            # If closest_flag is False, simply use the first pose in the list
            self.target_x = self.new_poses[0][1]
            self.target_y = self.new_poses[0][2]
            self.get_logger().info(f"New target set: {self.new_poses[0][0]} at ({self.target_x}, {self.target_y})")

    def control_loop(self):
        """Control loop to navigate the turtle to the current target."""
        if self.current_pose is None or not self.new_poses:
            return  # If there's no pose or targets, do nothing

        # Calculate distance and angle errors
        distance_error = math.sqrt((self.target_x - self.current_pose.x) ** 2 + (self.target_y - self.current_pose.y) ** 2)
        angle_to_target = math.atan2(self.target_y - self.current_pose.y, self.target_x - self.current_pose.x)
        angle_error = angle_to_target - self.current_pose.theta
        angle_error = math.atan2(math.sin(angle_error), math.cos(angle_error))  # Normalize angle error

        # Create a Twist message for velocity commands
        twist_msg = Twist()

        # Control gains for linear and angular velocities
        k_linear = 1.2
        k_angular = 1.2

        # Navigation logic
        if abs(angle_error) > 1:  
            twist_msg.linear.x = k_linear * distance_error
            twist_msg.angular.z = k_angular * angle_error
        elif distance_error > 0.2: 
            twist_msg.linear.x = k_linear * distance_error
            twist_msg.angular.z = k_angular * angle_error
        else:
            # Target is reached
            twist_msg.linear.x = 0.0
            twist_msg.angular.z = 0.0

            # Wait for the kill service to be available
            while not self.kill_client.wait_for_service(1.0):
                self.get_logger().info("Waiting for kill service...")

            # Kill the turtle at the target
            request = Kill.Request()
            request.name = self.new_poses[0][0]  # Use the first pose's name
            future = self.kill_client.call_async(request)
            future.add_done_callback(self.handle_response)

            self.get_logger().info(f"Target reached at ({self.target_x}, {self.target_y})!")
            
            # Remove the completed pose and set the next target
            self.new_poses.pop(0)
            self.set_next_target()

        # Publish the velocity command
        self.velocity_publisher.publish(twist_msg)

        # If no targets remain, stop the timer
        if not self.new_poses:
            self.get_logger().info("All targets have been reached!")
            self.destroy_timer(self.timer)

    def handle_response(self, future):
        """Handle the response from the kill service."""
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().info(f"Service call failed: {e}")


def main(args=None):
    """Main entry point for the controller node."""
    rclpy.init(args=args)
    node = Controller()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
