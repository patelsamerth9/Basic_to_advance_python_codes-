l1=[1,2,3,4,5,6,6,7,8,9,10 ]     
l1=l1.append(11)
print(l1)  # This will print None because append() returns None
l2=[1,2,3,4,5,6,6,7,8,9,10 ]     
l2=l2 + [11]
print(l2)  # This will print the updated list with 11 added at the end