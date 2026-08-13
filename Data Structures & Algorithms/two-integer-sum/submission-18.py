class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we know the number we need to get to the target based on every number we have, now we will 
        # add the element we are checking to the output list, 
        # find if the right number index we append it to the output list
        # otherwise we clear the list and try the next element 
        output = []
        position = -1;
        for i in range(len(nums)):
            output.clear()
            output.append(i)
            diff = target - nums[i]
            try: 
                position = nums.index(diff,i+1)
                output.append(position)
                return output
            except ValueError:
                continue
                

                
                    

        