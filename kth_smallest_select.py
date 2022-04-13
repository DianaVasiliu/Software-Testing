import random

def quickselect(A,k,f_pivot = random.choice):
    pivot = f_pivot(A)
    L = [x for x in A if x < pivot]
    E = [x for x in A if x == pivot]
    H = [x for x in A if x > pivot]

    if k < len(L):
        return quickselect(L,k,f_pivot)
    elif k < len(L) + len(E):
        return E[0]
    else:
        return quickselect(H,k-len(L)-len(E),f_pivot)

def pivot_mediana(A):
    if len(A) <= 5:
        return sorted(A)[len(A) // 2]
    subliste = [sorted(A[i : i+5]) for i in range (0, len(A), 5)]
    mediane = [subl[len(subl) // 2] for subl in subliste]
    return pivot_mediana(mediane)


def kthSmallest(n:int, k:int, x:list):
    A = []
    for i in range(n):
        A.append(x[i])
    return quickselect(A, k, pivot_mediana)