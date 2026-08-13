class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterate through the numbers in the list 
        output = []
        for i in range(len(nums)):
            # thats iterating through all the elements
            # j starts from one after i and loops till the end of the array 
            for j in range(i+1,len(nums)): 
                if nums[i] + nums[j] == target:
                    output.append(i)
                    output.append(j)
                    return output
                    

        