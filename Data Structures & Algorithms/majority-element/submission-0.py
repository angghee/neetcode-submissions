class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        x = 0
        for num in nums:
            if nums.count(num) > majority:
                majority = nums.count(num)
                x = num
        return x