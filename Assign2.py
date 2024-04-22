"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
import math

number_1 = float(input("enter a number: "))
number_2 = float(input("enter another number: "))
hypotenuse_float = input("is the first or second number the hypotenuse? (type first/second): ")

if hypotenuse_float=="first":
    hypotenuse_bool = 0
elif hypotenuse_float=="second":
    hypotenuse_bool = 1
else:
    print("ENTER ONLY FIRST OR SECOND! NOTHING ELSE!")
    exit()

hypotenuse = [number_1, number_2][hypotenuse_bool]
side = [number_1, number_2][1-hypotenuse_bool]

try:
    other_size = math.sqrt(hypotenuse**2 - side**2)

    print("the missing side is ~"+str(round(other_size,1))+" units long")
except:
    print("THE HYPOTHENOUS OR SIDE VALUES ARE INVALID TRY AGAIN WITH CORRECT NUBMERS!!")



