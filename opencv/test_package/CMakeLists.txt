project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_library(FFMPEG_avformat_LIBRARY avformat)
find_library(FFMPEG_avcodec_LIBRARY avcodec)
find_library(FFMPEG_avutil_LIBRARY avutil)
find_library(FFMPEG_avdevice_LIBRARY avdevice)
find_library(FFMPEG_avresample_LIBRARY avresample)
find_library(FFMPEG_avutil_LIBRARY avutil)
find_library(FFMPEG_swscale_LIBRARY swscale)

message(${FFMPEG_avformat_LIBRARY})
message(${FFMPEG_avcodec_LIBRARY})
message(${FFMPEG_avutil_LIBRARY})
message(${FFMPEG_avdevice_LIBRARY})
message(${FFMPEG_avresample_LIBRARY})
message(${FFMPEG_avutil_LIBRARY})
message(${FFMPEG_swscale_LIBRARY})

add_executable(example example.cpp)
target_link_libraries(
  example 
  ${CONAN_LIBS} 
  ${FFMPEG_avcodec_LIBRARY} 
  ${FFMPEG_avdevice_LIBRARY} 
  ${FFMPEG_avformat_LIBRARY} 
  ${FFMPEG_avutil_LIBRARY}
  ${FFMPEG_avresample_LIBRARY}
  ${FFMPEG_avutil_LIBRARY}
  ${FFMPEG_swscale_LIBRARY}
)

# CTest is a testing tool that can be used to test your project.
# enable_testing()
# add_test(NAME example
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND example)
