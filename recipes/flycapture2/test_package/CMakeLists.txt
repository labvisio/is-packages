project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_path(FLYCAPTURE_INCLUDE_DIRS 
 NAMES 
  FlyCapture2.h
 PATH_SUFFIXES
  flycapture
)
message("!! FLYCAPTURE HEADERS=${FLYCAPTURE_INCLUDE_DIRS}")

add_executable(example example.cpp)
target_link_libraries(example ${CONAN_LIBS})
include_directories(example ${FLYCAPTURE_INCLUDE_DIRS})
set_property(TARGET example PROPERTY CXX_STANDARD 11)