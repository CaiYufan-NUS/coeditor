import random
import char

def password_generator(min_length, max_length):
  chars = char.get_chars()
  random.shuffle(chars)
  password = ''.join(random.choice(chars) for x in range(random.randint(min_length, max_length)))
  print('Password: ' + password)
  return password

password_generator(10, 18)
