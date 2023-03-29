def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print("Swapping", arr[i], "and", arr[min_idx], "...Done!")
    print("Selection sort complete. Here's the sorted list:", arr)

selection_sort([5,416,54,21,6135,15,741])