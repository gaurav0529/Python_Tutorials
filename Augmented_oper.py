#Augmented Assignment Operator (+=, -=, *=, /=, %=, //=)
print("Enter a Number")
a=int(input())
print("choose operation")
print("add --> For addition\nsub --> For subtraction \nmul --> For Multiply \ndiv --> For Division \nmod --> For Modulus \nfdiv --> For Floor Division \nexpo --> For Exponent")
choose=str(input())
print("Enter Second Number")
b=int(input())
if choose=="add":
    a+=b
    print(a)
elif choose=="sub":
    a-=b
    print(a)
elif choose=="mul":
    a*=b
    print(a)
elif choose=="div":
    a/=b
    print(a)
elif choose=="mod":
    a%=b
    print(a)
elif choose=="fdiv":
    a//=b
    print(a)
elif choose=="expo":
    a**=b
    
    print(a)
else:
    print("\t\t Invalid Operation")
    print("Please Open Your Headlight(Eyes) And Type Correct Operation.  \n\t\t   ThankYou")
    

