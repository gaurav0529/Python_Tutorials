a="hello"
b="1234"
c="Hello world"
d="123der"
e=" "
print("isalpha")
print(a.isalpha())
print(b.isalpha())
print(c.isalpha())
print(d.isalpha())
print(e.isalpha())
print("\n")
print("isalnum")
print(a.isalnum())
print(b.isalnum())
print(c.isalnum())
print(d.isalnum())
print(e.isalnum())
print("\n")
print("isspace")
print(a.isspace())
print(b.isspace())
print(c.isspace())
print(d.isspace())
print(e.isspace())
print("\n")
print("startswith")
print(a.startswith("he"))
print("\n")
print("endswith")
print(c.endswith("ld"))
print("\n")
print("length of a",len(a))
f=a.ljust(20,"_")
print(f)
g=a.center(20,"_")
print(g)

  
