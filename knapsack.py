def knap(profits, weights, capacity, shift=0):
    #  print(profits, weights, capacity, shift)
    if capacity <= 0 or shift >= len(profits):
        #  print('<-')
        return 0

    profit1 = 0
    if weights[shift] <= capacity:
        profit1 = profits[shift] + knap(profits, weights, capacity - weights[shift], shift=shift+1)

    profit2 = knap(profits, weights, capacity, shift=shift+1)

    #  print(profit1, profit2)
    return max(profit1, profit2)

profits = [1, 6, 10, 16, 5, 6, 7, 8, 9, 10, 7, 8, 19]
weights = [1, 2, 3, 5,   6, 5, 4, 3, 4, 5,  1, 4, 1]
capacity = 100

print(knap(profits, weights, capacity))
