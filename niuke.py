import sys

from sympy.codegen.fnodes import intent_out

from test_three_sum import result


#region[noob6:牛牛学加法]
# num_list = map(int, input().split(' '))
# y = list(num_list)
# print(y[0]+y[1])
#endregion[]

#region[noob7：疫情死亡率]
# temp = map(int,input().split(' '))
# para_list = list(temp)
# death_rate = para_list[1]/para_list[0] * 100
# print(f'{death_rate:.3f}%')
#endregion[]

#region[noob8：计算带余除法]
# for line in sys.stdin:
#     a = line.split()
#     b = map(int, a)
#     z= list(b)
#     result_1 = z[0] // z[1]
#     result_2 = z[0] % z[1]
#     print(f'{result_1} {result_2}')
#endregion[]

#region[noob9：整数的个位]
# for line in sys.stdin:
#     a = line.split()
#     b = [int(x) for x in a]
#     print(b[0]%10)
#endregion[]

#region[noob10：整数的十位]
# x = int(input())
# y = x // 10
# print(y%10)
#endregion[]

#region[noob11：平方根]
# import math
# x = int(input())
# y = math.sqrt(x)
# result = math.floor(y)
# print(result)
#endregion[]

#region[noob12：反向输出一个四位数]
# a = input()
# y = [str(x) for x in a]
# c = y[::-1]
# temp= ''.join(c)
# print(temp)
#endregion[]

#region[noob13：温标转换]
# K = float(input())
# F = (K - 273.15) * 1.8 + 32
# print(f'{F}')
#endregion[]

#region[noob14：绕距]
# import math
# start = input().split()
# destination = input().split()
# start_coord = [int(x) for x in start]
# destination_coord = [int(x) for x in destination]
# d_e = math.sqrt((start_coord[0]-destination_coord[0])** 2 + (start_coord[1]-destination_coord[1])**2)
# d_m = abs(start_coord[0]-destination_coord[0])+abs(start_coord[1]-destination_coord[1])
# dist = abs(d_m-d_e)
# print(dist)
#endregion[]

#region[noob15：求四位数各个数位之和]
# x = input()
# y = [int(x) for x in x]
# r=0
# for i in y:
#     r += i
# print(r)
#endregion[]

#region[noob16：时间转换]
# sec = int(input())
# h = sec // 3600
# m = (sec % 3600) // 60
# s = (sec % 3600) % 60
# print(f'{h} {m} {s}')
#endregion[]

#region[noob17:计算机内存]
# n = int(input())
# x = (n*1024*1024) // 4
# print(x)
#endregion[]

#region[noob18：牛牛学立体]
# a = input().split(' ')
# y = [int(x) for x in a]
# S = (y[0]*y[1]+y[0]*y[2]+y[1]*y[2]) * 2
# V = y[0]*y[1]*y[2]
# print(f'{S}\n{V}')
#endregion[]

#region[noob21：明天星期几]
# d = int(input())
# week = [i for  i  in range(1,8)]
# if d == 7:
#     print(week[0])
# else:
#     print(week[week.index(d) + 1])
#endregion[]

#region[noob24：卡拉兹函数]
# n = int(input())
# if n % 2 == 0 :
#     f = n/2
# else:
#     f = 3*n+1
# print(int(f))
#endregion[]

#region[noob29：多组输入a+b 2]
# T = int(input()) # 输入组数
# for x in range(T):#用循环来表示会输入几行这个思路要学会！！！
#     a,b = map(int,input().split(' ')) #题目暗示了输入两个数字a,b且用空格隔开
#     print(a+b)
#endregion[]

#region[noob30：多组输入a+b 3]
# flag = True
# while flag:
#     a, b = map(int, input().split(' '))
#     if a != 0 and b != 0:
#         print(a+b)
#     else:
#         flag = False
#endregion[]

#region[noob31：素数判断]
# import math
# T = int(input())
# for x in range(T):
#     n = int(input())
#     if n <= 1 :
#         print('No')
#     elif n == 2:
#         print('Yes')
#     elif n % 2 == 0:
#         print('No')
#     else:
#         #假设 n 有一个因数 d，那么 n = d * k，其中 d 和 k 都是大于 1 的自然数。这时候，如果 d 大于 n 的平方根，那么 k 就必须小于 n 的平方根，因为如果 d 和 k 都大于平方根，它们的乘积就会大于 n。所以，如果 n 有一个大于平方根的因数，那么一定有一个小于平方根的因数。
#         # 因此，只要检查到平方根为止，如果没有因数的话，肯定能在这个范围内找到，反之，如果这个范围内没有因数，那么 n 就是素数。
#         for i in range(3,int(math.sqrt(n))+1,2):
#             if n % i == 0:
#                 print('No')
#                 break
#         else:
#             print('Yes')
# endregion#endregion[]

