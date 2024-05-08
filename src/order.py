from enum import Enum

class Side(Enum):
    BUY = "buy"
    SELL = "sell"


class OrderType(Enum):
    LIMIT = "limit"
    MARKET = "market"

def isValidEnum(EnumClass, value):
    return any(value == item.value for item in EnumClass)

class Order:
    def __init__(self, type, side, qnt, price = None) -> None:
        self.type = type
        self.side = side
        self.price = price
        self.qnt = qnt

    def updateOrder(self, price, qnt):
        self.price = price
        self.qnt = qnt