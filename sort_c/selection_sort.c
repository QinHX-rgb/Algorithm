#include <stdio.h>

void selection_sort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx]) min_idx = j;
        }
        // 交换
        int temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
}

int main() {
    int data[] = {29, 10, 14, 37, 13};
    int n = sizeof(data)/sizeof(data[0]);
    selection_sort(data, n);
    printf("Selection Sort: ");
    for(int i=0; i<n; i++) printf("%d ", data[i]);
    return 0;
}