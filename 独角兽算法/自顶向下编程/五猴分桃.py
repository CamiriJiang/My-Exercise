#五猴分桃问题：有n个桃子，5个猴子从这些桃子中分，第一只猴子先吃掉1个再把剩下的均分成5堆再拿走一堆；第二只猴子吃掉1个再把剩下的再均分成5堆再拿走一堆，
#第三只猴子吃掉1个再把剩下的均分成5堆再拿走一堆，第四只猴子吃掉1个再把剩下的均分成5堆再拿走一堆，第五只猴子吃掉1个再把剩下的均分成5堆再拿走一堆，求N
def get_peach(monkeys):
    """根据猴子的数量返回总桃子数"""
    n = 1
    while not dividable(n,monkeys):
        n += 1
    return n
def dividable(n,monkeys):
    for _ in range(monkeys): #_表示无名变量
        n = divide(n,monkeys)
        if n is None:
            return False
    return True

def divide(n,monkeys):
    n -= 1
    if n % monkeys == 0:
        n = (n // monkeys ) * (monkeys - 1)
        return n
    else:
        return None

if __name__ == '__main__':
    print(get_peach(5))
