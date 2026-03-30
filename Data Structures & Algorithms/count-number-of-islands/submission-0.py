class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()
        islands = 0

        def bfs(j,k):
            q = collections.deque()
            visited.add((j,k))
            q.append((j,k))
            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(len(grid)) and c in range(len(grid[0])) 
                    and grid[r][c] == '1' and (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))              


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] =="1" and (i,j) not in visited:
                    bfs(i, j)
                    islands +=1

        return islands



        