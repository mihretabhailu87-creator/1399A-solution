k = int(input())
for _ in range(k): 
    count = False
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n-1):
        if abs(a[i+1]-a[i])>1:
           count=True
           break
    print("NO" if count else "YES")

    

    

    




    