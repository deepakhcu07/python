# Program to sort list of integers using Selection Sort


# Defining a selection sort method

def selection_sort(numbers ):
    n = len(numbers)

    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if numbers[j] < numbers[min] :
                min = j
        if i!= min:
            numbers[i], numbers[min] = numbers[min], numbers[i]

    return numbers




numbers = [11,7,18,5,45,23,22]

print("\n Before Sorting ")
print(numbers)
numbers = selection_sort(numbers)
print("\n After Sorting")
print(numbers)