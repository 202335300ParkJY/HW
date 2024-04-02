src0 = [1, 7, 5]
src1 = [2, 3, 8]

def list(map(lambda x: abs(x[0]-x[1]), zip(src0,src1)))
print(def) # 결과는 다음과 같음 : [1, 4, 3]