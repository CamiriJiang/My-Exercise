import torch

# # 设置数据类型和设备
# dtype = torch.float  # 张量数据类型为浮点型
# device = torch.device("cpu")  # 本次计算在 CPU 上进行
# #region[张量]
# # 创建并打印两个随机张量 a 和 b
# a = torch.randn(2, 3, device=device, dtype=dtype)  # 创建一个 2x3 的随机张量
# b = torch.randn(2, 3, device=device, dtype=dtype)  # 创建另一个 2x3 的随机张量
#
# print("张量 a:")
# print(a)
#
# print("张量 b:")
# print(b)
#
# # 逐元素相乘并输出结果
# print("a 和 b 的逐元素乘积:")
# print(a * b)
#
# # 输出张量 a 所有元素的总和
# print("张量 a 所有元素的总和:")
# print(a.sum())
#
# # 输出张量 a 中第 2 行第 3 列的元素（注意索引从 0 开始）
# print("张量 a 第 2 行第 3 列的元素:")
# print(a[1, 2])
#
# # 输出张量 a 中的最大值
# print("张量 a 中的最大值:")
# print(a.max())
#
# # 创建一个 2x3 的全 0 张量
# a = torch.zeros(2, 3)
# print(a)
#
# # 创建一个 2x3 的全 1 张量
# b = torch.ones(2, 3)
# print(b)
#
# # 创建一个 2x3 的随机数张量
# c = torch.randn(2, 3)
# print(c)
#
# # 从 NumPy 数组创建张量
# import numpy as np
# numpy_array = np.array([[1, 2], [3, 4]])
# tensor_from_numpy = torch.from_numpy(numpy_array)
# print(tensor_from_numpy)
#
# # 在指定设备（CPU/GPU）上创建张量
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# d = torch.randn(2, 3, device=device)
# print(d)
# #endregion[]
# #region[常用张量操作]
# # 张量相加
# e = torch.randn(2, 3)
# f = torch.randn(2, 3)
# print(e + f)
#
# # 逐元素乘法
# print(e * f)
#
# # 张量的转置
# g = torch.randn(3, 2)
# print(g.t())  # 或者 g.transpose(0, 1)
#
# # 张量的形状
# print(g.shape)  # 返回形状
#endregion[]
#region[梯度和自动微分]
# 创建一个需要梯度的张量
# tensor_requires_grad = torch.tensor([1.0], requires_grad=True)
#
# # 进行一些操作
# tensor_result = tensor_requires_grad * 2
#
# # 计算梯度
# tensor_result.backward()
# print(tensor_requires_grad.grad)  # 输出梯度
#endregion[]
#region[自动求导]
#自动求导（Automatic Differentiation，简称Autograd）是深度学习框架中的一个核心特性，它允许计算机自动计算数学函数的导数。

#在深度学习中，自动求导主要用于两个方面：一是在训练神经网络时计算梯度，二是进行反向传播算法的实现。

#自动求导基于链式法则（Chain Rule），这是一个用于计算复杂函数导数的数学法则。链式法则表明，复合函数的导数是其各个组成部分导数的乘积。在深度学习中，模型通常是由许多层组成的复杂函数，自动求导能够高效地计算这些层的梯度。

#动态图与静态图：

#动态图（Dynamic Graph）：在动态图中，计算图在运行时动态构建。每次执行操作时，计算图都会更新，这使得调试和修改模型变得更加容易。PyTorch使用的是动态图。

#静态图（Static Graph）：在静态图中，计算图在开始执行之前构建完成，并且不会改变。TensorFlow最初使用的是静态图，但后来也支持动态图。

#PyTorch 提供了自动求导功能，通过 autograd 模块来自动计算梯度。

#torch.Tensor 对象有一个 requires_grad 属性，用于指示是否需要计算该张量的梯度。

#当你创建一个 requires_grad=True 的张量时，PyTorch 会自动跟踪所有对它的操作，以便在之后计算梯度。
# 创建一个需要计算梯度的张量
# x = torch.randn(2, 2, requires_grad=True)
# print(x)
# # 执行某些操作
# y = x + 2
# z = y * y * 3
# out = z.mean()
# print(out)
# # 反向传播，计算梯度
# out.backward()
# # 查看 x 的梯度
# print(x.grad)
#endregion[]
#region[神经网络：nn.Module]
# import torch.nn as nn
# import torch.optim as optim
#
# # 定义一个简单的全连接神经网络
# class SimpleNN(nn.Module): #从nn.Module继承，这是pytorch的基本类
#     def __init__(self):
#         super(SimpleNN, self).__init__()
#         self.fc1 = nn.Linear(2, 2)  # 输入层到隐藏层
#         self.fc2 = nn.Linear(2, 1)  # 隐藏层到输出层
#
#     def forward(self, x):
#         x = torch.relu(self.fc1(x))  # ReLU 激活函数
#         x = self.fc2(x)
#         return x
#
#
# # 创建网络实例
# model = SimpleNN()
#
# # 打印模型结构
# print(model)
# # 随机输入
# x = torch.randn(1, 2)
# # 前向传播
# output = model(x)
# print(output)
# # 定义损失函数（例如均方误差 MSE）
# criterion = nn.MSELoss()
# # 假设目标值为 1
# target = torch.randn(1, 1)
# # 计算损失
# loss = criterion(output, target)
# print(loss)
# # 定义优化器:优化器在训练过程中更新神经网络的参数，以减少损失函数的值（使用 Adam 优化器）
# optimizer = optim.Adam(model.parameters(), lr=0.001)
# # 训练步骤
# optimizer.zero_grad()  # 清空梯度
# loss.backward()  # 反向传播
# optimizer.step()  # 更新参数
#endregion[]

#region[数据集]
import torch
from torch.utils.data import Dataset

# 自定义数据集类
class MyDataset(Dataset):
    def __init__(self, X_data, Y_data):
        """
        初始化数据集，X_data 和 Y_data 是两个列表或数组
        X_data: 输入特征
        Y_data: 目标标签
        """
        self.X_data = X_data
        self.Y_data = Y_data

    def __len__(self):
        """返回数据集的大小"""
        return len(self.X_data)

    def __getitem__(self, idx):
        """返回指定索引的数据"""
        x = torch.tensor(self.X_data[idx], dtype=torch.float32)  # 转换为 Tensor
        y = torch.tensor(self.Y_data[idx], dtype=torch.float32)
        return x, y

# 示例数据
X_data = [[1, 2], [3, 4], [5, 6], [7, 8]]  # 输入特征
Y_data = [1, 0, 1, 0]  # 目标标签

# 创建数据集实例
dataset = MyDataset(X_data, Y_data)

from torch.utils.data import DataLoader

# 创建 DataLoader 实例，batch_size 设置每次加载的样本数量
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# 打印加载的数据
for epoch in range(1):
    for batch_idx, (inputs, labels) in enumerate(dataloader):
        print(f'Batch {batch_idx + 1}:')
        print(f'Inputs: {inputs}')
        print(f'Labels: {labels}')
