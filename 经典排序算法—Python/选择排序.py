import random

def selection_sort(arr):
    """
    选择排序：每一轮在未排序序列中找到最小元素，存放到排序序列的起始位置。
    时间复杂度: O(n^2), 空间复杂度: O(1)
    """
    n = len(arr)
    for i in range(n):
        min_idx = i # 记录最小元素的索引
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # 交换到当前起始位
    return arr

if __name__ == "__main__":
    data = [random.randint(1, 100) for _ in range(8)]
    print(f"原始数组: {data}")
    print(f"选择排序: {selection_sort(data)}")