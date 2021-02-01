import random

M, F = map(int, input().split())

print(1)

for i in range(M):
    print(random.choice(['M', 'F']), end='')
print()

for i in range(F):
    print(random.choice(['M', 'F']), end='')
print()

