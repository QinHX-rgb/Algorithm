#include <stdio.h>

// 辅助函数：交换两个整数的值
void swap(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}

/* 分区函数：核心逻辑
   选定最后一个元素为基准(pivot)，把小的移到左边，大的移到右边
*/
int partition(int arr[], int low, int high) {
    int pivot = arr[high];    // 基准值
    int i = (low - 1);        // i 是较小元素的索引

    for (int j = low; j <= high - 1; j++) {
        // 如果当前元素小于或等于基准
        if (arr[j] <= pivot) {
            i++; 
            swap(&arr[i], &arr[j]);
        }
    }
    // 将基准值换到中间位置（i+1）
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

/* 快速排序主函数 */
void quick_sort(int arr[], int low, int high) {
    if (low < high) {
        // pi 是分区后的基准点下标
        int pi = partition(arr, low, high);

        // 分别对左右两部分进行递归排序
        quick_sort(arr, low, pi - 1);
        quick_sort(arr, pi + 1, high);
    }
}

// 打印数组的辅助函数
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int data[] = {10, 7, 8, 9, 1, 5, 2, 6};
    int n = sizeof(data) / sizeof(data[0]);

    printf("原始数组: ");
    printArray(data, n);

    quick_sort(data, 0, n - 1);

    printf("排序后结果: ");
    printArray(data, n);

    return 0;
}