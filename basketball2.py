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
    if s>max:
        max=s
print(max)
    
         