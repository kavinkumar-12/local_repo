ar=int(input("enter number of rows of matrix A : "))
bc=int(input("enter number of columns of matrix B : "))
abc=int(input("enter number of columns of A and rows of B : "))

matrix_A=[]
matrix_B=[]
result=[]


for i in range(0,ar):
    row=list()
    for j in range(0,abc):
        a=int(input(f"matrix A [{i}][{j}] : "))
        row.append(a)
    matrix_A.append(row)

for i in range(0,abc):
    row=[]
    for j in range(0,bc):
        a=int(input(f"matrix B [{i}][{j}] : "))
        row.append(a)
    matrix_B.append(row)
print("\n\n")
for i in range(0,ar):
    for j in range(0,abc):
        print(f"{matrix_A[i][j]}",end=" ")
    print("\n")
print("\n")
for i in range(0,abc):
    for j in range(0,bc):
        print(f"{matrix_B[i][j]}",end=" ")
    print("\n")        

for i in range(0,ar):
    row=list()
    for j in range(0,bc):
        temp=0
        for k in range(0,abc):
            a=matrix_A[i][k]*matrix_B[k][j]
            temp+=a
        row.append(temp)
    result.append(row)

for i in range(0,ar):
    for j in range(0,bc):
        print(f"{result[i][j]}",end=" ")
    print("\n")    