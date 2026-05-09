l1=[11,22,33,44,55]
l2=[66,77,88,99,110]
# Concatenation
l3 = l1 + l2
print("Concatenated List:", l3)
# Repetition
l4 = l1 * 3
print("Repeated List:", l4)
l1.extend(l2)  # Using extend() to add elements of l2 to l1
l5=[11,22,33,44,55]
l6=[66,77,88,99,110]
l7=[11,22,33,44,55] 
x=l5==l7#boolean value will be printed True because both lists are same
y=l5 != l6
z=l5<l6
a=l6>l5#boolean value will be printed True because all elements of l6 are greater than l5
b=l5<=l7
c=l6>=l5#boolean value will be printed True because all elements of l6 are greater than l5    
d=l5==l6
print(x)#boolean value will be printed True because both lists are same
print(y)#boolean value will be printed True because both lists are not same
print(z)#boolean value will be printed True because all elements of l5 are less than l6
print(a)#boolean value will be printed True because all elements of l6 are greater than l
print(b)#boolean value will be printed True because both lists are same
print(c)#boolean value will be printed True because all elements of l6 are greater than l5
print(d)#boolean value will be printed False because both lists are not same    