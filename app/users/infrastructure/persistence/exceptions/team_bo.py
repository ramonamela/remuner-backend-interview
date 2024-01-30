class RepeatedTeamNameException(Exception):
    def __init__(self):
        super().__init__("Repeated team name")
