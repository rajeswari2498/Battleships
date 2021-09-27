#Write the function getFirstName(fullName),
#  which takes a string holding a two-word full name (in the format "Donald Knuth") 
# and returns just the first name.
#  You can assume the first name will be the first word of the name.
def getFirstName(fullName):
    a=fullName.split()[0]
    b=fullName.split()[1]
    return a
print(getFirstName("Donald Knuth"))