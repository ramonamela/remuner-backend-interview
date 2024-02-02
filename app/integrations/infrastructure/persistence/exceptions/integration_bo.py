class RepeatedIntegrationNameException(Exception):
    def __init__(self):
        super().__init__("Repeated integration name")


class IntegrationNotFoundException(Exception):
    def __init__(self):
        super().__init__("Integration does not exist")
