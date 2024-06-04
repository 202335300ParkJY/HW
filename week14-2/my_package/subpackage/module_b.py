from .module_a import greet

def greet_from_b():
    return __name__ + ":" + greet()

if __name__ == "__main__":
    print(greet_from_b())
