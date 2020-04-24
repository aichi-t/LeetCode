def isValid(s):
    stack = []
    right = {')': '(', ']': '[', '}': '{'}
    for bracket in s:
        if bracket not in right:
            stack.append(bracket)
        else:
            if not stack:
                return False
            popped = stack.pop()
            if right[bracket] != popped:
                return False
    return stack == []


if __name__ == "__main__":
    s = "(){()}[]"
    print(isValid(s))
