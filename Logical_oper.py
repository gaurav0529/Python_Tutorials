#Logial Operator (and, or, not)
print("There is range 0 to 50")
print("Choose Operations\n-->and\n-->or\n-->not")
o=input()
if o=="and":
    print("-->To print No. more than 0 AND less than 20")
    for a in range(50):
        if a>0 and a<20:
            print(a)
elif o=="or":
    print("\n\n-->To print No. more than 0 OR less than 20")
    for b in range(50):
        if b>0 or b<20:
            print(b)
elif o=="not":
    print("\n\n-->To print No. more than 0 OR less than 20")
    for c in range(50):
        if  not c<25:
            print(c)
    
