import time
import matplotlib.pyplot as plt

def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

sizes = [10, 100, 1000, 5000]
times = []  
reps = 3000  

for n in sizes:
    data = list(range(n))  
    start = time.perf_counter()
    for _ in range(reps):
        linear_search(data, -1)  
    elapsed = (time.perf_counter() - start) / reps * 1e6  
    times.append(elapsed)

for n, t in zip(sizes, times):
    print(f"Размер {n}: {t:.2f} мкс")

plt.plot(sizes, times, 'o-')
plt.xlabel('Размер списка, элементов')
plt.ylabel('Время поиска, мкс')
plt.title('Линейный поиск: время от размера списка')
plt.grid(True, alpha=0.4)
plt.show()