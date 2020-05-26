class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0
        smallest = largest = global_max = nums.pop(0)
        for num in nums:
            s_pro = num * smallest
            l_pro = num * largest
            smallest = min(num, s_pro, l_pro)
            largest = max(num, s_pro, l_pro)
            global_max = max(global_max, largest)
        return global_max


if __name__ == "__main__":
    s = Solution()
    # nums = [2, 3, -2, 4]
    # nums = [-2, 0, -1]
    nums = [-1, 8, -4]
    nums = [-2, 8, -4, -5, -2]
    print(s.maxProduct(nums))
