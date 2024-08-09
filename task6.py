def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_calories = 0
    chosen_items = []

    for item, info in sorted_items:
        if budget >= info['cost']:
            chosen_items.append(item)
            total_calories += info['calories']
            budget -= info['cost']
    
    return chosen_items, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    item_names = list(items.keys())
    costs = [items[item]['cost'] for item in item_names]
    calories = [items[item]['calories'] for item in item_names]
    
    # Ініціалізуємо таблиці DP
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # З’ясовуємо обрані страви
    chosen_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen_items.append(item_names[i - 1])
            w -= costs[i - 1]

    total_calories = dp[n][budget]

    return chosen_items, total_calories


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

print("Жадібний алгоритм:")
chosen_items, total_calories = greedy_algorithm(items, budget)
print("Вибрані страви:", chosen_items)
print("Загальна калорійність:", total_calories)

print("\nДинамічне програмування:")
chosen_items, total_calories = dynamic_programming(items, budget)
print("Вибрані страви:", chosen_items)
print("Загальна калорійність:", total_calories)