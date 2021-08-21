a=int(input ("a="))
b=int(input ("b="))
c=int(input ("c="))
d=b*b-4*a*c
if d>0:
    x1=(-b+d**0.5)/(2*a)
    x2=(-b-d**0.5)/(2*a)
    print("X1=",(x1))
    print("x2=",(x2))
