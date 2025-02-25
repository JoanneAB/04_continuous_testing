#!/usr/bin/env python3
# coding: utf-8

import io
import sys
sys.path +=['../src']

from get_data import *

# ----------------------------------------------------------------
def test_username_NoSpace(monkeypatch):
  """
  Check if no space in username
  """
  monkeypatch.setattr('sys.stdin', io.StringIO('test test'))
  assert get_username() is None 

# ----------------------------------------------------------------
def test_username_NotEmpty(monkeypatch):
  """
  Check username not empty
  """
  monkeypatch.setattr('sys.stdin', io.StringIO('\n'))
  assert get_username() is None 

# ----------------------------------------------------------------
def test_username_correct(monkeypatch):
  """
  Check a correct username
  """
  monkeypatch.setattr('sys.stdin', io.StringIO('moi'))
  assert get_username() == 'moi'


# ================================================================
# ================================================================
def test_password_8char(monkeypatch):
  """
  Check password has at least 8 char
  """
  monkeypatch.setattr('sys.stdin', io.StringIO('qwertyu'))
  assert get_password() is None 

# ----------------------------------------------------------------
def test_password_1number(monkeypatch):
  """
  Check password has at least one number
  """
  monkeypatch.setattr('sys.stdin', io.StringIO('qwertyui'))
  assert get_password() is None

# ----------------------------------------------------------------
def test_password_1char(monkeypatch):
  """
  Check password has at least one letter
  """
  monkeypatch.setattr('sys.stdin', io.StringIO('12345678'))
  assert get_password() is None

# ----------------------------------------------------------------
def test_password_1specialChar(monkeypatch):
  """
  Check password has at least one special character
  """
  monkeypatch.setattr('sys.stdin', io.StringIO('qwerty45'))
  assert get_password() is None

# ----------------------------------------------------------------
def test_password_correct(monkeypatch):
  """
  Check a correct password
  """
  monkeypatch.setattr('sys.stdin', io.StringIO('qwerty@45'))
  assert get_password() == "qwerty@45"

# ================================================================
# ================================================================
def test_email_at(monkeypatch):
  """
  Check e-mail has a @
  """
  monkeypatch.setattr('sys.stdin', io.StringIO('moiatici.com'))
  assert get_email() is None

# ----------------------------------------------------------------
def test_email_dot(monkeypatch):
  """
  Check e-mail has a .
  """
  monkeypatch.setattr('sys.stdin', io.StringIO('moi@icidotcom'))
  assert get_email() is None

# ----------------------------------------------------------------
def test_email_correct(monkeypatch):
  """
  Check a correct e-mail
  """
  monkeypatch.setattr('sys.stdin', io.StringIO('moi@ici.com'))
  assert get_email() == 'moi@ici.com'
