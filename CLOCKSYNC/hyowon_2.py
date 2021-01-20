# switchs = [[0, 1, 2], # 1 5번째로 결정
#           [3, 7, 9, 11], # 11 1번째로 결정
#           [4, 10, 14, 15], # 10 2번째로 결정
#           [0, 4, 5, 6, 7], # 6 2번째로 결정
#           [6, 7, 8, 10, 12], # 8, 12 1번째로 결정
#           [0, 2, 14, 15], # 0, 2, 14, 15 는 6번째로 결정
#           [3, 14, 15], # 3 5번째로 결정
#           [4, 5, 7, 14, 15], # 7 3번째로 결정
#           [1, 2, 3, 4, 5], # 4, 5 4번째로 결정
#           [3, 4, 5, 9, 13]] # 13 1번째로 결정

moves = [
    [11, [3, 7, 9, 11]],
    [13, [3, 4, 5, 9, 13]],
    [8, [6, 7, 8, 10, 12]],
    [10, [4, 10, 14, 15]],
    [6, [0, 4, 5, 6, 7]],
    [7, [4, 5, 7, 14, 15]],
    [4, [1, 2, 3, 4, 5]],
    [1, [0, 1, 2]],
    [3, [3, 14, 15]],
    [0, [0, 2, 14, 15]]
]

# tmp = [0] * 16
# for switch in switchs:
#     for conn in switch:
#         tmp[conn] += 1
# print(tmp)

# 1번째로 결정: 11[1], {8, 12}[], 13+(9)
# 2번째로 결정: 10, 6
# 3번째로 결정: 7
# 4번째로 결정: {4, 5}
# 5번째로 결정: 1, 3
# 6번째로 결정: {0, 2, 14, 15}

if __name__ == "__main__":
    C = int(input())
    for _ in range(C):
        clocks = list(map(lambda x: int(x) // 3 % 4, input().strip().split()))
        
        cnt = 0
        for move in moves:
            while clocks[move[0]] != 0:
                cnt += 1
                for i in move[1]:
                    clocks[i] = (clocks[i] + 1) % 4

        solved = True
        for clock in clocks:
            if clock != 0:
                solved = False
                break
        
        if solved:
            print(cnt)
        else:
            print(-1)
