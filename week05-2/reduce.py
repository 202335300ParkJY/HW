from functools import reduce

src = [1,2,3,4,5]

dst = reduce(lambda i,j: i+j, src)
print(dst) # 결과 : 15