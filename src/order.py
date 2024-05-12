from enum import Enum
import itertools

class Side(Enum):
    BUY = "buy"
    SELL = "sell"


class OrderType(Enum):
    LIMIT = "limit"
    MARKET = "market"

def isValidEnum(EnumClass, value):
    return any(value == item.value for item in EnumClass)

class Order:
    idIt = itertools.count()
    def __init__(self, type, side, qnt, price = None) -> None:
        self.type = type
        self.side = side
        self.price = price
        self.qnt = qnt
        #implement id
        self.id = next(self.idIt)

        if self.type == OrderType.LIMIT.value:
            print(f"Order created: {self.side} {self.qnt} @ {abs(self.price)} {self.id}")

    def __lt__(self, other):
        if self.price != other.price:
            return self.price < other.price
        else:
            return self.id < other.id
    
    def __str__(self):
        if self.price != None:
            return f"[{self.id}] {self.side} {self.qnt} @ {abs(self.price)}"
        else:
            return f"{self.type} {self.side} {self.qnt}"

    def updateOrder(self, price, qnt):
        self.price = price
        self.qnt = qnt
    
    def invertPrice(self):
        self.price = self.price*(-1)
    