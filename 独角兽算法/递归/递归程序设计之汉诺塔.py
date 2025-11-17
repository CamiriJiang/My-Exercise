#没明白这个递归逻辑：数学归纳法下，直接假设n=1或n=2和n-1的情况成立，然后编写n是的程序
#前提假设是一次只能移动一个盘？
def hanoi(plates_num, start, mid, end):
    if plates_num == 1:
        # print('move %s = %d 到 %s' % (start, 1, end))
        print(f'把1从{start}移动到{end}')
    else:
        hanoi(plates_num-1,start,end,mid) #直接假设n-1时情况成立
        # print('move %s = %d 到 %s' % (start, plates_num, end))
        print(f'把{plates_num}从{start}移动到{end}')
        hanoi(plates_num-1,mid,start,end)



if __name__ == '__main__':
    hanoi(3, 'A', 'B', 'C')