from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld= LaunchDescription()

    turtlesim_sim_node=Node(package="turtlesim",
                        executable= "turtlesim_node",
                        name="simulation"
                        )

    spawner_node=Node(package="spawner",
                      executable="spawn"
                      )
    
    controller_node=Node(package="controller",
                         executable="control"
                         )
    
    ld.add_action(turtlesim_sim_node)
    ld.add_action(spawner_node)
    ld.add_action(controller_node)

    return ld

    