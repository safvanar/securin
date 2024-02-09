from typing import *


Die  = list 
Pair = tuple
standard_pair = None  
standard_sums= None

def undoom_dice(d1, d2):
    global standard_pair 
    global standard_sums
    standard_pair = (d1, d2) 
    standard_sums = distribution_of_sums(standard_pair)
    return undoom_dice_list()


def undoom_dice_list() -> List[Pair]:
    return [pair for pair in all_pairs(all_dice())
            if distribution_of_sums(pair) == standard_sums
            and pair != standard_pair]

def all_pairs(dice) -> List[Pair]: 
    return [(A, B) for A in dice for B in dice if A <= B]


Bag = sorted 

def distribution_of_sums(pair) -> List[int]:
    (A, B) = pair
    return Bag(a + b for a in A for b in B)

def ints(start, end) -> range: 
    return range(start, end + 1)


def all_dice() -> List[Die]:
    return [[1, b, c, d, e, f]
            for b in ints(2, 10) 
            for c in ints(b, 10)
            for d in ints(c, 10)
            for e in ints(d, 10) 
            for f in ints(e, 10)]


# Input
Die_A = [1, 2, 3, 4, 5, 6]
Die_B = Die_A

# Output
die_pattern_final = undoom_dice(Die_A, Die_B)
print("New Die A:", die_pattern_final[0][0])
print("New Die B:", die_pattern_final[0][1])