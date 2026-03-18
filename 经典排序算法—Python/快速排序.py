import random

def quick_sort(arr):
    """
    快速排序：选定一个基准(pivot)，将数据分为小于、等于、大于基准的三部分，递归处理。
    平均速度最快，实际应用最广。
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2] # 选中间值为基准
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    data = [random.randint(1, 100) for _ in range(8)]
    print(f"原始数组: {data}")
    print(f"快速排序: {quick_sort(data)}")