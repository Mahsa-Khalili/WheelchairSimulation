# CARIS Wheelchair GAZEBO-ROS Repository
This repository contains three ROS packages: 
## 1. **wheelchair_gazebo**: 
### Launch files:
- **wheelchair.launch**: The main launch file loading gazebo-rviz models
  - loading a XACRO file into the parameter server `<param name = "robot_description" ... >`
  - defining wheelchair's default pose `<arg name = "x_pos" ...>`
  - spawing the urdf robot `<node name="urdf_spawner" ...>`
  - starting gazebo `include file = "$(find gazebo_ros)/launch/empty_world.launch> ...`
  - starting rviz `<node name=rviz ...>`
  - loading *wheelchair_control.launch*
  - converting joint states to TF for rviz `<node name = "robot_state_publisher" ... >`
  - rqt_robot_steering: steering the robot using rqt_robot_steering `<node name = "rqt_robot_steering" ... >`
  - rqt_gui: sending joint position `<node name = "rqt_gui" ... >`
 - **config.rviz**: Default rviz configuration 
  
### gazebo models: 
- This folder contains mesh/config/sdf files of gazebo objects (e.g., ramp)
#### **Python scripts**: This folder contains python scripts (e.g., script to read left/right input torque from a csv file and apply to the left/right wheels.
#### **world files**: This folder contains custom world files
## 2. **wheelchair_description**
- **meshes**: This folder contains .stl filrs of the main wheelchair components
- **urdf**: This folder contains the main urdf.xacro file of the wheelchair
## 3. **wheelchair_control**
- **config**: This folder contains the .yaml controller files
- **launch**: This folder contains the launch file to load controllers
