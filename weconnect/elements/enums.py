from weconnect.elements.control_operation import ControlInputEnum


class MaximumChargeCurrent(ControlInputEnum,):
    MAXIMUM = 'maximum'
    REDUCED = 'reduced'
    INVALID = 'invalid'
    UNKNOWN = 'unknown'

    @classmethod
    def allowedValues(cls):
        return [MaximumChargeCurrent.MAXIMUM, MaximumChargeCurrent.REDUCED]


class UnlockPlugState(ControlInputEnum,):
    OFF = 'off'
    ON = 'on'
    PERMANENT = 'permanent'
    UNKNOWN = 'unknown'

    @classmethod
    def allowedValues(cls):
        return [UnlockPlugState.OFF, UnlockPlugState.ON]


class BatteryCareMode(ControlInputEnum,):
    ACTIVATED = 'activated'
    DEACTIVATED = 'deactivated'
    UNKNOWN = 'unknown'

    @classmethod
    def allowedValues(cls):
        return [BatteryCareMode.ACTIVATED, BatteryCareMode.DEACTIVATED]
