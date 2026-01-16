import re
re.match('abc', 'abcdef')
print(re.match('abc', 'abcdef'))  # <re.Match object; span=(0, 3), match='abc'>
re.search('abc', '123abcdef')
print(re.search('abc', '123abcdef'))  # <re.Match object; span=(3, 6), match='abc'>
re.findall('abc', 'abcdefabcghi')
print(re.findall('abc', 'abcdefabcghi'))  # ['abc', 'abc']
re.sub('abc', 'xyz', 'abcdefabcghi')
print(re.sub('abc', 'xyz', 'abcdefabcghi'))  # 'xyzdef  