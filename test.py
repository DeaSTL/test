import math

a = "password"
b = 2
for i in a:
    b = b ^ hash(i)*1000000000
    print(b)
