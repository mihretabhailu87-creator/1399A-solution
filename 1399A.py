k = int(input())
for _ in range(k): 
    posible = False
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n-1):
        if abs(a[i+1]-a[i])>1:
           posible=True
           break
    print("NO" if posible else "YES")

    

    

    




    