import sys


class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = dict()
        for i in range(len(s)):
            if s[i] in letters:
                letters[s[i]] = sys.maxsize
            else:
                letters[s[i]] = i

        result = sys.maxsize
        for letter in letters.keys():
            if letters[letter] < result:
                result = letters[letter]

        return -1 if (result == sys.maxsize) else result


if __name__ == '__main__':
    mySol = Solution
    print(mySol.firstUniqChar(mySol, "loveleetcode"))