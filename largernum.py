a1=int(input())
k=list(map(int,input().split()))
k.sort(reverse=True)
for i in range(0,a1):
  print(k[i],end="")
