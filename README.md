# CARIS Wheelchair GAZEBO-ROS Repository
This repository contains three ROS packages: 
## 1. **wheelchair_gazebo**: 
### Launch files:
- **wheelchair.launch**: The main launch file 
  - loading an XACRO file to the parameter server `<param ... >`
  - defining wheelchair's default pose
  - spawing the urdf robot
  - starting gazebo 
  - starting rviz 
  - loading wheelchair_control.launch
  - converting joint states to TF for rviz
  - rqt_robot_steering: steering the robot using rqt_robot_steering
  - rqt_gui: sending joint position
  
#### **gazebo models**: This folder contains added objects to the gazebo sim (e.g., ramp)
#### **Python scripts**: This folder contains python scripts (e.g., script to read left/right input torque from a csv file and apply to the left/right wheels.
#### **world files**: This folder contains custom world files
## 2. **wheelchair_description**
- **meshes**: This folder contains .stl filrs of the main wheelchair components
- **urdf**: This folder contains the main urdf.xacro file of the wheelchair
## 3. **wheelchair_control**
- **config**: This folder contains the .yaml controller files
- **launch**: This folder contains the launch file to load controllers
