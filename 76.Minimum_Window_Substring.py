import collections


def found_target(to_find):
    return to_find == 0


def minWindow(s, t):
    target_count = collections.Counter(t)
    start, end, to_find = 0, 0, len(t)
    min_window = ""

    for end in range(len(s)):

        # If we see the target letter, decrease the number of chars to find
        if target_count[s[end]] > 0:
            to_find -= 1

        # Decrease the target count for the current letter
        target_count[s[end]] -= 1

        # if all leetters in the target are found
        while found_target(to_find):
            window_len = end - start + 1
            if not min_window or window_len < len(min_window):
                min_window = s[start:end+1]

            target_count[s[start]] += 1
            if target_count[s[start]] > 0:
                to_find += 1
            start += 1
    return min_window


if __name__ == "__main__":
    s = "ad0becodebanc"
    t = 'bc'
    # s = "a"
    # t = "a"
    print(minWindow(s, t))
