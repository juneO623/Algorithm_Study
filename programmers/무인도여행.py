def solution(maps:list[str]) -> list[int]:
    answer = []
    maps = list(map(list, maps))

    def dfs(r, c):
        num = 0
        if (r < 0 or c < 0 or r >= len(maps) or c >= len(maps[0]) or maps[r][c] == "X"):
            return 0
        else:
            num += int(maps[r][c])
            maps[r][c] = "X"
            return num + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)
    
    for row in range(len(maps)):
        for col in range(len(maps[0])):
            if maps[row][col] != "X":
                answer.append(dfs(row, col))

    if (len(answer) == 0):
        return [-1]
    
    print(sorted(answer))
    return sorted(answer)

solution(["X591X", "X1X5X", "X231X", "1XXX1"])