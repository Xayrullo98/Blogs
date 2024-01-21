# # def binary_search(list, elem):
# #     first = 0
# #     last = len(list) - 1
# #
# #
# #     while first < last:
# #         mid = (first + last) // 2
# #         guess = list[mid]
# #         if guess == elem:
# #              return f"Found {guess}"
# #         if elem < guess:
# #             last = mid - 1
# #             print(last, 'last')
# #         else:
# #             first = mid + 1
# #             print(first, 'first')
# #     return None
# # print('ddddd')
# # print('ddddd')
# #
# #
# # d = binary_search([1, 2, 3, 4, 5, 6, 7, 8], 6)
# # print(d)
#
# # def arrangeCoins( n: int) -> int:
# #     j = 1
# #     while n > 0:
# #
# #         print(j,'dddddddddddddddddd')
# #         j += 1
# #         n -= j
# #         print(n, 'fffff')
# #     return j-1
# # s = arrangeCoins(8)
# # print(s)
#
#
# import turtle
# j = turtle.Turtle()
# j.forward(20)
# print(j)
#

"""
Sort the following string alphabetically, from z to a, and assign it to the variable sorted_letters.
letters = "alwnfiwaksuezlaeiajsdl"
"""

letters = "alwnfiwaksuezlaeiajsdl"

f = list(letters)
f.sort()
f.reverse()
sorted_letters = ''.join([i for i in f])
print(sorted_letters)

"""
Given the same dictionary, medals, now sort by the medal count. Save the three countries with the highest medal count to the list, top_three.

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
"""


# def g(k,d):
#
#     return d[k]
# medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
# ks = medals.keys()
#
# top_three = sorted(ks,key=lambda x : g(x,medals),reverse = True)[:3]
# print(top_three)
#
# def last_four(x):
#     f = list([str(i)[-4:] for i in x])
#     return f
# ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
# d = last_four(ids)
# d.sort()
# d.reverse()
# print(d)
#
#
# def change(string):
#     return str(string).join(" Nice to meet you!")

#
# def findSmaller(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index
#
#
# def selectionSort(arr):
#     newArr = []
#     for i in range(len(arr)):
#         smallest = findSmaller(arr)
#         newArr.append(arr.pop(smallest))
#     return newArr
#
#
# print(selectionSort([5, 3, 6, 2, 10]))

def insertion_sort(arr):
    for i in range(1,len(arr)-1):
        value = arr[i]
        while arr[i-1]>value:
            arr[i-1],value = value,arr[i-1]
            i=i-1
    return arr

print(insertion_sort(arr=[2,33,4,5,5,6,7,8,8,9]))
