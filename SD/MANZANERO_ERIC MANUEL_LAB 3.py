# Bubble Sort and Linear Search Implementation

def bubble_sort(numbers):
    """Sorts a list using Bubble Sort algorithm."""
    n = len(numbers)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]  # Swap
    return numbers

def linear_search(numbers, target):
    """Searches for a number in the list using Linear Search."""
    for index, num in enumerate(numbers):
        if num == target:
            return index  # Return index if found
    return -1  # Return -1 if not found

# Main program
try:
    # Input: Accept a list of numbers
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    # Sorting using Bubble Sort
    sorted_numbers = bubble_sort(numbers)
    print("\nSorted Numbers:", sorted_numbers)

    # Searching for a number
    target = int(input("\nEnter number to search for: "))
    index = linear_search(sorted_numbers, target)

    # Output the search result
    if index != -1:
        print(f"✅ Number found at index {index}")
    else:
        print("❌ Number not found.")
except ValueError:
    print("⚠️ Error: Please enter valid numeric values.")
