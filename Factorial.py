def factorial(number):
    if number == 0:
        return 1
    elif number == 1:
        return 1
    else:
        print(number)
        return number*factorial(number - 1)
    
print(factorial(4))