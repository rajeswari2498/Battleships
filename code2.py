def count(s1, s2):
    str1=s1.lower()
    str2=s2.lower()
    if str2 in str1:
        return str1.count(str2)
    return 0
print(count("MissiSSippi", "Ss"))


