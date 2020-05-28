class Solution:
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans


if __name__ == "__main__":

    s = Solution()
    # n = 1010
    # n = 00000010100101000001111010011100
    print(s.reverseBits(n))
