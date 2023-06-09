project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

find_package(prometheus-cpp CONFIG REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example PRIVATE prometheus-cpp::prometheus-cpp)
set_property(TARGET example PROPERTY CXX_STANDARD 11)
