import random
import matplotlib.pyplot as plt
from collections import defaultdict
from tabulate import tabulate

# Аналітичні ймовірності для порівняння
MATH_PROB = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78,
}

def simulate_dice_rolls(num: int):
    results = defaultdict(int)
    
    # Симуляція кидання кубиків
    for _ in range(num):
        roll = random.randint(1, 6) + random.randint(1, 6)
        results[roll] += 1
    
    # Обчислення ймовірностей
    probabilities = {key: value / num for key, value in results.items()}
    return probabilities

def plot_probabilities(prob: dict) -> None:
    x_values, y_values = zip(*sorted(prob.items()))
    
    plt.figure(figsize=(10, 6))
    plt.bar(x_values, y_values, color="skyblue")
    plt.xticks(range(2, 13))
    plt.xlabel("Сума")
    plt.ylabel("Ймовірність")
    plt.title("Розподіл ймовірностей сум при киданні двох кубиків")
    plt.grid(axis="y", linestyle="--")
    plt.show()

def main():
    num_simulations = 1000000
    probabilities = simulate_dice_rolls(num_simulations)
    
    # Підготовка даних для порівняння
    data = []
    for total in range(2, 13):
        probability = probabilities.get(total, 0) * 100
        data.append([total, probability, MATH_PROB[total]])
    
    # Виведення таблиці з ймовірностями
    print(
        tabulate(
            data,
            headers=["Сума", "Монте-Карло (%)", "Аналітична ймовірність (%)"],
            tablefmt="pipe",
        )
    )
    
    # Побудова графіка
    plot_probabilities(probabilities)

if __name__ == "__main__":
    main()