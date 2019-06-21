print("Armstrong")
print("Enter Number")
a=input()
l=len(a)
A=0
a=int(a)
for i in range(l):
    r=a%10
    A=A+r**l
    a//=10
print(A)
