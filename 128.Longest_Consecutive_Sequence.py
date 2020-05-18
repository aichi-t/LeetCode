class Solution:
    def longestConsecutive(self,nums):
        longest_streak = 0
        memo = set(nums)
        for num in nums:
            if num-1 not in memo:
                current_num = num
                streak = 1

                while current_num + 1 in memo:
                    current_num += 1
                    streak += 1
                longest_streak = max(longest_streak,streak)

        return longest_streak
if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    # nums = [1,2,0,1]
    # nums = [1,3,5,2,4]
    # nums = [0,3,7,2,5,8,4,6,0,1]
    s = Solution()
    print(s.longestConsecutive(nums))
