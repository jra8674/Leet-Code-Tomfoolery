class Solution(object):
    def majorityElement(nums):
        n = len(nums)
        out = 0
        for num in nums:
            if nums.count(num) > (n/2):
                out = num
                break
        return out

    print(majorityElement([3,2,3]))
    print(majorityElement([2,2,1,1,1,2,2]))
