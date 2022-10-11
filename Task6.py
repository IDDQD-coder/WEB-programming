dict = {} 
def decorator (func): 
    def wrapper(x): 
        global dict 
        if x in dict: 
            print("Из кэша") 
            return str(dict[x]) 
        else:   
            dict[x]=str(func(x)) 
            print("Посчитано") 
            return str(dict[x])     
    return wrapper 
@decorator 
def IsSimple(x): 
    for i in range(2,x): 
        if (x%i)==0: 
            return str("False") 
    return str("True") 
     
list=[1,2,1,4,7,5,9,6,4] 
for i in list: 
    print(i,' ',IsSimple(i))
