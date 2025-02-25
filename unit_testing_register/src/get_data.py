#!/usr/bin/env python3
# coding: utf-8

# ----------------------------------------------------------------
def get_username():
  """
  - not empty
  - no spaces
  """
  username=input("Your username :")
  if (len(username) and " " not in username):
    return username
  else:
    print("Invalid username")

# ----------------------------------------------------------------
def get_password():
  """
  - at least 8 characteres
  - at least one number
  - at least one letter
  - at least one special character
  """

  password = input("Your password :")
  if (len(password) > 7) and \
     any(i.isdigit() for i in password) and \
     any(i.isalpha() for i in password) and \
     any(not i.isalnum() for i in password):
    return password
  else:
    print("Invalid password")


# ----------------------------------------------------------------
def get_email():
  """
  - contains a @
  - contains a .
  """
  email = input("Your e-mail address :")
  if '@' in email and '.' in email:
    return email
  else:
    print("Invalid email")


# ----------------------------------------------------------------
# ----------------------------------------------------------------
if __name__=='__main__':
#  get_username()
#  get_password()
  get_email()
