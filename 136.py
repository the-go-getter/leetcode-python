from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = set()
        for num in nums:
            if num in result:
                result.remove(num)
            else:
                result.add(num)

        return result.pop()

if __name__ == '__main__':
    mySol = Solution
    print(mySol.singleNumber(mySol, [4,1,2,1,2]))