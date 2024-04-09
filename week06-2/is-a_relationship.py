class Human:
    def __init__(self, name):
        Human.ds_type = "Human"
        self.job = None
        self.name = name

    def introduce(self):
        print("------------------------")
        print(f"제 이름은 {self.name}입니다.")
        print(f"제 직업은 {self.job}입니다.")
        print(f"저의 종족은 {Human.ds_type}입니다.")

class Warrior (Human): # is-a relationship

    def __init__(self, name):
        super().__init__(name)
        self.job = "Warrior"

    def bash (self):
        print("강타 능력")