
'''
采用0切割办法得到连续1
'''
def findMaxConsecutiveOnes(nums):
    s = ''.join(map(str, nums)).split('0')
    max = 0
    for i in s:
        if max < len(i):
            max = len(i)
    print(max)
    return max

'''
直接算
'''
def findMaxConsecutiveOnes(nums):
    sum = 0
    ans = 0
    for i in nums:
        if i == 1:
            sum += 1
            ans = max(sum, ans)
        else:
            sum = 0
    return ans

nums = [1,0,1,1,0,1]
# nums = [1,1,0,1,1,1]
findMaxConsecutiveOnes(nums)