#region[noob32：牛牛学数列]
# n = int(input())
# S = [((-1)**(x-1)) * x for x in range(1,n+1)]
# print(sum(S))
#endregion[]

#region[noob33：牛牛学数列2]
# n = int(input())
# S = [1/x for x in range(1,n+1)]
# print(sum(S))
#endregion[]

#region[noob34：最大的差]
# n = int(input())
# for i in range(n): #表示接收n行输入！这个方法要学会！
#     try:
#         x = input().split(' ')
#         y = [int(i) for i in x]
#         y.sort()
#         print(y[-1]-y[0])
#     except EOFError:
#         # 当遇到文件结束错误时，跳出循环
#         break
#endregion[]

#region[noob35：牛牛学数列4]
# n = int(input())
# s = 0
# for x in range(1,n+1):
#     for i in range(1,x+1):
#         s += i
# print(s)
#endregion[]

#region[noob36：牛牛学数列5之斐波那契数列]
# n = int(input())
# my_list = [1,1]
# for i in range(2,n):
#     my_list.append(my_list[i-1]+my_list[i-2])
# print(my_list[n-1])
#endregion[]

#region[noob37：数位之和]
# n = input()
# if int(n) < 0 :
#     y = abs(int(n))
#     z = str(y) #一定要记住整数不是可迭代对象，而字符串是一个可迭代对象
#     x = [int(i) for i in z]
# else:
#     y= list(n)
#     x =[int(i) for i in y]
# print(sum(x))
#endregion[]

#region[noob38：牛牛数数]
# n = int(input())
# for i in range(1,n+1):
#     if i % 4 != 0 and 4 not in [i for i in str(i)] :
#         print(i)
#endregion[]

#region[noob39：牛牛学数列6]
# n = int(input())
# A = [0,1,1]
# if n == 1:
#     print(A[0])
# elif n == 2 or n == 3:
#     print(A[1])
# else:
#     for i in range(2,n):
#         A.append(A[i]+2*A[i-1]+A[i-2])
# print(A[n-1])
#endregion[]

#region[noob40：二维斐波那契数列：不会！！！]
# def twoD_fibonacci(n, m):
#     MOD = 10 ** 9 + 7
#     # 初始化二维数组
#     dp = [[0] * (m + 1) for _ in range(n + 1)]
#     # 根据递推关系初始化边界条件
#     for i in range(1, n + 1):
#         dp[i][1] = 1
#     for j in range(1, m + 1):
#         dp[1][j] = 1
#     # 填充剩余的二维数组
#     for i in range(2, n + 1):
#         for j in range(2, m + 1):
#             dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD
#
#     return dp[n][m]
# # 读取输入
# n, m = map(int, input().split())
# # 计算并打印结果
# print(twoD_fibonacci(n, m))
#endregion[]

#region[noob41：神秘石像的镜像序列]
# n = input().split(' ')
# r = n[::-1]
# a = ' '.join(r[1:])
# print(a)
#endregion[]

#region[noob42：左侧严格小于计数]
# n = int(input())
# a = input().split(' ')  # 只读取一次输入
# ai = [int(x) for x in a]  # 获取包含n个数字的数组
# b = #endregion[]
# for i in range(n):  # i = 0,1
#     c = 0  # 计数器初始化
#     if i == 0:# 如果i等于0，则当前元素左侧没有元素
#         b.append(str(0))
#         continue
#     for j in ai[:i]:  # 检查当前元素左侧的所有元素 for j in ai[:1]
#         if j < ai[i]:  # 如果左侧元素小于当前元素 ai[0]<ai[1]
#             c += 1
#     b.append(str(c))  # 将计数结果转为字符串添加到列表中
# r = ' '.join(b)  # 用空格连接结果
# print(r)
#endregion[]

#region[noob43：牛牛的数学作业]
# T = int(input())
# for i in range(T): #每张试卷有两行对应输入：试卷上数字的个数和有哪些数字
#     r2 = 0
#     n = int(input()) #第一行输入整数 ,表示试卷上数字的个数及试卷数字列表的长度
#     ai = [int(x) for x in input().split(' ')] #第二行输入n个整数
#     r1 = sum(ai) /  n
#     for x in range(n):
#         r2 += ((ai[x]-r1)**2)/ n
#     print(f'{max(ai)-min(ai)} {r2:.3f}')
#endregion[]

#region[noob44：数组计数维护]
# T  = int(input())
# for i in range(T):
#     S = 0
#     cnt = 0
#     first_line = input().split(' ')
#     n = int(first_line[0])
#     k = int(first_line[1])
#     second_line =  input().split(' ')
#     a = [int(x) for x in second_line]
#     for x in range(1,n+1):
#         if a[x-1] >= k:
#             S += a[x-1]
#         elif a[x-1] == 0 and S >= 1 :
#             S -= 1
#             cnt += 1
#         else:
#             continue
#     print(cnt)
#endregion[]

