class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(row, col):
            directions = [[0,1], [0,-1],[1,0],[-1,0]]
            curr = 1
            q = deque()
            q.append((row,col))

            while q:
                r1, c1 = q.pop()
                
                for dr, dc in directions:
                    r, c = r1+dr, c1+dc
                    if (r<rows and c<cols and r>=0 and c>=0 and grid[r][c] == 1 
                and (r,c) not in visited):
                        visited.add((r,c))
                        q.append((r,c))
                        curr +=1
                        
            return curr


        for r in range(rows):
            for c in range(cols):
                if (r<rows and c<cols and r>=0 and c>=0 and grid[r][c] == 1 
                and (r,c) not in visited):
                    visited.add((r,c))
                    curr1 = bfs(r,c)
                    area = max(area, curr1)
        
        return area