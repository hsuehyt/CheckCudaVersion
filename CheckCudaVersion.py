import torch

# Check the version of CUDA
cuda_version = torch.version.cuda

print(f"The current CUDA version installed is {cuda_version}.")
