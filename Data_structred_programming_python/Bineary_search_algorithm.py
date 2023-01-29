""" Bineary search algoritham  """

#
# def Bineary_search(arr,n,s_data):
#     l = 0
#     r = n-1
#     mid=(l+r)//2 #akhona sob somoy floor division nita hoba
#     for i in range(n):
#         if arr[i] == mid:
#             return i
#         elif s_data > arr[mid]:
#             l= mid +1
#         else:
#             r= mid-1
#
#
# arr=[12,23,4,5,7,8,9,10,13,14]
# s_data=int(input("Input search Data :"))
# n=len(arr)
#
# print(Bineary_search(arr,n,s_data))

"""
  another Bineary search program
"""


def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1

arr=[5,6,7,8,9,10,11,12,13,14,15]
low=0
high=len(arr)-1
x=11

result=binary_search(arr,low,high,x)
print(result)

# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")








# def Bineary_search(arr,x,l,h,n):
#     mid = (l + h) // 2
#     for i in range(n):
#         if arr[i] == mid:
#                 return mid
#         elif x > arr[mid]:
#                 l= mid +1
#         else:
#               r= mid-1
#
# arr=[4,5,6,7,8,9,10,11,12,13,25]
# x=int(input("Input search values :"))
# low=0
# high=len(arr)-1
# n=len(arr)
#
# print(Bineary_search(arr,x,low,high,n))
