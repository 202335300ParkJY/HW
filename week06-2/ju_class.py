
class MyOp:
    #---------------------------------------------------
    #이 부부능 생략가능함.
    #
    # class attribute ( class variable, class methods, instance mrthods)
    
    # 1. class variable
    cnt = 0
    type = "MyOp."
    version = "0.1"
    
    @classmethod # 어떤  특수한 기능을 아래의 함수에 추가해줌.
    def print_version(cls):
        print(cls.version)
        
    #---------------------------------------------------
    # instance attributes
    #
    def __init__(self):
        self.ret_value = None # instance variable, instance attributes
        MyOp.cnt += 1
        
    def run(self, a, b):
        print('operands=',a,b)
        return self. ret_value    
        
    @staticmethod # class 자체에 대한건 없으나 class attribute에 접근만 가능. 다른 언어에서는 중요하게 사용. 선언한 곳에 정적으로 있음.
    def s_method():
        pass
    
        
if __name__ == "__main__":
    MyOp.print_version()
    print(MyOp.cnt)
    
    a = MyOp()
    print(MyOp.cnt)
    print(a.cnt)
    
    b = MyOp()
    print(b.cnt)
    
    a.run(3,4)
    b.run("a","b")
    
    print('===========')
    # or MyOp.run(a, 3, 4)
    a.run(3, 4)