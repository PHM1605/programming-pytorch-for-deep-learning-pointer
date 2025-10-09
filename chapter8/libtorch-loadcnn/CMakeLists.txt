cmake_minimum_required(VERSION 3.18 FATAL_ERROR)
project(libtorch-loadcnn)

find_package(Torch REQUIRED)
add_executable(libtorch-loadcnn load-cnn.cpp)
target_link_libraries(libtorch-loadcnn "${TORCH_LIBRARIES}")
set_property(TARGET libtorch-loadcnn PROPERTY CXX_STANDARD 17)
