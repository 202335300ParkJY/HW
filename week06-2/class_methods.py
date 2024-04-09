class Test:

  cnt = 0  # class variable

  def __init__(self):
    self.ins_v = 0
    Test.cnt += 1

  @classmethod
  def get_Test_Cnt(cls):
    print(f'{type(cls)}: {isinstance(cls,Test)}')
    return Test.cnt

  # # manual로 class method로 만들기!
  # get_Test_cnt = classmethod(get_Test_Cnt())

a = Test()
print(Test.get_Test_Cnt())
b = Test()
print(Test.get_Test_Cnt())

# instance를 통해서도 호출이 가능함.
print(a.get_Test_Cnt())