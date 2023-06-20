project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

find_package(expected REQUIRED CONFIG)

add_executable(example example.cpp)
target_link_libraries(example expected::expected)
set_property(TARGET example PROPERTY CXX_STANDARD 11)