#region[noob45：记数问题]
#自己的写法，开销太大
# n,x = input().split(' ')#n = 11,x = 1
# n_list = [i for i in range(1,int(n)+1)]#['1','2','3','4','5','6','7','8','9','10','11']
# c = 0
# for i in n_list: #i = 1->i = 2
#     temp = [int(y) for y in str(i)]#temp = [1]->temp = [2]
#     for j in temp:
#         if int(x) == j:
#             c += 1  #c = 1
# print(c)
#优化写法
# n, x = input().split(' ')
# c = 0
# for i in range(1, int(n)+1):
#     # 直接在数字的字符串表示中查找x
#     c += str(i).count(x) #记住count的用法
# print(c)
#endregion[]

#region[noob46：约瑟夫环:不会！！！！]
# n, k, m = map(int, input().split(' '))
# # 创建循环链表，存储人员编号
# people = list(range(n))
# # 当前报数的起始位置（k表示从编号为k的人开始即从第k+1个人开始）
# current_pos = k % n  # 处理k>=n的情况，其实这一步是多余的，因为题目规定了k<n，但是这一步给下面做了启示。
# #当k<n时，k % n = k.由于取余计算可以表示周期中的位置，因此k % n = k（k本来就表示n个人内的位置）。
# # 当队伍中还有超过1个人时继续循环
# while len(people) > 1:
#     # 计算要出队的人的位置
#     # (current_pos + m - 1) % len(people) 是要出队的人的索引
#     # 减1是因为从1开始报数报m个数，索引会增加m-1
#     out_pos = (current_pos + m - 1) % len(people) # (current_pos + m - 1)将列表循环看待即n个人之后又重新回到第一个人，只不过索引是一直往后加的。
#     #因此，用(current_pos + m - 1) 对人数取余可以表示这个索引在这个“环”里的位置索引，这个取余用法很重要
#     people.pop(out_pos)#移出队伍
#     # 更新下一轮报数的起始位置
#     # 由于是圆形结构，故当有一个人出队后，其余所有人的位置都会往前移动一位，因此下一轮开始的位置应该就是出队人的位置。
#     current_pos = out_pos % len(people) #为什么还要取余： 通过 % len(people) 操作，我们可以保证 current_pos 始终在有效的索引范围内 [0, len(people)-1] 内。
#     #和前面的说明一样，当k>=n时，k对n的取余结果是位置编号，当k<n时，k对n的取余结果仍然是k。
# # 输出最后剩下的"大王"编号
# print(people[0])
#endregion[]

#region[noob47：校门外的树:因为对集合不熟悉所以一开始没写出来]
#长度为L的树可以种L+1棵树
# L , M = map(int,input().split(' ')) #输入 500 3
# tree = list(range(L+1))
# left_index = L
# right_index = 0
# temp = set()
# for i in range(M):#(150,300)、(100,200)、(470,471)
#     li , ri = map(int,input().split(' '))#输入 470 471
#     temp = temp.union(set(tree[li:ri+1]))
# print(len(tree)-len(temp))
#endregion[]

#region[noob48：单组_二维数组]
# n, m = map(int, input().split(' '))
# r = []
# for i in range(n):
#     a = [int(i) for i in input().split(' ')]
#     for x in a:
#         r.append(x)
# print(sum(r))
#endregion[]

#region[noob49：上三角矩阵判定]
#这道题用flag来表示只要...就....的情况。光有一个break没办法在满足条件的同时也跳出外层循环
# n = int(input())
# matrix = []
# flag = True
# for i in range(n):
#     row_list = [int(i) for i in input().split(' ')]
#     matrix.append(row_list)
# for row in range(len(matrix[0])): #不严谨的写法 ：row会从0取到每行有多少个数-1。
#     column = 0
#     while column < row:
#         if matrix[row][column] != 0:
#             flag = False
#             break
#         column += 1
# if flag == False:
#     print('NO')
# else:
#     print('YES')
# endregion[]

#region[noob50：矩阵转置:不用Numpy就能实现转置]
# n, m = map(int, input().split(' '))
# matrix = []
# matrix_t = [0]* m
# for row in range(n):
#     row_list = [int(i) for i in input().split(' ')]
#     matrix.append(row_list)
# for column in range(m):
#     temp = []
#     for row in range(n):
#         temp.append(matrix[row][column])
#         matrix_t[column] = temp
# for i in range(m):
#     b= [str(x) for x in matrix_t[i]]
#     a = ' '.join(b)
#     print(a)
#endregion[]

