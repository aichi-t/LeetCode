# Requirements
# Don't use division and O(N)


def productExceptSelf(nums):

    answer = []
    product = 1
    for i in range(len(nums)):
        answer.append(product)
        product *= nums[i]

    product = 1
    for i in range(len(nums)-1, -1, -1):
        answer[i] *= product
        product *= nums[i]

    return answer

    # Time Complexity : O(N)
    # Space Complexity : O(N)
    # left = []
    # right = []
    # current_left = 1
    # for i in range(len(nums)):
    #     if i == 0:
    #         left.append(current_left)
    #     else:
    #         current_left *= nums[i-1]
    #         left.append(current_left)

    # current_right = 1
    # for j in range(len(nums)-1, -1, -1):
    #     if j == len(nums)-1:
    #         right.insert(0, current_right)
    #     else:
    #         current_right *= nums[j+1]
    #         right.insert(0, current_right)

    # return map((lambda x, y: x * y), left, right)


if __name__ == "__main__":

    nums = [1, 2, 3, 4]  # [24,12,8,6]
    # nums = [7, 2, 3, 4]  # [24,84,56,42]

    print(productExceptSelf(nums))
