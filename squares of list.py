t=int(input("Enter how many number want to put in list"))
q=[]
for i in range(t):
    z=int(input())
    q.append(z)
print("given list-",q)
g=list(map((lambda b:b**2),q))
print("output-",g)