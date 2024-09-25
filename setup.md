# Importing VM Automatically

To run VM on Linux departmental machines, the command below runs a bash script that fetches and configures the VM:

`/shared/storage/cs/www/robostar/auro/auro.sh`

Check the ROS environment setup in the VM using the command:

`printenv | grep ROS`

This should output the following:

```
ROS_VERSION=2
ROS_PYTHON_VERSION=3
ROS_DOMAIN_ID=30
ROS_LOCALHOST_ONLY=1 or 0
ROS_DISTRO=humble
```

# Basics

## Creating a Package

Create a workspace and a corresponding `src` directory. Navigate to the `src` folder and run the following to create a package:

`ros2 pkg create --build-type ament_python --license Apache-2.0 [package_name]`


