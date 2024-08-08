#def fact(a):
 #   if (a==1 or a==0):
  #      return 1
   # else:
    #    return a*fact(a-1)
#num=int(input("enter the number"))
#print("the factorial of the number is ", fact(num))
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
x=int(input("enter the number"))
result=factorial(x)
print(result)








 
def factorial(n):
   fact=1
   for i in range(1,n+1):
      fact=fact*i
      return fact
x=int(input("enter the number"))
result=factorial(x)
print(result)