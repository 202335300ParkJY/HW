class Model:
  def train(self):
    print('train!!')
  def predict(self):
    print('predict!')

class MyANN:
  def __init__(self, model):
    self.model = model