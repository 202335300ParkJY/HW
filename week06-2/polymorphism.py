class Dog:
    def __init__(self,name):
        self.name = name

    def bark(self):
        print("멍멍")

    def __str__(self):
        return f"Dog {self.name}"

class Poodle(Dog):
    def bark(self):
        print("왈왈")

    def __str__(self):
        return f"Poolde {self.name}"

class Samoyed(Dog):
    def bark(self):
        print("컹컹")
    def __str__(self):
        return f"Samoyed {self.name}"

if __name__ == "__main__": # 각기 다른 행동들
    d0 = Poodle("뽀미")
    d1 = Samoyed("삐삐")
    d2 = Samoyed("엘씨")
    l = [d0,d1,d2]

    for c in l:
        c.bark() # 동일한 메세지 하나만으로 다들 각자 본인이 할 것들(각기 다른 하울링)을 함.
        if isinstance(c, Dog):
            print(f"{c} is a Dog.")
        else:
            print(f"{c} is not a Dog.")
