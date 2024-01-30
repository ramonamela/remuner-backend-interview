class RepeatedEmailException(Exception):
    def __init__(self):
        super().__init__("Repeated team name")
