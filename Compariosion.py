#Comparision Operator (>,<,>=,<=,!=,==)
print("Enter two numbers for Comparision")
a=int(input())
b=int(input())
print(" Choose Operations:- \n<  Less Than\n>  More Than\n<=  Less Than Equal To\n>=  More Than Equal To\n!=  Not Equal To\n==  Equal To")
choose=input()
if choose=="<":
    print(a<b)
elif choose==">":
    print(a>b)
elif choose=="<=":
    print(a<=b)
elif choose==">=":
    print(a>=b)
elif choose=="!=":
    print(a!=b)
elif choose=="==":
    print(a==b)
else:
    print("Invalid operator")
