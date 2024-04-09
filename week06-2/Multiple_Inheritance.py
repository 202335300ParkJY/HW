class Human: # super class임.
    def __init__(self, name): # self는 instance의 이름./ __init__ 은 생성자임. 복잡한 지식 없이 생성 가능.
        Human.ds_type = "Human"
        self.job = None
        self.name = name

    def introduce(self): 
        print("------------------------")
        print(f"제 이름은 {self.name}입니다.")
        print(f"제 직업은 {self.job}입니다.")
        print(f"저의 종족은 {Human.ds_type}입니다.")

class Warrior (Human): # 이 아래에 것들은 다 sub class임.

    def __init__(self, name):
        super().__init__(name)
        self.job = "Warrior"

    def bash (self):
        print("강타 능력")

class Knight(Warrior):
    def __init__(self, name):
        super().__init__(name)
        self.job = "knight"
    def riding (self):
        print("말타기 능력")

class Healer (Human):
    def __init__(self, name):
        super().__init__(name)
        self.job = "Healer"

    def healing (self):
        print("치료하기 능력")
        
        
class Paladin (Knight, Healer):
    def __init__(self, name):
        super().__init__(name)
        self.hob = "Paladin"     

if __name__ == "__main__": # 다 instance임.
    ins0 = Human("김 아무개")
    ins1 = Warrior("이 아무개")
    ins2 = Healer("박 아무개")
    ins3 = Knight("박 기사")
    ins4 = Paladin("서 아무개")
    ins4,introduce()
    ins4.healing()
    ins4.riding()
    
print(Paladin.mor())
     # 이걸 통해 한번에 가능해(공동 작업)/ 같은 introduse로 했는데 직업이 다 다르게 나오는 것을 "다양성"으로 봄.
        # 입력 값을 넣으면 다 출력값이 나오는데, type에 따라 조금 다르게 표현할뿐임.
# 단순히 코드를 따라서 입력하기 보다는 자신에게 맞도록 수정해야한다.

