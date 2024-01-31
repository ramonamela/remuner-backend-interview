class RepeatedTeamNameException(Exception):
    def __init__(self):
        super().__init__("Repeated team name")


class TeamNotFoundException(Exception):
    def __init__(self):
        super().__init__("Team does not exist")
