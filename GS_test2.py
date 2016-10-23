def climbStairs(n):
    # write your code here
    if n <= 2:
        return n
    result = [1, 2, 4]
    for i in range(n - 3):
        result.append(result[-3] + result[-2] + result[-1])
    return result[-1]


if __name__ == "__main__":
    tmp = climbStairs(100)
    print(tmp)