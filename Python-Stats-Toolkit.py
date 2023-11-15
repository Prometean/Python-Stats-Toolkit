# Function to receive correct input
def get_input():
    while True:
        try:
            # Create the list numbers that take the inputs of the users.
            numbers = [int(x) for x in input("Enter a list of numbers separated by spaces:").split()]
            return numbers
        except ValueError:
            # This block is execute if the convertion to int fails
            print("Please, enter only numbers. Try again.")

# Function to get average and median from the input numbers of the users
def calculate_avg_median_list(numbers):
    # Creating variable to receive list length
    len_nums = len(numbers)
    # Sorting list numbers
    numbers = sorted(numbers)
    
    if len_nums == 0:
        print("List is empty. Please, next time insert a list of numbers separated by spaces")
        return 
    
    # Calculate the avg 
    avg = sum(numbers) / len_nums 
    print(f"The average of the list is: {avg}")
    
    # Calculation of the median
    if len_nums % 2 != 0:
        median = numbers[len_nums // 2]
    else:
        median = (numbers[(len_nums // 2) - 1] + numbers[len_nums // 2]) / 2
    
    print(f"The median number of the list: {median}") 
    
# Calling the function
numbers = get_input()

# calling & printing function 
calculate_avg_median_list(numbers)