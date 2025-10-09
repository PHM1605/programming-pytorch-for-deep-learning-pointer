#include <torch/script.h>
#include <iostream>
#include <memory>

int main(int argc, const char* argv[]) {
  torch::jit::script::Module module = torch::jit::load("cnnnet.pt");
  std::cout << "model loaded ok\n";
  // Create a vector of inputs
  std::vector<torch::jit::IValue> inputs;
  inputs.push_back(torch::rand({1,3,224,224}));
  // Forward pass
  at::Tensor output = module.forward(inputs).toTensor();
  std::cout << "Output tensor:\n" << output << std::endl;
  return 0;
}