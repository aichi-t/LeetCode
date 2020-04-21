class Solution:
    def maxArea(self,height):
        l,r = 0, len(height)-1
        max_cap = 0
        loop = True
        while l < r:
            max_cap = max(max_cap,min(height[l],height[r])*(r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_cap

        # while loop:
        #     if height[l] <= height[r]:
        #         for i in range(l,r):
        #             if height[i] > height[l]:
        #                 l = i
        #                 loop = True
        #                 break
        #             loop = False
        #     else:
        #         for j in range(r,l,-1):
        #             if height[j] > height[r]:
        #                 r = j
        #                 loop = True
        #                 break
        #             loop = False
        #     if loop:
        #         max_cap = max((min(height[r],height[l])*(r-l)),max_cap)
        # return max_cap

        

if __name__ == "__main__":
    # height = [3,9,3,4,7,2,12,6]
    height = [1,8,6,2,5,4,8,3,7]
    s = Solution()
    s.maxArea(height)
