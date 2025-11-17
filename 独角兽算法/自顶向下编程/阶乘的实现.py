#求100的阶乘的精确解算法
def fac(n):
    """这个方法的结果位数会非常大，要保存起来非常占用内存，故不能这样写
    """
    result = 1
    for i in range(2,n+1):
        result *= i
    return result

def fac2(n):# n = 3
    """
    优化后的函数
    """
    result = [1]
    for i in range(2,n+1): # i 从2~4取值，循环2次.i = 2
        mul(result,i)         #这个函数的功能应该要和result *= i一样 mul([1],2)
    return to_string(result)#i=2时result = [2]；i=3时result = [6]
def mul(result,a): # mul([1],2)
    """
    这个函数的功能应该要和result *= i一样
    原理：被乘数的每一位与乘数相乘，先对10取余表示结果的个位，对10取整表示进位，再用被乘数的下一位与乘数相乘然后加上上一次的进位，再重复进行对10取余表示结果的个位，对10取整表示进位..
    """
    add = 0
    for i in range(len(result)):
        result[i] *= a # result = [2]
        result[i] += add # result[i] = result[i] + add result = [2]
        add = result[i] // 10 #add = 0
        result[i] %= 10 # result[i] = result[i] % 10 result = [2]
    while add > 0:#add = 0
        result.append(add % 10)
        add //= 10

    return  result

def to_string(result):
    """
    把result转换成字符串
    """
    result.reverse()
    return ''.join(map(str,result))


if __name__ == '__main__':
    for n in range(2,7): #n=3
        print('%d! = %s'%(n,fac2(n)) )


