class RetrievalError(Exception):
    pass


class SetterError(Exception):
    pass


class ControlError(SetterError):
    pass


class AuthentificationError(Exception):
    pass


class APICompatibilityError(Exception):
    pass