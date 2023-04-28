from itertools import permutations

n, m = map(int, input().split(" "))

pm = permutations([str(a) for a in range(1, n+1)], m)

pm = ([int("".join(p)) for p in pm])

for i in pm:
    for j in str(i):
        print(j, end=" ")
    print()