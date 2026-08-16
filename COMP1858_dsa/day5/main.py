a = [10, 8, 20, 193, 231]


def sumNum(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result


print(sumNum(20))


def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)


print(sum(20))


def sumeven(a, b):
    start = a if a % 2 == 0 else a + 1
    end = b if b % 2 == 0 else b - 1
    if start == end:
        return 0
    return end + sumeven(start, end - 2)


print(sumeven(10, 21))

# recursion max
