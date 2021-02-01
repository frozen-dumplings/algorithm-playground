if __name__ == "__main__":
    C = int(input())

    for _ in range(C):
        member = "".join(["0" if i == "F" else "1" for i in input().strip()])
        fan = "".join(["0" if i == "F" else "1" for i in input().strip()])

        cnt = 0
        memberBinary = int(member, 2)
        fanBinary = int(fan, 2)
        memberLength = len(member)
        
        for i in range(len(fan) - memberLength + 1):
            if not(memberBinary & fanBinary):
                cnt += 1
            fanBinary >>= 1

        print(cnt)
