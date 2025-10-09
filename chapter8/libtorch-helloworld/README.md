## Install CUDA 12.6 Toolkit
Remove any old CUDA versions first
```bash
sudo apt remove --purge 'nvidia-cuda-toolkit'
sudo apt autoremove
sudo rm -rf /usr/local/cuda*
```
Download CUDA 12.6 runfile installer
```bash
wget https://developer.download.nvidia.com/compute/cuda/12.6.0/local_installers/cuda_12.6.0_560.28.03_linux.run
sudo sh cuda_12.6.0_560.28.03_linux.run
```
During installation
- Uncheck "Driver"
- Choose only CUDA Toolkit

Verify installation
```bash
ls /usr/local/cuda-12.6/bin/nvcc
/usr/local/cuda-12.6/bin/nvss --version
```
Expected cuda version 12.6 \

Add CUDA to `~./bashrc`
```bash
export PATH=/usr/local/cuda-12.6/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-12.6/lib64:$LD_LIBRARY_PATH
export CUDACXX=/usr/local/cuda-12.6/bin/nvcc
```
Then `source ~/.bashrc`

## Download and extract Libtorch
Download and extract Libtorch 
```bash
https://download.pytorch.org/libtorch/cu126/libtorch-shared-with-deps-2.8.0+cu126.zip
unzip libtorch-shared-with-deps-2.8.0+cu126.zip 
```

## Build
```bash
mkdir build && cd build
cmake -DCMAKE_PREFIX_PATH=/media/phm1605/hddstorage1/Projects/programming-pytorch-for-deep-learning-pointer/libtorch -DCMAKE_CUDA_COMPILER=/usr/local/cuda-12.6/bin/nvcc -DCMAKE_CUDA_ARCHITECTURES=86 ..
make
```

## Run
```bash
./libtorch-helloworld
```