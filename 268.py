from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        size = len(nums)
        for num in nums:
            sum += num

        return int((size * (size + 1) / 2)) - sum

if __name__ == '__main__':
    mySol = Solution
    print(mySol.missingNumber(mySol, [9,6,4,2,3,5,7,0,1]))