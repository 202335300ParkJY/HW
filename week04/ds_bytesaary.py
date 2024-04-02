print('test')

def ds_print(c):
    print(f'(c & 0xFF :#88b)')
    
a = bytearray([0b00000000])
b = bytearray([0b11111100])

c0 = a[0]^b[0]
ds_print(c0)
c1 = ~b[0]
ds_print(c1)
