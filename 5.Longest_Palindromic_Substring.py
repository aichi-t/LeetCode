def longestPalindrome(s):
    """
    Naiive solution.
    Time complexity : O(N^3) -> O(N^2) substrings to consider and O(N) to check if each substring is a palindrome
    Space complexity: O(1)
    """
    longest = ""
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i:j] == s[i:j][::-1]:
                longest = longest if len(longest) > len(s[i:j]) else s[i:j]
    return longest

def longestPalindrome2(s):
    """
    The idea is that a palindrome can be extended if the left end character and the right end character is the same
    A palindrome can have odd length or even length and for the even length palindrome, the center of the string consists
    of two duplicate characters.

    We can scan the string to see if it can be extended both ways.
    We also need another scan for the even length palindromes.

    Time complexity: O(2N) * O(N) =-> O(N^2)
    Space complexity : O(1)
    """
    if len(s) < 2:
        return s

    longest = ""
    for i in range(len(s)):
        str1 = extendPalindrome(s,i,i)  
        longest = str1 if len(str1) > len(longest) else longest      
        str2 = extendPalindrome(s,i,i+1)
        longest = str2 if len(str2) > len(longest) else longest      
        
    return longest

def extendPalindrome(s,l,r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]


if __name__ == "__main__":  
    
    s = "ddbabdd"
    # print(longestPalindrome(s))    
    print(longestPalindrome2(s))