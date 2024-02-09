combination_distribution = [[0] * 6 for _ in range(6)]

for i in range(1,7):
    for j in range(1,7):
        combination_distribution[i-1][j-1] = i+j

print("Distribution of all the combinations: ")
for r in combination_distribution:
    print(r)