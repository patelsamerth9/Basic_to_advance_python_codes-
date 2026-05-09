s='99776655'
s2=s.isdigit()#this is only valid for string containing only digits
print(s2)
s3='9977a6655'#this is false because of 'a' it only supports digits
s4=s3.isdigit()
print(s4)
s5=s.isdecimal()#this is only valid for string containing only decimal values
print(s5)
s6='99776.655'#this is false because of '.' it only supports decimal values
<<<<<<< HEAD
s7=s6.isdecimal()   
=======
s7=s6.isdecimal()#this is only valid for string containing only decimal values   
>>>>>>> 775b7034bdbbdf99f32c735c6a2ca588cb54215f
print(s7)
s8=s6.isascii()#this is valid for string containing ascii values
print(s8)
s9=s6.isalnum()#this is valid for string containing alphanumeric values
print(s9)
s10=s.isascii()#this is valid for string containing ascii values
print(s10)