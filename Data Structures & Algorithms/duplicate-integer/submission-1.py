class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = set()
        for i in range(len(nums)):
            if nums[i] in new:
                return True
            new.add(nums[i])
        return False