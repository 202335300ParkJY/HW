src_list = range(1,10)
print(src_list, type(src_list))

ret_list = [x**2 for s in src_list if x%2 == 0]

ret_list = []
for x in src_list:
    tmp = x**2
    ret_list.append(tmp)
print(ret_list)
