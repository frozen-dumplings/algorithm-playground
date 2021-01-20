def findNext(visited):
  finished = True
  for i in range(n):
    if visited[i] == False: # if not all(visited):
      finished = False
  if finished:
    return 1

  count = 0
  jjin = 0
  for i in range(n):
    if visited[i] == 0:
      jjin = i
      break
  for j in range(n):
    if visited[jjin] == 0 and visited[j] == 0 and friend[jjin][j]:
      visited[jjin] = visited[j] = 1
      count += findNext(visited)
      visited[jjin] = visited[j] = 0
      
  return count

c = int(input())

for _ in range(c):
  n, m = map(int, input().split())
  friend = [[0 for i in range(n) ] for j in range(n)]
  friendInput = list(map(int, input().split())) # [int(x) for x in input().split()]
  for i in range(m):
    friend[friendInput[2 * i]][friendInput[2 * i + 1]] = 1
    friend[friendInput[2 * i + 1]][friendInput[2 * i]] = 1
  
  visited = [0 for i in range(n)] # [0] * n

  print(findNext(visited))
