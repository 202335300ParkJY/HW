x = 10 # 글로벌 변수

def foo(): # 로컬 변수
    x = 20
    print(x)
    
foo() # 20
print(x) # 10
