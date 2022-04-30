from core.api.enums.global_enums import Statuses


class PlayerBuilder:

    def __init__(self):
        self.result = {}

    def set_status(self, status=Statuses.ACTIVE.value):
        self.result["account_status"] = status
        return self

    def set_balance(self, balance=0):
        self.result["balance"] = balance
        return self
