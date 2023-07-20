project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

find_package(flycapture2 REQUIRED)

list(APPEND libraries
    "flycapture2::flycapture2"
)

add_executable(example example.cpp)
target_link_libraries(example PRIVATE ${libraries})
