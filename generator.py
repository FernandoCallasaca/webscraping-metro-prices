def my_gen():
   a = 1
   yield a

   a = 2
   yield a

   a = 3
   yield a

my_first_gen = my_gen()
print(next(my_first_gen))
print(next(my_first_gen))
print(next(my_first_gen))


def pair_numbers():
   i = 2
   while True:
      yield i
      i+=2

pair_numbers_100 = pair_numbers()

for i in range(100):
   print(next(pair_numbers_100))