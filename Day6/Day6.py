# Task 1
nums = [6, 5, 2, 10, 7]
print(nums)
nums = [i+2 for i in nums]
print("The updated list is:", nums)

# Task 2
x = 5
for i in range(0, x + 1):
    for j in range(x - i, 0, -1):
        print(j, end=' ')
    print()

# Task 3
n = int(input("Enter the number: "))
Fibonacci = [0, 1]
if n <= 0:
    print("The Fibonacci Series upto " + str(n) + " is: ", Fibonacci[0])
else:
    for x in range(2, n):
        num = Fibonacci[x-2] + Fibonacci[x-1]
        Fibonacci.append(num)
print("The Fibonacci series upto " + str(n) + " is:", Fibonacci)


# Task 4
def Armstrong(n):
    n = int(input("Enter the number: "))
    sum = 0
    temp = n

    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if n == sum:
        print(n, "is an Armstrong number")
    else:
        print(n, "is not an Armstrong number")


print(Armstrong(n))

# Task 5
for i in range(1, 11):
    print(9,"*",i,"=",9*i)

# Task 6
n = int(input("Enter the number: "))
if n==0:
    print(n," is 0")
elif n>0:
    print(n,"is POSITIVE")
else:
    print(n,"is NEGATIVE")

# Task 7
days = int(input("Enter the number of days: "))
years = int(days/365)
weeks = int((days % 365) / 7)
print("The Age for",days,"days is",years,"years and",weeks,"weeks.")

# Task 8
import math
sum_num = math.sin(math.pi/6) + math.cos(math.pi/4)
print("The sum of sin(π/3) and cos(π/4) is",sum_num)

# Task 9
print("Calculator")
print("Select: 1 -> Add  || 2 -> Substract || 3 -> Multiply || 4 -> Divide")
operation = int(input("Enter the operation choice: "))

if operation == 1:
    x = int(input("Enter operand 1:"))
    y = int(input("Enter operand 2:"))
    print("Addition of",x,"and",y,"is",x+y)
elif operation == 2:
    x = int(input("Enter operand 1:"))
    y = int(input("Enter operand 2:"))
    print("Subtraction of",x,"and",y,"is",x-y)
elif operation == 3:
    x = int(input("Enter operand 1:"))
    y = int(input("Enter operand 2:"))
    print("Multiplication of",x,"and",y,"is",x*y)
elif operation == 4:
    x = int(input("Enter operand 1:"))
    y = int(input("Enter operand 2:"))
    print("Division of",x,"and",y,"is",x/y)
else:
    print("Please make a valid Choice from 1 to 4")