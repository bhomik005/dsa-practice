# need to check if we have an empty space at the end
# if we do, then we can just insert the element and it will be a constant time operation
# O(1) time
def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n


# removing last element here mean setting the value to 0
# assuming we have at least one element stored in the array
# O(1) time operation
def removeEnd(arr, length):
    if length > 0:
        arr[length - 1] = 0


# arr = [1, 2, 4, 5]
# we would want to insert element 3 b/w 2 and 4, i = 2
# arr = [1, 2, 3, 4, 5]
# O(n) time operation
def insertMiddle(arr, i, n, length):
    # shift the elements to the right by 1
    for idx in range(length - 1, i - 1, -1):
        arr[idx + 1] = arr[idx]

    # insert the element
    arr[i] = n


# arr = [1, 2, 3, 4, 5]
# O(n) time operation
def removeMiddle(arr, i, length):
    # shift the elements to the left by 1
    for idx in range(i, length - 1):
        arr[idx] = arr[idx + 1]

    # make the last element 0
    arr[length - 1] = 0


# traversing through the list of elements
# O(n) time operation
def printArr(arr, capacity):
    for idx in range(capacity):
        print(arr[idx], end=" ")
