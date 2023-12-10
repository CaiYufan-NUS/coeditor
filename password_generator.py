from random import *
def password_generator(min_length, max_length):
  password = ''.join(choice(chars) for x in range(randint(min_length, max_length)))
  print('Password: %s' % password)
  return password
