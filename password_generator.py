from random import *
import char

def password_generator(min_length, max_length):
  chars = char.get_chars()
  password = ''.join(choice(chars) for x in range(randint(min_length, max_length)))
  print('Password: %s' % password)
  return password
