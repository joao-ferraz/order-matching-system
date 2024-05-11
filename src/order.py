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
        #implement id
        self.id = 1

    def __lt__(self, other):
        return self.price < other.price
    
    def __str__(self):
        if self.price != None:
            return f"{self.side} {self.qnt} @ {abs(self.price)}"
        else:
            return f"{self.type} {self.side} {self.qnt}"

    def updateOrder(self, price, qnt):
        self.price = price
        self.qnt = qnt
    
    def invertPrice(self):
        self.price = self.price*(-1)
    