from itertools import permutations

n = int(input())
k = int(input())
cards = list(input() for _ in range(n))

cards_combi = permutations(cards, k)
cards_combi = sorted(set([(int("".join(a)) for a in cards_combi)]))
print(len(cards_combi))