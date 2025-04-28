# # Write a program to find the second smallest number in an array?

# arr = [10, 1, 20, 2, 4, 6]

# if len(arr) < 2:
#     print("array must have atleast two elements")

# else:
#     smallest = second_smallest = float('inf')

#     for num in arr:
#         if num < smallest:
#             second_smallest = smallest
#             smallest = num
#         elif smallest < num < second_smallest:
#             second_smallest = num
#     if second_smallest == float('inf'):
#         print("There is no second smallest element (all elements must be same)")
#     else:
#         print("The second smallest number is: ", second_smallest)




# # Write a program to find the second largest number in an array?

# # Sample array
# arr = [12, 5, 8, 19, 1, 19, 7]

# # First, check if the array has at least two elements
# if len(arr) < 2:
#     print("Array must have at least two elements")
# else:
#     # Initialize first and second largest to a very small value
#     largest = second_largest = float('-inf')

#     for num in arr:
#         if num > largest:
#             second_largest = largest
#             largest = num
#         elif largest > num > second_largest:
#             second_largest = num

#     if second_largest == float('-inf'):
#         print("There is no second largest element (all elements might be the same)")
#     else:
#         print("The second largest number is:", second_largest)





# # Find the 3rd largest element without sorting
# arr = [1, 6, 3, 4, 5, 2]

# if len(arr) < 3:
#     print("Array must have at least three elements")

# else:
#     first = second = third = float('-inf')

# for num in arr:
#     if num > first:
#         third = second
#         second = first
#         first = num
#     elif first > num > second:
#         third = second
#         second = num

#     elif second > num > third:
#         third = num

# if third == float('-inf'):
#     print("There is no third largest element (elements may be duplicates)")
# else:
#     print("The third largest element is: ", third)




# #Find the 3rd smallest element without sorting

# arr = [2, 3, 55, 7, 7, 10]

# if len(arr) < 3:
#     print("Array must have at least 3 elements")
# else:
#     first = second = third = float('inf')

#     for num in arr:
#         if num < first:
#             third = second
#             second = first
#             first = num
#         elif first < num < second:
#             third = second
#             second = num
#         elif second < num < third:
#             third = num
#     if third == float('inf'):
#         print("There is no third smallest element(elements may be duplicates)")
#     else:
#         print("Third smallest number is ", third)




# # Find the kth largest element in the array

# arr = [3, 4, 2, 6, 4, 8, 1, 9]

# k = 3

# if k > len(arr) or k <= 0:
#     print("Invalid value of k")

# else:
#     unique_arr = list(set(arr))

# if k > len(unique_arr):
#     print("Not enough unique elements")
# else:
#     largest_elements = []

#     while k > 0:
#         max_num = float('-inf')
#         for num in unique_arr:
#             if num > max_num:
#                 max_num = num

#         largest_elements.append(max_num)
#         unique_arr.remove(max_num)

#         k -= 1
#         print(f"The kth largest element is: {largest_elements[-1]}")