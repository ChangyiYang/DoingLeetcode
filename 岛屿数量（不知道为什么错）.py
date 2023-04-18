# https://leetcode.cn/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        
        # 转换为在图中寻找greatest component

        visited = set()

        n = len(grid)
        m = len(grid[0])

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '0':
                    continue
                    
                if (i,j) in visited:
                    continue

                # else, do DFS


                count += 1

                stack = []

                stack.append((i,j))
                visited.add((i,j))


                while stack:
                    i,j = stack.pop()


                    if i != n-1 and grid[i+1][j] == '1' and (i+1, j) not in visited:
                        stack.append((i+1,j))
                        visited.add((i+1,j))
                        

                    if i != 0 and grid[i-1][j] == '1' and (i-1,j) not in visited:
                        stack.append((i-1,j))
                        visited.add((i-1,j))
                    
                    if j != 0 and grid[i][j-1] == '1' and (i, j-1) not in visited:
                        stack.append((i,j-1))
                        visited.add((i,j-1))

                    if j != m-1 and grid[i][j+1] == '1' and (i, j+1) not in visited:
                        stack.append((i,j+1))
                        visited.add((i,j+1))



        return count