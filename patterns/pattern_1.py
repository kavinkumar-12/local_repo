def printbox(a):
    l=(n*2)+(n-2)*2
    for j in range(1,1+n):
        print("#",end=" ")
        h=j
    print()
    for j in range(l,l-(n-2),-1):
        print("#"," "*(((n-2)*2)-1),"#")
        h+=1
    for k in range(l-(n-2),h,-1):
        print("#",end=" ")

n=int(input("enter a number to print box pattern : "))
printbox(n)