def HM_get_generator(end):
    for i in range(0, end+1):
            yield i 
g = HM_get_generator(3) 

for i in g:
    print(i)