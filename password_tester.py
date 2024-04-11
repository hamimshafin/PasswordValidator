from password_validator import PasswordValidator
from adv_password_validator import AdvPasswordValidator


def display_errors(pv):
    """
    Display the errors found in the provided PasswordValidator object.

    :param pv: pv (PasswordValidator): The PasswordValidator object containing the password validation results.
    :return: None
    """
    # Print a message indicating that the password is invalid
    print(f'{pv} is an invalid password')

    # For loop for each error
    for e in pv.get_errors():
        # Print each error message
        print(e)


def default_validator():
    """
    This function validates a set of default passwords using a PasswordValidator object.
    It prints whether each password is valid or invalid and displays errors if any.

    :return: None
    """
    # Test passwords
    passwords = ("AAbb12!*", "Abb12!*", "AAb12!*", "AAbb!*", "AAbb12!", "b!")
    pv = PasswordValidator()

    # For loop for each password
    for p in passwords:
        # Check if the password is valid using the PasswordValidator object
        if pv.is_valid(p):
            # If valid, print a message
            print(f'{pv} is a valid password')
        else:
            # If invalid, display errors
            display_errors(pv)

        print()


def advance_validator():
    passwords = ("AAbb12!*", "Abb12!*", "AAb12!*", "AAbb!*", "AAbb12!", "b!")
    pv = PasswordValidator()

    # For loop for each password
    for p in passwords:
        # Check if the password is valid using the PasswordValidator object
        if pv.is_valid(p):
            # If valid, print a message
            print(f'{pv} is a valid password')
        else:
            # If invalid, display errors
            display_errors(pv)

        print()


if __name__ == '__main__':
    default_validator()
    advance_validator()
