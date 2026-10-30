def main():
    # Create an empty list to store the numbers
    numbers = []
    
    print("Please enter 20 numbers.")
    
    # Ask the user to enter 20 numbers using a loop
    for i in range(20):
        while True:
            try:
                # Prompt the user for a number
                num = float(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                
    # Calculate required data
    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    
    # Display the results
    print("\n--- Number Analysis Results ---")
    print(f"Lowest number: {lowest}")
    print(f"Highest number: {highest}")
    print(f"Total of the numbers: {total}")
    print(f"Average of the numbers: {average}")

# Call the main function to run the program
if __name__ == "__main__":
    main()
