def canJump(nums):
    # O(N), O(1) space
    remain, index = nums[0] + 1, 0
    for i in range(len(nums)):
        remain -= 1
        index = i
        remain = max(nums[i], remain)
        if remain == 0:
            break
    return index == len(nums) - 1


def canJump2(nums):
    # Copied from solutions.
    last_pos = len(nums) - 1
    for i in range(len(nums)-1, -1, -1):
        if i + nums[i] >= last_pos:
            last_pos = i
    return last_pos == 0


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 3]
    # nums = [3, 2, 1, 0, 4]
    print(canJump(nums))
    print(canJump2(nums))
