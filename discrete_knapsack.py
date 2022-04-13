from numpy import array

def discrete_knapsack(n:int, G: array, g:array, c:array):
    obiecte = []
    for i in range(n):
        obiecte.append((i,g[i],c[i],c[i]/g[i]))

    obiecte.sort(key = lambda x: x[3], reverse=True)
    rucsac = []
    i = 0
    while i < n and G != 0:
        ob = obiecte[i]
        if ob[1] <= G:
            ob = ob + (1,)
            rucsac.append(ob)
            G = G - ob[1]

        else:
            fr = G / ob[1]
            ob = ob + (fr,)
            rucsac.append(ob)
            G = 0

        i += 1

    return rucsac