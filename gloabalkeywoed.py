g_x = 10

def func(i):
    global g_x
    tmp = i + g_x
    g_x = 20
    print(tmp)
    
func(11)
print(g_x)