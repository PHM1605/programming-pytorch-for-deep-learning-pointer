cmake_minimum_required(VERSION 3.18 FATAL_ERROR)
project(libtorch-helloworld)

find_package(Torch REQUIRED)
add_executable(libtorch-helloworld helloworld.cpp)
target_link_libraries(libtorch-helloworld "${TORCH_LIBRARIES}")
set_property(TARGET libtorch-helloworld PROPERTY CXX_STANDARD 17)
