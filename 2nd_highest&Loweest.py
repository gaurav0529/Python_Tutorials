print("second Highest and second Lowest from the list")
print("Number of List Elements")
n=int(input())
l=[]
print("Enter Number to create List")
for i in range(n):
    l.append(input())
print("Created List",l)
l.sort()
print("Sorted List",l)
print("Second Highest No : %s\nSecond Lowest No :%s"%(l[n-2],l[1]))
