project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

find_package(rabbitmq-c REQUIRED CONFIG)

add_executable(example example.cpp)
if(RABBITMQ_SHARED)
    target_link_libraries(example PRIVATE rabbitmq::rabbitmq)
else()
    target_link_libraries(example PRIVATE rabbitmq::rabbitmq-static)
endif()
