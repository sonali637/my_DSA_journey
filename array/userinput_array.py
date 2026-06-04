from array import *
arr = array('i',[])
n = int(input('enter a number'))

                  
for i in range(0,n):
    arr.append(int(input("enter next input")))
for x in arr:
    print(x, end=" ")    