def projects_with_maximum_profits(starts: list, ends: list, profits: list):
    projects = []
    for i in range(len(starts)):
        projects.append((starts[i], ends[i], profits[i]))
        
    n = len(projects)
    last = [0] * (n + 1)
    cMax = [0] * (n + 1)
    projects.sort(key=lambda x: x[1])
    
    for i in range(1, n + 1):
        for j in range(i - 1, 0, -1):
            if projects[i - 1][0] >= projects[j - 1][1]:
                last[i] = j
                break
        cMax[i] = max(cMax[i - 1], projects[i - 1][2] + cMax[last[i]])
        
    return cMax[n]
