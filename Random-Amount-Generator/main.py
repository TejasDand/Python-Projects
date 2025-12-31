from statistics import mean
from random import randint
import math

def round_up_to_nearest_10(n):
    """
    Rounds a number up to the nearest multiple of 10.
    """
    # Divide by 10, round up to the nearest integer, then multiply by 10
    return math.ceil(n / 10) * 10 

def range_input(a, b):
    """
    Taking input from the user to create a random amount and also shows the average of that random amounts.
    """

    r = int(input("How much random numbers do you want? "))
    avg = []
    
    for i in range(1, r+1):
       random_amount = randint(a, b)
       avg.append(random_amount)
       
       print(f"{i}. {round_up_to_nearest_10(random_amount)}")

    print(f"The average is: {round(mean(avg), 2)}")


num1 = int(input("Enter lower number: "))
num2 = int(input("Enter higher number: "))

range_input(num1, num2)