class IntegrationNotFoundException(Exception):
    def __init__(self):
        super().__init__("Integration does not exist")
