import numpy as np

class Solution(object):
    def majorityElement(nums):
        nums = np.array(nums)
        n = len(nums)/2
        out = 0
        for num in nums:
            count = (nums == num).sum()
            if count > n:
                out = num
                break
        return out      

    print(majorityElement([3,2,3]))
    print(majorityElement([2,2,1,1,1,2,2]))
