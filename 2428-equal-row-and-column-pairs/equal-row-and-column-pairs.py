class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        ans = 0
        n = len(grid)

        for i in range(n):
            curr_row = grid[i][:]

            for col in range(n):
                curr_col = []

                for el in range(n):
                    curr_col.append(grid[el][col])
                
                if curr_col == curr_row:
                    ans += 1
        
        return ans