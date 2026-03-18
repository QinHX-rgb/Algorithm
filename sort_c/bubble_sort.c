#include <stdio.h>

// 1. 算法实现
void bubble_sort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// 2. 必须有入口函数 main
int main() {
    int data[] = {64, 34, 25, 12, 22};
    int n = sizeof(data) / sizeof(data[0]);

    bubble_sort(data, n);

    printf("排序后的数组: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", data[i]);
    }
    printf("\n");
    return 0;
}