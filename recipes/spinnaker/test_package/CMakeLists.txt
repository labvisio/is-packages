project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_path(SPINNAKER_INCLUDE_DIRS 
 NAMES 
  Spinnaker.h
 PATH_SUFFIXES
  spinnaker
)
message("!! SPINNAKER HEADERS=${SPINNAKER_INCLUDE_DIRS}")
  
# find_library(SPINNAKER_LIBRARY 
#  NAMES 
#   Spinnaker
# )
# message("!! SPINNAKER LIBRARY=${SPINNAKER_LIBRARY}")

add_executable(example example.cpp)
target_link_libraries(example ${CONAN_LIBS})
include_directories(example ${SPINNAKER_INCLUDE_DIRS})
set_property(TARGET example PROPERTY CXX_STANDARD 11)
