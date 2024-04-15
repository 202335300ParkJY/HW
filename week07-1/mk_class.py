class CustomClass (SuperClass0) : # class 정의 헤더. 클래스의 이름과 부모를 지정.

    # class
    class_variable0 = None # class가 가지는 attribute를 assignment로 생성.

    @classmethod # @classmethod 데코레이터(클로저와 같음)를 통해 classmethod를 정의
    def class_method(cls, *args): # class method 정의 (필요하지 않은 경우가 많음), *args은 paching으로 *은 무한적으로 받겠다는 의미.
        # 첫번째 파라메터 cls에 class method를 호출하는 class객체가 할당됨.
        print(f'{cls.class_variable0=}') # cls.을 앞에 붙이고 접근함.
        
#---------------------위에 두 문단은 사용해도 되고 안해도됨. 아래 instance 매우 중요!!!----------------        

    # instance
    def __init__(self, *args): 
        # 생성자. 반드시 만들고, 여기서 instance attribute를 할당으로 추가함.
        # self 는 생성되는 instance를 가르킴.
        super().__init__()             # 부모 클래스의 생성자는 거의 대부분 꼭 호출해줘야함. 
        self.instance_variable0 = None # instance attribute를 assignment로 생성. 동적으로 할당해서 동적으로 제거 가능하나 절대 사용 금지. -> 생성자에서 하는 것이 맞음.
        self.instance_variable1 = None # instance attribute를 assignment로 생성. 위와 같음. 그리고 반드시 self. 해야함.

    def instance_method(self, *args): # instance method 정의.
        print(type(self).cv)           # class variable에 접근 가능.
        print(CustomClass.cv)          # class이름으로 class variable에 접근.
        print(self.instance_Variable0) # instance variable에 접근 가능.

    # static # class method와 유사함. class에 하나씩 할당하는 공유함. @staticmethod 추가 필수. 자유롭지만 비워두면 현재 class에 접근 불가. 재활용이 떨어지나 fure function(입력 받고 연산만 하는)에서만 사용.
    @staticmethod
    def static_method(): # static method 정의.
        # instance의 variable을 바꾸지 않는 pure function 만드는데 사용됨.
        # class method로 거의 대부분 대처 가능하므로 많이 사용되지 않음.
        print(CustomClass.cv)          # class이름으로 class variable에 접근.