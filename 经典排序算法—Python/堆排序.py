import random

def heapify(arr, n, i):
    """调整大顶堆"""
    largest = i
    l, r = 2 * i + 1, 2 * i + 2
    if l < n and arr[l] > arr[largest]: largest = l
    if r < n and arr[r] > arr[largest]: largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # 交换
        heapify(arr, n, largest) # 递归调整

def heap_sort(arr):
    """
    堆排序：利用二叉堆性质。先建大顶堆，再不断将堆顶(最大值)交换到末尾并重新调整。
    空间复杂度为 O(1)。
    """
    n = len(arr)
    # 1. 建立大顶堆
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # 2. 逐一提取元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # 交换堆顶到末尾
        heapify(arr, i, 0)
    return arr

if __name__ == "__main__":
    data = [random.randint(1, 100) for _ in range(8)]
    print(f"原始数组: {data}")
    print(f"堆排序:   {heap_sort(data)}")