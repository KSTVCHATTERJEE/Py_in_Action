
x = int(input("Enter first number "))
y = int(input("Enter second number "))
z = x+y
print("Sum = ",z)

number = float(input("Enter a number "))
if number>0:
    print("Positive Number")
elif number==0:
    print("Zero")
else:
    print("Negative Number")
    
    
def diff21(n):
    if n>21:
        result = 2*abs(n-21)
    else:
        result = 21-n
    return result

n = int(input("Enter a number"))
result = diff21(n)
print(result)

def sum_double(x,y):
    if x==y:
        result=2*(x+y)
    else:
        result=x+y
    return result
x = int(input("Enter 1st No. "))
y = int(input("Enter 2nd No. "))
result=sum_double(x,y)
print(result)

def missing_char(str,n):
    return str[0:n] + str[n+1:]
str = input("Enter String ")
n = int(input("Enter Index No "))
answer=missing_char(str,n)
print(answer)