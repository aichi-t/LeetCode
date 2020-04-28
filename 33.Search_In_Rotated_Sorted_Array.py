def search(nums, target):
    # Intuition : O(logN) Binary search. Find the pivot and binary search

    l, r = 0, len(nums)-1

    while l <= r:
        m = (l+r) // 2
        left, right, mid = nums[l], nums[r], nums[m]
        if mid == target:
            return m
        elif left <= mid:
            # Pivot is on the RHS
            if left <= target < mid:
                r = m - 1
            else:
                l = m + 1
        else:
            if mid < target <= right:
                l = m + 1
            else:
                r = m - 1
    return -1


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 8, 0, 1, 2]
    target = 3
    print(search(nums, target))
