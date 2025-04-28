# Write a program to find the second smallest number in an array?

arr = [1]

if len(arr) < 2:
    print("array must have atleast two elements")

else:
    smallest = second_smallest = float('inf')

    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    if second_smallest == float('inf'):
        print("There is no second smallest element (all elements must be same)")
    else:
        print("The second smallest number is: ", second_smallest)