#region[noob51：杨辉三角：不会！]
# n = int(input())
# trangle = []
# for i in range(n):
#     row = [1] * (i+1) #初始化每行的值为1,此时每行已经是一个列表了
#     for j in range(1, i): #排除首尾的1，对每个中间值计算
#         row[j] = trangle[i-1][j-1] + trangle[i-1][j] #即使不用numpy，用列表来表示矩阵的行列也是这样
#     trangle.append(row) #row就是每行计算好之后的列表
# for i in range(n):
#     print(' '.join(map(str,trangle[i])))#输出杨辉三角
#endregion[]

#region[noob52：扫雷：不会！]
# n , m = map(int, input().split(' '))
# matrix = [1] * n
# # 创建一个二维列表（n*m），用于存储矩阵,矩阵每个元素都是空字符
# result = [['' for _ in range(m)] for _ in range(n)]
# # 记录8个方向的偏移量
# directions = [(-1, -1), (-1, 0), (-1, 1),
#               (0, -1),           (0, 1),
#               (1, -1),  (1, 0),  (1, 1)]
# #得到初始矩阵
# for i in range(n):
#     lei = input()
#     lei_1 = [char for char in lei]
#     matrix[i] = lei_1
# # 处理每个位置
# for i in range(n):
#     for j in range(m):
#         # 如果当前位置是雷，直接标记为*
#         if matrix[i][j] == '*':
#             result[i][j] = '*'
#         else:
#             # 统计周围8个方向的雷数
#             count = 0
#             for dx, dy in directions: #好写法！由于directions是元组列表，每个元组都有两个值，所以可以用dx和dy来接收。
#                 ni, nj = i + dx, j + dy #因为i、j分别表示当前位置的行和列，dx和dy仅表示偏移量，因此ni和nj才是要统计的位置坐标
#                 # 检查边界
#                 if 0 <= ni < n and 0 <= nj < m:
#                     # 如果邻格是雷，计数加1
#                     if matrix[ni][nj] == '*':
#                         count += 1
#             result[i][j] = str(count)
# # 输出结果
# for i in range(n):
#     print(''.join(result[i]))
#endregion[]

#region[noob53：年轻人不讲5的]
# s = input()
# s= s.replace('5','*')
# print(s)
#endregion[]

#region[noob54：斗兽棋]
# s1 , s2 = input().split(' ')
# a = ['elephant', 'tiger', 'cat', 'mouse']
# if a.index(s2) - a.index(s1) == 1 :
#     print('win')
# else:
#     if s1 == 'mouse' and s2 == 'elephant':
#         print('win')
#     elif s1 == 'elephant' and s2 == 'mouse':
#         print('lose')
#     elif a.index(s1) - a.index(s2) == 1:
#         print('lose')
#     else:
#         print('tie')
#endregion[]

#region[noob55：添加逗号]
# s = [char for char in input()]
# gap =[ i for i   in range(3,len(s),3)]
# gap = gap[::-1] #关键一步：为了让插入逗号不影响原始索引，所以要倒序插入
# for i in gap:
#     s.insert(-i,',')
# print(''.join(s))
#endregion[]

#region[noob56：BFS]
# s = input().strip()
#
# # 将字符串转换为小写以便不区分大小写比较
# s_lower = s.lower()
#
# # 要查找的目标字符串
# target = "bob"
#
# # 查找"bob"第一次出现的位置
# position = s_lower.find(target)
#
# # 如果找到了，输出位置；否则输出-1
# if position != -1:
#     print(position)
# else:
#     print(-1)
#endregion[]

#region[noob57：凯撒加密]
# n = int(input())
# s = list(input())
# result = []
# word_map = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# for i in s:
#     temp_idx = (word_map.index(i) + n ) % 26
#     password = word_map[temp_idx]
#     result.append(password)
# print(''.join(result))
#endregion[]

#region[noob59：简写单词]
# s = list(input().split(' '))
# result = []
# for i in range(len(s)):
#     word = [char for char in s[i]]
#     result.append(word[0].upper())
# print(''.join(result))
#endregion[]

#region[noob65：一元二次方程]
# class Solution:
#     def judgeSolutions(self, a: int, b: int, c: int) -> bool:
#         delta = b * b - 4 * a * c
#         if delta < 0:
#             return False
#         else:
#             return True
#endregion[]

#region[noob67：求阶乘]
# class Solution:
#     def factorialOfN(self, n: int) -> int:
#         mod = 10 ** 9 + 7
#         if n == 0:
#             return 1
#         else:
#             result = 1
#             for i in range(1, n+1):
#                 result = (result * i) % mod
#             return result
# endregion[]

#region[noob70：两点间的距离]
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
# class Solution:
#     def calculateDistance(self , point_A: Point, point_B: Point) -> float:
#         return ((point_A.x - point_B.x) ** 2 + (point_A.y - point_B.y) ** 2) ** 0.5
# endregion[]

#region[noob71：两直线交点]





















































