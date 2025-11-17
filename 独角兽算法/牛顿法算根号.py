def sqrt(y_hat):
    # y = x^2, dy = 2x
    x = 1
    for _ in range(5):
        x = (y_hat+ x * x)/(x * 2) #delta y = y_hat - y = 2x * delta x -> delta x = delta y / 2x-> x + deltax x = x + (y_hat-y)/2x
    return print(f'{y_hat}的平方根是：{x:.4f}')

if __name__ == '__main__':
    y_hat = float(input('请输入一个正数：'))
    sqrt(y_hat)


#牛顿法有个缺点就是某些情况下在靠近最优解的过程中没有步长概念，容易发生巨幅震荡导致计算机崩溃。即使加入了步长概念，即使依据delta x = delta y / dx这个公式来算deltax也容易在dx无限趋于0时发生错误