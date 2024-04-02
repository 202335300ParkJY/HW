def test_fn( a, *, key0=None):
  """ a 파라메터까지만 positional argument로 할당가능하고, 
  * 이후에 있는 key0는 keyword argument로만 사용가능함.
  """
  print(f'a={a}')
  print(f'key0={key0}')

a = 10
test_fn(a)
test_fn(a,key0=1)
