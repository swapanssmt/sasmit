import numpy as np 
def rot(a,b,i,j,lom):
    id=np.identity(lom)
    theta=np.arctan(b/a)
    print("Value of theta= ",theta)
    id[i+1][i+1]=np.cos(theta)
    id[j][j]=np.cos(theta)
    id[i+1][j]=(-1)*np.sin(theta)
    id[j][i+1]=np.sin(theta)
    print("Rotation matrix")
    print(np.round(id,4))
    return id
A=np.array([[15,4,3,2,-1],[4,25,6,-7,8],[3,6,27,8,9],[2,-7,8,319,10],[-1,8,9,10,100]])
B=A
print("STEPS : ")
lom=len(A[0])
for k in range(lom):
    for l in range(k+2,lom):
        bm=rot(B[k][k+1],B[k][l],k,l,lom)
        B=((bm.transpose()).dot(B)).dot(bm)
        print("Matrix after multiplying ratation matrix")
        print(np.round(B, 4))
rounded = np.round(B, 4)
print("Orginal Matrix")
print(A)
print("tri-diagonal Matrix")
print(rounded)
