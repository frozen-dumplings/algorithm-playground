if __name__ == "__main__":
    C = int(input())

    for _ in range(C):
        n = int(input())
        inputMap = []
        for _ in range(n):
            inputMap.append(list(map(int, input().strip().split())))
        
        reachable = [[False for i in range(n)] for i in range(n)]

        reachable[0][0] = True

        for i in range(n):
            for j in range(n):
                # print(i, j)
                if reachable[i][j]:
                    if i + inputMap[i][j] < n:
                        reachable[i + inputMap[i][j]][j] = True
                    if j + inputMap[i][j] < n:
                        reachable[i][j + inputMap[i][j]] = True

                # for i in range(n):
                #     print(reachable[i])
                # print()


        if reachable[n - 1][n - 1]:
            print("YES")
        else:
            print("NO")
