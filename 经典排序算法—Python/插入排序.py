import random

def insertion_sort(arr):
    """
    插入排序：通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
    适用于小规模或基本有序的数据。
    """
    for i in range(1, len(arr)):
        key = arr[i] # 当前待插入的数
        j = i - 1
        # 将比 key 大的数向后移动一位
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key # 插入空位
    return arr

if __name__ == "__main__":
    data = [random.randint(1, 100) for _ in range(8)]
    print(f"原始数组: {data}")
    print(f"插入排序: {insertion_sort(data)}")