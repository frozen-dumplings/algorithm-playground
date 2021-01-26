if __name__ == "__main__":
    C = int(input())

    for _ in range(C):
        N = int(input())
        fences = list(map(int, input().strip().split()))
        fences.append(0)
        stack = [(-1, 0)]
        answer = 0

        for i, fence in enumerate(fences):
            height = 100001
            index = i
            while len(stack) > 0 and stack[-1][1] > fence:
                height = min(height, stack[-1][1])
                width = i - stack[-1][0]
                answer = max(answer, height * width)
                index = stack[-1][0]
                stack.pop()

            stack.append((index, fence))

        print(answer)
        # start = 0
        # height = fence[0]
        # area = fence[0]
        # maxArea = area
        # print(start, height, area, maxArea)

        # for i in range(1, len(fence)):
        #     if min(height, fence[i]) * (i - start + 1) >= fence[i]:
        #         height = min(height, fence[i])
        #         area = height * (i - start + 1)
        #     else:
        #         start = i
        #         height = fence[i]
        #         area = fence[i]

        #     maxArea = max(area, maxArea)
        #     print(start, height, area, maxArea)

        # print(maxArea)


