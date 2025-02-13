"""
Module with own errors
"""


class NoDataException(Exception):
  """ Custom exception for when no data is found in database. """
  def __init__(self, message):
    super().__init__(message)
    self.status = 404


class InputInvalidException(Exception):
  """ Custom exception for when input is invalid. """
  def __init__(self, message):
    super().__init__(message)
    self.status = 400


class UnauthorizedException(Exception):
  """Custom exception for when user is not authorized."""
  def __init__(self, message):
    super().__init__(message)
    self.status = 401
