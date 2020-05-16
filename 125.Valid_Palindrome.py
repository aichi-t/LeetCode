class Solution:
    def isPalindrome(self,s):
        s = list(filter(lambda x: 97 <= ord(x) <= 122 or 48 <= ord(x) <= 57 ,map(lambda y: y.lower(),s)))
        left,right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def isPalindrome2(self, s):
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l <r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1; r -= 1
        return True 

if __name__ == "__main__":
    # s = "appleppa"
    # s = "A man, a plan, a canal: Panama"
    s = ""
    solution = Solution()
    print(solution.isPalindrome(s))