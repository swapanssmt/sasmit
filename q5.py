import numpy as np 
def sn(va,i,fn):
    if(va>0):
        return 1
    elif(va<0):
        return -1
    else:
        return (fn[i-1])
def f(A,l):
    fn=np.ones(len(A[0])+1)
    fn1=np.ones(len(A[0])+1)
    fn1[1]=l-A[0][0]
    fn[1]=sn((l-A[0][0]),1,fn)
    for i in range(2,len(fn)):
        val=((l-A[i-1][i-1])*fn1[i-1])-((A[i-1][i-2])**2)*fn1[i-2]
        fn1[i]=val
        fn[i]=sn(val,i,fn)
    return fn
def snchange(M):
    j=0
    inti=-1
    for i in range(len(M)):
        if(M[i]==inti):
            j=j+1
            inti=inti*(-1)
    return j
def env(n,ns):
    fnl=[]
    for t in range(1,len(ns)):
        if(ns[t-1]!=ns[t]):
            fnl.append([n[t-1],n[t]])
    return fnl
def lr(n):
    ns=[]
    for k in n:
        ns.append(snchange(f(A,k)))
#    print(ns)
    return env(n,ns)
A=np.array([[15,5.4772,0,0,0],[5.4772,66.3,96.5585,0,0],[0,96.5585,282.6678,9.9845,0],[0,0,9.9845,62.1587,40.6893],[0,0,0,40.6893,59.8735]]) #put tri-diagonal matrix obtained in question 4
nl=500
n=np.arange(-3,nl)
lrange=lr(n)
#print (lrange)
en=[]
for y in range(len(lrange)):
    x=np.arange(lrange[y][0],lrange[y][1]+0.01,0.01)
#    print(x)
    en.append(lr(x))
print("tri-diagonal setup achieved from Q4")
print(A)
for g in range(len(en)):
    print(g+1," eigenvalue is in range ",en[g]," so eigen value is approx. ",np.round((en[g][0][0]+en[g][0][1])/2,3))
