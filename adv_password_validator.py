from password_validator import PasswordValidator


class AdvPasswordValidator(PasswordValidator):
    """
    This class inherits from PasswordValidator and adds additional validation rules.

    """
    def __init__(self, lowercase_min=2, uppercase_min=2, digit_min=2, symbol_min=2, min_length=8):
        """
        Initialize an AdvPasswordValidator object with specified criteria.
        :param lowercase_min: The minimum required lowercase characters in the password.
        :param uppercase_min: The minimum required uppercase characters in the password.
        :param digit_min: The minimum required digits in the password.
        :param symbol_min: The minimum required symbols in the password.
        :param min_length: The minimum length required for the password. Default is 8.
        """
        super().__init__(lowercase_min, uppercase_min, digit_min, symbol_min)
        _min_length = min_length

    def __is_min_length(self):
        """
        Checks to see if password meets minimum length requirement

        :return: None
        """


    def is_valid(self, password):
        """
        Checks to see if provided password is valid

        :param password: The password to be validated
        :return: True if password is valid, false if otherwise
        """

        super().is_valid(password)

        self._password = password
        self.is_valid(password)
        self.__is_min_length()
