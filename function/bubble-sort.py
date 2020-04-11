# Program to sort the list of integers




# Defining a function
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(i+1,n):
            if numbers[i] > numbers[j]:
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp




numbers = [11,7,18,5,45,23,22]

print("\n Before Sorting ")
print(numbers)
bubble_sort(numbers)
print("\n After Sorting")
print(numbers)