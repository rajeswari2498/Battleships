#write a function that finds the maximum value in a list of integers (without using the built-in max function).
def maximum(a):
    max = 0
    b=[1,4,8,6,5]
    for i in range(0,len(a)):
        if a[i] > max:
            max = a[i]
    return max
b=[1,4,8,6,5]
print (maximum(b))

