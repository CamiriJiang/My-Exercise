import random
import torch
from d2l import torch as d2l
from torch.autograd import backward

def synthetic_data(w, b, num_examples):  #@save
    """生成 y = Xw + b + 噪声"""
    X = torch.normal(0, 1, (num_examples, len(w)))  # normal(均值，标准差，（形状）)
    y = torch.matmul(X, w) + b  # matmul执行矩阵乘法X*w + b
    y += torch.normal(0, 0.01, y.shape)  # 默认噪声服从正态分布N（0，0.01^2），它的形状应该和y一样，因此应该传入y.shape参数
    return X, y.reshape((-1, 1))  # reshape(-1,1)将y变成一个列向量，-1 是一个特殊值，它不是真正的负数，而是一个占位符，意思是"自动推断这个维度的大小"。

true_w = torch.tensor([2, -3.4])
true_b = 4.2
# 自定义w和b来生成1000个样本的数据集
features, labels = synthetic_data(true_w, true_b, 1000)

def data_iter(batch_size, features, labels):
    """数据迭代器:对数据集进行遍历，每次抽取小批量样本，并使用它们来更新模型"""
    num_examples = len(features)
    indices = list(range(num_examples))  # 保证每份样本有不同的索引即给样本编号
    random.shuffle(indices)  # 打乱样本
    for i in range(0, num_examples, batch_size):  # 每次迭代，从数据集中抽取batch_size个样本,共抽取num_examples/batch_size份数据
        batch_indices = torch.tensor(indices[i: min(i + batch_size, num_examples)])
        yield features[batch_indices], labels[batch_indices]  # 利用yield关键字可以保存每次循环的结果

batch_size = 10

# 初始化参数
w = torch.normal(0, 0.01, size=(2, 1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)

def linreg(X, w, b):
    """线性回归模型"""
    return torch.matmul(X, w) + b

def squared_loss(y_hat, y):
    """均方损失"""
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2  # 保证y_hat和y的形状一致很重要

def sgd(params, lr, batch_size):
    """小批量随机梯度下降优化算法,lr是learning_rate"""
    with torch.no_grad():  # 禁用梯度计算
        for param in params:  # 遍历参数，对每个参数进行更新
            if param.grad is not None:
                param -= lr * param.grad / batch_size  # 更新参数
                param.grad.zero_()  # 清零梯度
            else:
                print(f'警告：{param}没有梯度')

lr = 0.03
num_epochs = 3
net = linreg  # 定义网络:线性回归模型
loss = squared_loss  # 定义损失函数:均方损失

for epoch in range(num_epochs):
    for X, y in data_iter(batch_size, features, labels):
        l = loss(net(X, w, b), y)  # 在数据迭代器里面y的形状是（batch_size,1）,并不是一个标量
        l.sum().backward()  # 对标量值执行反向传播，自动计算图中每个节点相对于最终损失的梯度，将计算得到的梯度存储在相应张量的 .grad 属性中
        sgd([w, b], lr, batch_size)
    with torch.no_grad():
        train_l = loss(net(features, w, b), labels)
        print(f'epoch {epoch + 1}, loss {float(train_l.mean()):f}')

print(w.reshape(true_w.shape),'\n',b)
print(f'w的误差为：{true_w - w.reshape(true_w.shape)}') #w.reshape(true_w.shape)很重要，如果形状不匹配的话就会利用广播规则来计算了
print(f'b的误差为：{true_b - b}')
