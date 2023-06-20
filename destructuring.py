#unpacking operator * aka destructuring

a = (1,2,3,4,5)
x, *rest = a
print(x)


a = [1, 2, 3, 4]
b = [4,5,6]
x,y,z,w = a
c,*rest = a
l =[*a,*b]
print(a)

#to destructuring
while(c):
    t,*l=l
    print(t)

print(*a)

print()