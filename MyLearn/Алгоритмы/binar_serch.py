def binarySearch(elem, arr):
    # return the index at which elem lies, or return false
    # if elem is not found
    # pre: array must be sorted
    return binarySearchHelper(elem, arr, 0, len(arr) - 1)

def binarySearchHelper(elem, arr, start, end):
    if start > end:
        return False
    mid = (start + end)//2
    if arr[mid] == elem:
        return mid
    elif arr[mid] > elem:
        # recurse to the left of mid
        return binarySearchHelper(elem, arr, start, mid - 1)
    else:
        # recurse to the right of mid
        return binarySearchHelper(elem, arr, mid + 1, end)

mas = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


a = binarySearch(1,mas)

print(a)

