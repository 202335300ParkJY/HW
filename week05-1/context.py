x = 10 # 전역 

def foo(a):
    b = 2 # 함수 컨텍스트
    return a + b

class Myclass:
    c = 3 # 클래스 컨텍스트 
    
    def __init__(self, d):
        self.d = d # 인스턴스 컨텍스트
        
    def method (self, e):
        f = 5 # 메서드 컨텍스트
        return self.d + e + f
    
result = foo(1) # 함ㅅ 호출에 따른 함수 컨텍스트 생성
print(result0) # 3

my_obj = Myclass(4) # 클래스 인스턴스 생성에 따른 인스턴스 컨텍스트 생성
result = my_obj.method(6) # 메서드 호풀에 따른 메서드 컴텍스트 생성
print(result) # 15
