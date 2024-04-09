class Car:

  def __init__(self, name="Anony"):
    self.name = name
    self.speed = 0

  def start(self,speed=30):
    self.speed = speed

  def stop(self):
    self.speed = 0

  def accelerate(self,speed):
    self.speed = self.speed + speed

  def __str__(self): # special method or magic method라 함. 이것들은 대응하는 오퍼레이터나 함수가 존재해 결과를 반환하고 반환된 것을 print에 넣음.
    return f"{self.name}:speed={self.speed}"

if __name__ == "__main__":
  a = Car("붕붕이")
  a.start() # 출발 메세지, 출발
  print(a)
  a.accelerate(20) # 액셀 메세지, 가속해
  print(a)
  a.stop() # 정지 메세지, 멈춰
  print(a)