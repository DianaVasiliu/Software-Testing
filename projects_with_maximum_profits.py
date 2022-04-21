def projects_with_maximum_profits(starts: list[int], ends: list[int], profits: list[float]) -> tuple[list, float]:
    projects = [(0, (0, 0), 0)]

    n = len(starts)

    for i in range(n):
        data = (starts[i], ends[i])
        projects.append((i, data, profits[i]))

    projects.sort(key=lambda x: x[1][1])  # sort by end date

    last = [0] * (n + 1)
    cMax = [0] * (n + 1)

    for i in range(1, n + 1):
        j = i - 1
        while j > 0:
            if projects[i][1][0] < projects[j][1][1]:
                j -= 1
            else:
                last[i] = j
                break

    for i in range(1, n + 1):
        cMax[i] = max(cMax[i - 1], projects[i][2] + cMax[last[i]])

    i = n
    sol = []
    while i > 0:
        if cMax[i] != cMax[i - 1]:
            sol.append(projects[i])
            i = last[i]
        else:
            i -= 1

    profit = sum([x[2] for x in sol])
    indices = list(reversed([x[0] for x in sol]))

    return indices, profit
