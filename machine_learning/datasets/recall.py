import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
import seaborn
from pathlib import Path
np.set_printoptions(threshold=np.inf, linewidth=1000)
my_array_1 = np.array([[1,2,3,4,5],[2,5,6,8,9]])
my_array_2 = np.empty(10,dtype=int)
my_array_3 = np.random.normal(0,2,(2,5))
my_array_4 = np.random.randint(0,10,(2,5))
my_array_5 = np.arange(0,9,2)
# print(my_array_5)
rng = np.random.default_rng(seed=42)
# 这是一个三维数组，形状为(3, 4, 5)
x3 = rng.integers(10, size=(2, 2, 2))
x4 = rng.integers(5, size=(2, 2, 2))
print(f"三维数组1号:\n{x3}\n 三维数组2号:\n{x4}")
# 堆叠数组
stacked_array = np.dstack([x3, x4])
print(f"堆叠后的数组:\n{stacked_array}")
