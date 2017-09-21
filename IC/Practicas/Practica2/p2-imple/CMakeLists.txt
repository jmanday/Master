cmake_minimum_required(VERSION 3.6)
project(p2)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES main.cpp Datas.cpp Datas.h Individuo.cpp)
add_executable(p2 ${SOURCE_FILES})