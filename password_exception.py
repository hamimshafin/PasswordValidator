class PasswordException(Exception):
    """
    Exception raised for password validation errors
    """
    def __init__(self, message, password):
        super().__init__(message)
