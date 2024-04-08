class Samp:
    def get_x(self):
        return self.x
if __name__ == "__main__":
    s = Samp() # S에 instance가 있음 
    s.x = 23 #주석처리시 에러. -> 동적으로 만들게 된다면 어디서 만들어졌는지 알 수 없음.
    # 생성자를 만들어서 특별한 method를 만들고 내가 할 것들을 초기화해서 할당하고 호출하는게 맞음.
    print(s.get_x())