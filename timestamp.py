import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
a=int(input('enter the time right now'))

if (a>0 and a< 12):
    print('GOOD MORNING SIR')
elif ( a>12 and a<6):
    print('good afternoon sir')
else:
    print('good evening sir')