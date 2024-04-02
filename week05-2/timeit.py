import timeit
unpack = ['사과', '바나나', '복숭아', '자두']

def test_fn0 ():
  ret = [ *unpack, *reversed(unpack)]
  return ret

print('the case of * :', round(timeit.timeit(test_fn0, number= 1000000),4))

def test_fn1 ():
  ret = [list(unpack), list(reversed(unpack))]
  return ret

print('the case of old approach :', round(timeit.timeit(test_fn1, number= 1000000),4))