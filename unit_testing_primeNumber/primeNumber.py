# ----------------------------------------------------------------
def prime_number():
  """
  Return True/False is an input number is prime or not
  """
  number = input("Your number :")
  try:
    for i in range(2, int(number)):
      if (int(number)%i) == 0:
        return False
    return True
  except ValueError:
    print("Invalid number")


