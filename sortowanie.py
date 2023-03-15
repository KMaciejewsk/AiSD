import random

def gen_random(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(1, 10*n))
    return arr

def gen_vshape(n):
    arr = []
    temp = n
    for i in range(n//2):
        arr.append(temp)
        temp -= 2
    temp += 1
    for i in range(n//2,n):
        arr.append(temp)
        temp += 2
    return arr

def gen_ashape(n):
    arr = []
    temp = 1
    for i in range(n//2):
        arr.append(temp)
        temp += 2
    temp += 1
    for i in range(n//2,n):
        arr.append(temp)
        temp -= 2
    return arr

def gen_asc(n):
    arr = []
    for i in range(n):
        arr.append(i+1)
    return arr

def gen_desc(n):
    arr = []
    for i in range(n):
        arr.append(n-i)
    return arr

def heapify(arr, n, i):
    smallest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and arr[smallest] > arr[l]:
        smallest = l
    if r < n and arr[smallest] > arr[r]:
        smallest = r
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def partition(arr, low, high):
    pivot = arr[low]
    print(pivot)
    strat = low + 1
    end = high
    while True:
        while strat <= end and arr[strat] >= pivot:
            strat += 1
        while strat <= end and arr[end] <= pivot:
            end -= 1
        if strat <= end:
            arr[strat], arr[end] = arr[end], arr[strat]
        else:
            break
    arr[low], arr[end] = arr[end], arr[low]
    return end

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
    return arr

import time

arr = gen_random(10)
arr2 = arr
print(arr)
start = time.time()
quick_sort(arr, 0, len(arr)-1)
end = time.time()
print("QS: ", end-start)
print(arr)
start = time.time()
heap_sort(arr2)
end = time.time()
print("HS: ", end-start)
print(arr2)
