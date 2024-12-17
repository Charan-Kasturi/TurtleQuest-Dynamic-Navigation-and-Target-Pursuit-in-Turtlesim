# **TurtleQuest: Dynamic Navigation and Target Pursuit in Turtlesim**

## **Introduction**

In this project, a simulated turtle robot navigates dynamically toward randomly spawned target turtles in a **ROS2-based Turtlesim environment**. The project demonstrates real-time robot motion control, custom message-based communication, and interaction with services to manage turtles efficiently.

---

## **What Happens in the Project?**

1. **Turtle Spawner** generates turtles at random positions in the Turtlesim simulation environment.  
2. **Main Turtle** navigates towards each spawned target using basic motion control principles.  
3. Once the main turtle reaches a target, the target turtle disappears (killed via a ROS2 service).  
4. The process continues until all turtles have been processed.

---

<div align="center">
  <img src="turtlesim.gif" alt="Turtle Simulation">
</div>


---

## **Dependencies**

Ensure you have the following software and tools installed:

### **1. ROS2 Humble (Ubuntu 22.04)**

Install using the [official ROS2 Humble guide](https://docs.ros.org/en/humble/Installation.html):

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install ros-humble-desktop
```

### **2. Turtlesim**
Install the Turtlesim simulation package:

```bash
sudo apt install ros-humble-turtlesim
```
### **3. Python 3.x**
Ensure Python3 is installed (pre-installed in Ubuntu 22.04).

### **4. Colcon**
Colcon is used for building ROS2 workspaces:

```bash
sudo apt install python3-colcon-common-extensions
```

## **Project Structure**
The project directory contains the following key components:
```bash
turtlesim_project/
│
├── turtlesim.launch.py    # Launch file to start the simulation and nodes
├── spawner/
│   ├── turtle_spawner.py  # Spawns turtles randomly and publishes their positions
│   └── __init__.py
│
├── controller/
│   ├── turtle_controller.py # Controls the main turtle to navigate and kill targets
│   └── __init__.py
│
└── custom_interfaces/
    ├── msg/
    │   └── NewTurtlePose.msg  # Custom message definition for turtle positions
    └── package.xml           # Custom interface package configuration
```

## **Steps to Run the Project**

### **1. Create and Build the Workspace**
#### **Open a terminal and create a new ROS2 workspace:**

```bash
mkdir -p ~/turtlesim_ws/src
cd ~/turtlesim_ws/src
```
#### **Copy the downloaded project files into the src directory:**

```bash
cp -r /path/to/turtlesim_project ~/turtlesim_ws/src/
```
#### **Build the workspace using colcon:**

```bash
cd ~/turtlesim_ws
colcon build
```

#### **Source the workspace setup file:**

```bash
source install/setup.bash
```

#### **Add it permanently to your shell profile so you don't have to source it every time:**

```bash
echo "source ~/turtlesim_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```




### **2. Launch the Project**

#### **Run the launch file to start the simulation, spawner, and controller:**

```bash
ros2 launch turtlesim_project turtlesim.launch.py
```


### 3. **Observe the Simulation**
- **Turtle Spawning:** New turtles will appear at random positions.
- **Main Turtle Navigation:** The main turtle will navigate towards each spawned turtle.
- **Target Kill:** Once the main turtle reaches a target, the target disappears.
