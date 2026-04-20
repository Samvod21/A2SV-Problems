t = int(input())
ans = []

for _ in range(t):
    n, m = map(int, input().split()) 
    grid = [list(map(int, input().split())) for _ in range(n)] 
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    def dfs(r, c):
        if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == 0 or visited[r][c]:
            return 0
        
        visited[r][c] = True
        volume = grid[r][c]

        volume += dfs(r + 1, c)
        volume += dfs(r - 1, c)
        volume += dfs(r, c + 1)
        volume += dfs(r, c - 1)
        
        return volume

    max_volume = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0 and not visited[i][j]:
                max_volume = max(max_volume, dfs(i, j))
                
    ans.append(max_volume)

for i in ans:
    print(i)