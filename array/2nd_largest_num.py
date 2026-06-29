num = [12,15,53,69,32,10,56,2,3,9]
largest=num[0]
sec_larg=num[0]
for i in range(len(num)):
    if num[i]>largest:
        largest = num[i]

for i in range (len(num)):
    if (num[i]>sec_larg and num[i] != largest ):
        sec_larg = num[i]
print("2nd largest number is",sec_larg)
print("1st largesr" ,largest)                
