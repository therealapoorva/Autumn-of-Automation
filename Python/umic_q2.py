x=input()
a=int(x)
while True:
    s= '10'
    while s != s[::-1]:
        a+=1
        s=str(a)
    print(a)
    break

