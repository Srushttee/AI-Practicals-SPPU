import time

def selection_sort(arr):
    n = len(arr)

    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

        # Display the current state of the array after each swap
        print(f"Step {i + 1}: {arr}")

# Input from the user
try:
    n = int(input("Enter the number of elements: "))
    if n <= 0:
        raise ValueError("Number of elements should be greater than 0.")

    arr = [int(input(f"Enter element {i + 1}: ")) for i in range(n)]

    print("\nOriginal array:", arr)

    # Record start time
    start_time = time.time()

    # Perform selection sort
    selection_sort(arr)

    # Record end time
    end_time = time.time()
    
    # Display sorted array
    print("\nSorted array:", arr)
    
    # Display time complexity
    print("\nTime Complexity: O(n^2)")
    
    # Display space complexity
    print("Space Complexity: O(1)")
    
    # Display total execution time
    print(f"Total Execution Time: {end_time - start_time:.6f} seconds")

except ValueError as e:
    print(f"Error: {e}")
