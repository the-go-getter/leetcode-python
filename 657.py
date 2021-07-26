class Solution:
    def judgeCircle(self, moves: str) -> bool:
        horizontal = 0
        vertical = 0
        for move in moves:
            if move == 'U':
                vertical += 1
            elif move == 'D':
                vertical -= 1
            elif move == 'L':
                horizontal -= 1
            elif move == 'R':
                horizontal += 1
        return (horizontal == 0 and vertical == 0)

if __name__ == '__main__':
    mySol = Solution
    print(mySol.judgeCircle(mySol, "LDRRLRUULRDL"))