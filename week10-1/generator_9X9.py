r0 = [ (i, j, i * j) for i in range(2,10) for j in range(1,10) if i == 2]

for i in r0:
    print(f'{i[0]} * {i[1]} = {i[2]}')
    
# r1 = ( (i,j,i * j) for i in range(2,10) for j in range(1,10) if i == 2)
# type(r1)

# enumerate로도 코드 작성이 가능함. (중요)