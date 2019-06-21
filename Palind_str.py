print("verify given String is palindrome or not")
print("Enter String")
s=input()
l=len(s)
p=""
for n in range(l-1,-1,-1):
    p=p+s[n]
if p==s:
    print("It is Palindrome")
else:
    print("It is not Palindrome")
