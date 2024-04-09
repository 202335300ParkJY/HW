# 클래스 예시
class MyClass:
    def __init__(self, name):
        self.name = name
        
    def say_hello(self):
        print(f"hello, my name is {self.name}")
        
# 클래스 인스턴스 생성
my_instance = MyClass("Bard")

# 클래스 이름 확인
print(my_instance.__class__.__name__) # MyClass

# 예외 처리 예시

try:
    raise ValueError("This is an error")
except ValueError as e:
    print(e.__class__.__name__) # ValueError
    