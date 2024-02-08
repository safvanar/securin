from itertools import product

def calculate_probabilities(die_A, die_B):
    total_combinations = 0
    sums_distribution = {}

    for i, j in product(die_A, die_B):
        total_combinations += 1
        total_sum = i + j
        sums_distribution[total_sum] = sums_distribution.get(total_sum, 0) + 1

    probabilities = {key: value / total_combinations for key, value in sums_distribution.items()}
    return probabilities

def undoom_dice(die_A, die_B):
    target_probabilities = calculate_probabilities(die_A, die_B)
    new_die_A = die_A[:]
    
    for i in range(1, 5):
        for j in range(6):
            if new_die_A.count(j+1) > 4:
                new_die_A.remove(j+1)
                break
                
    new_die_B = die_B[:]
    
    while True:
        probabilities = calculate_probabilities(new_die_A, new_die_B)
        
        if probabilities == target_probabilities:
            break
        
        for i in range(6):
            new_die_B[i] += 1
            
    return new_die_A, new_die_B

# Input
Die_A = [1, 2, 3, 4, 5, 6]
Die_B = Die_A

# Output
New_Die_A, New_Die_B = undoom_dice(Die_A, Die_B)
print("New Die A:", New_Die_A)
print("New Die B:", New_Die_B)
