s1='xyz'
s2='acd'
# Joining strings with a space separator
s3=s1.join(s2)#This will join the two strings with the separator as s1
print(s3)#Output: 'axzyd'
s4='-'
s5=s4.join(s2)#This will join the two strings with the separator as s4
print(s5)#Output: 'a-c-d'
s6=' '
s7=s6.join(s2)#This will join the two strings with the separator as s6
print(s7)#Output: 'a c d'
# The original strings remain unchanged, as strings in Python are immutable.
print(s1)#xyz
print(s2)#acd