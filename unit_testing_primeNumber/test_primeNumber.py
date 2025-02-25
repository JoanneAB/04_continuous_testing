import io

from primeNumber import prime_number

# ================================================================
# ================================================================
def test_primeNumber_NotPrime(monkeypatch):
  """
  Check if no space in username
  """
  monkeypatch.setattr('sys.stdin', io.StringIO('8'))
  assert prime_number() is False

# ----------------------------------------------------------------
def test_primeNumber_NotNumber(monkeypatch):
  """
  Check if no space in username
  """
  monkeypatch.setattr('sys.stdin', io.StringIO('a'))
  assert prime_number() is None

## ----------------------------------------------------------------
def test_primeNumber_correct(monkeypatch):
  """
  Check if no space in username
  """
  monkeypatch.setattr('sys.stdin', io.StringIO('7'))
  assert prime_number() is True
