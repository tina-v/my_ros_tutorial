cmake_minimum_required(VERSION 2.8.3)
project(my_ros_nodes)

find_package(catkin REQUIRED COMPONENTS
    message_generation
    my_ros_msgs
    std_msgs
    )


add_service_files(DEPENDENCIES
    my_ros_msgs
    )

generate_messages(DEPENDENCIES
    my_ros_msgs
    )

catkin_package(CATKIN_DEPENDS
    message_runtime
    my_ros_msgs
    std_msgs
    )


catkin_install_python(PROGRAMS
  script/counting.py
  script/getStatistics.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/script
)

