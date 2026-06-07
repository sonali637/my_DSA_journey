# find the missing number in an array using summation and XOR operation
# summition method:
def get_miss_summ(a):
    n =a[-1]
    total=n*(n+1)//2
    summ=sum(a)
    print(total-summ)

a=[1,2,4,5,6,7]
get_miss_summ(a)

print('\n')

# XOR method
def get_miss_nu_xor(a):
    n=len(a)
    xor_a =a[0]
    x2=0
    for index in range(1,n):
        xor_a=xor_a^a[index]
    for index in range(1,n+2):
        x2=x2^index
    print(xor_a^x2) 
a=[1,2,4,5,6,7]      
get_miss_nu_xor(a)    
