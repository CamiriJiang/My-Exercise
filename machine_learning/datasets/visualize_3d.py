import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 生成三维数组数据
rng = np.random.default_rng(seed=42)
x3 = rng.integers(10, size=(3, 4, 5))

print("三维数组 x3:")
print(x3)

# 方法1: 分别显示每个"页面"的热力图
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
fig.suptitle('三维数组的热力图可视化')

for i in range(3):
    im = axes[i].imshow(x3[i], cmap='viridis', aspect='auto')
    axes[i].set_title(f'页面 {i+1}')
    axes[i].set_xlabel('列')
    axes[i].set_ylabel('行')
    plt.colorbar(im, ax=axes[i])

plt.tight_layout()
plt.show()

# 方法2: 用3D散点图显示所有值
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# 准备数据
x_coords, y_coords, z_coords = [], [], []
colors = []

for i in range(3):  # 页面
    for j in range(4):  # 行
        for k in range(5):  # 列
            x_coords.append(k)
            y_coords.append(j)
            z_coords.append(i)
            colors.append(x3[i, j, k])

# 绘制3D散点图
scatter = ax.scatter(x_coords, y_coords, z_coords, c=colors, cmap='viridis', s=100)

ax.set_xlabel('列 (Column)')
ax.set_ylabel('行 (Row)')
ax.set_zlabel('页面 (Page)')
ax.set_title('三维数组的3D散点图可视化')

# 添加颜色条
plt.colorbar(scatter)

plt.show()

# 方法3: 显示每个页面的数值表格
fig, axes = plt.subplots(3, 1, figsize=(10, 8))
fig.suptitle('三维数组数值表格')

for i in range(3):
    axes[i].axis('tight')
    axes[i].axis('off')
    table = axes[i].table(cellText=x3[i], loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 1.2)
    axes[i].set_title(f'页面 {i+1}')

plt.tight_layout()
plt.show()