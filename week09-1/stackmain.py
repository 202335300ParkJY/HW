from stack import Stack

def main():
    # 스택 클래스 생성
    stack = Stack()

    # 스택에 요소 추가
    stack.push(10)
    stack.push(20)
    stack.push(30)

    # 스택의 top 요소 확인
    stack.peek()

    # 스택에서 요소 제거
    stack.pop()
    stack.pop()

    # 스택이 비어 있는지 확인
    print(f"스택이 비어있나? {stack.is_empty()}")

    # 스택의 top 요소 확인
    stack.peek()

    # 스택에서 요소 제거
    stack.pop()

    # 스택이 비어 있는지 확인
    print(f"스택이 비어있나? {stack.is_empty()}")

if __name__ == '__main__':
    main()
