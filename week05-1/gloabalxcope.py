# Global Scope!, g_func 와 nested_func에서 모두 접근이 가능하며 global 키워드가 적용됨
g_x = 'global'

def g_func(x):
    # Local Scope!, g_func의 function namespace로 g_func 의 관점에선 local이라고 불림.
    l_x = 'local of g_func'

    # Non-local Scope!, nested_func의 관점에서는 
    # nonlocal 키워드가 적용되는 Non-local scope임 (global과는 구분이 된다.).
    non_local_x = 'non-local'

    print('global_variable : ',g_x)
    print('parameter : ',x)
    print('local_variables of g_func :', l_x, non_local_x)

    def nested_func():
        # nested_func 의 관점에선 local임.
        l_x = 'local of nested func'
        l_y = 'y : local of nested func'
        print('global_variable : ',g_x)
        print('nonlocal of nested_func :', non_local_x)
        print('local_variables of nested_func :', l_x)

    nested_func()
    print(l_y) # NameError 발생. l_y 는 이 곳에서는 정의가 되지 않음. 
g_func(11)
print(non_local_x) # NameError 발생. non_local_x 는 이 곳에서는 정의가 되지 않음.
