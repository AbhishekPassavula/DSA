row=int(input("Number of rows:"))
col=row
#row for loop
for i in range(row):
    #column for loop
    for j in range(row):
        #printing "*" symbol
        if j==0 or i==row-1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()