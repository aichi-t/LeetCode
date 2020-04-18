def numDecodings(s):
    if not s or s.startswith('0'):
        return 0
    prev, prev_prev = 1, 1
    for i in range(1, len(s)):
        decoded = int(s[i-1:i+1])
        if 0 < < 27 and (decoded != 20 and decoded != 10):
            try:
                print(chr(64+decoded))
                memo += 1
            except:
                continue

    return memo


if __name__ == "__main__":
    s = '10'
    print(numDecodings(s))
