
def projects_with_maximum_profits(n:int, inc: list, fin:list, profit:list):
    proiecte = [(0,(0,0),0)]
    for i in range(1,n+1):
        data = (inc[i],fin[i])
        proiecte.append((i[i],data,profit[i]))

    proiecte.sort(key=lambda x: x[1][1]) #sortare dupa data de final

    ult = [0]*(n+1)
    cmax = [0]*(n+1)
    for i in range(1,n+1):
        j = i-1
        while j > 0:
            if proiecte[i][1][0] < proiecte[j][1][1]:
                j -= 1
            else:
                ult[i] = j
                break

    for i in range(1,n+1):
        cmax[i] = max(cmax[i-1], proiecte[i][2] + cmax[ult[i]])

    i = n
    sol = []
    while i > 0:
        if cmax[i] != cmax[i-1]:
            sol.append(proiecte[i][0])
            i = ult[i]
        else:
            i -= 1

    return sol.reverse()