class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        #ok i initially thot binary search for a second but thats pointless im not tryna find specific num. wb two pointer? increase/decrease left and right by 1 each time if l!=r and if thye do then return false. but na that wudnt work. hashing def the right approach here

        hashh = defaultdict(list)

        for num in nums:
            hashh[num].append(num)
            if len(hashh[num]) > 1:
                return True

        return False
