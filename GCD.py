largenum=int(input("Enter the large number:"))
smallnum=int(input("Enter the small number:"))
while(smallnum):
    numstore=smallnum
    smallnum=largenum%smallnum
    largenum=numstore
print("the GCD is:", largenum)