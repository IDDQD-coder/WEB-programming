dict = {}
count_dict = {}
counter = 0
print('Ведите количество использований кэша')
counter = int(input())
def decorator_arg(arg=int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            global dict
            global count_dict
            if args in dict:
                if count_dict[args] == arg:
                    count_dict[args] = 0
                    dict[args] = str(func(*args, **kwargs))
                    print("Пересчитано")
                    return str(dict[args])
                else:
                    print("Из кэша")
                    count_dict[args] += 1
                    return str(dict[args])
            else:
                dict[args] = str(func(*args, **kwargs))
                count_dict[args] = 0
                print("Посчитано")
                return str(dict[args])
        return wrapper
    return decorator
@decorator_arg(counter)
def IsSimple(x):
    for i in range(2, x):
        if (x % i) == 0:
            return str("False")
    return str("True")
list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in list:
    print(i, ' ', IsSimple(i))
    print(' ')
