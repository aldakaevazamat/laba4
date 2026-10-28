import random

# 1. Создаем массив (для примера из 8 чисел)
n = 8
arr = [round(random.uniform(-10, 10), 2) for _ in range(n)]
print("Исходный массив:", arr)

# --- Пункт 1: Сумма положительных элементов ---
sum_pos = sum(x for x in arr if x > 0)
print("1. Сумма положительных:", round(sum_pos, 2))

# --- Пункт 2: Произведение между max и min по модулю ---
# Находим индексы (позиции) элементов
idx_max = max(range(n), key=lambda i: abs(arr[i]))
idx_min = min(range(n), key=lambda i: abs(arr[i]))

# Берем срез от меньшего индекса к большему (не включая края)
start, end = min(idx_max, idx_min), max(idx_max, idx_min)
sub_array = arr[start + 1 : end]

# Считаем произведение
if len(sub_array) > 0:
    product = 1
    for x in sub_array:
        product *= x
    print(f"2. Произведение между ними: {round(product, 2)}")
else:
    print("2. Между max и min нет элементов")

# --- Пункт 3: Сортировка по убыванию ---
arr.sort(reverse=True)
print("3. По убыванию:", arr)