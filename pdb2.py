a=20
b=10


s=0
for i in range(a):
    # this line will raise zeroDivision error
    s +=a/b
    b -=1
