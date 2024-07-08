import random
import time
import heapq

random_list = [random.randint(0, 100000) for _ in range(100000)]

def measure_sort_time(sort_func, data):
    start_time = time.time()
    sort_func(data)
    end_time = time.time()
    return end_time - start_time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def counting_sort(arr):
    max_val = max(arr)
    m = max_val + 1
    count = [0] * m
    for a in arr:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1

def radix_sort(arr):
    RADIX = 10
    max_val = max(arr)
    placement = 1
    while placement <= max_val:
        buckets = [[] for _ in range(RADIX)]
        for num in arr:
            buckets[(num // placement) % RADIX].append(num)
        a = 0
        for b in range(RADIX):
            for num in buckets[b]:
                arr[a] = num
                a += 1
        placement *= RADIX

def heap_sort(arr):
    heapq.heapify(arr)
    sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]
    arr[:] = sorted_arr

sorting_algorithms = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort,
    "Counting Sort": counting_sort,
    "Radix Sort": radix_sort,
    "Heap Sort": heap_sort,
    "Tim Sort": sorted  # Using Python's built-in sorted function
}

results = {}
for sort_name, sort_func in sorting_algorithms.items():
    data_copy = random_list.copy()
    if sort_name in ["Quick Sort", "Tim Sort"]:

        start_time = time.time()
        sorted_data = sort_func(data_copy)
        end_time = time.time()
        results[sort_name] = end_time - start_time
    else:
        results[sort_name] = measure_sort_time(sort_func, data_copy)

for sort_name, time_taken in results.items():
    print(f"{sort_name}: {time_taken:.6f} seconds")