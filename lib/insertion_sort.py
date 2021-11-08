
def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        # Insert A[j] into the sorted sequence A[0 .. j - 1]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key

if __name__ == '__main__':
    unsorted_list = [3, 5, 2, 6, 99, 8, 4]
    insertion_sort(unsorted_list)
    print(unsorted_list)
