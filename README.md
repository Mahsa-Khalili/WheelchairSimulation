# CARIS Wheelchair GAZEBO-ROS Repository
This repository contains three ROS packages: 
## 1. **wheelchair_gazebo**: 
- **launch**: This folder contains the main launch file to load gazebo-rviz simulators. It also runs the associated controller launch file.
              *wheelchair.launch* 
- **models**: This folder contains added objects to the gazebo sim (e.g., ramp)
- **scripts**: This folder contains python scripts (e.g., script to read left/right input torque from a csv file and apply to the left/right wheels.
- **worlds**: This folder contains custom world files
## 2. **wheelchair_description**
- **meshes**: This folder contains .stl filrs of the main wheelchair components
- **urdf**: This folder contains the main urdf.xacro file of the wheelchair
## 3. **wheelchair_control**
- **config**: This folder contains the .yaml controller files
- **launch**: This folder contains the launch file to load controllers
