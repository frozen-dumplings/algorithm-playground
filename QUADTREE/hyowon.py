def parse(quadTreeInput):
    current = quadTreeInput.pop()

    if current == "x":
        tmp = []
        for _ in range(4):
            tmp.append(parse(quadTreeInput))
        return tmp
    else:
        return current
        
def upsideDown(node):
    if type(node) is str: # if node in ['w', 'b'] 난 요렇게함
        return node

    # ret = node[2:] + node[:2]
    # node[0], node[1], node[2], node[3] = node[2], node[3], node[0], node[1] 

    tmp = []
    for i in node:
        tmp.append(upsideDown(i))
    tmp[0], tmp[1], tmp[2], tmp[3] = tmp[2], tmp[3], tmp[0], tmp[1]

    return ''.join(tmp)

def makeOutput(quadTree):
    if type(quadTree) is str:
        return quadTree
    
    ret = "x"

    for node in quadTree:
        ret += makeOutput(node)

    return ret
    

if __name__ == "__main__":
    C = int(input())

    for _ in range(C):
        quadTreeInput = list(reversed(list(input().strip())))
        quadTree = parse(quadTreeInput)
        # print(quadTree)
        upsideDown(quadTree)
        # print(quadTree)
        print(makeOutput(quadTree))
        

        

        


    