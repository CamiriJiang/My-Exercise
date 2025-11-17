import torch
from d2l import torch as d2l

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
print("d2l imported successfully")

# 创建一个简单的张量
x = torch.tensor([1, 2, 3])
print("Tensor x:", x)

def A(x):
    return 2 * x
# 测试d2l中的一个简单函数
print("Testing d2l functions...")
y = torch.arange(4, dtype=torch.float32)
print("Tensor y:", y)
if __name__ == '__main__':
    z = A(10)
    m = A(10)**10
    print("A(10):", z,m)