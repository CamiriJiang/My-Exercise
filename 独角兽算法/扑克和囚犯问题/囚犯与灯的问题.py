import numpy as np
def prison(prisoners):
    turn_on = [False] * prisoners
    monitor = prisoners - 1
    turn_on[-1] = True #不管首次出去的人是谁，都将其视为monitor出去
    num = 1 #monitor负责开关灯，故他肯定是会开过灯，因此num从1开始
    lamp = False #假设一开始灯是灭的
    while num < prisoners:
        lamp,num = select(prisoners,turn_on,monitor,lamp,num)
        print(turn_on)
    print('所有囚犯都出去过')

def select(prisoners,turn_on,monitor,lamp,num):
    lucky_one = np.random.randint(0,prisoners)
    print(f'此次出去的人是：{lucky_one}')
    if lucky_one == monitor:
        if  lamp :
            num += 1
            lamp = False
        else:
            pass
    else:
        if lamp: #如果灯是亮的，只要出去的人不是monitor则什么也不做
            pass
        else: #如果灯是灭的
            if not turn_on[lucky_one]:#判断幸运儿是首次出去
                lamp = True
                turn_on[lucky_one] = True
            else : #如果幸运儿不是首次出去则什么也不做
                pass
    return lamp,num

if __name__ == '__main__':
    prison(4)