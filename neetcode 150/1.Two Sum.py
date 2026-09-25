class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #HASH MAP IS THE RIGHT SOLUTION

        hashh = {}

        for i, num in enumerate(nums):
            bang = target - num
            if bang in hashh:
                return (hashh[bang], i)
            else:
                hashh[num] = i
                #this is just saying like since u didnt find the complement then ur gonna have to update ur hashmap. so u add that number to hashmapp and set it to i for the index
