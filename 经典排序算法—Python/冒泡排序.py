import random

def bubble_sort(arr):
    """
    冒泡排序：通过相邻元素的比较和交换，使较大的元素逐渐向后移动。
    平均/最坏时间复杂度: O(n^2), 最好时间复杂度: O(n)
    """
    n = len(arr)
    for i in range(n):
        swapped = False # 优化：记录本轮是否有交换
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # 交换
                swapped = True
        if not swapped: # 若无交换，说明已经有序
            break
    return arr

if __name__ == "__main__":
    data = [random.randint(1, 100) for _ in range(8)]
    print(f"原始数组: {data}")
    print(f"冒泡排序: {bubble_sort(data)}")