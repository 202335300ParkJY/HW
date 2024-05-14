# 32 bytes 의 데이터.
bin_data = bytearray(range(0,32))
# bin_data = bytes(bin_data)

with open('bfile.bin', 'wb') as fout:
    cnt = fout.write(bin_data)
    print(f'{cnt} bytes is written!')
    
