def quickSelect(A, k, f_pivot):
    pivot = f_pivot(A)
    less = [x for x in A if x < pivot]
    equal = [x for x in A if x == pivot]
    higher = [x for x in A if x > pivot]

    if k < len(less):
        return quickSelect(less, k, f_pivot)
    elif k <= len(less) + len(equal):
        return equal[0]
    else:
        return quickSelect(higher, k - len(less) - len(equal), f_pivot)


def medianPivot(A):
    if len(A) <= 5:
        return sorted(A)[len(A) // 2]

    subLists = [sorted(A[i:i + 5]) for i in range(0, len(A), 5)]
    medians = [s[len(s) // 2] for s in subLists]
    return medianPivot(medians)


def kthSmallest(x: list[float], k: int) -> float:
    return quickSelect(x, k, medianPivot)
