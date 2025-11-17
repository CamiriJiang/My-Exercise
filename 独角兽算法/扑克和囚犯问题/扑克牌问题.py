#有一堆牌，取值是1~20无重复，假设抽取第一张是1放到桌子上，将后一张牌放到最后面，抽取第三张牌为2放到桌子上，将后2张牌又放到最后面，抽取第6张为3放到桌子上，将后3张牌放到最后面...
# 共抽20次，最终桌子上的排序是从20到1，求原始牌组次序。
#采用逆向思维来做这道题:由于最后一张牌一定是20，当抽到20时，原数组应该已经调整了19次，（正向调整：依次把前面的牌放到最后；逆向调整：依次把最后的牌放到最前面）...
def get_list(pokes):
    result = [pokes]
    for p in range(pokes-1,0,-1):
        for _ in range(p):
            flip(result)
        result.insert(0,p)
    return result
def flip(result):
    poke = result.pop()
    result.insert(0,poke)
if __name__ == '__main__':
     print(get_list(20))

