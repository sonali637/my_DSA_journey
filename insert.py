from array import *
val = array('i',[54,45,60,23,35,69])

val.insert(3,50)
for i in range(0,len(val)):
    print(val[i], end=" ")