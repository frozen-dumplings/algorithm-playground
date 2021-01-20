switchs = [[0, 1, 2],
          [3, 7, 9, 11], # 11은 여기만
          [4, 10, 14, 15],
          [0, 4, 5, 6, 7],
          [6, 7, 8, 10, 12], # 8, 12는 여기
          [0, 2, 14, 15],
          [3, 14, 15],
          [4, 5, 7, 14, 15],
          [1, 2, 3, 4, 5],
          [3, 4, 5, 9, 13]] # 13은 여기만

tmp = [0] * 16
for switch in switchs:
    for conn in switch:
        tmp[conn] += 1
print(tmp)

minCount = 1234567890

def dfs(clocks, switchIndex, cnt):
    global minCount
    if cnt >= minCount:
        return 1234567890

    solved = True
    for clock in clocks:
        if clock != 0:
            solved = False
            break

    if solved:
        return cnt

    if switchIndex == 10:
        return 1234567890

    ret = 1234567890
    for i in range(4):
        ret = min(ret, dfs(clocks, switchIndex + 1, cnt + i))
        minCount = ret
        for j in switchs[switchIndex]:
            clocks[j] = (clocks[j] + 1) % 4

    return ret

if __name__ == "__main__":
    C = int(input())
    for _ in range(C):
        clocks = list(map(lambda x: int(x) // 3 % 4, input().strip().split()))
        # CLOCKS = [(int(x) // 3) % 4 for x in input().split()]
        ret = dfs(clocks, 0, 0)
        
        if ret == 1234567890:
            print(-1)
        else:
            print(ret)

