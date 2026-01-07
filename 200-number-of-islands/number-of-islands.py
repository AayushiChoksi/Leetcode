class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def inbound(r,c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r,c):
            if not inbound(r,c):
                return
            if (r,c) in visited:
                return
            if grid[r][c] == '0':
                return

            visited.add((r,c))
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        island_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    island_count += 1
                    dfs(r,c)
        return island_count
        