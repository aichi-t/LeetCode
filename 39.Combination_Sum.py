def combinationSum(candidates, target):
    result = []
    candidates = sorted(candidates)

    def dfs(index, nums, remain):
        if remain == 0:
            result.append(nums)
            return
        for i in range(index, len(candidates)):
            if candidates[i] <= remain:
                dfs(i, nums+[candidates[i]], remain-candidates[i])

    dfs(0, [], target)
    return result


if __name__ == "__main__":

    print(combinationSum([2, 3,  6, 7], 7))
