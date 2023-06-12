project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

find_package(rabbitmq-c REQUIRED CONFIG)

add_executable(example example.cpp)
target_link_libraries(example PRIVATE rabbitmq-c::rabbitmq-c)
