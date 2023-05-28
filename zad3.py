import random
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    larger = [x for x in arr if x > pivot]
    return quicksort(smaller) + equal + quicksort(larger)

def countingsort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    sorted_arr = []
    for i in range(max_val + 1):
        sorted_arr.extend([i] * count[i])
    return sorted_arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def compare_sorting_algorithms(size):
    random_array = generate_random_array(size)

    start_time = time.time()
    sorted_array = quicksort(random_array)
    quicksort_time = time.time() - start_time

    start_time = time.time()
    sorted_array = countingsort(random_array)
    countingsort_time = time.time() - start_time

    start_time = time.time()
    sorted_array = heapsort(random_array)
    heapsort_time = time.time() - start_time

    print(f"Quicksort time: {quicksort_time} seconds")
    print(f"Countingsort time: {countingsort_time} seconds")
    print(f"Heapsort time: {heapsort_time} seconds")

# Testowanie dla losowej tablicy o rozmiarze 10000
compare_sorting_algorithms(10000)