def HM_get_generaotr(end):
    r = range(0, end+1)
    l = list(r)
    yield from l
    
g = HM_get_generaotr(3)

for i in g:
    print(i)
