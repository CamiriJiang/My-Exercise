import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rc('font', size=14)
plt.rc('axes', labelsize=14, titlesize=14)
plt.rc('legend', fontsize=14)
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)

pd.set_option('display.max_columns', None)
# 可以根据需要调整列宽
pd.set_option('display.max_colwidth', None)  # 不限制列宽
pd.set_option('display.width', 1000)  # 调整显示宽度

from sklearn.datasets import fetch_openml
#参数表示不让返回结果以DataFrame形式返回，而是返回numpy数组
mnist = fetch_openml('mnist_784', as_frame=False)

X,y = mnist.data,mnist.target
print(X,X.shape)
def plot_digit(image_data):
    image = image_data.reshape(28,28)
    plt.imshow(image, cmap='binary')
    plt.axis('off')
some_digit = X[0]
plot_digit(some_digit)
# plt.show()
print(y[0])