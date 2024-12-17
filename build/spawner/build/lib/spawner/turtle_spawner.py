# #!usr/bin/env python3

# import rclpy
# from rclpy.node import Node
# from turtlesim.srv import Spawn
# import random
# from custom_interfaces.msg import NewTurtlePose
# # from custom_interfaces.msg import PoseList
# class Spawner(Node):
#     def __init__(self):
#         super().__init__("spawner")
#         self.get_logger().info("Spinning spawner node...")
#         self.counter=0
#         self.spawner_client=self.create_client(Spawn,"/spawn")
#         self.spawing_rate=self.create_timer(3.5,self.spawner_callback)
#         self.publisher=self.create_publisher(NewTurtlePose,"poses",10)
#         # self.new_turtle_pose=[]

    
#     def spawner_callback(self):
#         self.counter+=1
#         while not self.spawner_client.wait_for_service(1.0):
#             self.get_logger().warn("Waiting fot the service spawn...")

#         request=Spawn.Request()
#         request.x=random.uniform(0.0,11.0)
#         request.y=random.uniform(0.0,11.0)
#         request.theta=random.uniform(0.0,6.28)
#         request.name=f"turtle_{str(self.counter)}" 
        
#         pose=NewTurtlePose()
#         pose.name=request.name
#         pose.x= request.x
#         pose.y=request.y
#         pose.theta=request.theta
#         # self.new_turtle_pose.append(pose)

#         # new_pose_msg=PoseList()
#         # new_pose_msg.data=self.new_turtle_pose
#         self.publisher.publish(pose)

#         future=self.spawner_client.call_async(request)
#         future.add_done_callback(self.handle_exeception)

    
#     def handle_exeception(self,future):
#         try:
#             response=future.result()
#             self.get_logger().info(f"Spawned {response.name}")
#         except Exception as e:
#             self.get_logger().info(f"Service call failed {e}")



# def main(args=None):
#     rclpy.init(args=args)
#     node=Spawner()
#     rclpy.spin(node)
#     rclpy.shutdown()


# if __name__=="__main__":
#     main()


import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
import random
from custom_interfaces.msg import NewTurtlePose

class Spawner(Node):
    def __init__(self):
        super().__init__("spawner")
        self.get_logger().info("Spinning spawner node...")
        
        # Counter to assign unique names to each turtle
        self.counter = 0

        # Client to call the `/spawn` service for creating new turtles
        self.spawner_client = self.create_client(Spawn, "/spawn")

        # Timer to control the spawning rate (spawns a new turtle every 3.5 seconds)
        self.spawning_rate = self.create_timer(3.5, self.spawner_callback)

        # Publisher to broadcast the newly spawned turtles' poses
        self.publisher = self.create_publisher(NewTurtlePose, "poses", 10)

    def spawner_callback(self):
        """Callback to handle the spawning of new turtles."""
        self.counter += 1  # Increment counter to ensure unique turtle names

        # Wait for the `/spawn` service to become available
        while not self.spawner_client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for the spawn service...")

        # Create a request for the `/spawn` service
        request = Spawn.Request()
        request.x = random.uniform(0.0, 11.0)  # Generate random x-coordinate
        request.y = random.uniform(0.0, 11.0)  # Generate random y-coordinate
        request.theta = random.uniform(0.0, 6.28)  # Generate random orientation (theta)
        request.name = f"turtle_{str(self.counter)}"  # Assign a unique name to the turtle
        
        # Create a NewTurtlePose message to store the new turtle's data
        pose = NewTurtlePose()
        pose.name = request.name
        pose.x = request.x
        pose.y = request.y
        pose.theta = request.theta

        # Publish the new turtle's pose to the `poses` topic
        self.publisher.publish(pose)

        # Call the `/spawn` service asynchronously
        future = self.spawner_client.call_async(request)

        # Set a callback to handle the service's response or exceptions
        future.add_done_callback(self.handle_exception)

    def handle_exception(self, future):
        """Handle the response or exceptions from the spawn service."""
        try:
            response = future.result()
            # Log the name of the successfully spawned turtle
            self.get_logger().info(f"Spawned {response.name}")
        except Exception as e:
            # Log any exceptions that occur during the service call
            self.get_logger().info(f"Service call failed: {e}")

def main(args=None):
    """Main entry point for the spawner node."""
    rclpy.init(args=args)
    node = Spawner()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
