# time complexity n
def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)

print(sum(100))

# time complexity n/2
def sumOdds(start, end):
    if start == end:
        return 0
    return start + sumOdds(start + 2, end)

# time complexity n^2
