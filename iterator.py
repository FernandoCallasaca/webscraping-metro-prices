my_list = [1,2,3,4,5]

my_iter = iter(my_list)

try:
   while True:
      print(next(my_iter))
except StopIteration as st:
   print(st)
finally:
   print('Successful execution!')
