def myTuple(*args):
    print(args)

def myDict(**kwargs):
  if 'age' in kwargs:
    print('the age is {}'.format(kwargs['age']))
  else:
    print('there is no age')

myTuple(1,2,3)
myDict(name='test', age=12)