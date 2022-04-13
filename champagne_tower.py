def champagneTower() -> float:
    file = open("champagneTower.txt")
    data = file.readline()
    data = data.split()

    try:
        poured = int(data[0])
        query_row = int(data[1])
        query_glass = int(data[2])
    except ValueError:
        return -1.0

    dp = [[0] * k for k in range(1, 102)]
    dp[0][0] = poured

    for r in range(query_row + 1):
        for c in range(r + 1):
            quantity = (dp[r][c] - 1.0) / 2.0
            if quantity > 0:
                dp[r + 1][c] += quantity
                dp[r + 1][c + 1] += quantity

    return min(1.0, dp[query_row][query_glass])
