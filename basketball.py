'''a=[1,2,3,4,5]
for i in a:
    if a[i]>0:
        n = (a[i]*i+1)+(a[i+1]*(i+2))
        print(n)'''

inp1=int(input())
inp2=int(input())
arr=list(map(int,input().split()))
max=-1
for i in range(0,len(arr)-inp2+1):
    temp=arr[i:i+inp2]
    k,s=1,0
    for j in temp:
        s += (j*k)
        k += 1
    if s > mx:
        mx=s
    print(mx)
        