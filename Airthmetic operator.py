#Airthmetic Operator
#(  + , - , * , / , % ,// (Floor division) and ** (Exponent)
print("enter a number")
a=int(input())
print("choose operation")
print("add --> For addition\nsub --> For subtraction \nmul --> For Multiply \ndiv --> For Division \nmod --> For Modulus \nfdiv --> For Floor Division \nexpo --> For Exponent")
choose=str(input())
print("Enter Second Number")
if choose=="add":
    b=int(input())
    print(a+b)
elif choose=="sub":
    b=int(input())
    print(a-b)
elif choose=="mul":
    b=int(input())
    print(a*b)
elif choose=="div":
    b=int(input())
    print(a/b)
elif choose=="mod":
    b=int(input())
    print(a%b)
elif choose=="fdiv":
    b=int(input())
    print(a//b)
elif choose=="expo":
    b=int(input())
    print(a**b)
else:
    print("\t\t Invalid Operation")
    print("Please Open Your Headlight(Eyes) And Type Correct Operation.  \n\t\t   ThankYou")
    
