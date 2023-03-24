import time

"""
Algorytm sortujacy napisany według pseudokodu dostarczonego przez prowadzącego zajęcia.
"""


def insertion(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A


"""
Testowanie najlepszego przypadku i najgorszego.

Przypadek najlepszy
"""
for n in [2000, 4000, 8000, 16000, 32000]:
    A = list(range(1, n + 1))
    start_time = time.time()
    insertion(A)
    end_time = time.time()
    print(f"Best-case for n={n}: {end_time - start_time:.5f} seconds")

"""
Przypadek najgorszy.
"""
for n in [2000, 4000, 8000, 16000, 32000]:
    A = list(range(n, 0, -1))
    start_time = time.time()
    insertion(A)
    end_time = time.time()
    print(f"Worst-case for n={n}: {end_time - start_time:.5f} seconds")

"""
Obliczanie stosunku FN/TN
"""
for n in [2000, 4000, 8000, 16000, 32000]:

    A = list(range(1, n + 1))
    start_time = time.time()
    insertion(A)
    end_time = time.time()
    try:
        best_case_ratio = n / (end_time - start_time)
    except ZeroDivisionError:
        best_case_ratio = 0

    A = list(range(n, 0, -1))
    start_time = time.time()
    insertion(A)
    end_time = time.time()
    worst_case_ratio = (n ** 2) / (end_time - start_time)

    print(f"n={n}, Przypadek najlepszy: {best_case_ratio:.2f}, Przypadek najgorszy: {worst_case_ratio:.2f}")
