project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)

find_package(SimpleAmqpClient REQUIRED)

list(APPEND libraries
    "SimpleAmqpClient::SimpleAmqpClient"
)

add_executable(example example.cpp)
target_link_libraries(example PRIVATE ${libraries})
