class Stack(list): # append와 pop, peak, is_empty와 같이 스택을 구현할 떄 필요한 메서드가 존재하기 때문에 리스트로 받는다.
    def __init__(self):
        # 초기화 시 list의 생성자를 호출하여 빈 리스트를 생성한다.
        super().__init__()

    def push(self, element):
        # 스택에 요소를 추가하는 메서드로, element를 스택에 추가한다.
        self.append(element)
        print(f"'{element}'을 push합니다.")

    def pop(self):
        # 스택에서 요소를 제거하는 메서드로, 스택이 비어있으면 None 반환한다.
        if self.is_empty():
            print("스택이 비었습나다. element를 pop하지 못합니다.")
            return None
        # 부모 리스트 클래스으 pop 메서드를 사용해서 요소를 제거하고 반환한다.
        element = super().pop()
        print(f"'{element}'을 pop합니다.")
        return element

    def is_empty(self):
        # 스택이 비어 있는지 확인하는 메서드로, 스택의 길이가 0인지 아닌지 확인하고 결과 반환한다.
        return len(self) == 0

    def peek(self):
        # 스택의 top 요소를 확인하는 메서드로, 스택이 비어있으면 None 반환한다.
        if self.is_empty():
            print("스택이 비었습나다. element를 pop하지 못합니다.")
            return None
        # 스택의 마지막으로 push된 값인 top 요소를 반환한다.
        top_element = self[-1]
        print(f"마지막으로 push된 값은 '{top_element}'")
        return top_element
