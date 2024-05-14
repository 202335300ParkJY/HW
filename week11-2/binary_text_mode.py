np_c = bytes([128])
np_c_str = np_c.decode('ascii',errors='ignore')
np_c1 = bytes([129])
np_c1_str = np_c.decode('ascii',errors='ignore')
null_c = bytes([0])
null_str = null_c.decode('ascii', errors='ignore')

with open('bin2txt.txt', 'wb') as f:
    f.write('a'.encode('ascii'))
    f.write(np_c)
    f.write(null_c)
    f.write(null_c)
    f.write(np_c1)
    f.write('b'.encode('ascii'))