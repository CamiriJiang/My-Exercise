from fontTools.qu2cu.qu2cu import Solution
from sympy.solvers.diophantine.diophantine import length


class Solution1(object):
    """
    给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。
    """
    def twoSum(self, nums:list[int], target):
        """
         暴力枚举法
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return print([i, j])
        return  []
    def twoSum_1(self, nums:list[int], target):
        """
        哈希法
        """
        hashtable = {}
        for i, num in enumerate(nums):
 # 如果哈希表中存在 target - num，说明哈希表中存在一个数记为A，使得A+num=target。此时返回A和num的数组下标。
            if target - num in hashtable:
                return print([hashtable[target - num], i])#i表示这个num的下标，hashtable[target - num]表示A的下标
            hashtable[num] = i#将值:索引作为一个键值对存储在字典中
        return  []  # 没有找到，就返回空列表。
import collections
class Solution49(object):
    """
    49. 字母异位词分组
    给定一个字符串数组，将字母异位词组合在一起。字母异位词定义为：字母相同，但排列不同的字符串。

    示例:
    输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
    输出:
    [
    ["ate","eat","tea"],
    ["nat","tan"],
    ["bat"]
    ]
    说明：
    所有输入均为小写字母。
    不考虑答案输出的顺序。
    """
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        排序法，观察最后结果的的共同特征：每个单词组成字母排序完之后是一模一样的，因此可以将其作为字典的key,单词作为对应的value。
        前半部分是自己的写法
        """
        # dic_1 = {}
        # for x in strs:
        #     sorted_x = ''.join(sorted(x))
        #     word_list = []
        #     if sorted_x not in dic_1:
        #         dic_1[sorted_x] = word_list
        #         dic_1[sorted_x].append(x)
        #     else:
        #         dic_1[sorted_x].append(x)
        # return list(dic_1.values())
        if len(strs) < 2:
            return [strs]
        result = {}
        for s in strs:
            #sorted('abc')->['a','b','c']
            # ''.join(['a','b','c'])->'abc'
            #temp='abc'
            temp = ''.join(sorted(s))
            result[temp] = result.get(temp, []) + [s] #get方法的参数是temp，如果temp不存在，则返回一个空列表。空列表+[s]就相当于是result[temp]=[s]
        return result.values()

    def groupAnagrams_1(self, strs: list[str]) -> list[list[str]]:
        """
        用哈希表：利用和独热编码相似的思想对字母进行独热编码。可以观察到字母异位词的特点是每个字母相同且出现的字数相等。
        """
        if len(strs) < 2:
            return [strs]
        result={}
        for s in strs:#["eat","tea","tan"]-> s ='eat'
            count = [0] * 26
            for c in s:#c ='e','a','t'
                count[ord(c)-ord('a')] += 1 #count=[1,0,0,0,1,..,1,...0]
            keys = tuple(count)#keys=(1,0,0,0,1,..,1,...0)，将其变为可哈希对象
            result[keys] = result.get(keys, [])+[s]#result = {count():['eat']}
        return list(result.values())
class Solution128(object):
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        128. 最长连续序列
        给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

        请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

        示例 1：
        输入：nums = [100,4,200,1,3,2]
        输出：4
        解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
        """
#region[自己的解法]
        # if not nums:
        #     return 0
        # num_list=[]
        # for num in nums:
        #     sequence = [num]
        #     while num+1 in nums:
        #         temp_index = nums.index(num+1)
        #         sequence.append(nums[temp_index])
        #         num_list.append(sequence)
        #         num += 1
        # if  num_list  :  #考虑num_list为空的情况很重要：
        #     #例如[0, 0] - 0后面应该是1，但数组中没有1
        #     #没有任何两个数字是连续的，例如[1,5,7]
        #     result = [len(s) for s in num_list]
        #     print(num_list)
        #     return max(result)
        # else:
        #     return 1
#endregion[]
#region[官方解法]
        if not nums: # 考虑nums为空
            return 0
        num_set = set(nums) # 将数组转换为集合，可以去除重复元素，并且在遍历数组时，可以跳过重复元素，让时间复杂度为O（1）
        longest_streak = 0 #初始化最长连续序列长度为0，基本思想和计数器类似，只不过这里看透了“长度”本质是离散化的。

        for num in num_set:
            if num - 1 not in num_set: # 只有当num-1不在集合中时，才说明num是一个新的连续序列的起点。这是代码思路的精华所在！！！！
                # 如果num-1在集合里，则从下面的while可以看出来num在之前说不公已经出现或者已经被放在集合中了
                current_num = num
                current_streak = 1 # 当前连续序列的长度
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak) #这样就避免我自己写时，当nums_list为空或其他特殊情况时，用max()出现错误的问题
        return longest_streak
class Solution283:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        283. 移动零
        给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

        请注意 ，必须在不复制数组的情况下原地对数组进行操作。

        示例 1:
        输入: nums = [0,1,0,3,12]
        输出: [1,3,12,0,0]

        示例 2:
        输入: nums = [0]
        输出: [0]
        """
        for x in nums:
            if x == 0:
                nums.remove(x)
                nums.append(0)
class Solution11:
    def maxArea(self, height: list[int]) -> int:
        """
        11. 盛最多水的容器
        给定一个长度为 n 的整数数组height。有n条垂线，第 i 条线的两个端点是(i, 0)和(i, height[i])。

        找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。——面积最大

        返回容器可以储存的最大水量。

        说明：你不能倾斜容器。
        """
#region[自己的解法:双重for循环]
        # s = []
        # for x,y in  enumerate(height):
        #     for x1,y1 in enumerate(height[x+1:]):
        #         h = min(y,y1)
        #         actual_index = x+x1+1
        #         l = abs(x-actual_index)
        #         s.append(h*l)
        # return max(s)
#endregion[]
        #region[官方解法:使用双指针法优化]
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # 计算当前面积
            h = min(height[left], height[right])
            w = right - left
            current_area = h * w
            # 更新最大面积
            max_area = max(max_area, current_area) #记住这种更新的写法

            # 移动较短的板子，因为这样才能可能找到更大的面积。
            # 双指针的基本做法就是根据某个条件每次只移动一个指针，直到条件不满足，再去移动另一个指针。
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
        #endregion[]
class Solution15:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        15. 三数之和
        给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k即三个nums的不同元素组成一个整数列表
        同时还满足 nums[i] + nums[j] + nums[k] == 0 。->这三个元素相加为0
        请你返回所有和为 0 且不重复的三元组。
        注意：答案中不可以包含重复的三元组。
        """
        nums.sort()
        result = []
        if len(nums) < 3:
            return []
        # 添加提前终止条件：如果数组的最小值大于0或者最大值小于0，则不可能有和为0的三元组
        if nums[0] > 0 or nums[-1] < 0:
            return []
            
        for i in range(len(nums)-2):
            # 避免遍历重复的元素
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # 如果当前数字大于0，则后面的数字都是正数，不可能有和为0的三元组
            if nums[i] > 0:
                break
            left = i + 1
            right = len(nums) - 1
            while left < right:
                three_sum = nums[i]+nums[left]+nums[right]
                if three_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # 检查这个组合是否已经在结果中
                    while left < right and nums[left] == nums[left+1]:
                    #由于数组已经排序，所有相同的元素必然连续排列，此时左指针将右移到下一个不同的元素或左、右指针相遇处，这样处理可以避免添加重复的三元组
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif three_sum > 0:
                    right -= 1
                else:
                    left += 1
        return result




























