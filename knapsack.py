def dynamic_programming_knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    selected_items = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(i - 1)
            j -= weights[i - 1]
        i -= 1

    return dp[n][capacity], selected_items[::-1]

def greedy_knapsack(weights, values, capacity):
    n = len(weights)
    ratios = [(values[i] / weights[i], i) for i in range(n)]
    ratios.sort(reverse=True)

    selected_items = []
    total_weight = 0
    total_value = 0

    for ratio, index in ratios:
        if total_weight + weights[index] <= capacity:
            selected_items.append(index)
            total_weight += weights[index]
            total_value += values[index]

    return total_value, selected_items


weights = [2, 1, 4, 4]
values = [4, 3, 6, 8]
capacity = 8

max_value, selected_items = dynamic_programming_knapsack(weights, values, capacity)
print("Maksymalna wartość:", max_value)
print("Wybrane przedmioty:", selected_items)

max_value, selected_items = greedy_knapsack(weights, values, capacity)
print("Maksymalna wartość:", max_value)
print("Wybrane przedmioty:", selected_items)
