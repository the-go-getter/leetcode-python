class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        base = 1
        while (base <= n):
            if base == n:
                return True
            else:
                base = base * 2

        return False

if __name__ == '__main__':
    mySol = Solution
    print(mySol.isPowerOfTwo(mySol, 64))