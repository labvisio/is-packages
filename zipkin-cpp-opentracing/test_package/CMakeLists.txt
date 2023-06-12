project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

find_package(opentracing-cpp REQUIRED CONFIG)
find_package(zipkin-cpp-opentracing REQUIRED CONFIG)

list(APPEND libraries
    "opentracing-cpp::opentracing-cpp"
    "zipkin-cpp-opentracing::zipkin-cpp-opentracing"
)

add_executable(example example.cpp)
target_link_libraries(example PRIVATE ${libraries})
set_property(TARGET example PROPERTY CXX_STANDARD 11)
