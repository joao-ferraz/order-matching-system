from order import *
from heapq import *
from validate import *
from matching import *

userCommand = [None]
#userCommand[0] = "start"

sellOrderBook = []
buyOrderBook = []

while userCommand[0] != "end":

    userInput = input()

    if userInput.strip():
        userCommand = userInput.split()

        match userCommand[0]:
            case "limit":
                try:
                    orderType, side, price, qnt = validLimitOrder(userCommand)
                except:
                    continue
                
                newOrder = Order(orderType, side, qnt, price)
                if newOrder.side == Side.BUY.value:
                    findMatch(newOrder,sellOrderBook, buyOrderBook)
                else:
                    newOrder.invertPrice()
                    findMatch(newOrder,buyOrderBook, sellOrderBook)
                                   
            case "market":
                try:
                    orderType, side, qnt = validMarketOrder(userCommand)
                except:
                    continue
                
                newOrder = Order(orderType, side, qnt)
                if newOrder.side == Side.BUY.value:
                    matchMarketOrder(newOrder,sellOrderBook)
                else:
                    matchMarketOrder(newOrder,buyOrderBook)
        
    else:
        userCommand = "No words in the input"

print("buy orders")
for i in range(len(buyOrderBook)):
    print(heappop(buyOrderBook))

print("Sell orders")
for i in range(len(sellOrderBook)):
    print(heappop(sellOrderBook))
