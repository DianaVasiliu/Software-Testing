import re


def minimum_halls_scheduling(n: int, data: list[str]):
    pattern = re.compile('[0-9]?[0-9]:[0-9][0-9]')
    shows = []
    for i in range(n):
        line = data[i]
        line = line.split()
        startTime = line[0]
        endTime = line[1]
        if not (pattern.fullmatch(startTime) and pattern.fullmatch(endTime)):
            return "Error: Invalid input, must match pattern"
        if startTime > endTime:
            return "Error: Invalid input, must be valid interval"
        pair = (i, startTime, endTime)
        shows.append(pair)

    shows.sort(key=lambda p: p[1])     # sorting by start time

    numberOfHalls = 1
    halls = [[shows[0]]]
    for x in shows[1:]:
        for i in range(numberOfHalls):
            if x[1] >= halls[i][-1][2]:
                halls[i].append(x)
                break
        else:
            numberOfHalls += 1
            halls.append([x])

    return halls
