class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for index in range(len(nums)):
            if nums[index] in seen:
                return True
            seen.add(nums[index])

        return False