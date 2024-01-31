class RepeatedEmailException(Exception):
    def __init__(self):
        super().__init__("Repeated team name")


class UserNotFoundException(Exception):
    def __init__(self):
        super().__init__("User does not exist")
