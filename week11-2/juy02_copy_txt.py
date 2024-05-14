r_bin = bytes()
with open('./week11-2/bfile.bin', 'rb') as fin:
    chunk = 5
    while buf := fin.read(chunk):
        r_bin += buf
print(len(r_bin))
print(list(map(int,r_bin)))

def juy02(src, dst):
    with open(src, 'rb', encoding='utf-8', errors='ignore') as fin:
        buf = fin.read()
        
    with open(dst, 'rb', encoding='utf-8', errors='ignore') as fout:
        fout.write(buf)
        # print(buf)
        
src = 'C:/Usere/GC.Downloads/linux_cmds.md'
dst = 'out0.txt'
juy02(src, dst)

