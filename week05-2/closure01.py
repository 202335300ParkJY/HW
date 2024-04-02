def gen_closure(p):
    call_cnt = 0
    
    def _ds_power (b, return_cnt=False):
        nonlocal call_cnt
        call_cnt += 1
        ret =b**p
        if not return_cnt:
            return ret
        return ret, call_cnt

    return _ds_power

p2_func = gen_closure(2)
print(p2_func(10))

P3_func = gen_closure(3)
r, c_p3 = P3_func(10, True)
print(r)

r, c_p2 = p2_func(10, True)
print(f'10^2={r}')
print(f'power2 : call_cnt={c_p2}')
print(f'power3 : call_cnt={c_p3}')

for idx,c in enumerate(P3_func,__closure__):
    print(f"p3_func's encising variable[{idx}]:{c,cell_contenrs}")
