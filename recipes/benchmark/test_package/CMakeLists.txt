project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

find_package(benchmark REQUIRED CONFIG)

add_executable(example example.cpp)
target_link_libraries(example benchmark::benchmark)
set_property(TARGET example PROPERTY CXX_STANDARD 11)
