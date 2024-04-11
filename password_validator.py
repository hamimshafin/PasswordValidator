from password_exception import PasswordException


class PasswordValidator():
    """
    A class for validating passwords based on specified criteria.

    """
    def __init__(self, lowercase_min=2, uppercase_min=2, digit_min=2, symbol_min=2):
        """
        Initialize a PasswordValidator object with specified criteria.
        :param lowercase_min: The minimum required lowercase characters in the password. Default is 2.
        :param uppercase_min: The minimum required uppercase characters in the password. Default is 2.
        :param digit_min: The minimum required digits in the password. Default is 2.
        :param symbol_min: The minimum required symbols in the password. Default is 2.
        """
        self._lowercase_min = lowercase_min
        self._uppercase_min = uppercase_min
        self._digit_min = digit_min
        self._symbol_min = symbol_min

        self._password = None
        self._errors = []

    def __validate_lower_case(self):
        """
        Validate the presence of lowercase characters in the password.

        :return: None
        """
        # Count the number of lowercase characters in the password
        char_count = sum(1 for char in self._password if char.isalpha() and char.islower())

        # Check if the count is less than the required minimum
        if char_count < self._lowercase_min:
            error = f"Required {self._lowercase_min} lowercase letters but only contained {char_count}"
            raise PasswordException(error, self._password)

    def __validate_upper_case(self):
        """
        Validates the presence of uppercase characters in the password.

        :return: None
        """
        # Count the number of uppercase characters in the password
        char_count = sum(1 for char in self._password if char.isalpha() and char.isupper())

        # Check if the count is less than the required minimum
        if char_count < self._uppercase_min:
            error = f"Required {self._uppercase_min} uppercase letters but only contained {char_count}"
            raise PasswordException(error, self._password)

    def __validate_symbol(self):
        """
        Validates the presence of symbols in the password.

        :return: None
        """
        # Count the number of symbols in the password
        symbol_count = sum(1 for char in self._password if not char.isalnum() and not char.isspace())

        # Check if the count is less than the required minimum
        if symbol_count < self._symbol_min:
            error = f"Required {self._symbol_min} symbols but only contained {symbol_count}"
            raise PasswordException(error, self._password)

    def __validate_digit(self):
        """
        Validates the presence of digits in the password.

        :return: None
        """
        # Count the number of digits in the password
        digit_count = sum(1 for char in self._password if char.isdigit())

        # Check if the count is less than the required minimum
        if digit_count < self._digit_min:
            error = f"Required {self._digit_min} digits but only contained {digit_count}"
            raise PasswordException(error, self._password)

    def get_errors(self):
        """
        Gets the list of errors

        :return: A list containing validation errors
        """
        return self._errors

    def __str__(self):
        """
        This function returns the password stored in PasswordValidator as a string
        :return: The password
        """
        return self._password

    def is_valid(self, password):
        """
        Checks to see if provided password is valid
        :param password: the password to be validated
        :return: True if the password is valid, and false if otherwise
        """
        self._password = password

        self._errors.clear()

        try:
            self.__validate_lower_case()
        except PasswordException as e:
            self._errors.append(e)

        try:
            self.__validate_upper_case()
        except PasswordException as e:
            self._errors.append(e)

        try:
            self.__validate_symbol()
        except PasswordException as e:
            self._errors.append(e)

        try:
            self.__validate_digit()
        except PasswordException as e:
            self._errors.append(e)

        if len(self._errors) == 0:
            return True
        else:
            return False
