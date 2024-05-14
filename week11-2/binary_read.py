r_bin = bytes()
with open('./week11-2/bfile.bin', 'rb') as fin:
    chunk = 5
    while buf := fin.read(chunk):
        r_bin += buf
print(len(r_bin))
print(list(map(int,r_bin)))