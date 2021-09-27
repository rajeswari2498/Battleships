lst = ["a", "b", 1, 2] 
#We are assigning a variable called lst and in that we are giving some parameters
print(lst[1])
#By using the variable we have to print the lst[1] so the output will print as b
s = " " 
#we are assigning a varaible called s
for i in range(len(lst)):
#We are assigning the for loop and i is the variable 
# with in the range we are finding out the length of the lst and 
# it will repeat the condition until the lst is printed.
    s = s + str(lst[i])
# By this condition we are finding out the length of the lst
print(s)
#The output of s will be printed