def search(nums,target):
    for i,n in enumerate(nums):
        if n == target:
            return i
    return -1
nums = [4,5,6,7,0,1,2] 
target = 8
search(nums,target)