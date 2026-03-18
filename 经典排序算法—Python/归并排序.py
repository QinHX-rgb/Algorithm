import random

def merge_sort(arr):
    """
    归并排序：利用分治法。将数组拆分至最小后，再两两有序合并。
    时间复杂度始终为 O(n log n)，是稳定的排序算法。
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # 递归拆分左侧
    right = merge_sort(arr[mid:]) # 递归拆分右侧
    
    return merge(left, right)

def merge(left, right):
    """合并两个有序列表"""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:]); result.extend(right[j:])
    return result

if __name__ == "__main__":
    data = [random.randint(1, 100) for _ in range(8)]
    print(f"原始数组: {data}")
    print(f"归并排序: {merge_sort(data)}")