#
# def inseration_sort(arr):
#     for i in range(1, len(arr)):
#
#         key = arr[i]
#
#         # Move elements of arr[0..i-1], that are
#         # greater than key, to one position ahead
#         # of their current position
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#
#
# arr=[43,31,26,29,12]
# print(arr)
# inseration_sort(arr)
# print("Printed array values insertion ")
# print(arr)

def insertions_sorting(arr):
    for i in range(1,len(arr)):
         temp=arr[i]
         j = i-1
         while(j >= 0) and(temp < arr[j]):
             arr[j+1]=arr[j]
             j -=1
         arr[j+1] = temp





arr=[43,31,26,29,12]
insertions_sorting(arr)
print(arr)
