b=int(input("enter the no::"))
a=[1,3,5,7,9,11,12,15]
if(b%2==0):
    b=b-1
    for i in range(0,b):
        print(a[i])