from typing import List


class Solution:

    def getCombos(self, digits, keymap, result, position, currentString):
        if (position == len(digits)):
            result.append(currentString)
            currentString = ''
            return

        alphabets = keymap[int(digits[position])]
        for alphabet in alphabets:
            self.getCombos(self, digits, keymap, result, position + 1, currentString + alphabet)

    def letterCombinations(self, digits: str) -> List[str]:
        keymap = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        result = []
        if digits is None or len(digits) == 0:
            return result
        self.getCombos(self, digits, keymap, result, 0, '')
        return result

if __name__ == '__main__':
    mySol = Solution
    print(mySol.letterCombinations(mySol, "23"))