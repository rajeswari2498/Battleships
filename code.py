#Write a python program that stores "Donald Knuth" in a variable.
#  Use the string operators to extract the first name i.e., "Donald",
#  and store it in a variable. Similarly, extract the last name, i.e., Knuth, 
# and store it in another variable. 
# Print the Last name followed by First name to the screen. 
# So, the output has to be Knuth Donald.
#str="Donald Knuth"
#d1=str[0:6]
#d2=str[7:12]
#print(d2+" "+d1)
#s="Donald Knuth" l=len(s) name= s[0:6] last= s[7:l] print(last+" "+name)

#Write the function getFirstName(fullName), 
# which takes a string holding a two-word full name (in the format "Donald Knuth") 
# and returns just the first name. 
# You can assume the first name will be the first word of the name separated by a space.
#  Device an algorithm such that the function extracts the first name for any given fullName.
#def getFullName(fullName):
 #   temp=""
  #  for i in range(len(fullName)):
   ##    if fullName[i]==" ":
     ##print(getFullName("Donald Knuth"))

s="Donald Knuth"
for i in range(len(s)):
    if s[i]=="":
        s[i]=s[:6]
print(s[i])




