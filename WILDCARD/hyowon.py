def match(wildcard: str, filename: str) -> bool:
    if not wildcard and not filename:
        return True
    
    if wildcard and not filename:
        if wildcard[0] != "*":
            return False
        return match(wildcard[1:], filename)
    elif not wildcard and filename:
        return False
    else:
        if wildcard[0] == "?": 
            return match(wildcard[1:], filename[1:])
        elif wildcard[0] == "*":
            return match(wildcard, filename[1:]) or match(wildcard[1:], filename)
        else:
            if wildcard[0] != filename[0]:
                return False
            return match(wildcard[1:], filename[1:])

if __name__ == "__main__":
    C = int(input())

    for _ in range(C):
        wildcard = input().strip()
        N = int(input())
        filenames = []
        for _ in range(N):
            filenames.append(input().strip())

        filenames.sort()

        for filename in filenames:
            if match(wildcard, filename):
                print(filename)