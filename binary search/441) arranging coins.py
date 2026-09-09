class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        final = 0
        while l <= r:
            mid = (l+r)//2
            total = ((mid/2)*(mid+1))
            if (total > n):
                r = mid - 1
            else:
                l = mid + 1
                res =  max(mid,final)
        return res
