t=int(input())
for i in range(t):
    s1,s2=input().split(" ")
    p=s1[::-1]
    q=s2[::-1]
    if('t'+p[1:])==('t'+s2[1:]):
        print("Yes")
    elif('t'+s1[1:])==('t'+q[1:]):
        print("Yes")
    elif('t'+s1[1:])==('t'+s2[1:]):
        print("Yes")
    else:
        print("No")
