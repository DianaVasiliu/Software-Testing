from numpy import number

def fractional_knapsack(value:list, weight:list, capacity:number):
    index = list(range(len(value)))
    # contains ratios of values to weight
    ratio = [v/w for v, w in zip(value, weight)]
    # index is sorted according to value-to-weight ratio in decreasing order
    index.sort(key=lambda i: ratio[i], reverse=True)
 
    max_value = 0
    for i in index:
        if weight[i] <= capacity:
            max_value += value[i]
            capacity -= weight[i]
        else:
            max_value += value[i]*capacity/weight[i]
            break
 
    return max_value