#求20以内任意两个整数的最大公因数——辗转相除法
def gcd(a,b):
    """
    自动算20以内任意数的
    """
    for a in range(1,21):
        for b in range(1,21):
            a = abs(a)
            b = abs(b)
            if a < b :
                 a , b = b , a
            while b != 0:
                a = b
                b = a % b
    return a

if __name__ == '__main__':
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    print('最大公约数是：', a)
