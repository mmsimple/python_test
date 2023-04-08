# 当前左侧的乘以右侧的
def productExceptSelf(nums):
    length = len(nums)
    left, right, answer = [0] * length, [0] * length, [0] * length

    left[0] = 1
    for i in range(1, length):
        left[i] = left[i-1] * nums[i-1]

    right[length-1] = 1
    for i in reversed(range(length-1)):
        right[i] = right[i+1] * nums[i+1]

    for i in range(length):
        answer[i] = left[i] * right[i]

    print(answer)
    return answer

# nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
productExceptSelf(nums)