from random import *
import get_chars.get_chars

def password_generator(min_length, max_length):
  chars = get_chats()
  password = ''.join(choice(chars) for x in range(randint(min_length, max_length)))
  print('Password: %s' % password)
  return password
