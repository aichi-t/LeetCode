class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums)-1
        while l < r-1:
            mid = (l+r) // 2
            if nums[r] > nums[mid]:
                r = mid
            else:
                l = mid+1
        return min(nums[l], nums[r])


if __name__ == "__main__":
    s = Solution()
    nums = [3, 4, 5, 1, 2]
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    nums3 = [-1]
    nums4 = [3, 4, 0, 1, 2]
    # assert(s.findMin(nums) == 1)
    # assert(s.findMin(nums2) == 1)
    # assert(s.findMin(nums) == 1)
    # assert(s.findMin(nums) == 1)
    # assert(s.findMin(nums) == 1)
    print(s.findMin(nums4))
