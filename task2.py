import turtle 
import math

# Функція для малювання "дерева Піфагора"
def draw_pythagoras_tree(t, length, level):
    if level == 0:
        t.forward(length)
        t.backward(length)
    else:
        t.forward(length)
        t.left(45)
        draw_pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1)
        t.right(90)
        draw_pythagoras_tree(t, length * math.sqrt(2) / 2, level - 1)
        t.left(45)
        t.backward(length)


def main():
    level = int(input("Введіть рівень рекурсії: "))
    length = 100  # Довжина основного сегменту

    screen = turtle.Screen()
    screen.title("Дерево Піфагора")

    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість малювання
    t.left(90)  # Поворот черепахи вертикально вверх

    draw_pythagoras_tree(t, length, level)

    screen.mainloop()

if __name__ == "__main__":
    main()