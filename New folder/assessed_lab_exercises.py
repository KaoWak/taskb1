
# Week 4
def calculator(num1, num2, operator):
    """
    This function performs basic arithmetic and comparison operations on two numbers.

    Parameters:
    num1 (int or float): The first number.
    num2 (int or float): The second number.
    operator (str): A string representing the operation to perform. The valid operators are:
        - "+" for addition
        - "-" for subtraction
        - "*" for multiplication
        - "/" for division
        - "%" for modulus
        - ">" for greater than comparison
        - ">=" for greater than or equal to comparison
        - "<" for less than comparison
        - "<=" for less than or equal to comparison

    Returns:
    result: The result of the arithmetic operation or comparison. The type of the result depends on the operator:
        - int or float for arithmetic operations
        - bool for comparison operations

    Example Usage:
    --------------
    calculate(4, 5, "*")  # Output: The result is: 20
    calculate(10, 2, "/")  # Output: The result is: 5.0
    calculate(7, 7, ">=")  # Output: The comparison result is: True

    Note:
    -----
    - If division by zero is attempted, the function prints an error message and does not return a result.
    - If an invalid operator is provided, the function prints an error message and does not return a result.
    """
    result = None
    #None != None
    if operator == "+":
        result = num1 + num2
        print(f"The result is: {result}")
    elif operator == "-":
        result = num1 - num2
        print(f"The result is: {result}")
    elif operator == "*":
        result = num1 * num2
        print(f"The result is: {result}")

    elif operator == "/":
        if num2 == 0:
         return("divide by 0 is not posssible")
        else :
            result = num1 / num2
            print(f"The result is: {result}")

    elif operator == "%":
        result = num1 % num2
        print(f"The result is: {result}")

    elif operator == ">":
        if num1 > num2:
            result = True
        else :
            result = False
        print(f"The result is: {result}")

    elif operator == ">=":
        if num1 >= num2:
            result = True
        else :
            result = False
        print(f"The result is: {result}")

    elif operator == "<":
        if num1 < num2:
            result = True
        else :
            result = False
        print(f"The result is: {result}")

    elif operator == "<=":
        if num1 <= num2:
            result = True
        else :
            result = False
        print(f"The result is: {result}")
    else:
        return("Invalid operator.")

    return result
def max_of_three(num1, num2, num3):
    """
    This function takes three integers as input and returns the maximum of the three given numbers.

    Parameters:
    num1 (int): The first number.
    num2 (int): The second number.
    num3 (int): The third number.

    Returns:
    int: The maximum of the three numbers.
    """
    # Hint: you are required to make use of maximum variable that is returned by the function below.
    # Complete your code implementation here...
    maximum = num1 
    if num2 > num1 : 
        maximum = num2 

    if num3 > maximum : 
        maximum = num3 
    
    return maximum
def winning_numbers(user_list, winning_list):
    """
    This function checks if the user's numbers match the predefined winning numbers.

    Parameters:
    user_list (list): A list of three integers representing the user's chosen numbers.
    winning_list (list): A list of integers representing the winning numbers.

    Returns:
    str: A string indicating the prize won:
        - "First" if all three numbers match the winning numbers.
        - "Second" if two numbers match the winning numbers.
        - "Third" if one number matches the winning numbers.
        - "No" if none of the numbers match the winning numbers.

    Example:
    --------
    winning_list = [5, 14, 17]
    user_list = [3, 5, 10]
    result = winning_numbers(user_list, winning_list)
    # Output: "Third" (since one number, 5, matches the winning numbers)

    user_list = [14, 5, 10]
    result = winning_numbers(user_list, winning_list)
    # Output: "Third" (since two numbers, 14 and 5, match the winning numbers)

    The function also prints a message indicating the prize won.
    """

    # Function implementation here ...
    matches = len(set(user_list) & set(winning_list))
    if matches == 3:
        prize = "First"
    elif matches == 2 :
        prize = "Second"
    elif matches == 1 :
        prize = "Third"
    else : 
        prize = "No"

    # Print the result
    print(f"Congratulations, you won {prize} prize!")
    return prize

# Week 5
def are_anagrams(str1, str2):
    """
    This function checks if two strings are anagrams of each other.

    Parameters:
    ----------
    str1 : str
        The first string to be compared.
    str2 : str
        The second string to be compared.

    Returns:
    -------
    bool:
        Returns True if the two strings are anagrams, otherwise False.

    Example:
    --------
    are_anagrams("listen", "silent")  # Output: True
    are_anagrams("hello", "world")    # Output: False
    """

    # Function implementation here ...
    str1_sorted = sorted(str1.replace(" ", "").lower())
    str2_sorted = sorted(str2.replace(" ", "").lower())
    
    return str1_sorted == str2_sorted
