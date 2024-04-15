# closuer 로 인자로 주어진 self_arg를 통해
# 특정 instance를 설정하고,
# 해당 instance의 x attribute를 출력하는 
# 함수를 반환.
def some_method(self_arg): # closure기법으로 self를 기억.
    def func():
        print(f"hi! : {self_arg.x}")
    return func

class Samp:
    def get_x(self):
        return self.x


class SampTwo:
    def get_x(self):
        return self.x

if __name__ == "__main__":
    s = Samp()
    s.x = 23 #주석처리시 에러.
    s.dynamic_get = some_method(s)  # 동적 method추가.
    s.dynamic_get() #23

    print("------------")
    s2 =SampTwo()
    s2.x = 77
    s2.dynamic_get = some_method(s2)
    s2.dynamic_get() #77
    s2.x = 33
    s2.dynamic_get() #33

    print("------------")
    s2.dynamic_get_one = some_method(s) # s의 x를 출력하는 function을 s2메서드로 등록.
    s2.dynamic_get_one() # 23
    s.x = 2323
    s2.dynamic_get_one() # 2323, 이런 유연성은 안쓰는게 낫지 않을까?
    print("------------")
    print(s.get_x())
    print("------------")
    del s.x  # attribute인 x를 동적으로 제거
    print(s.get_x()) # attribute가 제거되어 AttributeError가 발생함.
