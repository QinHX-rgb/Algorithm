import random

def shell_sort(arr):
    """
    希尔排序：插入排序的改进版。使用增量(gap)分组，使数组基本有序后再进行最终插入排序。
    时间复杂度取决于增量序列，通常优于 O(n^2)。
    """
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2 # 缩小增量
    return arr

if __name__ == "__main__":
    data = [random.randint(1, 100) for _ in range(10)]
    print(f"原始数组: {data}")
    print(f"希尔排序: {shell_sort(data)}")