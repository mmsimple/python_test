

# def pivotIndex(nums):
#     for i in range(len(nums)):
#       l = nums[:i]
#       r = nums[i+1:]

#       if sum(l) == sum(r):
#         print(i)
#         return i
  
#     return -1



'''
一次遍历，左右两边相等条件为 current_sum + nums[i] = sum - right
current_sum = right
2 * current_sum + nums[i] = sum
'''

# def pivotIndex(nums):
#     sum1 = sum(nums)

#     current_sum = 0
#     for i in range(len(nums)):
#         if 2 * current_sum + nums[i] == sum1:
#             return i
#         current_sum += nums[i]
#     return -1


'''
和上面同理
'''
def pivotIndex(nums):
    left,right=0,sum(nums)
    for i in range(len(nums)):
        left+=nums[i-1] if i>0 else 0
        right-=nums[i]
        if left==right:
            return i
    return -1



# nums = [1, 7, 3, 6, 5, 6]
nums = [1, 2, 3]
s = pivotIndex(nums)
print(s)