Lengthofseries=int(input("The length of seires you want is: "))
n1=0
n2=1
count=0
if Lengthofseries<0:
    print("Fibonacci series not possible")
elif Lengthofseries==1:
    print("Fibonacci series is",n1)
else: 
    print("Fibonacci series:")
    while count<Lengthofseries:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count=count+1
              
 
    