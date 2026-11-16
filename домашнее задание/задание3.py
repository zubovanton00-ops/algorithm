import random

def linear_search(lst, target):
    """Возвращает индекс первого вхождения target в lst или -1, если элемент не найден."""
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

random.seed(42)
data = [random.randint(1, 10000) for _ in range(100)]

targets = [data[0], data[len(data) // 2], data[-1], 99999]
results = {t: linear_search(data, t) for t in targets}

print("Список (первые 10 элементов):", data[:10])
print("Результаты поиска:", results)