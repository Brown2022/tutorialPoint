#!/usr/bin/python 3

def binary_search(arr, x):
    """
    Search for the element x int he sorteed lidt arr using the binary
    serach algorithm.

    Return the index element if it is found, or -1 if it is not found.

    """

    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid -1
        else:
            return mid
        return -1
