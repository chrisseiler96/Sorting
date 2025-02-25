# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    is_sorted = False
    while is_sorted == False:
        swaps = 0
        for i in range(0, len(arr)-1):
            next_i = i+1
            if arr[i] > arr[next_i]:
                arr[i], arr[next_i] = arr[next_i],arr[i]
                swaps += 1 

        if swaps == 0:
            is_sorted = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr