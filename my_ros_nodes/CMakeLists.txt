cmake_minimum_required(VERSION 2.8.3)
project(my_ros_nodes)

find_package(catkin REQUIRED COMPONENTS
    message_generation
    std_msgs
    my_ros_msgs
    )


add_service_files(FILES
    GetCount.srv
    )

generate_messages(DEPENDENCIES
    my_ros_msgs
    )

catkin_package(CATKIN_DEPENDS
    message_runtime
    std_msgs
    )


catkin_install_python(PROGRAMS
  script/counting.py
  script/getStatistics.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/script
)

