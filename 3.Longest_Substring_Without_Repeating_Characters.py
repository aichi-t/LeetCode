def lengthOfLongestSubstring(s):
    hmap = {}
    start = 0
    longest = 0
    for i,letter in enumerate(s):
        if letter in hmap and start <= hmap[letter]:
            start = hmap[letter] + 1
        else:
            longest = max(longest,i-start + 1)
        hmap[letter] = i
    return longest 

if __name__ == "__main__":
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))