def fractional_knapsack(nrObjects: int, W: int, weights: list, values: list) -> float:
    objects = []
    for i in range(nrObjects):
        objects.append((i, weights[i], values[i], values[i]/weights[i]))

    objects.sort(key=lambda x: x[3], reverse=True)
    knapsack = 0
    i = 0

    while i < nrObjects and W != 0:
        obj = objects[i]

        if obj[1] <= W:
            knapsack += obj[2]
            W = W - obj[1]
        else:
            knapsack += obj[2] * W / obj[1]
            W = 0

        i += 1

    return knapsack
