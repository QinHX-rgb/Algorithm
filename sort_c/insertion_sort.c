#include <stdio.h>

void insertion_sort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

int main() {
    int data[] = {12, 11, 13, 5, 6};
    int n = 5;
    insertion_sort(data, n);
    printf("Insertion Sort: ");
    for(int i=0; i<n; i++) printf("%d ", data[i]);
    return 0;
}