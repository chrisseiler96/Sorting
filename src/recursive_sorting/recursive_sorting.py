# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    for i in range(len(merged_arr)):
        print("i=",i)
        print(arrA, arrB)
        if len(arrA) > 0 and len(arrB) > 0:
            if arrA[0] <= arrB[0]:
                merged_arr[i] = arrA[0]
                del arrA[0]
            else:
                merged_arr[i] = arrB[0]
                del arrB[0]
        elif len(arrA)>0:
            merged_arr[i] = arrA[0]
            del arrA[0]
        else:
            merged_arr[i] = arrB[0]
            del arrB[0]

    print(merged_arr)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    length = len(arr)
    if length > 1:
        half = length//2
        merged = merge(merge_sort(arr[:half]), merge_sort(arr[half:]))
        arr = merged
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
