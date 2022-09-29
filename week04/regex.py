import re


def find_name(line):
    #this gives first and last names that are formated properly.
    pattern = r'[A-Z][a-z]\w* [A-Z][a-z]\w*' 
    result = re.findall(pattern,line)
     #This will take any common title and will print the properly formated name until a space
    pattern = r'((?:Dr\.|Mr\.|Ms\.|Miss|Mr|Ms) [A-Z][a-z]\w*[A-Z][a-z]\w*)'
    result = result + re.findall(pattern,line)
  #First initial, last name
    pattern = r'([A-Z]\s[A-Z][a-z]\w*)'
    result = result + re.findall(pattern,line)
    return result
    pattern = r'((?:Dr\.|Mr\.|Ms\.|Miss|Mr|Ms) [A-Z][a-z]\w*)'
    result = result + re.findall(pattern,line)
  #First initial, last name
    pattern = r'([A-Z]\s[A-Z][a-z]\w*)'
    result = result + re.findall(pattern,line)
    return result
  #inital and . followed by last name or last name followed by , and first name
    pattern = r'([A-Z],\s*[A-Z][a-z]\w*)'
    result = result + re.findall(pattern,line)
    return result

f = open("names.txt")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)
