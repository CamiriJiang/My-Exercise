import torch
import torchvision
from torch.utils import data
from torchvision import transforms
from d2l import torch as d2l
from IPython import display
trans = transforms.ToTensor() #totensor的功能是将图像转换为张量，并将值归一化到[0,1]的范围
#FshionMNIST数据集由10个类别的图像组成，每个类别的图像由6000张训练数据集和10000张测试数据集构成。每个输入的图像均为高度（h）28x宽度（w）28的灰度图（通道只有1），其值域为[0,255]。
mnist_train = torchvision.datasets.FashionMNIST(root="../data", train=True, transform=trans, download=True)
mnist_test = torchvision.datasets.FashionMNIST(root="../data", train=False, transform=trans, download=True)

batch_size = 256
train_iter , test_iter = d2l.load_data_fashion_mnist(batch_size)
num_input = 784
num_output = 10
w = torch.normal(0, 0.01, (num_input, num_output), requires_grad=True)# w.shape->(784,10)
b = torch.zeros(num_output, requires_grad=True)# b.shape->(10,)
def softmax(X):
    """实现softmax函数"""
    X_exp = torch.exp(X)
    partitions = X_exp.sum(1, keepdims=True) # 按轴1（行）求和，keepdims=True 保留维度
    return X_exp / partitions
def net(X):
    """实现网络,会得到y_hat的softmax值"""
    return softmax(torch.matmul(X.reshape((-1, w.shape[0])), w) + b) #X.reshape((-1, w.shape[0]))可以保证特征矩阵大小为（sample_number，特征数）-> w的大小为（784，10）因此w.shape[0]表示784