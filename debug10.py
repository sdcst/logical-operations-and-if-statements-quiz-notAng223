#!python3
"""
Debug this program so that it runs correctly

original code:
x = 3
y = 4
if x or y  >= 3 :
    print("at least 1 number is greater than or equal to 3") 
elif x >= 3:
    print('only x is greater than or equal to 3')
elif y >= 4:
    print('only y is greater than or equal to 4')
else
    print("Both numbers are less than 3")
"""
# i dont exacly know what to do here, if "at least 1 number is greater than or equal to 3" then 
# "only x is greater than or equal to 3" or "only y is greater than or equal to 4" will never run.
# It seems like you want me to make it so that it prints "Both are greater than or equal to 3", 
# "x is greater than 3 or equal to", "y is greater than or equal to 3" or "neither are greater than or equal to 3"
# however, that would require changing the print statements and so far it seems like those are to be unchanged
# overall to prove to you (and myself) that I can do this, I have created 2 seporate code pieces depending on
# that exactly you want me to fix.

# if you cant mark whatever one is the correct interpritation or 
# if my comments just dont make any sence just mark #1


# interptritation #1 (primary)
x = 3
y = 4
if x >= 3 and y  >= 3 :
    print("both numbers are greater than or equal to 3") 
elif x >= 3:
    print('only x is greater than or equal to 3')
elif y >= 4:
    print('only y is greater than or equal to 4')
else:
    print("Both numbers are less than 3")

print("--------")
# interptritation #2 (secondary)
x = 3
y = 4
if x >= 3 or y  >= 3 :
    print("at least 1 number is greater than or equal to 3")

if x >= 3:
    print('only x is greater than or equal to 3')
elif y >= 4:
    print('only y is greater than or equal to 4')
else:
    print("Both numbers are less than 3")


