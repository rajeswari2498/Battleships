def seperate(s):
    l = len(s)
    temp = s[0:len(s)-1:2]+s[1:len(s)-1:2]
    return temp

print(seperate("a-c-e-g-i-")) 
