#this is used to check if a string starts with a specific prefix and ends with a specific suffix
s = 'hello how are you doing today?'
s1=s.startswith(  'hello')#check if string starts with 'hello'
s2=s.endswith('today?')#check if string ends with 'today?'
print(s1)
print(s2)#syntax: string.startswith(prefix,start,end) and string.endswith(suffix,start,end)
s3=s.removeprefix('hello ')#removes the prefix 'hello ' from the string
s4=s.removesuffix(' today?')#removes the suffix ' today?' from the string
print(s3)#syntax: string.removeprefix(prefix) and string.removesuffix(suffix)
print(s4) 
s5=s.partition('are')#partitions the string into a tuple of three parts: the part before the separator, the separator itself, and the part after the separator
print(s5)#syntax: string.partition(separator)
s6=s.rpartition('are')#partitions the string into a tuple of three parts    : the part before the separator, the separator itself, and the part after the separator, searching from the right
print(s6)#syntax: string.rpartition(separator)  
s7='hello how are you doing today? hello'
s8=s7.replace('hello','hi',1)#replaces the first occurrence of 'hello' with 'hi'
print(s8)#syntax: string.replace(old,new,count)  
