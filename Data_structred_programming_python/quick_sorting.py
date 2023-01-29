
"""
Write a program a quick sort algoritham
"""
#
# def pattions(arr,low ,high):
#
#     pivot=arr[high]
#     print(pivot)
#
#     i= low-1
#     for j in range(low,high):
#         if arr[j] <= pivot:
#             i +=1
#             (arr[i],arr[j])=(arr[j],arr[i])
#
#     (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
#
#     return i+1
#
# def quick_Sort(arr ,low,high):
#
#     if high > low:
#         pi=pattions(arr,low ,high)
#
#         quick_Sort(arr,low,pi-1)
#         quick_Sort(arr,pi+1,high)
#
#
# data = [1, 7, 4, 1, 10, 9, -2]
# print("Unsorted Array")
# print(data)
#
# size = len(data)
#
# quick_Sort(data, 0, size - 1)
#
# print('Sorted Array in Ascending Order:')
# print(data)

def pattions(arr,low,high):
    pivot=arr[high]

    i=low-1
    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            (arr[i],arr[j])=(arr[j],arr[i]) # conditions true holo a[i][j] sthay swaping

    (arr[i+1],arr[high])=(arr[high],arr[i+1]) # i+1 and high sthay swap hoba

    return  i+1


def quickSort(arr,low ,high):
     if high > low:
         # calling the recursive functions
         pi=pattions(arr,low,high)


         # Recursive call on the left of pivot
         quickSort(arr, low, pi - 1)

         # Recursive call on the right of pivot
         quickSort(arr, pi + 1, high)


data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)
