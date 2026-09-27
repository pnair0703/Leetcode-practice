class Solution:
    def isPalindrome(self, s: str) -> bool:
        #alr kinda cheating off neetcode but the idea is set another function that checks if its alphanumeric which is anything thats a number or letter using ascii val. then do logic myself

        l , r = 0, len(s) - 1
        # i set the function that checks if its alphanumeric, so now how do i check if its palindrome?
        while l < r:
            if not (self.isalphnummy(s[l])):
                l+=1
            elif not self.isalphnummy(s[r]) :
                r-=1
            elif(s[l].lower() != s[r].lower()):
                return False
            else:
                l+=1
                r-=1

        return True

    def isalphnummy(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <=  ord('z') or
        ord('0') <= ord(c) <= ord('9'))
