import collections

NUMBER_OF_SHOES = int(input())
SIZES_IN_STOCK = collections.Counter(map(int, input().split()))

TOTAL_REVENUE = 0

for _ in range(int(input())):
    size, price = map(int, input().split())
    if SIZES_IN_STOCK[size]:
        TOTAL_REVENUE += price
        SIZES_IN_STOCK[size] -= 1

print(TOTAL_REVENUE)