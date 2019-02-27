def qsort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i >= pivot]

    return qsort(less) + [pivot] + qsort(greater)   


if __name__ == "__main__":
    print(qsort([13, 1, 5, 2, -2, 3, 3, 1]))
    print(qsort([1]))
    print(qsort([1, 2]))
    print(qsort([2, 1]))
    print(qsort([2, 1, 0]))
    print(qsort([-1, -1, -2, -1, 0, 0]))
