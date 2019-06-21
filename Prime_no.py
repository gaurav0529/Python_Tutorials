print("WAP to check number is prime or not")
print("Enter Number")
n=int(input())
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
        break
if flag==0 and n!=1:
    print(n," is Prime number")
else:
    print(n,"is not Prime Number")
