def champagneTower(poured: int, query_row: int, query_glass: int) -> float:
    if poured < 0 or query_row < 0 or query_glass < 0:
        return -1
    if query_row >= 100 or query_glass >= 100:
        return -2
    if query_glass > query_row:
        return -3

    dp = [[0] * k for k in range(1, 101)]
    dp[0][0] = poured

    for r in range(query_row + 1):
        for c in range(r + 1):
            quantity = (dp[r][c] - 1.0) / 2.0
            if quantity > 0:
                dp[r + 1][c] += quantity
                dp[r + 1][c + 1] += quantity

    return min(1.0, dp[query_row][query_glass])