def calculate_average(numbers):
    """
    This function calculates the average of a list of numbers using a for loop.

    Parameters:
    ----------
    numbers : list
        A list of numerical values (int or float).

    Returns:
    -------
    float:
        The average of the numbers in the list. If the list is empty, returns None.

    Example:
    --------
    calculate_average([10, 20, 30, 40, 50])  # Output: 30.0
    """
    
    # Function implementation here ...
    total = 0
    for sum in numbers:
        total += sum

    average = total / len(numbers)
    return average
def calculate_weekly_pay(hours_worked):
    """
    Calculate the weekly pay for an employee based on the number of hours worked.
    
    Parameters:
    hours_worked (int): The total number of hours worked by the employee in a week.
    
    Returns:
    float: The total weekly pay.
    """
    regular_rate = 12  # £12 per hour for up to 35 hours
    overtime_rate = 18  # £18 per hour for hours worked beyond 35 hours
    standard_hours = 35  # Threshold for regular pay


    total_pay = 0
    if hours_worked <= standard_hours:
        total_pay = hours_worked * regular_rate
    else:
        regular_pay = standard_hours * regular_rate
        overtime_hours = hours_worked - standard_hours
        overtime_pay = overtime_hours * overtime_rate
        
        total_pay = regular_pay + overtime_pay

    return total_pay
def is_prime(num):
    """Checks if a number is prime.

    Input:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:

    boolean = is_prime(5)   # returns True
    print(boolean)
    """

    if num < 2 : 
        return False
    if num == 2 :
        return True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def sum_of_evens(min_value, max_value):
    
    """Find the sum of even numbers between two given numbers (inclusive).

    Args:
        min_value (int): Minimum number
        max_value (int): Maximum number

    Returns:
        total: sum of the even numbers between min_value and max_value

    Example:

    min_value = 10
    max_value = 13
    total = sum_of_evens(min_value, max_value)
    print(total) # total is 22.

    """
    total = 0
    for value in range(min_value, max_value + 1):
        if value % 2 == 0:
            total += value

    return total

# Week 6
def celsius_to_fahrenheit(celsius):
   # complete your function implementation... 
   # return output
 
 conversion = 1.8 * celsius 
 fahrenheit = conversion + 32
 return fahrenheit 
def decrypt_cypher_text(encrypted_text, key):
#     # function implementation here...
    decrypted_text = ""
    for char in encrypted_text :
        ascii_code = ord(char)
        new_ascii_code = ( ascii_code - key) % 256
        decrypted_text += chr(new_ascii_code)
    return decrypted_text
def find_maximum_difference(a, b):
#     # code implementation here...
    max_a = max(a)
    min_a = min(a)
    max_b = max(b)
    min_b = min(b)

    maximum = max(abs(max_a - min_b), abs(max_b - min_a))

    return maximum
def fuel_cost(distance_miles):
# Constants
 MPG = 50  # Miles per gallon
 LITERS_PER_GALLON = 4.5
 PRICE_PER_LITER = 1.49  

 gallons_needed = distance_miles / MPG
    
 liters_needed = gallons_needed * LITERS_PER_GALLON 
 total_cost = liters_needed * PRICE_PER_LITER
    
 return total_cost
def is_golden_number(n):
#     # function implementation ...
    if n < 0 or n > 1000 : 
        return False 
    
    for a in range(1, n):
        b = n - a
        if (a * b) % 1000 == 0:
            return True
        
    return False #boolen
def km_to_miles(kilometers):
    # complete function implementation here...

    conversion = 0.6200 
    miles = kilometers * 0.62
    return round(miles, 3)
def letter_occurrence(input_string):
     # complete function implementation...
    # return count
   
    count = 0

    for x in input_string:
       
        if x == 'a' or x == 'A':

            count += 1

    return count
def annual_net_income(gross_salary):
    # complete your function implementation here...
    #return net_salary
    if gross_salary >= 45000:
        tax_rate = 0.50
    elif 30000 <= gross_salary < 45000:
        tax_rate = 0.30
    else:
        tax_rate = 0.15
        
    net_salary = gross_salary * (1 - tax_rate)
    return net_salary






