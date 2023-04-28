import random


def LOMUTO_QUICKSORT(A, i, j):
    if i < j:
        p = PARTITION(A, i, j)
        LOMUTO_QUICKSORT(A, i, p - 1)
        LOMUTO_QUICKSORT(A, p + 1, j)


def PARTITION(A, i, j):
    pivot = A[j]
    left = i - 1
    for right in range(i, j):
        if A[right] <= pivot:
            left += 1
            A[left], A[right] = A[right], A[left]
    A[left + 1], A[j] = A[j], A[left + 1]
    return left + 1


def test():
    n = 50
    A = [random.randint(1, 100) for _ in range(n)]
    print("Przed sortowaniem:", A)
    LOMUTO_QUICKSORT(A, 0, n - 1)
    print("Po sortowaniu:", A)


test()
