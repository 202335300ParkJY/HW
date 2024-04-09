class Myint(int):
    
    # int 클래스를 상속받아 __str__ 메서드를 overriding하는 예제
    
    
    def __str__(self):
        
        # __str__ 메서드를 overriding하여 10진수 문자열 대신 2진수 문자열을 반환합니다.
        
        return f"{bin(self)}"
    
def __repr__(self):
    return f"=>{hex(self), super().__repr__()}"

def __add__(self, op):
    # return super().__add__(op) - 2
    return int().__add__(self,op) - 2

# 예시
if __name__ == "__main__":
    num1 = Myint
    num2 = Myint
    
    ...
    
    
    
    
    # class My~~(MyOp)
    