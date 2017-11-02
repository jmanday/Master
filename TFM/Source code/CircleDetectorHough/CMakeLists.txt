# project name
PROJECT(CIRCLE_DETECTOR_HOUGH)

# project name
CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

# find and setup OpenCV for this project
FIND_PACKAGE( OpenCV REQUIRED )

# .cxx sources
SET(CDH_SRCS_CXX
  CircleDetectorHough.cpp
  main.cpp
)

ADD_EXECUTABLE(cdh ${CDH_SRCS_CXX})

TARGET_LINK_LIBRARIES(cdh ${OpenCV_LIBS})
