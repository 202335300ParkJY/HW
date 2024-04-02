def ex_func(j):
    
    def nested_func(i):
        return i ** 2
    
    for c in range(j):
        print(nested_func(c))