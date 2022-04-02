o=int(input("Enter how many number want to put in list"))
p=[]
for i in range(o):
    q=int(input())
    p.append(q)
print("given list-",p)
k=list(map((lambda a:a*3),p))
print("-output list-",k)