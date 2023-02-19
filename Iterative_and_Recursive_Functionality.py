#factorial function with both iterative and recursion

#define the numbers for use in functions
num1 = int(0)
num2 = int(5)
num3 = int(10)
num4 = int(25)
num5 = int(50)
num6 = int(100)

           
#iterative factorial
def iter_factorial(num):
    total = 1
    for i in range(1, num+1):
        total = total * i
    return total

#print the results of use of iterative function
print("Factorial results with an iterative function")
print(f"{num1}! = {iter_factorial(num1)}")
print(f"{num2}! = {iter_factorial(num2)}")
print(f"{num3}! = {iter_factorial(num3)}")
print(f"{num4}! = {iter_factorial(num4)}")
print(f"{num5}! = {iter_factorial(num5)}")
print(f"{num6}! = {iter_factorial(num6)}")


#recursion factorial
def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

#print the results of use of recursive function
print("Factorial results with a recursive function")
print(f"{num1}! = {factorial(num1)}")
print(f"{num2}! = {factorial(num2)}")
print(f"{num3}! = {factorial(num3)}")
print(f"{num4}! = {factorial(num4)}")
print(f"{num5}! = {factorial(num5)}")
print(f"{num6}! = {factorial(num6)}")

