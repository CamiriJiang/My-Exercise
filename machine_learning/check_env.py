import torch
from d2l import torch as d2l

print("=== PyTorch 环境配置检查 ===")
print(f"PyTorch 版本: {torch.__version__}")
print(f"CUDA 可用: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"CUDA 版本: {torch.version.cuda}")
    print(f"GPU 数量: {torch.cuda.device_count()}")
    print(f"当前 GPU: {torch.cuda.get_device_name(0)}")

print("\n=== d2l 包导入检查 ===")
try:
    import d2l.torch as d2l_torch
    print("✓ d2l.torch 导入成功")
except Exception as e:
    print(f"✗ d2l.torch 导入失败: {e}")

print("\n=== 基本功能测试 ===")
# 测试张量创建
x = torch.randn(3, 4)
print(f"随机张量创建: {x.shape}")

# 测试数据加载器
from torch.utils.data import DataLoader, TensorDataset
data = torch.randn(10, 3)
labels = torch.randint(0, 2, (10,))
dataset = TensorDataset(data, labels)
dataloader = DataLoader(dataset, batch_size=2)
print("DataLoader 创建成功")

# 测试简单的神经网络
model = torch.nn.Linear(3, 1)
print(f"线性层创建成功: {model}")

# 测试优化器
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
print("优化器创建成功")

# 测试损失函数
loss_fn = torch.nn.BCEWithLogitsLoss()
print("损失函数创建成功")

print("\n=== 环境配置完成 ===")
print("您现在可以开始使用李沐老师的《动手学深度学习》PyTorch版本进行学习了！")