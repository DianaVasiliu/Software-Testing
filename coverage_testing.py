from anagrams import *
from champagne_tower import *
from fractional_knapsack import *
from kth_smallest_select import *
from minimum_halls_scheduling import *
from projects_with_maximum_profits import *
from zigzag_conversion import *

are_anagrams("race", "crab")
are_anagrams("123", "1234")
are_anagrams("listen", "silent")

champagneTower(-1, 0, 0)
champagneTower(1, 1, 1)
champagneTower(1, 321, 321)
champagneTower(1, 10, 15)
champagneTower(2, 1, 1)

fractional_knapsack(3, 50, [10, 20, 30], [60, 100, 120])

kthSmallest([1, 1, 2, 6, 2, 4, 4, 7], 4)
kthSmallest([1.9, 2.7, 3.2], 3)
kthSmallest([1, 7, 4, 3, 3, 8], 2)

minimum_halls_scheduling(3, ["12:00 14:00", "15:00 16:00", "12:30 14:00"])
minimum_halls_scheduling(1, ["abcd"])
minimum_halls_scheduling(1, ["12 34"])
minimum_halls_scheduling(1, ["12:00 10:00"])

projects_with_maximum_profits([2, 1, 2], [3, 2, 5], [4, 4, 4])

convert("ABC", 1)
convert("ABCDEFG", 5)
