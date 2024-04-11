from password_validator import PasswordValidator
from password_exception import PasswordException


class AdvPasswordValidator(PasswordValidator):
    """
    This class inherits from PasswordValidator and adds additional validation rules.

    """
    def __init__(self, lowercase_min=2, uppercase_min=2, digit_min=2, symbol_min=2, min_length=8, max_length=32, specific_symbol=('@', '#', '$')):
        """
        Initialize an AdvPasswordValidator object with specified criteria.
        :param lowercase_min: The minimum required lowercase characters in the password.
        :param uppercase_min: The minimum required uppercase characters in the password.
        :param digit_min: The minimum required digits in the password.
        :param symbol_min: The minimum required symbols in the password.
        :param min_length: The minimum length required for the password. Default is 8.
        """
        super().__init__(lowercase_min, uppercase_min, digit_min, symbol_min)
        self._min_length = min_length
        self._max_length = max_length
        self._specific_symbol = specific_symbol

    def __is_min_length(self):
        """
        Checks to see if password meets minimum length requirement

        :return: None
        """
        if len(self._password) < self._min_length:
            error = f"Password length must be at least {self._min_length} characters"
            raise PasswordException(error, self._password)

    def __is_max_length(self):
        """
        Checks to see if password meets minimum length requirement

        :return: None
        """
        if len(self._password) > self._max_length:
            error = f"Password length must be less than {self._max_length} characters"
            raise PasswordException(error, self._password)

    def __is_specific_symbol(self):
        """
        Checks to see if password has specific symbols

        :return: None
        """
        if self._password != self._specific_symbol:
            error = f"Password length must be {self._specific_symbol} characters"
            raise PasswordException(error, self._password)

    def is_valid(self, password):
        """
        Checks to see if provided password is valid

        :param password: The password to be validated
        :return: True if password is valid, false if otherwise
        """

        super().is_valid(password)
        self._password = password

        self._errors.clear()

        try:
            self.__is_min_length()
        except PasswordException as e:
            self._errors.append(e)

        try:
            self.__is_max_length()
        except PasswordException as e:
            self._errors.append(e)

        try:
            self.__is_specific_symbol()
        except PasswordException as e:
            self._errors.append(e)

        if len(self._errors) == 0:
            return True
        else:
            return False





