def IsSimple(x):
    for i in range(2,x):
        if (x%i)==0:
            return str("False")
    return str("True")
    
print("Input number: ")
x=int(input())
print(IsSimple(x))