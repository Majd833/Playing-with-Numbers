def hcf(smallnum,largenum):
    while(smallnum):
        numstore=smallnum
        smallnum=largenum%smallnum
        largenum=numstore
    return largenum
largenum=int(input("Enter the large num:"))
smallnum=int(input("Enter the small num:"))
lcm=int(smallnum/hcf(smallnum,largenum)*largenum)
print("the lcm is:",lcm)