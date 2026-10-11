import os
import time

# ANSI-последовательности для управления цветом и курсором
RED = '\033[41m \033[0m'
WHITE = '\033[47m \033[0m'
RESET = '\033[0m'
#1. Генерация флага Швейцарии

def draw_flag():
    print("--- 1. Флаг Швейцарии ---")
    # Матрица символов для отображения креста Швейцарии
    flag = [
        [RED]*11,
        [RED]*11,
        [RED]*4 + [WHITE]*3 + [RED]*4,
        [RED]*4 + [WHITE]*3 + [RED]*4,
        [RED]*2 + [WHITE]*7 + [RED]*2,
        [RED]*4 + [WHITE]*3 + [RED]*4,
        [RED]*4 + [WHITE]*3 + [RED]*4,
        [RED]*11,
        [RED]*11,
    ]
    for row in flag:
        print("".join(row))
    print()

        
        
                
# 2. Генерация повторяющегося узора 'j'

def draw_pattern():
    print("--- 2. Patrón (Узор j) ---")
   # Шаблон из двух соединенных окружностей (узор j)
    p1 = "  / \\   / \\  "
    p2 = " (   ) (   ) "    
    p3 = "  \\ /   \\ /  "
    
    # Dibujar patrón repetido varias veces
    repeats = 3
    print((p1 * repeats))
    print((p2 * repeats))
    print((p3 * repeats))
    print()
        
# 3. Анимация из 4 кадров

def run_animation():
    # Символы управления курсором (возврат в начало консоли)
    CLEAR_CONSOLE = 'cls' if os.name == 'nt' else 'clear'
    
    frames = [
        "  (  o.o  )  [Frame 1: Guarding]",
        "  (  -.-  )  [Frame 2: Blinking]",
        "  (  ^.^  )  [Frame 3: Happy]",
        "  (  O.O  )  [Frame 4: Surprised]"
    ]
    
    for _ in range(2):  # Повторить цикл анимации 2 раза
        for frame in frames:
            os.system(CLEAR_CONSOLE)  # Очистить консоль
            print("\033[H", end="") # Escape-последовательность переноса курсора в начало
            print("--- 3. Анимация (4 кадра) ---")
            print("\n\n" + frame + "\n\n")
            time.sleep(0.4)
            
            
#4. Процентная диаграмма (sequence.txt)

def draw_diagram():
    print("--- 4. Диаграмма процентного соотношения ---")
    filename = "sequence.txt"

    try:
        with open(filename, "r") as f:
            numbers = [float(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден. Использование тестовых данных...")
        numbers = [-5, -3, -2, -1, 0, 1, 2, 3, 4, 5, 10, -8, 0, 2]
    # # Условие варианта 10: Числа от -3 до 3 и остальные
    in_range_count = 0
    others_count = 0

    for num in numbers:
        if -3 <= num <= 3:
            in_range_count   += 1
        else:
            others_count += 1

    total = in_range_count + others_count   
    if total == 0:
        print("Файл не содержит чисел.")
        return

    pct_in_range = (in_range_count / total) * 100
    pct_others = (others_count / total) * 100

    print(f"Всего чисел: {total}")
    print(f"Числа от -3 до 3: {in_range_count} ({pct_in_range:.1f}%)")
    print(f"Остальные числа: {others_count} ({pct_others:.1f}%)\n")

    # Вывод гистограммы
    scale = 50
    bar1 = int((pct_in_range / 100) * scale)
    bar2 = scale - bar1

    print("Процентная диаграмма (100%):")
    print("От -3 до 3 : [" + "█" * bar1 + " " * (scale - bar1) + f"] {pct_in_range:.1f}%")
    print("Остальные  : [" + "█" * bar2 + " " * (scale - bar2) + f"] {pct_others:.1f}%")
    print()
# 5. Допзадание: График функции y = x / 3

def draw_function_graph():
    print("--- 5. Допзадание: График функции y = x / 3 ---")
    height = 10  # Высота не менее 9 строк
    width = 30
    
    # Инициализация пустой двумерной матрицы для системы координат
    grid = [[" " for _ in range(width)] for _ in range(height)]

    # Расчет точек первой четверти графика
    for x in range(width):
        y = int(round(x / 3.0))
        if 0 <= y < height:
            # Инверсия оси Y для консольного вывода (сверху вниз)
            row = (height - 1) - y
            grid[row][x] = "*"

    # Построчный вывод графика с осями
    for r_idx, row in enumerate(grid):
        y_val = height - 1 - r_idx
        print(f"{y_val:2d} | " + "".join(row))
    
    print("     " + "-" * width)
    print("       " + "".join([str(i % 10) for i in range(width)]))
    print()


# Главный блок программы

if __name__ == "__main__":
    draw_flag()
    draw_pattern()
    draw_diagram()
    draw_function_graph()
    
    input("Нажмите Enter для запуска анимации...")
    run_animation()