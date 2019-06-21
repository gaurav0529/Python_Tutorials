print("verify given Number is palindrome or not")
print("Enter Number")
n=input()
l=len(n)
n=int(n)
N=n
P=0
for i in range(l):
    r=n%10
    P=P*10+r
    n=n//10
print("Given Number is ",N)
print("Reverse Number is ",P)
if P==N:
    print("Number is Palindrome")
else:
    print("Number is Not Palindrome")
