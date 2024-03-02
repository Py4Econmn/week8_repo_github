## Regular expression
# https://www.rexegg.com/regex-lookarounds.html - lookahead, behind
import re

# stata example
# word by word decomp
# D-F orsn ugnud

# regex, regexp
# meta characters
# [] . ^ $ * + ? {} () \ |
# 

#special sequences
#https://pynative.com/python-regex-special-sequences-and-character-classes/

# regex tool
# https://regex101.com/


# findall - find all matches within the string
string = 'hello 12, hi 8987. Howdy 34'
pattern = '\d+' # find all numbers      + *(greedy algorithm)
result = re.findall(pattern, string) 
print(result)

result2 = re.findall('\d{1,2}', string) 
result2 = re.findall('\d{2}', string) 
result3 = re.findall('\d{3}', string) 
result1 = re.findall('\d{1}', string) 

re.findall('[D-F]', "LIFE is really cool. Looking forward to it.") # find CAPITAL letters between D and F
re.findall('[D-F]+', "LIFE is really cool. Looking forward to it.")

# search – first match anywhere in string
string = "My iPython is fun console of Python "
match = re.search('Python', string) # search word Python
match.group()
match = re.search('Bold', string) # search word Python
match.group() # match == None
re.findall('Python', string)

string = '39801 356, 2102 1111'
pattern = '(\d{3})\s(\d{2})' # Three digit number followed by space followed by two digit number
# match variable contains a Match object. 
match = re.search(pattern, string) 

match.group(1)
match.group(2)
match.group(1, 2)
match.groups()

# no group
pattern = '\d{3}\s\d{2}'
match = re.search(pattern, string) 
match.group()
pattern = '(\d{3})(\s)(\d{2})'
match = re.search(pattern, string) 
match.group(3)

# lookahead, behind
string = '39801 356, 2 102 11 is 11'
pattern = '\s(\d{3})\s(\d{2})\s' # Space, three digit numbers followed by space, followed by two digit number
# match variable contains a Match object. 
match = re.search(pattern, string) 

string = '39801 356, 2aa_adfd102 11 dlfjdk is 11'
pattern = '(?<!\d)(\d{3})\s(\d{2})(?!\d)' # Three digit number followed by space followed by two digit number
# match variable contains a Match object. 
match = re.search(pattern, string) 
match

string = '39801 356, 2aa_adfd102 11 dlfjdk is 11 153 22'
pattern = '(?<!\d)(\d{3})\s(\d{2})(?!\d)' 
match = re.findall(pattern, string) 
match


# match - match at the beginning of string
result = re.match("[0-9]{1,3}", "hi 12345 bhey 135456")
result = re.match("[0-9]{1,3}", "12345 dfdf 456")
result.group()


# split
string = 'Twelve 121563245, Eighty 1 nine 89.'
pattern = '\d{}'
result = re.split(pattern, string) 
print(result)

result = re.split("\s+", "  Baldan   Gombo ") 
print(result)

result = re.split("\s", "  Baldan   Gombo") 
print(result)

# sub
string = 'abc 12\
de 23 \n f45 6'
pattern = '\s+'
replace = ''
new_string = re.sub(pattern, replace, string) 
print(new_string)


text = "Dorj Bat. He was born on 17th of February, 1995\
Has got bachelor degree. Phone: 99779977, uses Mobicom. \
Graduated 3rd secondary school of Khovd aimag. \
Citizen ID KhO95021701. PIN code of Khan bank card is 0011\
Lives with his wife and two children."


citizenId = re.findall("\w{2,4}(?=\d{8})\d{8}",text) # YeYe EE
citizenId2 = re.findall("\w{2,4}\d{8}",text) # YeYe EE
citizenId3 = re.findall("\w{2,4}(?<=\w)\d{8}",text)   # YeYe EE
# just numbers in ID
citizenId4 = re.findall("(?<=\w)\d{8}",text)   # YeYe EE

region    = re.findall("(Khovd|Uvs|Zavkhan)",text)  # r"D:\sugarkhuu\s"
mobileOperator = re.findall(r"(Mobicom|Unitel|Skytel|G-mobile)",text)
mobile_number  = re.search("(?<=\s)\d{8}",text).group()
bank           = re.findall("\s(\w+)\sbank",text)[0]
nChild         = re.findall("\s(\w*)\schildren",text)



# difference between * and +
text = 'ab ab17'
re.findall(r'ab\d+', text)
re.findall(r'ab\d*', text)



text = 'Ehner1Nuhur1Huuhed17'
re.findall(r'[a-z]+\d+[a-z]+\d+[a-z]+\d*', text,re.IGNORECASE)
re.findall(r'[a-z]+\d+[a-z]+\d+[a-z]+\d*', text)


# ?<= lookbehind, ?= lookahead
# + 1 or more, * 0 or more
# [a-z][A-Z][0-9] - groups w = [a-zA-Z0-9_]
# . any character, \ escape

# again
# https://regex101.com/