from array import *
val = array('I',[54,45,60,23,35,69])

val.insert(1,269)
val.append(969)
val[3]=300

copyArray = array(val.typecode ,(x for x in val))
                  
for i in range(0,len(val)):
    print(copyArray[i], end=" ")