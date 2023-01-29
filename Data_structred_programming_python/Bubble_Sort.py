
# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)-1-i):
#             if arr[j]> arr[j+1]:
#                 temp=arr[j]
#                 arr[j]=arr[j+1]
#                 arr[j+1]=temp
#     for i in range(len(arr)):
#         print(arr[i])
#
# arr=[22,14,12,18,9]
#
# bubble_sort(arr)

"""
Bubble sort program
"""

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]> arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

    for i in range(len(arr)):
        print(arr[i])

arr=[22,14,12,18,9]
bubble_sort(arr)

