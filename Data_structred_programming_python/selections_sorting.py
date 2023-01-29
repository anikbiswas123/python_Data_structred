
# def selaction_Sorting(arr,size):
#     for ind in range(size):
#         min_index = ind
#
#         for j in range(ind + 1, size):
#             # select the minimum element in every iteration
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         # swapping the elements to sort the array
#         (arr[ind], arr[min_index]) = (arr[min_index], arr[ind])
#
# arr=[9,13,15,11,2]
# print(arr )
# size=len(arr)
# print("selection sorting")
# selaction_Sorting(arr,size)
# print(arr)

def selection(arr,size):
    for ind in range(size):
        min = ind
        for j in range(ind+1,size):
            if arr[j] < arr[min]:
                min = j

            (arr[ind],arr[min]) = (arr[min],arr[ind])

arr=[9,13,15,11,2]
size=len(arr)
print(arr)
print("")
selection(arr,size)
print(arr)