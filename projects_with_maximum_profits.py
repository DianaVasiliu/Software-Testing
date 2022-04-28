
def projects_with_maximum_profits(inc: list, fin:list, profit:list):
    P = []
    for i in range(len(inc)):
        P.append((inc[i], fin[i], profit[i]))
    n=len(P)
    ult=[0]*(n+1)
    cmax=[0]*(n+1)
    P.sort(key=lambda x:x[1])
    for i in range(1,n+1):
        for j in range(i-1,0,-1):
            if P[i-1][0]>=P[j-1][1]:
                ult[i]=j
                break
        cmax[i]=max(cmax[i-1],P[i-1][2]+cmax[ult[i]])
    return cmax[n]
