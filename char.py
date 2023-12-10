import string

def get_chars():
  letters = [letter for letter in string.ascii_letters]
  digits = [digit for digit in string.digits]
  symbols = [symbol for symbol in string.punctuation]
  chars = letters + digits + symbols
  return chars
