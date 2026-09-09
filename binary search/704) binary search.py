class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r: #do less tha or equal to r bc lets say the array is hella small and then u calculate mid and gotta go greater so l = mid + 1 and then u cross r that helps u determine ur done searching array. idk just remember less than or equal to r
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
