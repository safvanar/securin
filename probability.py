from fractions import Fraction

combination_distribution = [[0] * 6 for _ in range(6)]

for i in range(1,7):
    for j in range(1,7):
        combination_distribution[i-1][j-1] = i+j

print("Distribution of all the combinations: ")
for r in combination_distribution:
    print(r)

probabilities = {}

for i in range(2, 13):
    count = sum(row.count(i) for row in combination_distribution)
    probabilities[i] = Fraction(count / 36).limit_denominator()

print("Probability of all possible sums:")
for sum_value, probability in probabilities.items():
    print(f"P(Sum = {sum_value}) = {probability}")