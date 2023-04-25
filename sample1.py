def add(number1, number2):
    return number1 + number2

num1 = 4
num2 = 5
total = add(num1, num2)
print("The sum of {} and {} is {}".format(num1, num2, total))

# pip3 install pylint==2.11.1
# pylint sample1.py
# Pylint goes through every line of code and gives you a list all the non-compliant lines.
# Pylint gives you a compliance score (10 being maximum).