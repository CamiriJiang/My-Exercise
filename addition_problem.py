# 读取数据组数
T = int(input())

# 处理每组数据
for _ in range(T):
    # 读取两个整数a和b
    a, b = map(int, input().split())
    # 输出它们的和
    print(a + b)